def reverse(head):
    # Initialize the previous node to None (this will be the new tail after reversal)
    prev = None
    
    # Initialize the current node as the head of the linked list
    current = head
    
    # Traverse the list until we reach the end (when current is None)
    while current:
        # Store the next node temporarily before we change the current node's next pointer
        next_ = current.next
        
        # Reverse the current node's next pointer to point to the previous node
        current.next = prev
        
        # Move the prev pointer one step forward to the current node
        prev = current
        
        # Move the current pointer to the next node (original next node, saved earlier)
        current = next_
    
    # After the loop, prev will point to the new head of the reversed linked list
    return prev
