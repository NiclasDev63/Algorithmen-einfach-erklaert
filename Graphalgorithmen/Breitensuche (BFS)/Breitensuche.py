from collections import defaultdict
from collections import deque


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
    # In der dieser Funktion ist der eigentlichte Algortihmus implmenetiert
    def breitensuche(self, s):

        # Hier erstellen wir eine Liste mit False werten
        # um nachzuvollziehen, welche Knoten bereits besucht wurden
        besucht = [False] * len(self.graph)
        
        # Hier erstellen wir eine Queue und
        # übergeben ihr unseren Startknoten
        queue = deque([s])

        # Hier geben wir an, dass unser Startknoten bereits besucht wurde
        besucht[s] = True

        # Erste Schleife, 
        # Wird solange ausgeführt, bis die Queue leer ist
        while queue:

            # Hier entfernen wir ganz nach dem Prinzip (First in First out) den ersten Wert der Liste
            # und weisen ihn unserem s zu
            s = queue.popleft()
            
            # Gibt den aktuellen Knoten aus
            print(s, end = " ")

            # Zweite Schleife
            # Folgt den Kanten der aktuellen Knoten
            for i in self.graph[s]:

                # Hier wird überprüft, ob der Knoten bereits besucht wurde
                # Falls nein, füge wir ihn unserer Queue hinzu und geben an,
                # dass dieser Knoten nun besucht wurde
                if not besucht[i]:
                    queue.append(i)
                    besucht[i] = True
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
g.breitensuche(2)
