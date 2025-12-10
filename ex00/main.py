class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None


def lst_display(head: Node, length: int | None = None, end: str = '\n'):
    if not head or length == 0:
        return

    print(f"[{head.data}]", end='')

    remaining = None if length is None else length - 1

    curr = head.next
    while curr and (remaining is None or remaining > 0):
        print(" -> ", end='')
        print(f"[{curr.data}]", end='')
        curr = curr.next

        if remaining is not None:
            remaining -= 1

    print(end=end)

def lst_add_end(head: Node, new: Node):
    if not head or not new:
        return

    while head.next:
        head = head.next

    head.next = new

def lst_reverse(head: Node) -> Node:
    if not head or not head.next:
        return head

    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

def lst_merge(a: Node, b: Node) -> Node:
    if not a:
        return b
    if not b:
        return a

    if a.data <= b.data:
        a.next = lst_merge(a.next, b)
        return a
    else:
        b.next = lst_merge(a, b.next)
        return b

def find_middle(head: Node) -> Node:
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def lst_sort(head: Node) -> Node:
    if not head or not head.next:
        return head

    mid = find_middle(head)
    right = mid.next
    mid.next = None

    left_sorted = lst_sort(head)
    right_sorted = lst_sort(right)

    return lst_merge(left_sorted, right_sorted)


def main():

    head = Node(0)

    lst_add_end(head, Node(1))
    lst_add_end(head, Node(2))
    lst_add_end(head, Node(3))
    lst_add_end(head, Node(4))
    lst_add_end(head, Node(5))
    lst_add_end(head, Node(6))

    print("Before reverse:")
    lst_display(head)

    print("After reverse:")
    head = lst_reverse(head)
    lst_display(head)

    print("\nBefore sort:")
    lst_display(head)
    head = lst_sort(head)

    print("Sorted:")
    lst_display(head)

    head1 = Node(1)
    lst_add_end(head1, Node(2))
    lst_add_end(head1, Node(3))

    head2 = Node(4)
    lst_add_end(head2, Node(5))
    lst_add_end(head2, Node(6))

    print("\nTwo lists:")
    lst_display(head1)
    lst_display(head2)

    print("Merged:")
    lst_display(lst_merge(head1, head2))


if __name__ == "__main__":
    main()
