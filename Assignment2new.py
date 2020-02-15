class Stack:
    data=[]

    def is_empty(self):
        return self.data==[]

    def push(self, node):
        self.data.append(node)

    def pop(self):
        if not self.is_empty():
            value=self.data[-1]
            del self.data[-1]
            return value
        else:
            print("Nothing to pop")

    def print_stack(self):
        length = int(len(self.data))
        length -= 1

        for e in reversed(self.data):
            print(e)
        for f in reversed(self.data):
            print(f)

     #print('print the stack vertical so that the top is printed first')





fruit = Stack()
fruit.pop()
fruit.push("Apple")
fruit.push("Banana")
fruit.pop()
fruit.push("Canned Yams")
fruit.push("Durian")
fruit.print_stack()
fruit.pop()
fruit.pop()
fruit.print_stack()




"""
Finish the Stack Class so that the print_stack method prints the stack vertically so that for instance ['a','b','c'] is printed 
a
b
c
"""

class Queue:
    data=[]

    def is_empty(self):
        return self.data==[]

    def enqueue (self, node):
        self.data.append(node)

    def dequeue (self):
        if not self.is_empty():
            value=self.data[-1]
            del self.data[-1]
            return value
        else:
            print("Queue is Empty")

    def is_empty(self):
        return self.data==[]

    def print_queue(self):
        length = int(len(self.data))
        length -= 1

        for e in reversed(self.data):
            print(e)
        for f in reversed(self.data):
            print(f)



"""
Write Queue functions for enqueue, dequeue, is_empty and print_queue
"""

q=Queue()

q.enqueue('Job 1')
q.enqueue('Job 2')
q.enqueue('Job 3')
q.print_queue()
q.dequeue()
q.dequeue()
q.print_queue()

