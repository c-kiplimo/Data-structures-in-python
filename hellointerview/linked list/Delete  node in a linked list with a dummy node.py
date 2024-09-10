def deleteNode(head, target):
    # Create a dummy node that points to the head of the list
    # This helps in handling edge cases, such as deleting the head node
    dummy = ListNode(0)
    dummy.next = head

    # Initialize the previous and current pointers
    prev = dummy
    curr = head

    # Traverse the list to find the target node
    while curr:
        if curr.val == target:
            # When the target node is found, bypass it by linking the previous node to the current node's next
            prev.next = curr.next
            # Exit the loop after deleting the node
            break
        # Move the previous and current pointers forward
        prev = curr
        curr = curr.next

    # Return the head of the updated list, which is the next node of the dummy node
    # The dummy node was used to simplify edge case handling
    return dummy.next
