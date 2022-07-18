class ListNode:
    def __init__(self, val:any=0, next=None):
        self.val = val
        self.next = next

def createListNode(r:int, values:list)->ListNode:
    if type(r) != int or type(values) != list:
        print(type(r), type(values))
        raise Exception('Invalid type for "values" or "r"!')
    tmp = 0
    root = ListNode(r)
    while values != []:
        if root.next == None:
            tmp = ListNode(values.pop(0))
            root.next = tmp
            continue
        tmp.next = ListNode(values.pop(0))
        tmp = tmp.next
    return root

def toList(node:ListNode)->list:
    tmp = node
    l = []
    while tmp != None:
        l.append(tmp.val)
        tmp = tmp.next
    return l