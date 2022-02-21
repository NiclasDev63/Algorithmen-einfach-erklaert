from collections import defaultdict

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
        pass
    
    def tiefensuche(self, v):
        pass