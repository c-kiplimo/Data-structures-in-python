import heapq

class Solution:
    def kthLargest(self, nums, k):
        # If the list is empty, return None
        if not nums:
            return 
        
        # Initialize an empty min-heap
        heap = []
        
        # Iterate over each number in the input list
        for num in nums:
            # If the heap has fewer than k elements, add the current number to the heap
            if len(heap) < k:
                heapq.heappush(heap, num)
            # If the heap has k elements, compare the current number to the smallest (heap[0])
            # If the current number is larger, replace the smallest element with the current number
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
        
        # The kth largest element will now be at the root of the heap
        return heap[0]
