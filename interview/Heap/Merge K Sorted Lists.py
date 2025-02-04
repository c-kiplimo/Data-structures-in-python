from heapq import heappush, heappop

def mergeKLists(lists):
    # If the input list is empty, return None
    if not lists:
        return None

    # Initialize an empty heap to store nodes of the linked lists
    heap = []
    
    # Push the head nodes of all non-empty linked lists onto the heap
    for i, node in enumerate(lists):
        if node:
            # Push a tuple of (node value, list index, node) onto the heap
            heappush(heap, (node.val, i, node))
    
    # Create a dummy node to serve as the starting point of the merged list
    dummy = ListNode(0)
    curr = dummy

    # While there are elements in the heap, continue merging
    while heap:
        # Pop the smallest element from the heap (node with the smallest value)
        val, idx, node = heappop(heap)
        # Append this node to the merged list
        curr.next = node
        # Move the current pointer to the next node in the merged list
        curr = curr.next

        # If there are more nodes in the current list, push the next node onto the heap
        if node.next:
            # The tuple includes the next node's value, the index of the list, and the next node itself
            heappush(heap, (node.next.val, idx, node.next))

    # Return the merged list, which starts from the node following the dummy node
    return dummy.next
