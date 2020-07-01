from SortAlgorithms import SortAlgorithms
from random import randint
import time
import xls
ARRAY_LENGTH = [1000, 10000, 100000, 1000000, 10000000]


class SortAlgorithmsCallers:
    """
    O método do construtor dessa classe tem por objetivo criar um objeto da classe xls,
    bem como construir o arquivo e preenchelo com informações padrão.
    Todos os métodos dessa classe tem por objetivo chamar o algoritmo de ordenação
    já com os vetores aleatórios gerados. Além disso, em cada método o cronômetro é iniciado.
    Após isso, uma soma dos dez tempos é feita e então é retirada uma média delas.
    Com o resultado em mãos, esse valor é exportado para um Excel. Reiterando: Todos os métodos,
    aqui, exercem o mesmo papel, mudando apenas o algoritmo invocado.
    """

    def __init__(self):
        self.xls_builder = xls.XLS()
        self.xls_builder.build_xls()

    def merge_sort(self):
        time_array = {}
        mean_array = {}
        length = 0
        """Loop que percorre todas as quantidades de elementos contodos no array_length"""
        while length < len(ARRAY_LENGTH):
            sum = 0
            test_again = 0
            while test_again < 10:
                """Loop que percorre dez vezes o mesmo número de valores gerados para retirar a média"""
                arr = [randint(0, 1000) for i in range(ARRAY_LENGTH[length])]  # Gera um arr aleatório
                sort_algorithms = SortAlgorithms()  # Constroi um objeto do tipo SortAlgorithms
                start_time = time.time()  # Inicia o cronômetro
                sort_algorithms.mergeSort(arr)  # Executa ordenação
                time_array[test_again] = time.time() - start_time  # Termina o cronômetro e armazena o tempo
                sum += time_array[test_again]  # Cria um vetor de soma dos tempos
                test_again += 1
            mean_array[length + 2] = sum / 10  # Cria um vetor de média dos tempos
            length += 1

        self.xls_builder.write_mean_value('2', mean_array)  # Exporta para o Excel o vetor de médias

    """Executa o mesmo processo acima, porém invoca o método bubble sort"""
    def bubble_sort(self):
        time_array = {}
        mean_array = {}
        length = 0
        while length < len(ARRAY_LENGTH):
            sum = 0
            test_again = 0
            while test_again < 10:
                arr = [randint(0, 10) for i in range(ARRAY_LENGTH[length])]
                sort_algorithms = SortAlgorithms()
                start_time = time.time()
                sort_algorithms.bubbleSort(arr)
                time_array[test_again] = time.time() - start_time
                sum += time_array[test_again]
                test_again += 1
            mean_array[length + 2] = sum / 10
            length += 1

        self.xls_builder.write_mean_value('3', mean_array)

    """Executa o mesmo processo acima, mas agora invoca o método insertion sort"""
    def insertion_sort(self):
        time_array = {}
        mean_array = {}
        length = 0
        while length < len(ARRAY_LENGTH):
            sum = 0
            test_again = 0
            while test_again < 10:
                arr = [randint(0, 1000) for i in range(ARRAY_LENGTH[length])]
                sort_algorithms = SortAlgorithms()
                start_time = time.time()
                time_array[test_again] = sort_algorithms.insertionSort(arr)
                time_array[test_again] = time.time() - start_time
                sum += time_array[test_again]
                test_again += 1
            mean_array[length + 2] = sum / 10
            length += 1

        self.xls_builder.write_mean_value('4', mean_array)

    """Executa o mesmo método acima, mas agora invoca o método quick sort"""
    def quick_sort(self):
        time_array = {}
        mean_array = {}
        length = 0
        while length < len(ARRAY_LENGTH):
            sum = 0
            test_again = 0
            while test_again < 10:
                arr = [randint(0, 1000) for i in range(ARRAY_LENGTH[length])]
                sort_algorithms = SortAlgorithms()
                start_time = time.time()
                sort_algorithms.quickSort(arr)
                time_array[test_again] = time.time() - start_time
                sum += time_array[test_again]
                test_again += 1
            mean_array[length + 2] = sum / 10
            length += 1

        self.xls_builder.write_mean_value('5', mean_array)

    """Executa o mesmo método acima, mas agora invoca o método quick sort"""
    def counting_sort(self):
        time_array = {}
        mean_array = {}
        length = 0
        while length < len(ARRAY_LENGTH):
            sum = 0
            test_again = 0
            while test_again < 10:
                arr = [randint(0, 1000) for i in range(ARRAY_LENGTH[length])]
                sort_algorithms = SortAlgorithms()
                start_time = time.time()
                """Para o count sort, é passado além do arr o máximo valor encontrado nele"""
                sort_algorithms.countSort(arr, max(arr))
                time_array[test_again] = time.time() - start_time
                sum += time_array[test_again]
                test_again += 1
            mean_array[length + 2] = sum / 10
            length += 1

        self.xls_builder.write_mean_value('6', mean_array)
        self.xls_builder.close_sheet()
