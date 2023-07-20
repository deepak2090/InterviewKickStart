class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


# Create the first linked list
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(6)

list2 = ListNode(5)
list2.next = ListNode(88)
list2.next.next = ListNode(99)
list2.next.next.next = ListNode(100)

list3 = ListNode(3)
list3.next = ListNode(4)
list3.next.next = ListNode(5)
list3.next.next.next = ListNode(6)

list4 = ListNode(11)
list4.next = ListNode(15)
list4.next.next = ListNode(19)
list4.next.next.next = ListNode(20)

my_list = [list1, list2, list3, list4]




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

#circularnode(list1)

def printcircularnode(head):
    temptr = head
    result = [head.val]
    head = head.next
    while head !=temptr:
        result.append(head.val)
        head = head.next
    return result

#print(printcircularnode(list1))
import heapq
def mergefirstnodes(lst):
    #create a list array result which will store 
    #only first element of the array for each linked list
    result = []
    head = None
    tail = None
    for firstnode in lst:
        if firstnode:
            heapq.heappush(result,[firstnode.val, firstnode])
    while result:
        minval, minptr = heapq.heappop(result)
        if head is None:
            head = minptr
            tail = minptr
        else:
            tail.next = minptr
            tail =  tail.next
        tail.next = None
    return head

#outputfirstelement = mergefirstnodes(my_list)
#print("the first elements are: " , printnode(outputfirstelement))


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(6)

list2 = ListNode(5)
list2.next = ListNode(88)
list2.next.next = ListNode(99)
list2.next.next.next = ListNode(100)

list3 = ListNode(3)
list3.next = ListNode(4)
list3.next.next = ListNode(5)
list3.next.next.next = ListNode(6)

list4 = ListNode(11)
list4.next = ListNode(15)
list4.next.next = ListNode(19)
list4.next.next.next = ListNode(20)

my_list = [list1, list2, list3, list4]

def mergesortedNodes(list):
    result = []
    for element in list:
        if element:
            heapq.heappush(result, element.val)
            element = element.next
    root = ListNode(0)
    dummy = None
    for x in heapq.nsmallest(len(result), result):
        if dummy == None:
            dummy = ListNode(x)
            root.next = dummy
        else:
            dummy.next = ListNode(x)
            dummy = dummy.next
    return root.next


outputmerged = mergesortedNodes(my_list)
print("the merged output is: " ,printnode(outputmerged))
