# Quicksort
Quicksort gehört zu den fortgeschritteneren Sortieralgorithmen und ist dank Divide and Conquer wesentlich schneller als bspw. Bubble- oder Insertionsort.
Des weiteren verbraucht Quicksort im vergleich zu Mergesort weniger Speicher, weshalb dieser als der schnellere Algorithmus angesehen wird.

### Laufzeitkomplexität:

**Im schlimmsten Fall**: O( n² ) Dieser Fall tritt ein, wenn immer das Letzte Element als pivot Element gewählt wird und die Liste in absteigender Reihenfolge bereits sortiert ist <br>
**Im Normalfall**: O( n log(n) )<br>
**Im Optimalfall**: O( n log(n) )

### Platzkomplexität
Die Platzkomplexität beträgt O( log(n) ).<br>
Hierbei handelt es sich laut Definition um einen In-Place Algorithmus, da der extra Speicher lediglich für die Rekursion und nicht für das Bearbeiten der Eingabe verwendet wird.

### Funktionsweise
**1.)** Als erstes bestimmen wir unser Pivot Element. Hierzu gibt es verschiedene Ansätze, die je nach Implementation variieren können.<br>
**Beispiele:**

+ Man wählt immer das letzte Element als Pivot Element aus.
+ Man wählt immer das erste Element als Pivot Element aus.
+ Man wählt das Pivot Element aus zufällig aus.

**2.)** 
