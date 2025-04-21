from typing import Self

class ListNode:
    def __init__(self, value=0, next: Self = None):
        self.value = value
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
# Creating a linked list with a cycle for demonstration:
node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)


node1.next = node3
#node2.next = node3
#node3.next = node1  # Cycle here
print(has_cycle(node1))


