def pesquisa_binaria(nums, target):
  """
  Função para realizar uma busca binária em uma lista ordenada.

  Args:
  nums (list): Lista de elementos ordenados onde o 'target' será procurado.
  target (int, float, etc.): O valor a ser procurado na lista 'nums'.

  Retorna:
  int: O índice do 'target' na lista 'nums' se encontrado, caso contrário, retorna -1.
  """
  low = 0
  high = len(nums) - 1

  while low <= high:
    # Calcula o índice do meio da lista
    mid = int((low + high) / 2)
    
    # Se o elemento do meio é o target, retorna o índice
    if nums[mid] == target:
      return mid
    # Se o elemento do meio é maior que o target, ajusta o high
    elif nums[mid] > target:
      high = mid - 1
    # Se o elemento do meio é menor que o target, ajusta o low
    elif nums[mid] < target:
      low = mid + 1

  # Retorna -1 se o target não for encontrado
  return -1

# Exemplo de uso da função pesquisa_binaria
arr = [5]
target = pesquisa_binaria(arr, 5)
print(target)  # Saída: 0

# Descrição das Funções
# Função pesquisa_binaria(nums, target):
# Realiza uma busca binária na lista ordenada nums para encontrar o valor target.
# Argumentos:
# nums: Uma lista de elementos ordenados onde o target será procurado.
# target: O valor a ser procurado na lista nums.
# Retorna:
# O índice do target na lista nums se encontrado. Caso contrário, retorna -1.
# Passo a Passo do Código
# Inicialização: Define os ponteiros low e high como os índices inicial e final da lista, respectivamente.
# Laço While: Continua enquanto low for menor ou igual a high. Isso assegura que ainda existem elementos para serem verificados.
# Cálculo do Meio: Calcula o índice do meio da lista como mid = int((low + high) / 2).
# Verificação do Meio:
# Se nums[mid] for igual ao target, retorna o índice mid.
# Se nums[mid] for maior que o target, o high é ajustado para mid - 1, eliminando a metade superior da lista.
# Se nums[mid] for menor que o target, o low é ajustado para mid + 1, eliminando a metade inferior da lista.
# Retorno Final: Se o target não for encontrado na lista, a função retorna -1.
# Exemplo de Uso
# O código de exemplo cria uma lista arr com um único elemento [5] e chama a função pesquisa_binaria para encontrar o índice do valor 5. A saída é 0, indicando que o target foi encontrado na posição 0 da lista.
# Esse algoritmo é eficiente, especialmente para listas grandes, pois tem uma complexidade de tempo O(log n), o que significa que o número de comparações necessárias cresce lentamente à medida que o tamanho da lista aumenta.