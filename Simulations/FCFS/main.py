#FCFS
class Process:
#jakie cechy przyjmuje objekt
    def __init__(self, pid, arrival, pr_time):
        self.pid = pid          # od process_id (id procesu)
        self.arrival = arrival  # od arrival_time (kiedy sie pojawil)
        self.pr_time = pr_time  # od processing_time (ile czasu jest potrzebne na przetwarzanie)

        self.started = 0        # kiedy sie zaczal (w rzeczywistosci)
        self.wait = 0           # ile czasu czekal
        self.end = 0            # kiedy sie skonczyl (w rzeczywistosci)
        self.done = False       # czy sie skonczyl? (false=Nie, True=tak)


#funkcja na wyswietlenie wszystkich informacji o procesie
    def displayProcessInfo(self,object):
        print(str(object.pid)+ "    "+str(object.wait)+ "    "+str(object.arrival)+ "    "+str(object.pr_time)+ "    "+str(object.started)+ "    "+str(object.end))

#zczytywanie danych z plika (pliki testowe są w folderze "tests" i maja nazwe testX.txt, gdzie X to numer testu
def reading(filename):


    path = "tests/"+filename  # budujemy sciezke
    processes = []            # tu beda objekty, czyli procesy

    #odczyt z plika
    with open(path, 'r') as file:
        for line in file:
            s = line
            pid, arrival, pr_time = map(int, s.split())
            processes.append(Process(pid, arrival, pr_time))  # dodajemy odczytany objekt do listy
    return processes


#obliczenia
def calculate(pr):
    cur_time = 0
    for i in range(len(pr)):         #dla każdego procesu
        while pr[i].done == False:   #dopoki on nie bedzie wykonany
            if cur_time >= pr[i].arrival:

                #obliczenia kiedy sie zacznie proces, kiedy sie skonczy, ile czasu czekał, etc.
                pr[i].started = cur_time
                pr[i].end = pr[i].pr_time + pr[i].started
                pr[i].wait = pr[i].started - pr[i].arrival
                pr[i].done = True
                cur_time = pr[i].end
            else:
                cur_time += 1

#funkcja na graficzne przedstawienie odpowiedzi
def graphics(pr):
    l = max(pr[i].end for i in range (len(pr)))              #"dlugosc" wykresu
    maxid = max(pr[i].pid for i in range (len(pr)))
    print("ID"+" "*(len(str(maxid))-1)+"|_"+"_"*l)           #"czapka"
    for obj in pr:
        t = l-obj.arrival-obj.wait-obj.pr_time               # ile czasu zostanie po wykonaniu procesu
        spacje = " "*(len(str(maxid)) - len(str(obj.pid)))   #dodajemy spacje aby kreski byly w jednym slupie

        #budowanie tak zwanej linii wykresu dla podanego procesa
        s = spacje+str(obj.pid)+" | "+("."*obj.arrival)+("-"*obj.wait)+("#"*obj.pr_time)+("."*t)
        print(s)


def statistics(objects):
    avg_waiting = 0
    for obj in objects:
        avg_waiting += obj.wait
    avg_waiting /= len(objects)
    print("\nŚrednia długość oczekiwania: ",avg_waiting)
    print("Czas który potrzebujemy aby wykonać wszystkie procesy: ", max(objects[i].end for i in range (len(objects))))
    print("Suma czasu, potrzebnego na wykonanie wszystkich procesów: ", sum(objects[i].pr_time for i in range (len(objects))))



filename = str(input("Wprowadz numer plika testowego: "))

filename = "test"+str(filename)+".txt"  #tworzymy nazwe plika (np. test1.txt)

arr_of_obj = reading(filename)          #odczytujemy dane z danego testu

#sortujemy wg zasady "kiedy otrzymaliśmy ten proces
# (jak otrzymalismy wiecej niz jeden proces w tym samym czasie no to patrzymy na id procesu:
# im mniejsze id tym wieksze pierwszenstwo)"
arr_of_obj.sort(key=lambda x: (x.arrival, x.pid))


#obliczmy kiedy sie zacznie proces itd
calculate(arr_of_obj)

#sortujemy wg id (dla wykresu)
arr_of_obj.sort(key=lambda x: x.pid)

#tworzymy wykres i wyswietlamy
graphics(arr_of_obj)

statistics(arr_of_obj)



#--------------------OPCJONALNIE----------------------
# wyswietlenie informacji o procesach
# (id, moment_przyjęcia, czas_na_przetworzanie, czas_gdy_sie_zaczął, czas_gdy_się_skończył)


for obj in arr_of_obj:
    obj.displayProcessInfo(obj)

