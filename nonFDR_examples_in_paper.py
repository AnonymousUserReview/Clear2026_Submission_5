#%%
import local_grapl.dsl as dsl
from FDR_triple import triple_id

# %% test cases for non-FDR ADMGs (Figure 3 in the paper)
# (a)
test_graph = '  Z; X; Y; U;\
                X -> U; \
                U -> Z; \
                Z -> Y; \
                Z <-> Y; \
                X <-> U; \
                X <-> Y;' 
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "fast")
FDR_triple_identifiable, triple_result  
# %%
# (b)
test_graph = '  Z; X; Y; U; V;\
                X -> U; \
                U -> Z; \
                Z -> Y; \
                V -> X; \
                V -> U; \
                V -> Z; \
                Z <-> Y; \
                X <-> Y;'              
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
FDR_triple_identifiable, triple_result  
#%%
# (c)
test_graph = '  Z; X; Y; U; \
                Z -> Y; \
                X -> Z; \
                U -> X; \
                U -> Z; \
                U -> Y; \
                X <-> Y;'              
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
FDR_triple_identifiable, triple_result  

#%%
# (d)
test_graph = '  Z; X; Y; U; \
                X -> Z; \
                Z -> Y; \
                U -> X; \
                U -> Z; \
                U -> Y; \
                X <-> Y;'              
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
FDR_triple_identifiable, triple_result  

#%%
# (e)
test_graph = '  Z; X; Y; M; V; W; \
                X -> Z; \
                Z -> Y; \
                X -> W; \
                W -> V; \
                V -> Z; \
                M -> W; \
                M <-> Z; \
                M <-> Y; \
                X <-> Y;'       
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
FDR_triple_identifiable, triple_result  

#%%
# (f)
test_graph = '  Z; X; Y; V; M; \
                X -> Z; \
                Z -> Y; \
                V -> M; \
                M -> Z; \
                M -> Y; \
                M <-> Y; \
                X <-> V; \
                X <-> Y;'       
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
FDR_triple_identifiable, triple_result  