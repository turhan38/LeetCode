# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if(head !=None):
            tempArray = []
            tempArray.append(head.val)
            while head.next != None:
                head = head.next
                tempArray.append(head.val)
            i = 0
            uniqueCount = 0
            while i < len(tempArray):
                tempC = tempArray.count(tempArray[i])
                if tempC > 1:
                    i+=tempC
                else:
                    tempArray[uniqueCount] = tempArray[i] 
                    uniqueCount+=1
                    i += 1
            if(uniqueCount>0):
                head = ListNode(tempArray[0])
                tempNode = head
                for i in range(1,uniqueCount):
                    tempNode.next = ListNode(tempArray[i])
                    tempNode = tempNode.next
            else:
                head = None
        return head
        