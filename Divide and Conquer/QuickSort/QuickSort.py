def partition(liste, low, high):
    pivot = liste[high]
    low_temp = low
    high_temp = high

    while low < high:

        while high > low_temp and liste[high] >= pivot:
            high -= 1
        
        while low < high_temp and liste[low] < pivot:
            low += 1
        
        if low < high:
            liste[low], liste[high] = liste[high], liste[low]
        
    if liste[low] > pivot:
        liste[high_temp], liste[low] = liste[low], liste[high_temp]

    return low



def quicksort(unsortierte_liste, low, high):

    if low < high:
        pivot = partition(unsortierte_liste, low, high)

        quicksort(unsortierte_liste, low, pivot - 1)

        quicksort(unsortierte_liste, pivot + 1, high)



list = [20, 21, 13, 6, 85, 16]

vorletzter_wert = len(list)-1

quicksort(list, 0, vorletzter_wert)

print(list)