import heapq

class Solution:
    def kClosest(self, points, k):
        # Initialize an empty max-heap to store the k closest points
        heap = []
        
        # Iterate through each point in the list
        for i in range(len(points)):
            # Extract x and y coordinates of the point
            x, y = points[i]
            
            # Calculate the squared distance from the origin (0, 0) to avoid using square root
            distance = x * x + y * y
            
            # If the heap has fewer than k elements, add the current point with its distance
            if len(heap) < k:
                heapq.heappush(heap, (-distance, i))
            # If the heap is full and the current point is closer than the farthest in the heap
            elif distance < -heap[0][0]:
                # Replace the farthest point with the current point
                heapq.heappushpop(heap, (-distance, i))
        
        # Return the list of the k closest points by extracting the indices from the heap
        return [points[p[1]] for p in heap]
