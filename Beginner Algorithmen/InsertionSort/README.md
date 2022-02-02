# Insertionsort
### Funktionsweise
Insertionsort ist einfacher sortier Algorithmus, welcher wegen seiner Funktionsweise oft mit dem Sortieren von Karten in der Hand verglichen wird.
Hierbei wird das aktuelle Element mit seinem Vorgänger verlgichen und gegebenfalls getauscht.
Dies passiert solange, bis das aktuelle Element nicht mehr kleiner als sein Vorgänger ist oder wir am Ende besser gesagt am Anfang der Liste angekommen sind.
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
Im Folgenden habe ich ein Bild eingefügt, welches den ganzen Vorgang anhand von unserer Liste noch einmal visuell darstellt.
<br>
<br>

![image](https://user-images.githubusercontent.com/83044113/151985003-15de7671-3d58-453e-be47-9703563fd799.png)

<br>
<br>
Nun schauen wir uns eine Implementierung des Algorithmus in Python an.
<br>
<br>

```python
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
<br>
Quellen:
<br>
https://www.geeksforgeeks.org/insertion-sort/
<br>
