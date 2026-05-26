from model.model import Model
myModel = Model()
myModel.buildGraph(5)
nodi,archi= myModel.getGraphDetails()

print(f"Num nodes : {nodi} e num edges : {archi}")
