#FIFO
import queue
changes = 0 #ilość stron które zamieniliśmy

class PageCell:
    def __init__(self, id):
        self.id = id        # id komórki
        self.content = []   # jakie strony mieliśmy w tej "komórce"
        self.page = "x"     # jakiej strony używamy w tej "komórce" pamięci ("x" = z niczego się nie korzystamy)
        self.first_use = -1 # kiedy zaczelismy korzystac z obecnej strony
        self.last_use = -1  # kiedy ostatni raz "odswiezylismy" obecną stronę


def display(objects):
    """
    Wyświetla na ekranie wszystkie strony, których używaliśmy w każdej komórce pamięci

    :param objects: tablica ze wszystkimi komórkami pamięci
    :type objects: List [object]

    :return: None
    """
    for obj in objects:
        print(obj.content)


def reading(num):
    """
    Zczytujemy dane z pliku testowego

    :param num: numer plika testowegoo
    :type num: int

    :return: Liczba komórek pamięci; kolejka składająca się z których stron używamy
    :rtype numCells: int
    :rtype q: queue.Queue
    """

    path = "tests/test" + str(num) + ".txt"
    numCells = 0
    q = queue.Queue()
    with open(path, 'r') as file:
        for line in file:
            if numCells == 0:
                numCells = int(line)
            else:
                s = line
                arr = list(map(int, s.split()))
                for el in arr:
                    q.put(int(el))
    return numCells, q


def calculate(q, cells):
    """
    funkcja segreguje strony z ktorych uzywamy i rozklada ich po komorkam pamięci wg algorytmu LRU


    :param q: kolejka z wykorzystaniem stron
    :param cells: komórki pamięci
    :return:
    """

    global changes

    curt = 0    # obecny czas
    while list(q.queue):

        page = q.get()      # bierzemy pierwszy element z kolejki (ten element sie usuwa z 'q' i się zapisuje w zmienną 'page')
        cur_pages = []      # tworzymy/czyścimy tablicę ze stronami których mamy w pamięci (na razie jest pusta)

        # patrzymy jakie strony zapisane w komórkach
        for cell in cells:
            cur_pages.append(cell.page)


        if page not in cur_pages:
            # w przypadku gdy nie mamy obecnej stony w żadnej komórce
            cells.sort(key=lambda x: (x.first_use, x.id))
            changes += 1

            # zmieniamy cechy komórki którą wybraliśmy jako "ofiarę"
            cells[0].content.append(page)               # dodajemy do "historii" tej komórki obecną stronę
            cells[0].first_use = curt                   # zmieniamy kiedy za pierwszym razem użyliśmy nowej strony
            cells[0].page = page                        # zmieniamy obecną stronę
            cells[0].last_use = curt                    # kiedy ostatni raz korzystaliśmy z obecnej strony (czyli teraz)
            for i in range(1, len(cells)):
                cells[i].content.append(cells[i].page)  # zapisujemy "historię" dla reszty komórek (ona się nie zmieniła wiec dodajemy ostatnią stronę)
        else:
            # przypadek gdy już mamy obecną stronę w pamięci
            cells.sort(key=lambda x: x.id)

            # sprawdzamy każdą komórkę, czy ona nam pasuje
            for index in range(len(cells)):
                if cells[index].page == page: # w przypadku jak ta komórka nam pasuje, no to tylko zmienimy kiedy ostatni raz używaliśmy z obecnej strony
                    cells[index].last_use = curt

                # w dowolnym przypadku (czy pasuje nam obecna komorka czy nie) zapisujemy w historii stronę
                cells[index].content.append(cells[index].page)
        curt += 1


def table(cells):
    """
    Funkcja do wyświetlania tak zwanego grafiku względem id komórki pamięci oraz czasu

    :param cells: tablica w której komórki pamięci (każda ma swoje cechy)
    :type cells: List[object]

    :return: None
    """
    l = len(cells[0].content) # długość grafiku
    cur_id = 1
    print("ID" + "| " + "_" * (l * 2 - 1))  # tworzymy "czapkę"
    for cell in cells:   # tworzymy dla każdej komórki swój id i wpisujemy całą historię w grafik
        print(cur_id, "| ", end='')
        for el in cell.content:
            print(el, '', end='')
        print()
        cur_id += 1


cells = []          # tworzymy pustą tablicę w której będą komórki pamięci
k = int(input("Wprowadź numer testu: "))
numCells, q = reading(k)        # zczytujemy dane

# zapisujemy
for i in range(numCells):
    cells.append(PageCell(i))

calculate(q, cells)

cells.sort(key=lambda x: x.id)
table(cells)
print("\nIlość zastępowanych stron: ", changes)
# display(cells)