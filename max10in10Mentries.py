from heapq import heappush,heappop
def findMax(arr):
  heap = []
  res = []
  for i in range(len(arr)):
    if len(heap)<10:
      heappush(heap,arr[i])
    else:
      if heap[0] < arr[i]:
        heappop(heap)
        heappush(heap,arr[i])
  if  len(heap)>10:
        heappop(heap)
  for i in range(10):
    res.append(heappop(heap))
  return res
