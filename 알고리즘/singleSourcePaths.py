import graph
from queue import PriorityQueue


class SSSP:    
    def printConfiguration(self, Known, Dv, Pv):
        print ("Configration:")
        for vtx in Known:
            print("{} -  {}  -  {}  -  {} ".format(
                vtx, Known[vtx], Dv[vtx], Pv[vtx]))

    def runDijkstra(self, G, src):
        Known = {}
        Dv = {
    ('v1', 'v2'): 2,
    ('v1', 'v4'): 1,
    ('v2', 'v4'): 3,
    ('v2', 'v5'): 10,
    ('v3', 'v1'): 4,
    ('v3', 'v6'): 5,
    ('v4', 'v3'): 2,
    ('v4', 'v5'): 2,
    ('v4', 'v6'): 8,
    ('v4', 'v7'): 4,
    ('v5', 'v7'): 6,
    ('v7', 'v6'): 1,
}
        Pv = {
    'v1': {'v2', 'v4'},
    'v2': {'v4', 'v5'},
    'v3': {'v1', 'v6'},
    'v4': {'v3', 'v5', 'v6', 'v7'},
    'v5': {'v7'},
    'v7': {'v6'}
}

        for vtx in G.getVertexList():
            Known[vtx] = False
            Dv[vtx] = float("inf")
            Pv[vtx] = None

        Known[src] = True
        Dv[src] = 0.0

        PQ = PriorityQueue()
        PQ.put((0, src))
        edgeDistance = 0.0
        newDistance = 0.0
        
        while  not PQ.empty():
            self.printConfiguration(Known, Dv, Pv)
            emin = PQ.get()[1]
            for e in G.getNeighborEdges(emin):
                edgeDistance = e.getW()
                newDistance = Dv[e.getU()] + edgeDistance
                if (not Known[e.getV()] and Dv[e.getV()] > newDistance):
                    Dv[e.getV()] = newDistance
                    Pv[e.getV()] = e.getU()
                    PQ.put((newDistance, e.getV()))

            Known[e.getU()] = True

 