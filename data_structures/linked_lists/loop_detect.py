# ctci 2.8

def loop(node):
    slow = node
    fast = node
    while True:
        if slow == fast:
            return True
        elif not slow.next:
            return False
        elif not fast.next or not fast.next.next:
            return False
        slow = slow.next
        fast = fast.next.next
