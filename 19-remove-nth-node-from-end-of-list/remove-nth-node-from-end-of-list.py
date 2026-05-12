# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        tmpList = []
        while head!=None:
            tmpList.append(head.val)
            head = head.next
        lenList = len(tmpList)
        if(lenList>1):
            head = ListNode()
            tmpHead = head
            for i in range(lenList):
                if i!=(lenList-1)-(n-1):
                    tmpHead.val = tmpList[i]
                    if(i!=lenList-1 and (i+1!=(lenList-1)-(n-1)or i+2 <=lenList-1)):
                        tmpHead.next = ListNode()
                        tmpHead = tmpHead.next
            return head
        else:
            return None