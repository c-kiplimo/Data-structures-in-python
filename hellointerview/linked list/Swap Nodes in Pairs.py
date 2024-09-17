def swapPairs(head):
  dummy = ListNode(0)
  dummy.next = head
  tail, first = dummy, head

  while first and first.next:
    second = first.next

    # swap nodes
    tail.next = second
    first.next = second.next
    second.next = first

    tail = first
    first = first.next

  return dummy.next