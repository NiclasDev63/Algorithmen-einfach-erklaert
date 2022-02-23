# Dijkstra`s Algorithmus
Dijkstra`s Algorithmus gehört zu den sogennanten Greedy-Algorithmen. Diese zeichnen sich dadurch aus, das sie in jedem
Teilschritt, im Bezug auf die Vorgaben, das best mögliche Ergebnis erzielen.<br>

**Wichtig:**<br>
Dijkstra`s Algorithmus kann lediglich in Graphen mit positiven Gewichten verwendet werden.
Wenn man einen Graphen mit negativen Gewichten hat, ist dieser Algorithmus ungeeignet und man sollte beispielsweise auf den Bellman Ford Algorithmus zurückgreifen.

### Laufzeitkomplexität:

Die Laufzeitkomplexität beträgt **O(V^2)**<br>
V ist die Anzahl der Knoten<br>

### Platzkomplexität

Die Platzkomplexität beträgt ebenfalls **O(V^2)**.<br>

### Funktionsweise

Vorab unser Graph, in welchem wir Dijkstra`s Algorithmus anwenden:

![image](https://user-images.githubusercontent.com/83044113/155374222-8f670d8b-acae-4bda-afb1-99ac7c2b303f.png)

Die Zahlen neben den Linien sind die sogennanten Gewichte.

**1.)** Zunächst suchen wir uns einen Startpunkt aus.
In unserem Fall, wählen wir die 0.
Danach schauen wir uns an, welche Knoten mit unserem Startknoten ( 0 ) verbunden sind und zwar sind das die Knoten 1 und 7.
Also besuchen wir diese.

![image](https://user-images.githubusercontent.com/83044113/155375274-651e815f-65c8-445d-888a-148f9aa7bf22.png)


**Anmerkung:**
Die orangen Knoten wurden besucht und die grünen Knoten gelten als abgeschlossen und werden nicht weiter behandelt.
<br>
Die Zahlen an den Knoten sind die jeweiligen Kosten.


