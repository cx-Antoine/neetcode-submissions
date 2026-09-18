import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            stone = -stone
            heapq.heappush(maxHeap, stone)

       

        while len(maxHeap) > 1:
            rev1 = heapq.heappop(maxHeap)
            rev1 = -rev1
            rev2 = heapq.heappop(maxHeap)
            rev2 = -rev2

            weight = rev1 - rev2
            if weight > 0 :
                weight = -weight
                heapq.heappush(maxHeap, weight)
            else:
                continue
        else:
            if len(maxHeap) == 1:
                maxHeap[0] = -maxHeap[0]
                return maxHeap[0]
            else:
                return 0


        

        

        

        



        