def quicksort(arr, left, right):
  """
  Função para ordenar uma lista usando o algoritmo QuickSort.

  Args:
  arr (list): A lista de elementos a ser ordenada.
  left (int): O índice inicial da parte da lista a ser ordenada.
  right (int): O índice final da parte da lista a ser ordenada.

  Retorna:
  None: A lista é ordenada no lugar.
  """
  if left < right:
    # Encontra o índice do pivô após a partição
    pi = partition(arr, left, right)
    # Ordena recursivamente a sublista à esquerda do pivô
    quicksort(arr, left, pi - 1)
    # Ordena recursivamente a sublista à direita do pivô
    quicksort(arr, pi + 1, right)

def partition(arr, left, right):
  """
  Função auxiliar para realizar a partição da lista em relação a um pivô.

  Args:
  arr (list): A lista de elementos a ser particionada.
  left (int): O índice inicial da parte da lista a ser particionada.
  right (int): O índice final da parte da lista a ser particionada (também é o índice do pivô).

  Retorna:
  int: O índice do pivô na lista particionada.
  """
  # Define o pivô como o último elemento da lista
  pivot = arr[right]
  # Inicializa o índice do menor elemento
  i = left - 1
  
  # Percorre a lista da esquerda para a direita
  for j in range(left, right):
    # Se o elemento atual é menor ou igual ao pivô
    if arr[j] <= pivot:
      # Incrementa o índice do menor elemento
      i = i + 1
      # Troca os elementos arr[i] e arr[j]
      arr[i], arr[j] = arr[j], arr[i]
  
  # Troca o elemento na posição i+1 com o pivô
  arr[i + 1], arr[right] = arr[right], arr[i + 1]
  # Retorna o índice do pivô
  return i + 1

# Descrição das Funções
# quicksort(arr, left, right):

# Ordena a lista arr no intervalo de índices left a right usando o algoritmo QuickSort.
# Recursivamente chama a si mesma para ordenar as sublistas à esquerda e à direita do pivô.
# partition(arr, left, right):

# Realiza a partição da lista arr em relação ao elemento arr[right] (pivô).
# Reorganiza a lista de modo que todos os elementos menores ou iguais ao pivô fiquem à esquerda dele, e todos os elementos maiores, à direita.
# Retorna o índice do pivô após a partição.
# Notas
# O QuickSort é um algoritmo de ordenação com complexidade média de tempo de O(n log n), mas pode chegar a O(n²) no pior caso.
# Este algoritmo é "in-place", o que significa que a ordenação é feita diretamente na lista original, sem necessidade de espaço adicional significativo.