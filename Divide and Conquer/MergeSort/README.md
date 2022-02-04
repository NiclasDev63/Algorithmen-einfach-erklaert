# Mergesort
Mergesort gehört zu den fortgeschritteneren Sortieralgorithmen und ist dank Divide and Conquer wesentlich schneller als bspw. Bubble- oder Insertionsort.

### Laufzeitkomplexität:

**Im schlimmsten Fall**: O( n log(n) )<br>
**Im Normalfall**: O( n log(n) )<br>
**Im Optimalfall**: O( n log(n) )

### Platzkomplexität
Die Platzkomplexität beträgt O(n).<br>
Hier wird das Sortieren der Liste **NICHT** In-Place durchgeführt wird.

### Funktionsweise
**1.)** Die Länge der Liste wird durch zwei geteilt und abgerundet, um so die Mitte zu bestimmen.<br>
**2.)** Der Algorithmus wird zuerst mit der linken Hälfte der Liste aufgerufen und danach mit der Rechten.<br>
Dies passiert so lange, bis die beiden Hälften in ihre Einzelteile zerlegt wurden.<br>
**3.)** Anschließend werden alle Teile in der richtigen Reihenfolge wieder zusammengefügt.
<br>
<br>
Im Folgenden habe ich ein Bild eingefügt, welches den ganzen Vorgang mit unserer Liste noch einmal visuell darstellt.
<br>
<br>

![image](https://user-images.githubusercontent.com/83044113/152532577-b5b1cd07-eb3a-402f-82ef-455e2d633c63.png)
<br>
<br>
Nun schauen wir uns eine Implementierung des Algorithmus in Python an.
```python
"""

Anfang des Algorithmus

"""
def mergeSort(list):

    # überprüft, ob die Länge der übergebenen Liste größer als 1 ist
    if len(list) > 1:

        # länge der Liste
        n = len(list)

        # mitte der Liste
        mitte = n //2
        
        # linke hälfte der Liste
        linke_haelfte = list[:mitte]

        # rechte hälfte der Liste
        rechte_haelfte = list[mitte:]

        # ruft die Funktion mit der linke Hälfte der Liste auf und sortiert diese
        mergeSort(linke_haelfte)

        # ruft die Funktion mit der linken Hälfte der Liste auf und sortiert diese
        mergeSort(rechte_haelfte)

        # initialisiert die vairablen i, j und k und setzt den Startwert dieser auf 0
        i =  j = k = 0

        # erste Schleife
        # Diese Schleife wir solange durchlaufen, bis i größer oder gleich der Länge von der
        # linken Hälfte ist oder bis j größer oder gleich der Länge von der rechten Hälfte ist
        while i < len(linke_haelfte) and j < len(rechte_haelfte):

            # Wenn das Element, welches sich an der i Stelle von der linken Hälfte befindet
            # größer ist als das Element an der j Stelle der rechten Hälfte, bekommt unsere
            # übergebene Liste an der Stelle k den Wert zugewiesen, der sich an der i Stelle von der linken Hälfte befindet
            # und der Wert i erhöht sich um 1
            if linke_haelfte[i] < rechte_haelfte[j]:
                list[k] = linke_haelfte[i]
                i += 1

            # Ansonsten bekommt unsere übergebene Liste an der Stelle k den Wert zugewiesen,
            # der sich an der j Stelle von der rechten Hälfte befindet und der Wert j erhöht sich um 1    
            else:
                list[k] = rechte_haelfte[j]
                j += 1

            # Nach jedem Schleifendurchlauf wird der Wert k um 1 erhöht    
            k += 1

        # zweite Schleife
        # Hierdurch wird überprüft, ob sich noch ein Element in der linken Hälfte befindet,
        # welches noch nicht bei unserer übergebenen List einsortiert wurde
        while i < len(linke_haelfte):
            list[k] = linke_haelfte[i]
            k += 1
            i += 1
        
        # dritte Schleife
        # Hierdurch wird überprüft, ob sich noch ein Element in der rechten Hälfte befindet,
        # welches noch nicht bei unserer übergebenen List einsortiert wurde
        while j < len(rechte_haelfte):
            list[k] = rechte_haelfte[j]
            k += 1
            j += 1
"""

Ende des Algorithmus

"""            


# Wir erstellen eine Liste die sortiert werden soll
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# Diese Liste wird dann in unsere erstelle Funktion 
# übergeben und der Bubble Sort Algorithmus wird ausgeführt und sortiert die Liste
mergeSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))
```


<br>
<br>

**Quellen:**<br>
https://www.geeksforgeeks.org/merge-sort/
