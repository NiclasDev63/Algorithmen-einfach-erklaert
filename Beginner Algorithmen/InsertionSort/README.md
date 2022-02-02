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
Quellen:
<br>
https://www.geeksforgeeks.org/insertion-sort/
<br>
