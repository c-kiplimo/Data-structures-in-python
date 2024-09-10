def merge_two_lists(l1, l2):
    # Create a dummy node to serve as the starting point of the merged list
    # This helps in easily handling edge cases and simplifies list operations
    dummy = ListNode()
    # Initialize the tail pointer to keep track of the end of the merged list
    tail = dummy

    # Traverse both lists while there are nodes remaining in both
    while l1 and l2:
        # Compare the values of the current nodes from both lists
        if l1.val < l2.val:
            # If l1's node has a smaller value, attach it to the end of the merged list
            tail.next = l1
            # Move to the next node in l1
            l1 = l1.next
        else:
            # If l2's node has a smaller value, attach it to the end of the merged list
            tail.next = l2
            # Move to the next node in l2
            l2 = l2.next
        # Move the tail pointer to the new last node in the merged list
        tail = tail.next

    # At this point, one of the lists is exhausted
    # Attach the remaining part of the non-empty list to the end of the merged list
    # This works because the remaining list is already sorted
    tail.next = l1 or l2

    # Return the merged list starting from the node after the dummy node
    # The dummy node was only used as a placeholder
    return dummy.next
