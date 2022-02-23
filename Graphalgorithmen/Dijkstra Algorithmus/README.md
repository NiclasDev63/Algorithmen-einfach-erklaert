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

![image](https://user-images.githubusercontent.com/83044113/155377511-a76a116e-da07-4fa8-b0f1-cafc031855fe.png)


**Anmerkung:**
Die orangen Knoten wurden besucht und die grünen Knoten gelten als abgeschlossen und werden nicht weiter behandelt.
<br>
Die Zahlen an den Knoten sind die jeweiligen Kosten.

**2.)** Nun schauen wir uns den 7 Knoten an und besuchen alle Knoten, die von diesem aus erreichbar sind.
Anschließend wir auch dieser abgeschlossen.

![image](https://user-images.githubusercontent.com/83044113/155377274-0e6a732e-6426-466d-befb-61e92dad776b.png)

**3.)** Jetzt besuchen wir alle Knoten, welche von dem 1 Knoten aus erreichbar sind und schließen diesen ab.

![image](https://user-images.githubusercontent.com/83044113/155377986-a6a9aba9-ae43-4b4f-84de-959eddce30d1.png)

**4.)** Nun wiederholen wir die vorherige Schritte von unserem 2 Knoten aus und überprüfen beim besuchen von Knoten, ob es einen kostengünstigeren Weg gibt.

![image](https://user-images.githubusercontent.com/83044113/155378706-995a4eaa-9e56-496a-b9b0-c6c3f723c6e4.png)

Hier haben wir einen günstigeren Weg gefunden und updaten die Kosten des 8 Knoten von 15 auf 14.

**Diese Schritte werden wiederholt, bis alle Knoten abgeschlossen und die günstigen Kosten jedes Knoten berechnet wurden.**
<br>
<br>
**Zum Schluss sieht der Graph wie folgt aus:**

![image](https://user-images.githubusercontent.com/83044113/155380045-662312f2-220d-46ef-80b4-1464c9d18b52.png)

**WEITERES BEISPIEL:**

![image](https://user-images.githubusercontent.com/83044113/155380372-dd46c892-af36-416d-aec0-4c1a32c78c4f.png)





