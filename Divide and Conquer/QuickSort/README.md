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

**6.)** Die vorherigen Schritte werden solange wiederholt, bis low nicht mehr kleiner als high ist.

![image](https://user-images.githubusercontent.com/83044113/154836884-9b5fb71f-0ce9-451b-b8fc-f9a536916bdb.png)

Durch diesen Schritt haben wir erreicht, das auf der Linken Seite des pivot Elements alle Werte die kleiner und auf der Rechten Seite alle die größer sind stehen.

**7.)** Die Liste wird am pivot Element geteilt und alle Schritte werden erneut für die Teillisten ausgeführt.

![image](https://user-images.githubusercontent.com/83044113/154837148-3ff3c714-c9c3-4c09-94f1-b9792d911a82.png)

**8.)** Zum Schluss werden alle Teillisten zu einer sortierten Liste zusammengefügt

![image](https://user-images.githubusercontent.com/83044113/154837277-0d1f7adf-a551-486e-a1bb-f601fbec7546.png)

<br>
<br>

### Code Beispiel

```python
"""

Anfang des Algorithmus

"""
# In dieser Funktion wird das eigentlich
# Sortieren der Liste durchgeführt
def partition(liste, low, high):

    # Hier initialisieren wir unser pivot Element
    pivot = liste[high]

    # Hier erstellen wir eine Kopie unseres low wertes
    low_temp = low

    # Hier erstellen wir eine Kopie unseres high wertes
    high_temp = high

    # erste Schleife
    # Diese Schleife wird solange ausgeführt,
    # bis low nicht mehr kleiner als high ist
    while low < high:


        # zweite Schleife
        # Diese Schleife wird ausgeführt solange
        # high größer als der ursprüngliche Wert von low ist UND
        # das Element an der Stelle high größer oder gleich dem pivot Element ist
        while high > low_temp and liste[high] >= pivot:

            # Hier wird high bei jedem Durchlauf um 1 reduziert
            high -= 1
        
        # dritte Schleife
        # Diese Schleife wird ausgeführt solange
        # low kleiner als der ursprüngliche Wert von high ist UND
        # das Element an der Stelle low kleiner als das pivot Element ist
        while low < high_temp and liste[low] < pivot:

            # Hier wird low bei jedem Durchlauf um 1 erhöht
            low += 1
        
        # Hier wird überprüft, ob low kleiner als high ist.
        # Falls dies der Fall ist, werden die Elemente aus der Liste an der Stelle
        # low und high vertauscht
        if low < high:
            liste[low], liste[high] = liste[high], liste[low]

    # Nachdem alleine Schleife durchlaufen sind, überprüfen wir
    # ob Liste an der Stelle low kleiner ist als unser pivot Element.
    # Falls dies der Fall ist, werden die Elemente aus der Liste an der Stelle
    # low und an dem ursprünglichen high wert vertauscht
    if liste[low] > pivot:
        liste[high_temp], liste[low] = liste[low], liste[high_temp]

    # Zum Schluss geben wir hiermit den low Wert zurück
    return low


# Das ist unsere Hauptfunktion, in der Quick Sort implementiert wird
def quickSort(unsortierte_liste, low, high):

     # Hier wird überprüft, ob low kleiner als high ist.
    if low < high:

        # Hier rufen wir unsere sortier Methode auf und weisen der Variable
        # "pivot" den zurückgegebenen Wert zu
        pivot = partition(unsortierte_liste, low, high)

        # Hier rufen wir zuerst mit der einen Hälfte der Liste und
        # danach mit der anderen Hälfte der Liste unsere quicksort Methode auf
        quickSort(unsortierte_liste, low, pivot - 1)
        
        quickSort(unsortierte_liste, pivot + 1, high)
"""

Ende des Algorithmus

"""       




# Wir erstellen eine Liste die sortiert werden soll
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# Der Startindex unserer Liste
low = 0

# Das letzte Element unserer Liste
high = len(list)-1

# ruft unsere Funktion mit der zu sortierenden Liste auf
quickSort(list, low, high)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))
```
<br>
**Da alle Schritte meiner Meinung nach bereits sehr ausführlich behandelt wurden, werde ich nicht genauer auf den Code eingehen.**







