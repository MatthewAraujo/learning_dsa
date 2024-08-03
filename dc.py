def soma_recursive(arr):
  if arr == []:
    return 0
  soma = arr[len(arr)-1]
  arr.pop()
  return soma  + soma_recursive(arr)

def conta_lista(arr):
  if arr == []:
    return 0
  arr.pop()
  return 1 + conta_lista(arr)

def maior_numero(arr):
  if len(arr) == 2:
    return arr[0] if arr[0] > arr[1] else arr[1]
  sub_max = maior_numero(arr[1:])
  return arr[0] if arr[0] > sub_max else sub_max
  
arr = [1,2,3]
soma = soma_recursive(arr)
print(soma)

size = conta_lista(arr)
print(size)

maior = maior_numero(arr)
print(maior)