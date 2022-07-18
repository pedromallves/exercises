from my_packages import ListNode, toList, createListNode

def isPalindrome(head:ListNode)-> bool:
    """Check if a list node is palindrome

    Args:
        head (ListNode): The head of a list node

    Returns:
        bool: returns True if the list node is palindrome
    """
    arr = toList(head)
    for i in range(int(len(arr)/2)):
        if arr[i] != arr[-i-1]:
            return False
    return True

a = createListNode(4, [2, 3, 3, 2, 5])
b = createListNode(2, [5, 4, 7 , 7, 4, 5, 2])
print(isPalindrome(a), isPalindrome(b))