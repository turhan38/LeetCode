# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        tmpList = []
        while head !=None:
            tmpList.append(head.val)
            head = head.next
        zeroVal = 0
        lenTmpList = len(tmpList)
        if lenTmpList >0:
            while zeroVal<k%lenTmpList:
                lastVal = tmpList[lenTmpList-1]
                for i in range(lenTmpList):
                    tmpList[i],lastVal = lastVal,tmpList[i]
                zeroVal+=1
            head = ListNode(tmpList[0])
            tmpHead = head
            for i in range(1,lenTmpList):
                tmpHead.next = ListNode(tmpList[i])
                tmpHead = tmpHead.next
        return head