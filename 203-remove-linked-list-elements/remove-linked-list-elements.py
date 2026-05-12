# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        tempList = []
        while head !=None:
            if(head.val!=val):
                tempList.append(head.val)
            head = head.next
        lenTempList = len(tempList)
        if(lenTempList>0):
            head = ListNode(tempList[0])
            tempHead = head
            for i in range(1,lenTempList):
                tempHead.next = ListNode(tempList[i])
                tempHead = tempHead.next
            return head
        else:
            return None