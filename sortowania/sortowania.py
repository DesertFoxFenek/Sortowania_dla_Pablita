#Desert_Fox_Fenek

#Sortowanie przez wstawianie
def Ins_sort(L):
    for i in range(1,len(L)):
        P_el = L[i]                         # <- wyci¹gamy i-t¹ wartoœæ ze zbioru
        j = i - 1                           # <- do zmiennej pomocniczej zapisujemy wartoœæ indeksu o jeden wczeœniej

        while j>=0 and L[j]>P_el:
            L[j+1] = L[j]                   # <- przesuwamy elementy do momentu znalezienia mniejszej liczby lub trafienia na pocz¹tek listy
            j-=1

        L[j+1] = P_el                       # <- przypisanie wartoœci i-tej w nowe miejsce, od jej lewej strony nie ma ju¿ ¿adnej wiêkszej liczby

    return L

#Sortowanie przez wybieranie
def Sec_sort(L):
    for i in range(len(L)):
        m_id = i                            # <- ustawienie wartoœci naszego minimalnej wartoœci pod danym indeksem na na i
        
        for j in range(i+1,len(L)):         # <- szukamy najmniejszego elementu w naszej liœcie (mo¿na zobaczyæ jak zmiana z wyszukiwania liniowego na binarne zmieni czas dzia³ania)
            if L[m_id] > L[j]:
                m_id = j

        L[i], L[m_id] = L[m_id], L[i]       # <- zamiana pozycji

    return L



LPr_M = [22.4,3,5,2,1,0,-5,3.2,12,32,5.4,-2.5]    # <- ma³y zbiór liczb do posortowania
LPo_I = Ins_sort(LPr_M)
LPo_S = Sec_sort(LPr_M)

print("Sortowanie przez wstawianie")
for i in LPo_I: print(i)

print("\nSortowanie przez wybieranie")
for i in LPo_S: print(i)
