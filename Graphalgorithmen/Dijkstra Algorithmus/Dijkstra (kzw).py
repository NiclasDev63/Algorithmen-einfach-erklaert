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

    # Diese Funktion gibt uns den kürzesten Weg aus
    def kuerzesterWeg(self, src, goal, entfernung):

        # Setzt den Anfangswert von min auf unendlich
        min = float("inf")

        # Index des "günstigsten Knoten"
        min_index = goal

        # Liste unseres kürzesten Weges
        kzwList = []

        # Hier fügen wir unser Zielknoten der Liste hinzu
        kzwList.append(goal)

        # Erste Schleife
        # Startet bei 0 und läuft bis Knotenanzahl - 1
        for _ in range(self.knoten):
            goal = min_index

            # Überprüft ob der Startknoten gefunden wurde und bricht die Schleife ab
            if min_index == src:
                break

            # Erste Schleife
            # Startet bei 0 und läuft bis Knotenanzahl - 1
            for y in range(self.knoten):

                # Überprüft ob der aktuelle Knoten eine Verbindung mit einem anderen hat
                if self.graph[goal][y] != 0:

                    # Überprüft ob die Entfernung des Knoten y kleiner ist als min, 
                    # falls ja wird min auf die Entfernung des y Knoten gesetzt
                    if entfernung[y] < min:
                        min = entfernung[y]
                        min_index = y

            # Fügt den "günstigsten Knoten" unserer Liste hinzu            
            kzwList.append(min_index)

        # Kehrt unsere ganze Liste um, damit der Weg in der richtigen Reihenfolge angezeigt wird
        kzwList.reverse()

        # Gibt den Kürzesten Weg aus
        print(kzwList)


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
    def dijkstra(self, src, goal):

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

        # Hier rufen wir die "kuerzesterWeg" Funktion auf, 
        # um uns den kürzesten Weg ausgeben zu lassen
        self.kuerzesterWeg(src, goal, entfernung)
    

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
 
# Hier starten wir den Dijkstra Algorithmus und übergeben 
# ihn unseren Startknoten (src) und unser Zielknoten (goal)
g.dijkstra(0, 4)     