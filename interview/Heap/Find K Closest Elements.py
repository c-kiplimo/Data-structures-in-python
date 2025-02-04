import heapq

class Solution:
    def kClosest(self, nums, k, target):
        # Initialize an empty max-heap to store the k closest numbers to the target
        heap = []
        
        # Iterate over each number in the list
        for num in nums:
            # Calculate the absolute distance between the number and the target
            distance = abs(num - target)
            
            # If the heap contains fewer than k elements, add the current number and its distance
            if len(heap) < k:
                heapq.heappush(heap, (-distance, num))
            # If the heap is full and the current number is closer to the target than the farthest in the heap
            elif distance < -heap[0][0]:
                # Replace the farthest number with the current one, maintaining the heap size
                heapq.heappushpop(heap, (-distance, num))
        
        # Extract the k closest numbers from the heap (ignoring the distances)
        distances = [pair[1] for pair in heap]
        
        # Sort the result to return the k closest numbers in ascending order
        distances.sort()
        
        # Return the sorted list of k closest numbers to the target
        return distances
