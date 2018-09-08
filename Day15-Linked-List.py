'''
Task 
Complete the insert function in your editor so that it creates a new Node (pass data as the Node constructor argument) and inserts it at the tail of the linked list referenced by the head parameter. Once the new node is added, return the reference to the head node.

Note: If the  argument passed to the insert function is null, then the initial list is empty.

Input Format

The insert function has 2 parameters: a pointer to a Node named head, and an integer value, data. 
The constructor for Node has 1 parameter: an integer value for the data field.

You do not need to read anything from stdin.

Output Format

Your insert function should return a reference to the head node of the linked list.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
    def insert(self,head,data): 
        node = Node(data)

        current = head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            head = node
        return head    
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	          
