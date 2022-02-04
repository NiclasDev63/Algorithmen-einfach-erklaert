def mergeSort(list):
    if len(list) > 1:

        # Länge der Liste
        n = len(list)

        # Mitte der Liste
        mitte = n //2
        
        # Linke hälfte der Liste
        linke_haelfte = list[:mitte]

        # Rechte hälfte der Liste
        rechte_haelfte = list[mitte:]

        mergeSort(linke_haelfte)

        mergeSort(rechte_haelfte)

        i =  j = k = 0

        while i < len(linke_haelfte) and j < len(rechte_haelfte):

            if linke_haelfte[i] < rechte_haelfte[j]:
                list[k] = linke_haelfte[i]
                i += 1

            else:
                list[k] = rechte_haelfte[j]
                j += 1

            k += 1
        
        while i < len(linke_haelfte):
            list[k] = linke_haelfte[i]
            k += 1
            i += 1
        
        while j < len(rechte_haelfte):
            list[k] = rechte_haelfte[j]
            k += 1
            j += 1



list = [2, 23, 5, 331, 7, 22, 8787, 1, 3, 34, 2]
mergeSort(list)
print(list)
    


