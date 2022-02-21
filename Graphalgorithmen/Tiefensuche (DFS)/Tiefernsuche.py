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
    
    # Diese Funktion wird rekursiv aufgerufen
    def _tiefensuche(self, v, besucht):
        # Gibt den aktuellen Knoten aus
        print(v, end=" ")

        # Hier setzen wir den aktuellen Knoten auf besucht
        besucht[v] = True

        # Schleife die die Nachbarn unseres aktuellen Knoten besucht
        for i in self.graph[v]:

            # Hier wird überprüft, ob der Nachbarknoten bereits besucht wurde
            # Falls nein, rufen wir unsere "_tiefensuche" Funktion mit dem Nachbarknoten auf
            if not besucht[i]:
                self._tiefensuche(i, besucht)
    
    # Erstellt die besucht Liste und ruft die "_tiefensuche" Funktion auf
    def tiefensuche(self, v):
        # Hier erstellen wir eine Liste mit False werten
        # um nachzuvollziehen, welche Knoten bereits besucht wurden
        besucht = [False] * len(self.graph)

        # Hier rufen wir den eigentlichen Algorithmus auf
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