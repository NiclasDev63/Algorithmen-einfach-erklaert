# Insertionsort
Insertionsort ist ein einfacher Sortieralgorithmus, welcher wegen seiner Funktionsweise oft mit dem Sortieren von Karten in der Hand verglichen wird.

### Laufzeitkomplexität:

**Im schlimmsten Fall**: O(n²)<br>
**Im Normalfall**: O(n²)<br>
**Im Optimalfall**: O(n) (Dieser Fall tritt nur auf, wenn die Liste bereits sortiert ist.)<br>

### Platzkomplexität
Die Platzkomplexität beträgt O(1), da das Sortieren der Liste In-Place durchgeführt wird.

### Funktionsweise
Bei diesem Algorithmus wird das aktuelle Element mit seinem Vorgänger verlgichen und gegebenfalls getauscht.
Dies passiert solange, bis das aktuelle Element nicht mehr kleiner als sein Vorgänger ist oder wir am Anfang der Liste angekommen sind.
<br>
Ich finde, Algorithmen sind meistens am einfachsten zu verstehen, wenn man mal ein paar Schleifendurchläufe gesehen hat.
Aus diesem Grund werden wir genau das tun.
<br>
<br>
**Unsere Liste:**
<br>
[4, 3, 2, 10, 12, 1, 5, 6]
<br>
<br>
**Durchlauf 1:**
<br>
> i = 1

> j = 0 (da j immer i-1 ensptricht)

> Jetzt wird abgefragt: Ist das Element an der Stelle i (unser aktuelles Element), also die 3 kleiner als das Element an der Stelle j, also die 4? ja ist sie, das heißt beide Zahlen tauschen ihre Position.

<br>

**Durchlauf 2:**
> i = 2

> j = 1 (da j immer i-1 ensptricht)

> Jetzt wird abgefragt: Ist das Element an der Stelle i (unser aktuelles Element), also die 2 kleiner als das Element an der Stelle j, also die 4? ja ist sie, das heißt beide Zahlen tauschen ihre Position.

> Da wir aber noch nicht am Anfang der Liste angekommen sind, geht es weiter und j wird um 1 verringert, wodurch j = 0 ist.

> Ist das Element an der Stelle i (unser aktuelles Element), also die 2 kleiner als das Element an der Stelle j, also die 3? ja ist sie, das heißt beide Zahlen tauschen ihre Position.
<br>
So geht es weiter, bis wir am Ende unserer Liste angekommen sind, also bis n-1 (n entspricht der Länge der Liste).
<br>
<br>
Im Folgenden habe ich ein Bild eingefügt, welches den ganzen Vorgang mit unserer Liste noch einmal visuell darstellt.
<br>
<br>

![image](https://user-images.githubusercontent.com/83044113/151985003-15de7671-3d58-453e-be47-9703563fd799.png)

<br>
<br>
Nun schauen wir uns eine Implementierung des Algorithmus in Python an.
<br>
<br>

```python
"""

Anfang des Algorithmus

"""
                        
def insertionSort(list):

    # n = Länge der übergebenen Liste
    n = len(list)

    # erste Schleife
    # startet bei 1 und geht bis n-1
    for i in range(1, n):

        # ist das aktuelle Element, welches mit seinem Vorgänger verglichen wird
        aktuelles_element = list[i]


        # j ist der Vorgänger, der mit dem aktuellen Element verlgichen wird
        j = i-1

        # zweite Schleife
        # wird ausgeführt, solange j größer oder gleich 0 ist UND das aktuelle Element kleiner als sein Vorgänger ist
        while j >= 0 and aktuelles_element < list[j]:
            list[j + 1] = list[j]

            # reduziert den j Wert bei jedem Durchlauf durch die zweite Schleife um 1
            j -= 1
        
        # Fügt das aktuelle Element an die richtige Position ein
        list[j + 1] = aktuelles_element

"""

Ende des Algorithmus

"""



# die unsortierte Liste
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# ruft unsere Funktion mit der zu sortierenden Liste auf
insertionSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))
```
<br>
Da es bei dem ein oder anderen Leser bestimmt noch offene Fragen gibt, gehe ich nun auf die einzelnen Abschnitte des Codes ein.
<br>
<br>

```python
# erste Schleife
# startet bei 1 und geht bis n-1
for i in range(1, n):

    # ist das aktuelle Element, welches mit seinem Vorgänger verglichen wird
    aktuelles_element = list[i]
```
Hier fragt ihr euch vielleicht, wieso starten wir an der Stelle 1 und nicht an der Stelle 0, wie es bspw. bei dem Bubblesort Algorithmus üblich ist.
Das liegt daran, das i unser aktuelles Element ist und wie wir durch das vorherige Beispiel wissen, dieses immer mit seinem Vorgänger verglichen wird, was jedoch nicht möglich wäre, wenn wir an der stelle 0 beginnen, da wir dann am Anfang der Liste wären und es somit keinen Vorgänger gibt, wodurch ein Fehler entstehen würde, der das Programm zum Absturz bringt.
<br>
<br>
Fahren wir fort.
```python
# zweite Schleife
# wird ausgeführt, solange j größer oder gleich 0 ist UND das aktuelle Element kleiner als sein Vorgänger ist
while j >= 0 and aktuelles_element < list[j]:
    list[j + 1] = list[j]

    # reduziert den j Wert bei jedem Durchlauf durch die zweite Schleife um 1
    j -= 1

# Fügt das aktuelle Element an die richtige Position ein
list[j + 1] = aktuelles_element
```
Das ist unsere zweite Schleife.
Hier ist anders als bei der "for-Schleife"  keine feste Anzahl vorgeschrieben, wie oft die Schleife durchlaufen werden soll.
Stattdessen wird diese Schleife solange ausgeführt, bis j kleiner als 0 wird oder unser aktuelles Element nicht mehr kleiner als sein Vorgänger ist.

Falls einer der beiden Fälle noch nicht eingetreten ist, startet die Schleife und setzt das Element aus der Liste, welches sich an der Stelle j+1 befindet, an die Stelle j.

Danach wird der j Wert um 1 reduziert, da wir die Liste bis zu Anfang durchlaufen wollen.
<br>
**Bespiel:**
<br>
> Liste = [20, 21, 13, 6, 85, 16] und j = 3
> 
> Liste[j] = 6 (da wir bei 0 anfangen zu zählen)

> j -= 1 somit ist j = 2

> Liste[j] = 13

Nachdem die Schleife fertig durchlaufen ist, also eine der beiden Bedingungen nicht mehr erfüllt ist, setzten wir unser aktuelles Element auf list[j+1].
Hier setzten wir es auf j+1 und nicht auf j, da nach jedem Durchlauf der zweiten Schleife j-1 genommen wird.








<br>
<br>
Quellen:
<br>
https://www.geeksforgeeks.org/insertion-sort/
<br>
