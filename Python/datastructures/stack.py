class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            return None
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
if __name__ == "__main__":
    stack = Stack()
    stack.push("1")
    stack.push("2")
    print(stack)
    print(stack.size())
    print(stack.peek())
    stack.pop()
    print(stack)
    print(stack.isEmpty())
