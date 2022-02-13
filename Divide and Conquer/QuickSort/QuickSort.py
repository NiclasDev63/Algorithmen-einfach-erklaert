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

# ruft unsere Funktion mit der zu sortierenden Liste auf
quickSort(list)

# Hier geben wir unsere sortierte liste in der Konsole aus
print("Sortierte Liste: " + str(list))