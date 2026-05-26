import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph=nx.Graph()
        self._airports=DAO.getAllAirports()

        self._idMap={}
        for i in self._airports:
            self._idMap[i.ID]=i



    def buildGraph(self,n):
        nodes = DAO.getAllNodes(n,self._idMap)
        self._graph.add_nodes_from(nodes)
        self.getEdges()



    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)


    def getEdges(self):
        allTratte= DAO.getAllEdges(self._idMap)
        for t in allTratte:
            if t.airportP in self._graph and t.airportA in self._graph:
                self._graph.add_edge(t.airportA, t.airportP,weight=t.peso)










