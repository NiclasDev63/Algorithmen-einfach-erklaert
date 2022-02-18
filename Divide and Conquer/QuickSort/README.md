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
+ Man wählt das Pivot Element zufällig aus.

Das Pivot Element gilt als "Anhaltspunkt" zum sortieren der Liste.
In unserem Beispiel befindet sich dieses am Ende der Liste.

**2.)** Danach weisen wir dem Algorithmus noch ein low und ein high Element zu.
Das high Element befindet sich am oberen Ende der Liste und das low Element am unteren.

![image](https://user-images.githubusercontent.com/83044113/154667913-bbf0defa-bbbf-46f5-a148-be70a019d81e.png)

**3.)** Jetzt fangen wir an zu vergleichen, ob das high Element größer als das pivot Element ist.
Das ist der Fall, weshalb das high Element an der Stelle bleibt und wir einen Schritt nach links gehen.
Diesen Schritt wiederholen wir solange, bis das high Element nicht mehr größer oder gleich dem pivot Element ist.

![image](https://user-images.githubusercontent.com/83044113/154669678-e82acc6c-0c6a-4a57-95e3-49ce248ecd96.png)

Da das aktuelle high Element (die 6) kleiner als das pivot Element (die 16) ist, beenden wir diesesn Schritt und fahren mit dem nächsten fort.

**4.)** Jetzt überprüfen wir, ob das low Element kleiner als das pivot Element ist.
Das ist nicht der Fall, weshalb das low Element an der Stelle bleibt und wir zum nächsten Schritt über gehen.

![image](https://user-images.githubusercontent.com/83044113/154670863-3c023433-c2d2-4c51-9f45-21f41ba5dfd2.png)

**5.)** Da wir unsere Liste in zwei Hälften aufteilen wollen, in der die untere Hälfte aus Elementen besteht die kleiner und die rechte Hälfte aus Elementen besteht die größer als das pivot Element sind, tauschen wir nun die Werte, die sich in unseren aktuellen low und high Elementen befinden.<br>

**Vorher:**

![image](https://user-images.githubusercontent.com/83044113/154672300-aa13fbcb-20b1-409a-8172-34bcb6470c7d.png)

**Nachher:**

![image](https://user-images.githubusercontent.com/83044113/154672360-ff00841d-0f6f-49d3-bf2b-988e028e1d71.png)



