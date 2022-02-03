"""

Anfang des Algorithmus

"""
                        
def insertionSort(list):

    # n = Länge der übergebenen Liste
    n = len(list)

    # erste Schleife
    # startet bei 1 und geht bis n-1
    for i in range(1, n):

        # ist das aktuelle Element, welches mit seinem Vorgänger verglichen wird
        aktuelles_element = list[i]


        # j ist der Vorgänger, der mit dem aktuellen Element verlgichen wird
        j = i-1

        # zweite Schleife
        # wird ausgeführt, solange j größer oder gleich 0 ist UND das aktuelle Element kleiner als sein Vorgänger ist
        while j >= 0 and aktuelles_element < list[j]:
            list[j + 1] = list[j]

            # reduziert den j Wert bei jedem Durchlauf durch die zweite Schleife um 1
            j -= 1
        
        # Fügt das aktuelle Element an die richtige Position ein
        list[j + 1] = aktuelles_element

"""

Ende des Algorithmus

"""



# die unsortierte Liste
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# ruft unsere Funktion mit der zu sortierenden Liste auf
insertionSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))