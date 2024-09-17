def removeNthFromEnd(head, n):
  # Create a dummy node to handle edge cases (e.g., removing the head)
  dummy = ListNode(0)
  dummy.next = head

  # Initialize two pointers, both starting at the dummy node
  fast, slow = dummy, dummy

  # Move the fast pointer 'n' steps ahead
  for _ in range(n):
    fast = fast.next

  # Move both fast and slow pointers together until fast reaches the end
  # At this point, slow will be just before the node to be removed
  while fast.next:
    fast = fast.next
    slow = slow.next

  # Remove the nth node from the end by skipping the node slow.next points to
  slow.next = slow.next.next

  # Return the updated list, which starts at dummy.next
  # dummy.next handles cases where the head is removed
  return dummy.next
