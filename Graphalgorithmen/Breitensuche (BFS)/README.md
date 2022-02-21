# Breitensuche (Breadth First Search)
Die Breitensuche ermöglicht es uns einen Graphen von einem bestimmten Punkt aus zu durchqueren und beispielsweise den schnellsten Weg zu einem Knoten V zu finden.
Zusätzlich kann der Algorithmus beim Webcrawling verwendet werden um alle Links auf einer Webseite zu finden.
Ein Beispiel für letzteres findest du hier https://github.com/NiclasDev63/LinkGrabber.
### Laufzeitkomplexität:

**O( V+E )**<br>
V ist die Nummer der Knoten<br>
E ist die Nummer der Kanten<br>

### Funktionsweise

**1.)** Als erstes erstellen wir eine Liste namens Besucht und füllen diese mit False werten.
Sie soll genutzt werden um im Auge zu behalten welche Knoten wir besucht haben und welche nicht.
Die Anzahl der False Werte in der Liste entspricht der Anzahl von Knoten im Graphen.

![image](https://user-images.githubusercontent.com/83044113/154929189-e8774cef-c4f7-477d-9cc0-ac4541cb4538.png)

**2.)** Jetzt erstellen wir eine Queue und fügen unseren Startknoten dort hinein.
Parallel dazu setzen wir den Wert an der Stelle des Knoten in unserer "besucht" Liste auf True, damit dieser nicht erneut besucht wird.

![image](https://user-images.githubusercontent.com/83044113/154931950-aaa25e04-94c6-447a-a82f-e7369fdec662.png)

Diese Schritte werden jetzt wiederholt, bis alle Knoten des Graphen besucht wurden.

![image](https://user-images.githubusercontent.com/83044113/154933236-d3d9bfa4-a42b-4924-a8d1-888f5c549833.png)


![image](https://user-images.githubusercontent.com/83044113/154933550-b3b9696c-7d7d-4a30-bc1b-98ef739f679c.png)


![image](https://user-images.githubusercontent.com/83044113/154934764-47a983ab-c7ac-47e7-a1eb-4ba6644fa8a4.png)

![image](https://user-images.githubusercontent.com/83044113/154934829-fab7f150-fb70-48fe-9236-c0239209acc4.png)

![image](https://user-images.githubusercontent.com/83044113/154934888-16df78e0-44a9-411a-a272-3862f54ccd38.png)

![image](https://user-images.githubusercontent.com/83044113/154934942-b15989a1-9bd6-448c-b522-db848442630a.png)

<br>
<br>
Nun folgt eine Implementation des Algorithmus in Python:

```python
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
```
