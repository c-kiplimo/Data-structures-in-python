def is_palindrome(head):
  # Step 1: Find the middle node of the list using two pointers (slow and fast)
  slow = fast = head
  while fast and fast.next:
    fast = fast.next.next  # Move fast pointer two steps ahead
    slow = slow.next       # Move slow pointer one step ahead
  
  # At this point, slow will be at the middle of the list

  # Step 2: Reverse the second half of the list starting from the middle
  curr, prev = slow, None
  while curr:
    next_ = curr.next      # Save the next node
    curr.next = prev       # Reverse the current node's pointer
    prev = curr            # Move prev to the current node
    curr = next_           # Move curr to the next node (saved earlier)
  
  # After this loop, prev will point to the head of the reversed second half

  # Step 3: Compare the first half and the reversed second half of the list
  left, right = head, prev
  while right:              # We only need to compare until the end of the reversed half
    if left.val != right.val:  # If the values don't match, it's not a palindrome
      return False
    left = left.next        # Move left pointer forward in the first half
    right = right.next      # Move right pointer forward in the reversed half
  
  # If we complete the loop without mismatches, the list is a palindrome
  return True
