# implement_queue_with_stacks

stack1 = []
stack2 = []

def Enqueue(element):
    stack1.append(element)

def Dequeue():
    if len(stack2) == 0:
        if len(stack1) == 0:
            return None
        while len(stack1) > 0:
            p = stack1.pop()
            stack2.append(p)
        return stack2.pop()
