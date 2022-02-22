class Graph():

    def __init__(self, knoten):
        self.knoten = knoten

        self.graph = [[0 for spalte in range(knoten)]
        for zeile in range(knoten)]

    def printLösung(self, dist):
        print("Knoten \tEntfernung zum Startknoten")
        for knoten in range(self.knoten):
            print(knoten, "\t", dist[knoten])

    def _minEntfernung(self, entfernung, kzwSet):

        min = float("inf")

        for i in range(self.knoten):
            if entfernung[i] < min and kzwSet[i] == False:
                min = entfernung[i]
                min_index = i
                
        return min_index

    def dijkstra(self, src):
        entfernung = [float("inf")] * self.knoten

        entfernung[src] = 0

        kzwSet = [False] * self.knoten

        for _ in range(self.knoten):
            
            x = self._minEntfernung(entfernung, kzwSet)

            kzwSet[x] = True

            for y in range(self.knoten):
                if self.graph[x][y] > 0 and kzwSet[y] == False and entfernung[y] > entfernung[x] + self.graph[x][y]:
                        entfernung[y] = entfernung[x] + self.graph[x][y]

        self.printLösung(entfernung)         
        



g = Graph(9)


g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 

g.dijkstra(0)     