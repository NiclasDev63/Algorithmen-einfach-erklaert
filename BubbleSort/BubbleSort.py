def bubbleSort(list):

    # n entspricht der Länge der Liste
    n = len(list)

    """
    Hier beginnt die erste Schleife.
    Die schleife start bei 0 und geht bis n-1.
    Nach jedem durchlauf erhöhrt sich i um den Wert 1, also
    Durchlauf 1: i = 0
    Durchlauf 2: i = 1
    Durchlauf 3: i = 2
    ...
    Durchlauf n: i = n-1
    """
    for i in range(n):


        for j in range(n-i-1):

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
