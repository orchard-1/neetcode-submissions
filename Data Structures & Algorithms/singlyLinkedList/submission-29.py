class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index < 0 or self.size-1 < index :
            return -1
        if index == 0 :
            return self.head.val

        if self.head:
            curr = self.head
            val = curr.val
        else :
            return -1
        
        while index > 0 :  
            curr = curr.next
            if curr:
                val = curr.val
            index-=1
            
        return val
        
    def insertHead(self, val: int) -> None:
        if self.head:
            node = ListNode(val)
            node.next=self.head
            self.head = node
        else:
            self.head = self.tail = ListNode(val)
        self.size+=1

    def insertTail(self, val: int) -> None:
        if self.tail:
            node = ListNode(val)
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = ListNode(val) 
        self.size+=1

    def remove(self, index: int) -> bool:
        if index < 0 or self.size-1 < index :
            return False
        if index == 0 :
            self.head = self.head.next
            self.size-=1
            return True

        curr = self.head
        i=0
        while i < index-1 :
            curr = curr.next
            i+=1
        if curr.next == self.tail:
            self.tail = curr
            self.size-=1
            return True
        else:  
            curr.next = curr.next.next
            self.size-=1
            return True


    def getValues(self) -> List[int]:
        values =[]
        node = self.head
        while node:
            values.append(node.val)
            node = node.next
        return values


class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next
        
