from collections import defaultdict
from pydoc import visiblename

# Hier erstellen wir die Klasse Graph
class Graph:

    # Das ist der Konstruktor der Klasse
    # Hier erstellen wir ein defaultdict mit einer Liste,
    # welches genutzt wird um die Knoten und Kanten zu speichern
    def __init__(self):
        self.graph = defaultdict(list)

    # Diese Funktion ermöglicht es uns neue Knoten und Kanten hinzuzufügen
    def addEdge(self, u, v):
        self.graph[u].append(v)

        
    """

    Start des Algorithmus

    """
    def _tiefensuche(self, v, besucht):
        print(v, end=" ")
        besucht[v] = True
        for i in self.graph[v]:
            if not besucht[i]:
                self._tiefensuche(i, besucht)
    
    def tiefensuche(self, v):
        besucht = [False] * len(self.graph)
        self._tiefensuche(v, besucht)   
    """

    Ende des Algorithmus
    
    """

# Hier erstellen wir ein Objekt des Graphen
g = Graph()

# Hier erstellen wir neue Knoten mit Kanten
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# Hier rufen wir den Algortihmus auf 
# und übergeben ihn einen Startknoten
g.tiefensuche(2)