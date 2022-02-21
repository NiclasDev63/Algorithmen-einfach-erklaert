# Tiefensuche (Depth First Search)

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

