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
