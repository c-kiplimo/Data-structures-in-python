def reorderList(head):
  if not head or not head.next:
    return head

  # find middle node
  slow = fast = head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  # reverse second half of list
  prev, curr = None, slow
  while curr:
    next_ = curr.next
    curr.next = prev
    prev, curr = curr, next_

  # merge first and reversed second half of list
  first, second = head, prev
  while second.next:
    first.next, first = second, first.next
    second.next, second = first, second.next

  return head