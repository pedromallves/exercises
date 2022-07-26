from my_packages import ListNode, toList, createListNode

def addTwoNumbers(l1:ListNode, l2:ListNode)->ListNode:
    """Add values of two list nodes considering that they are reversed integers and each node is a digit

    Args:
        l1 (ListNode): head of list node 1
        l2 (ListNode): head of list node 2

    Returns:
        ListNode: Returns the sum of l1 and l2 as a ListNode
    """
    # starting variables
    sum = []
    l3 = None
    tmp = 0
    res = 0
    # adding the sum of l1 and l2 to list
    while l1 != None and l2 != None:
        tmp = l1.val + l2.val
        if res != 0:
            tmp +=1; res = 0
        if tmp > 9:
            res = 1
            sum.append(int(str(tmp)[1]))
        else:
            sum.append(tmp)
        l1 = l1.next
        l2 = l2.next
    # if l1 still have value, add to list, else, check if l2 still have values and add to list
    while l1 != None:
        tmp = l1.val + res
        res = 0
        if tmp > 9:
            res = 1
            sum.append(int(str(tmp)[1]))
        else:
            sum.append(tmp)
        l1 = l1.next
    while l2 != None:
        tmp = l2.val + res
        res = 0
        if tmp > 9:
            res = 1
            sum.append(int(str(tmp)[1]))
        else:
            sum.append(tmp)
        l2 = l2.next
    # check if there is still res
    if res:
        sum.append(res)
    tmp = None
    # parse list to listnode
    l3 = createListNode(sum[0], sum[1:])
    return l3

 # testing
a = createListNode(5,[1,2])
d = createListNode(5,[2,1])
list = addTwoNumbers(a, d)
b = toList(list)
print(b)
