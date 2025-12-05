#%%

from FDR_triple import triple_id
import local_grapl.dsl as dsl

#%% Test cases for FDR ADMGs Figure 1
# (a)
test_graph = '  X; U; M; Z; W; Y; L; V; K;\
                X -> U; \
                U -> M; \
                M -> Z; \
                Z -> Y; \
                W -> Z; \
                W -> Y; \
                K -> V; \
                V -> L; \
                V -> U; \
                V -> M; \
                X <-> Z; \
                K <-> Y; \
                L <-> X;'
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result 
#%% (b)
test_graph = '  Z; X; Y; M; U; V;\
                X -> M; \
                M -> V; \
                V -> Y; \
                Z -> Y; \
                U -> M; \
                U -> Z; \
                V <-> Y; \
                X <-> U; \
                X <-> Y;' 
               
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result 
#%% Test cases for FDR ADMGs Figure 2
# (a)
test_graph = 'M; X; Y; V; Z; \
               X->M; \
               M->Y; \
               V->Z; \
               Z->Y; \
               X<->V; \
               X<->Y;'
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   

#%% (b)
test_graph = '  M; X; Y; W; V;\
                X -> M; \
                M -> Y; \
                W -> M; \
                Y -> V; \
                M <-> V; \
                X <-> Y;'              
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result

#%% (c)
test_graph = '  M; X; Y; Z; U;\
                X -> M; \
                M -> Y; \
                Z -> M; \
                Z -> U; \
                X <-> Y; \
                U <-> Y;' 
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result
#%% (d)
test_graph = '  M; X; Y; V; U; \
                X->M; \
                M->Y; \
                U->V; \
                Y->U; \
                X<->V; \
                X<->Y; \
                Y<->U;'

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   



#%% (e)
test_graph = 'M; X; Y; V; U; \
               X->M; \
               X->U; \
               M->Y; \
               M->V; \
               U->V; \
               Y->U; \
               X<->Y; '

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result

#%% (f)
test_graph = '  M; X; Y; V; U; \
                X -> M; \
                M -> U; \
                U -> Y; \
                V -> U; \
                V -> Y; \
                M -> V; \
                X <-> U; \
                X <-> Y;'                

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result

#%% (g)
test_graph = '  M; X; Y; V; U;\
                X -> U; \
                U -> M; \
                M -> Y; \
                V -> U; \
                V <-> M; \
                X <-> Y;' 

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result

#%% (h)
test_graph = '  M; X; Y; D; H; S;\
                X -> M; \
                M -> Y; \
                X -> H; \
                H -> M; \
                M -> S; \
                S -> Y; \
                D -> X; \
                D -> Y; \
                X <-> Y;'
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result
#%% (i)
test_graph = '  X; M; V; Z; W; Y;\
                X -> M; \
                X -> V; \
                V -> M; \
                V -> Y; \
                M -> Z; \
                Z -> Y; \
                W -> Z; \
                W <-> Y; \
                X <-> Y;' 
               
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   
#%% (j)
test_graph = '  M; X; Y; V; U;\
                X -> M; \
                M -> V; \
                V -> Y; \
                X -> U; \
                U -> M; \
                U -> V; \
                V <-> Y; \
                X <-> Y;'

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   

#%% (k)
test_graph = '  Z; X; Y; M; U; V;\
                X -> U; \
                U -> M; \
                M -> Z; \
                Z -> Y; \
                U -> V; \
                V -> M; \
                V -> Z; \
                Z <-> Y; \
                X <-> U; \
                X <-> Y;' 
               
grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   

#%% (l)
test_graph = '  X; M; V; Z; Y;\
                X -> M; \
                M -> Z; \
                Z -> Y; \
                M -> V; \
                V -> Y; \
                V -> Z; \
                X <-> Z; \
                X <-> V;' 

grapl_obj = dsl.GraplDSL()
G = grapl_obj.readgrapl(test_graph)
triple_result, FDR_triple_identifiable = triple_id(G, X = {"X"}, Y = {"Y"}, 
                                                   output = "tabular", mode = "all")
triple_result   


