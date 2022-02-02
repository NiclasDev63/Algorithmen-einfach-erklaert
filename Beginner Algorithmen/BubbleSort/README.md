# Bubblesort

Dieser Algorithmus gehört zu den einfacheren und ist in der regel einer der ersten, die man lernt.
Er dient zum sortieren von Listen.
<br>
### Laufzeitkomplexität:

**Im schlimmsten Fall**: O(n²)<br>
**Im Normalfall**: O(n²)<br>
**Im Optimalfall**: O(n) (Dieser Fall tritt nur auf, wenn die Liste bereits sortiert ist.)<br>

### Platzkomplexität
Die Platzkomplexität beträgt O(1), da das Sortieren der Liste In-Place durchgeführt wird.
<br>
Im Folgenden werde ich dir die Funktionsweise des Bubble Sort Algorithmus anhand von Python Code und Illustrationen näher erleutern.
<br>
### Funktionsweise
Der Algorithmus beginnt beim ersten Element der Liste und überprüft jedes Mal aufs neues, ob das aktuelle Element größer ist als das darauf folgende.
Falls dies der Fall ist, werden die beiden Element getauscht und es geht weiter.
Falls dies nicht zutrifft, bleibt das aktuelle Element an derselben Stelle und wir fahren mit dem nächsten Element fort.
Einfach gesagt, schiebt der Algorithmus das Element an der Stelle n soweit ans Ende der Liste, bis das Element an der Stelle n+1, also das nächste Element größer ist.
Das Element, welches an letzter Stelle der Liste steht ist das größte und wird "eingefrohren".
<br>
<br>
Um dir dies einmal visuell zu veranschaulichen, habe ich eine kleine Illustration angefertigt.
Hierbei wird der Kasten des Elements orange eingefärbt, welches "eingefrohen" wurde.<br>
Das "i" neben den Kästchen gibt an, der wievielte Schleifendurchlauf es ist.<br>
(In der Informatik fängt man ab der 0 an zu zählen, weshalb wir bei i=0 beginnen)
<br>
<br>

![image](https://user-images.githubusercontent.com/83044113/151702325-27d2b846-b6b1-402c-b3f1-e5266ed2684f.png)

<br>
<br>
Nun schauen wir uns eine Implementierung des Algorithmus in Python an.
<br>
<br>

```python
"""                
Anfang des Algorithmus
"""

def bubbleSort(list):

    # n entspricht der Länge der Liste
    n = len(list)

    # Hier beginnt die erste schleife
    # Diese startet bei 0 und geht bis n-1
    for i in range(n):
        
        # Hier beginnt die zweite Schleife.
        # Diese schleife geht jedoch nur bis n-i-1
        for j in range(n-i-1):

            # Hier wird überprüft ob das Element an der Stelle j größer ist, als das Element eins weiter vorne.
            # Falls dies der Fall ist, werden die Elemente getauscht
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                
                      """                
                      Ende des Algorithmus
                      """


# Wir erstellen eine Liste die sortiert werden soll
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# Diese Liste wird dann in unsere erstelle Funktion 
# übergeben und der Bubble Sort Algorithmus wird ausgeführt und sortiert die Liste
bubbleSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))
```
<br>
<br>
Nun gehe ich auf einzelne Abschnitte des Codes ein, um mögliche Fragen direkt zu klären.
<br>
<br>

```python
 # Hier beginnt die erste schleife
 # Diese startet bei 0 und geht bis n-1
 for i in range(n):
        
    # Hier beginnt die zweite Schleife.
    # Diese schleife geht jedoch nur bis n-i-1
    for j in range(n-i-1):
```
<br>
<br>
Nun wirst du dich vielleicht vielleicht fragen, wieso geht die zweite Schleife bis n-i-1 und nicht ebenfalls bis n wie die erste.
Falls dies der Fall ist, würde ich dir empfehlen, noch einmal die oben eingefügte Illustration anzuschauen.
Wie man dort unschwer erkennen kann, wird ja immer das letzte Element "eingefrohren" und genau das erreichen wir mit n-1.
Gehen wir mal eine paar Schleifendurchläufe gemeinsam durch.
<br>
<br>
Durchlauf 1:<br> i = 0<br>
             n = 6 (Länge der Liste)<br>
             j macht 5 Durchläufe (6-0-1) (startet bei 0 und geht bis 4)
<br>
<br>             
Durchlauf 2:<br> i = 1<br>
             n = 6 (Länge der Liste)<br>
             j macht 4 Durchläufe (6-1-1) (startet bei 0 und geht bis 3)
<br>
<br>             
Durchlauf 3:<br> i = 2<br>
             n = 6 (Länge der Liste)<br>
             j macht 3 Durchläufe (6-2-1) (startet bei 0 und geht bis 2)
<br>
<br>
Jetzt denkst du dir wahrscheinlich okay, ich weiß jetzt wieso die zweite Schleife nur bis n-j geht, aber was ist mit der -1
<br>
Darauf gehe ich im folgenden Codeabschnitt ein.
<br>
<br>

```python
# Hier wird überprüft ob das Element an der Stelle j größer ist, als das Element eins weiter vorne.
# Falls dies der Fall ist, werden die Elemente getauscht
if list[j] > list[j+1]:
    list[j], list[j+1] = list[j+1], list[j]
```
<br>
<br>
Wie sich hieraus relativ unschwer erkennen lässt, wird das aktuelle Element n, immer mit dem nächsten Element n+1 verglichen.
Wenn man jedoch bereits am Ende der Liste angekommen ist und dieser Vergleich trotzdem durchgeführt wird, entsteht eine sogenannte "list index out of range" Exception, was auf Deutsch übersetzt einfach bedeutet, das es einen Fehler gibt und dein Programm abstürzt.
Das passiert, da man das Letzte Element in der Liste mit dem Nächsten vergleicht, obwohl kein nächstes existiert.
<br>
<br>
