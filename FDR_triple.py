
import copy as cp
from itertools import combinations

import local_grapl.dsl as dsl

def remove_outgoing(G, node):
    """Remove all outgoing edges (directed and bidirected) from the node.
       This modifies the graph in-place.
    """
    # Remove this node from its children's parents
    for child in G.ch({node}):
        G.vars[child].parents = G.vars[child].parents.difference({node})
    G.vars[node].children = set()
    return G

def remove_incoming(G, node):
    """Remove all incoming edges (directed and bidirected) to the node.
       This modifies the graph in-place."""
    for parent in G.pa({node}):
        G.vars[parent].children = G.vars[parent].children.difference({node})
    G.vars[node].parents = set()
    for bidirect in G.bi({node}):
        G.vars[bidirect].bidirects = G.vars[bidirect].bidirects.difference({node})
    G.vars[node].bidirects = set()
    return G

def ismsep_set(G, 
               source: set, 
               target: set, 
               cond = set()):
    """Check if the source set is m-separated from the target set given the condition set in the graph G.
       Returns True if m-separated, False otherwise.
    """
    for s in source:
        for t in target:
            if not G.ismsep(s, t, cond):
                return False

    return True

def triple_id(G, 
              X: set, 
              Y: set, 
              output: str = "naive",
              mode: str = "fast"):
    """
    Identify FDR triples (X*, Y*, M_S) for given sets X and Y in the ADMG G.
    
    Parameters:
    G : object grapl.ADMG
        The input acyclic directed mixed graph.
    X : set
        The set of treatment variables.
    Y : set
        The set of outcome variables.
    output : str, optional
        The format of the output. Options are "naive" (default) for a dictionary format
        and "tabular" for a pandas DataFrame format.
    mode : str, optional
        The mode of operation. Options are "fast" (default) to return the first found triple
        and "all" to return all valid triples.
        
    Returns:
    tuple
        A tuple containing:
        - If output is "naive": a dictionary with keys "X_star", "Y_star", and "M_S" containing lists of valid triples.
        - If output is "tabular": a pandas DataFrame with columns "X_star", "Y_star", and "M_S".
        - A boolean indicating whether at least one FDR triple was found.
    """
    
    if output not in ["naive", "tabular"]:
        raise ValueError("Invalid output format specified.")
    if mode not in ["fast", "all"]:
        raise ValueError("Invalid mode specified.")
    
    Y_star = Y
    Y_star_an = G.an(Y_star)
    G = G.sub(Y_star_an.union(X))
    V = G.nodes()
    Nb_Y_star = G.bi(Y_star)

    valid_triples = {"X_star": [], "Y_star": [], "M_S": []}
    X_star_candidates_dX = list(Y_star_an.difference(Y_star).difference(X))

    for i in range(len(X_star_candidates_dX)+1):
        for S_enlarge in combinations(X_star_candidates_dX, i):
            S = set(S_enlarge).union(X)    
            interior = Y_star_an.intersection(G.de(S))
            Nb_S = G.bi(S)
            Z_S = interior.difference(Nb_S.union(Nb_Y_star).union(Y_star).union(S))
            G_remove_incoming_S= cp.deepcopy(G)
            for S_i in S:
                G_remove_incoming_S = remove_incoming(G_remove_incoming_S, S_i)
            M_S = []
            for j in range(1, len(Z_S)+1):
                for M_enlarge in combinations(Z_S, j):
                    M = set(M_enlarge)
                    # Cond 1: There does not exist a directed path from S to Y that does not pass through de(M) in G
                    G_sub_M = cp.deepcopy(G).sub(V.difference(M))
                    de_S_in_GsubM = G_sub_M.de(S)
                    is_cond1 = len(Y_star.intersection(de_S_in_GsubM)) == 0
                    if not is_cond1:
                        continue
                    
                    # Cond 2: M m-separates S and Y in G with outgoing edges from S removed
                    G_remove_outgoing_S = cp.deepcopy(G)
                    for S_i in S:
                        G_remove_outgoing_S = remove_outgoing(G_remove_outgoing_S, S_i)
                    is_cond2 = ismsep_set(G_remove_outgoing_S, S, M)
                    if not is_cond2:
                        continue
                        
                    # Cond 3: nodewise m-separation of Y_star and M_i conditioning on S and M\{M_i} in G with incoming edges to S and outgoing edges from M_i removed
                    is_cond3 = True
                    for M_i in M:
                        G_remove_incoming_S_outgoing_Mi = cp.deepcopy(G_remove_incoming_S)
                        G_remove_incoming_S_outgoing_Mi = remove_outgoing(G_remove_incoming_S_outgoing_Mi, M_i)
                        cond_set = S.union(M.difference({M_i}))
                        is_cond3 = is_cond3 and ismsep_set(G_remove_incoming_S_outgoing_Mi, Y_star, {M_i}, cond_set)
                    if not is_cond3:
                        continue
                    
                    if mode == "all":
                        M_S.append(M)
                    elif mode == "fast":
                        valid_triples = {"X_star": [S], "Y_star": [Y_star], "M_star": [M]}
                        if output == "naive":
                            return valid_triples, True
                        elif output == "tabular":
                            import pandas as pd
                            df = pd.DataFrame(valid_triples)
                            return df, True
                                    
            if len(M_S) > 0:
                valid_triples["X_star"].append(S)
                valid_triples["M_S"].append(M_S)
                valid_triples["Y_star"].append(Y_star)
                
    if len(valid_triples["X_star"]) != 0:
        if output == "naive":
            return valid_triples, True
        elif output == "tabular":
            import pandas as pd
            df = pd.DataFrame(valid_triples)
            return df, True
    else:
        return None, False             
