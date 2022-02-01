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


# Wir erstellen eine Liste die sortiert werden soll
list = [20, 21, 13, 6, 85, 16]

# Hier geben wir unsere unsortierte liste in der Konsole aus
print("Unsortierte Liste: " + str(list))

# Diese Liste wird dann in unsere erstelle Funktion 
# übergeben und der Bubble Sort Algorithmus wird ausgeführt und sortiert die Liste
bubbleSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))
