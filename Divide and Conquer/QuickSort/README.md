# Quicksort
Quicksort gehört zu den fortgeschritteneren Sortieralgorithmen und ist dank Divide and Conquer wesentlich schneller als bspw. Bubble- oder Insertionsort.
Des weiteren verbraucht Quicksort im vergleich zu Mergesort weniger Speicher, weshalb dieser als der schnellere Algorithmus angesehen wird.

### Laufzeitkomplexität:

**Im schlimmsten Fall**: O( n² ) Dieser Fall tritt ein, wenn immer das Letzte Element als pivot Element gewählt wird und die Liste in absteigender Reihenfolge bereits sortiert ist <br>
**Im Normalfall**: O( n log(n) )<br>
**Im Optimalfall**: O( n log(n) )

### Platzkomplexität
Die Platzkomplexität beträgt O( log(n) ).<br>
Hier wird das Sortieren der Liste In-Place durchgeführt wird.
