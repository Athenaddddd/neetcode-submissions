class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        if len(students) < 1 :
            return 0
        elif len(sandwiches) < 1:
            return len(students)
        elif len(students) == 1:
            if sandwiches[0] == students[0]:
                return 0
            else:
                return 1
        elif len(sandwiches) == 1:
            if sandwiches[0] not in students:
                return len(students)
            else:
                return len(students) - 1
 
        first = Node(students[0])
        head = first
        tail = first
        origsize = len(students)
        size = 1

        for i in range(1,len(students)):
            new = Node(students[i])
            tail.next = new
            tail = tail.next
            size += 1
        
        # linkedlist for students created, now compare stack and student pref


        rej = 0
        while rej < size:
            
            if sandwiches[0] == head.val:
                sandwiches.pop(0)
                head = head.next
                size -= 1
                rej = 0
            else:
                tail.next = head
                head = head.next
                tail = tail.next
                tail.next = None
                rej += 1

        return size



        
        