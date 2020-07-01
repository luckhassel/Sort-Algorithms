class SortAlgorithms:
    """
    Cada método dessa classe contém um tipo de ordenação diferente. Eles
    são invocados através dos métodos da classe SortAlgorithms.
    """

    def mergeSort(self, arr):
        """
        Método merge sort. Basicamente, o algoritmo divide os elementos até que todos fiquem
        individualmente separados. Então ele irá comparando dois a dois, sempre fazendo assim grupos
        da ordem ordenados que serão comparados ao grupo que foi ordenado anteriormente.
        """
        if len(arr) > 1:
            mid = len(arr) // 2  # Acha o meio do vetor
            L = arr[:mid]  # Divide os elementos do array em duas metades
            R = arr[mid:]

            self.mergeSort(L)  # Ordena a primeira metade
            self.mergeSort(R)  # Ordena a segunda metade

            i = j = k = 0

            # Função auxiliar que copia os dados para vetor temporários L e R
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            # Essa funções auxiliares servem para verificar se algum elemento faltou
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def bubbleSort(self, arr):
        """
        Algoritmo simples porém ineficiente. Basicamente, ele percorre o array comparando-os
        dois a dois e verificando quem é menor. Assim ele percerre inúmeras vezes o vetor até que tudo
        esteja ordenado.
        """
        n = len(arr)

        # Passa por todos os elementos do vetor
        for i in range(n - 1):

            # Os últimos i elementos já estão no lugar
            for j in range(0, n - i - 1):

                # Passa pelo array de 0 até n-i-1
                # Swap if the element found is greater
                # Realiza a troca se o elementos achado for maior que o próximo
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def insertionSort(self, arr):

        # Traverse through 1 to len(arr)
        for i in range(1, len(arr)):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def quickSort(self, array):
        """
        A ordenação quicksort basicamente escolhe um pivô a cada "rodada" e vai ordenando os elementos
        ao seu redor. Ou seja, ele pega os elementos menores e passa para a esquerda e os maiores
        para a direita. Sendo assim, ele passa pelo vetor diversas vezes ordenando através desse pivô.
        """

        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]  # Cria um pivô
            for x in array:
                if x < pivot:
                    less.append(x)  # Vai anexando os elementos que são menores que o pivô
                elif x == pivot:
                    equal.append(x)  # Anexa os elementos iguais ao pivô
                elif x > pivot:
                    greater.append(x)  # Anexa os elementos maiores que o pivô
            return self.quickSort(less) + equal + self.quickSort(greater)  # Aqui ele junta as três listas e repete o processo
        else:
            return array

    def countSort(self, array1, max_val):
        """O algoritmo mais eficaz de todos. Basicamente, ele irá criar um array de posições
        e irá contar a quantidade de vezes que o elemento aparece. Após isso, ele irá cria um vetor com
        o número de posições do maior vetor seguinte e então começará a ordenação.
        """
        m = max_val + 1
        count = [0] * m

        for a in array1:
            # Contador de ocorrências
            count[a] += 1
        i = 0
        for a in range(m):
            for c in range(count[a]):
                array1[i] = a
                i += 1
