#Desert_Fox_Fenek

#Sortowanie przez wstawianie
def Ins_sort(L):
    for i in range(1,len(L)):
        P_el = L[i]                         # <- wyci�gamy i-t� warto�� ze zbioru
        j = i - 1                           # <- do zmiennej pomocniczej zapisujemy warto�� indeksu o jeden wcze�niej

        while j>=0 and L[j]>P_el:
            L[j+1] = L[j]                   # <- przesuwamy elementy do momentu znalezienia mniejszej liczby lub trafienia na pocz�tek listy
            j-=1

        L[j+1] = P_el                       # <- przypisanie warto�ci i-tej w nowe miejsce, od jej lewej strony nie ma ju� �adnej wi�kszej liczby

    return L

#Sortowanie przez wybieranie
def Sec_sort(L):
    for i in range(len(L)):
        m_id = i                            # <- ustawienie warto�ci naszego minimalnej warto�ci pod danym indeksem na na i
        
        for j in range(i+1,len(L)):         # <- szukamy najmniejszego elementu w naszej li�cie (mo�na zobaczy� jak zmiana z wyszukiwania liniowego na binarne zmieni czas dzia�ania)
            if L[m_id] > L[j]:
                m_id = j

        L[i], L[m_id] = L[m_id], L[i]       # <- zamiana pozycji

    return L



LPr_M = [22.4,3,5,2,1,0,-5,3.2,12,32,5.4,-2.5]    # <- ma�y zbi�r liczb do posortowania
LPo_I = Ins_sort(LPr_M)
LPo_S = Sec_sort(LPr_M)

print("Sortowanie przez wstawianie")
for i in LPo_I: print(i)

print("\nSortowanie przez wybieranie")
for i in LPo_S: print(i)
