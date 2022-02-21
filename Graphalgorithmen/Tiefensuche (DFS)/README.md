# Tiefensuche (Depth First Search)
Der Unterschied zwischen der Tiefen- und der Breitensuche liegt darin, dass wir bei der Tiefensuche ein Stack (Last in First out) anstatt eine Queue (First in First out) verwenden.
Hierdurch wird der Graph nicht in der Breite durchsucht, sondern es wird ein "weg" gegangen, bis man nicht mehr weiter gehen kann.

### Laufzeitkomplexität:

Die Laufzeitkomplexität beträgt **O( V+E )**<br>
V ist die Nummer der Knoten<br>
E ist die Nummer der Kanten<br>

### Platzkomplexität

Die Platzkomplexität beträgt **O( V )**.<br>

### Funktionsweise
**1.)** Als erstes erstellen wir eine Liste namens Besucht und füllen diese mit False werten. Sie soll genutzt werden um im Auge
zu behalten welche Knoten wir besucht haben und welche nicht. Die Anzahl der False Werte in der Liste entspricht der Anzahl von Knoten im Graphen.

![image](https://user-images.githubusercontent.com/83044113/154961110-35a6bd53-ff08-4b0d-871c-b7386afdbcef.png)

**2.)** Jetzt erstellen wir einen Stack und fügen unseren Startknoten dort hinein. Parallel dazu setzen wir den Wert an der Stelle des Knoten in unserer "besucht" Liste auf True, damit dieser nicht erneut besucht wird.

![image](https://user-images.githubusercontent.com/83044113/154963221-f073b3d3-891f-4ad4-bb7f-4e42ff0172ee.png)

**Nächster Schritt**

![image](https://user-images.githubusercontent.com/83044113/154969378-d72095ca-b05f-481a-b08e-504064ca46ca.png)

**Nächster Schritt**

![image](https://user-images.githubusercontent.com/83044113/154969509-20582ba9-98e0-426d-b9a7-be07a217fe98.png)

**Nächster Schritt**

![image](https://user-images.githubusercontent.com/83044113/154970231-7c55442d-a719-43cf-9928-ea3d9670c070.png)

Das machen wir solange bis man an einem Knoten ankommt, von welchen man nicht mehr weiter gehen kann.<br>
In unserem Fall ist das der Knoten 3.

![image](https://user-images.githubusercontent.com/83044113/154970358-12127dd4-1985-459e-9e4a-51bda82d08ba.png)

Von hier aus gehen wir Schritt für Schritt wieder zurück, bis wir einen Neuen Weg gehen können.

![image](https://user-images.githubusercontent.com/83044113/154970848-72e645f9-523a-4ae8-8e74-e56eb0a191c3.png)

**Nächster Schritt**

![image](https://user-images.githubusercontent.com/83044113/154970943-5a4152d9-7677-4b09-8115-0792121642ad.png)

Jetzt sind wir beim Knoten 4 angekommen.<br>
Von hier aus können wir einen neuen Knoten besuchen, nämlich den Knoten 2.

![image](https://user-images.githubusercontent.com/83044113/154971151-130edf9e-6d2b-4d57-8c31-dee2e6477e4e.png)

Da wir jetzt von der 2 aus keinen neuen Knoten mehr besuchen können, gehen wir einen Schritt zrück und entfernen ihn wieder aus unserem Stack.

![image](https://user-images.githubusercontent.com/83044113/154971378-395d73e0-52b0-46b3-adbf-623ebb9ef350.png)

Dies tuhen wir jetzt für alle Knoten in unserem Stack, bis er leer ist.

![image](https://user-images.githubusercontent.com/83044113/154971593-34ab7b47-e98b-4b42-b2d0-11f2a9a6803b.png)

Nun folgt wie gewohnt eine Implementation des Algorithmus in Python:
```python
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
```
