# Hier erstellen wir die Klasse Graph
class Graph():

    # Das ist der Konstruktor der Klasse
    # Hier speichern wir die Anzahl der Knoten und erstellen
    # einen vorerst ungewichteten Graphen
    def __init__(self, knoten):

        # Anzahl der gewünschten Knoten
        self.knoten = knoten

        # Erstellen einen ungewichteten Graph in der gewünschten Größe
        self.graph = [[0 for spalte in range(knoten)]
        for zeile in range(knoten)]

    # Diese Funktion dient zu Ausgabe der Entfernung
    # von Knoten n bis zum Startknoten
    def printLösung(self, entfernung):
        print("Knoten \tEntfernung zum Startknoten")
        for knoten in range(self.knoten):
            print(knoten, "\t", entfernung[knoten])


    """

    Start des Algorithmus

    """

    # Diese Funktion gibt den Knoten mit der 
    # kürzesten Entfernung zum vorherigen Knoten
    # zurück und wird intern vom Algorithmus aufgerufen
    def _minEntfernung(self, entfernung, kzwSet):

        # Setzt den Anfangswert von min auf unendlich
        min = float("inf")

        # Schleife
        # Startet bei 0 und läuft bis Knotenanzahl - 1
        for i in range(self.knoten):

            # Hier wird überprüft ob die Entfernung von Knoten an der Stelle i zum Startknoten
            # kleiner ist als min und ob dieser bereits besucht wurde
            if entfernung[i] < min and kzwSet[i] == False:

                # Ändert den Wert von min auf die Entfernung von Knoten i zum Startknoten
                min = entfernung[i]

                # Beinhaltet die Knotennummer 
                min_index = i

        # Gibt die Knotennummer von dem Knoten zurück, welcher die 
        # kürzeste Entfernung zum Startknoten hat und noch nicht besucht wurde
        return min_index
    
    # Der eigentliche Algorithmus
    def dijkstra(self, src):

        # Hier erstellen wir eine Liste mit unendlich Werten, die genauso viele
        # Elemente besitzt, wie es Knoten gibt
        entfernung = [float("inf")] * self.knoten

        # Zu Beginn setzen wir die Entfernung zum Startknoten (src) auf 0
        entfernung[src] = 0

        # Hier erstellen wir eine Liste mit False werten
        # um nachzuvollziehen, welche Knoten bereits besucht wurden
        kzwSet = [False] * self.knoten

        # Erste Schleife
        # Startet bei 0 und läuft bis Knotenanzahl - 1
        for _ in range(self.knoten):
            
            # Hier wird die Funktion "_minEntfernung" aufgerufen
            # und der Rückgabewert wird in unserer x Variable gespeichert
            x = self._minEntfernung(entfernung, kzwSet)

            # Setzt den aktuellen Knoten auf besucht
            kzwSet[x] = True

            # Zweite Schleife
            # Startet bei 0 und läuft bis Knotenanzahl - 1
            for y in range(self.knoten):

                # Hier wird überprüft ob es eine Verbindung zwischen dem Knoten x und einem anderen Knoten gibt
                # Falls es diese gibt, wird zusätzlich überprüft ob dieser andere Knoten bereits besucht wurde und 
                # ob die Entfernung von diesem zum Startknoten  durch eine andere Route noch verbessert werden kann
                if self.graph[x][y] > 0 and kzwSet[y] == False and entfernung[y] > entfernung[x] + self.graph[x][y]:

                        # Hier wird die Entfernung von Knoten y berechnet
                        entfernung[y] = entfernung[x] + self.graph[x][y]

        # Hier rufen wir die "printLösung" Funktion auf, um uns die Entfernungen
        # von Knoten n zum Startknoten ausgeben zu lassen
        self.printLösung(entfernung)
    

    """

    Ende des Algorithmus
    
    """
        


# Hier erstellen wir ein Objekt des Graphen und
# übergeben unsere gewünschte Knotenanzahl
g = Graph(9)

# Hier erstellen wir unser eigenen gewichteten Graphen
g.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
 
# Hier starten wir den Dijkstra Algorithmus und übergeben ihn unseren Startknoten (src)
g.dijkstra(0)     