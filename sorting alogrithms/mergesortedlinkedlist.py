class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


# Create the first linked list
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(6)


def printnode(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    return result

#print(printnode(list1))

def circularnode(head):
    tempptr = head
    while head is not None:
        head = head.next
        if head.next == None:
            head.next = tempptr
            break

circularnode(list1)

def printcircularnode(head):
    temptr = head
    result = [head.val]
    head = head.next
    while head !=temptr:
        result.append(head.val)
        head = head.next
    return result

print(printcircularnode(list1))
        

