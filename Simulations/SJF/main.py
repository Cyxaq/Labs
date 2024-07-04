# SJF

class Process:
#jakie cechy przyjmuje objekt
    def __init__(self, pid, arrival, pr_time):
        #cechy o ktorych wiemy na poczatku
        self.pid = pid          # od process_id (id procesu)
        self.arrival = arrival  # od arrival_time (kiedy sie pojawil)
        self.pr_time = pr_time  # od processing_time (ile czasu jest potrzebne na przetwarzanie)

        #cechy ktore obliczymy
        self.started = 0        # kiedy sie zaczal (w rzeczywistosci)
        self.wait = 0           # ile czasu czekal
        self.end = 0            # kiedy sie skonczyl (w rzeczywistosci)
        self.done = False       # czy sie skonczyl? (false=Nie, True=tak)


#funkcja na wyswietlenie wszystkich informacji o procesie
def displayProcessInfo(objects):
    for object in objects:
        print(object.pid, object.wait, object.arrival, object.pr_time, object.started, object.end, object.wait)

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

def sorting_sjf(pr):
    curt = 0
    pr.sort(key=lambda x: (x.arrival, x.pr_time))
    sorted_obj_arr = []

    while 0 < len(pr):
        i = 0

        while pr[0].arrival > curt:
            curt += 1
        min_pr_time = pr[0].pr_time
        ans_obj = pr[i]
        de = 0

        while pr[i].arrival <= curt:
            if pr[i].pr_time < min_pr_time:
                min_pr_time = pr[i].pr_time
                ans_obj = pr[i]
                de = i
            if pr[i].pr_time == min_pr_time and pr[i].pid < ans_obj.pid:
                de = i
                ans_obj = pr[i]

            if i < len(pr) - 1:
                i += 1
            else:
                break
        sorted_obj_arr.append(ans_obj)
        curt += ans_obj.pr_time
        pr.pop(de)
    return sorted_obj_arr





#obliczenia cechy
def calculate(pr):
    cur_time = 0
    for obj in pr:
        #pozbywamy przypadku gdy process sie zaczal przed tym jak wpadl
        if cur_time < obj.arrival:
            cur_time = obj.arrival
        #obliczamy cechy
        obj.started = cur_time
        obj.end = cur_time + obj.pr_time
        obj.wait = obj.started - obj.arrival
        obj.done = True
        #zmieniamy terazniejszy czas
        cur_time += obj.pr_time

#funkcja na graficzne przedstawienie odpowiedzi
def graphics(pr):
    print('\nLegenda: \n"-" : proces czeka \n"#" : proces się wykonuje \n"." : proces został wykonany albo jescze nie przyszedł \n')
    l = max(pr[i].end for i in range (len(pr)))              #"dlugosc" wykresu
    maxid = max(pr[i].pid for i in range (len(pr)))
    print("ID"+" "*(len(str(maxid))-1)+"|_"+"_"*l)           #"czapka"
    for obj in pr:
        t = l-obj.arrival-obj.wait-obj.pr_time               # ile czasu zostanie po wykonaniu procesu
        spacje = " "*(len(str(maxid)) - len(str(obj.pid)))   #dodajemy spacje aby kreski byly w jednym slupie

        #budowanie tak zwanej linii wykresu dla podanego procesa
        s = spacje+str(obj.pid)+" | "+("."*obj.arrival)+("-"*obj.wait)+("#"*obj.pr_time)+("."*t)
        print(s)


#statystyka
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


#posortujemy procesy wg zasady SJF
sorted_processes = sorting_sjf(arr_of_obj)

#obliczamy takie cechy jak: kiedy sie zaczal, ile czekal etc.
calculate(sorted_processes)

#sortujemy wg id (dla wykresu)
sorted_processes.sort(key=lambda x: x.pid)

processes = sorted_processes
#tworzymy wykres i wyswietlamy
graphics(processes)

statistics(processes)

#--------------------OPCJONALNIE----------------------
# wyswietlenie informacji o procesach
# (id, moment_przyjęcia, czas_na_przetworzanie, czas_gdy_sie_zaczął, czas_gdy_się_skończył)

displayProcessInfo(processes)

