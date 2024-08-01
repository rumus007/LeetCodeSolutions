


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print_list(self):
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.linkedListNumber(self.reverselinkedlist(l1))
        num2 = self.linkedListNumber(self.reverselinkedlist(l2))
        sum = num1 + num2
        digits = self.reversenum(sum)
        head = ListNode(int(digits[0]))
        current = head

        for i in digits[1:]:
            current.next = ListNode(int(i))
            current = current.next

        return head
    
    def reverselinkedlist(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
    def linkedListNumber(self, head):
        num = 0
        current = head
        while current:
            num = num * 10 + current.val
            current = current.next
        return num
    
    def reversenum(self, num):
        return str(num)[::-1]

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

result = Solution().addTwoNumbers(l1, l2)
print(result.print_list())