def pesquisa_binaria(nums, target):
  low = 0
  high = len(nums) - 1
  print(high)
  while low < high:
      mid = int((low+high) / 2)
      print(high)
      print(int(0/2))
      print(mid)
      if nums[mid] == target:
        return mid
      elif nums[mid] > target:
        high = mid - 1
      elif nums[mid] < target:
          low = mid + 1
  return -1
arr = [5]
target = pesquisa_binaria(arr,5)
print(target)