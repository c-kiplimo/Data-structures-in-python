def merge_lists(l1, l2):
    # If the first list is empty, return the second list
    if not l1: return l2
    # If the second list is empty, return the first list
    if not l2: return l1

    # Determine which list has the smaller first element and set it as the head of the merged list
    if l1.val < l2.val:
        head = l1  # Start with the first node of l1
        l1 = l1.next  # Move to the next node in l1
    else:
        head = l2  # Start with the first node of l2
        l2 = l2.next  # Move to the next node in l2

    # tail is used to build the merged list
    tail = head

    # Traverse both lists while both have nodes remaining
    while l1 and l2:
        # Compare the current nodes of both lists
        if l1.val < l2.val:
            tail.next = l1  # Attach the smaller node from l1 to the merged list
            l1 = l1.next  # Move to the next node in l1
        else:
            tail.next = l2  # Attach the smaller node from l2 to the merged list
            l2 = l2.next  # Move to the next node in l2
        # Move the tail pointer to the new last node in the merged list
        tail = tail.next

    # At this point, one of the lists is exhausted.
    # Attach the remaining part of the other list (whichever is not empty) to the merged list
    tail.next = l1 or l2

    # Return the head of the merged list
    return head
