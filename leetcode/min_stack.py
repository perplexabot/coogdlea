""" Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        from collections import deque

        self.stack = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] if self.stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack) if self.stack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


print("Iniitlaizing stack")
obj = MinStack()
print(" done")

print("Pushing 7")
obj.push(7)
print(" done")

print("Peaking at top")
print(" ", obj.top())
print(" peak complete")

print("Getting min")
print(" ", obj.getMin())
print(" done")

print("Popping")
obj.pop()
print(" done")

# stack should be empty at this point.
print("Hacking stack to observe it (expecting []).")
print(" ", obj.__dict__['stack'])
print(" done")

print("Popping")
obj.pop()
print(" done")

print("Peaking at top")
print(" ", obj.top())
print(" peak complete")

print("Getting min")
print(" ", obj.getMin())
print(" done")


print("Pushing 7")
obj.push(7)
print(" done")

print("Pushing 7")
obj.push(7)
print(" done")

print("Pushing 8")
obj.push(8)
print(" done")

print("Pushing 9")
obj.push(9)
print(" done")

# stack should be [7,7,8,9] at this point.
print("Hacking stack to observe it (expecting [7,7,8,9]).")
print(" ", obj.__dict__['stack'])
print(" done")

print("Getting min")
print(" ", obj.getMin())
print(" done")

print("Peaking at top")
print(" ", obj.top())
print(" peak complete")

print("Popping")
obj.pop()
print(" done")

# stack should be [7,7,8] at this point.
print("Hacking stack to observe it (expecting [7,7,8]).")
print(" ", obj.__dict__['stack'])
print(" done")

print("Popping")
obj.pop()
print(" done")

# stack should be [7,7] at this point.
print("Hacking stack to observe it (expecting [7,7]).")
print(" ", obj.__dict__['stack'])
print(" done")

print("Pushing 777")
obj.push(777)
print(" done")

# stack should be [7,7, 777] at this point.
print("Hacking stack to observe it (expecting [7,7,777]).")
print(" ", obj.__dict__['stack'])
print(" done")

print("Peaking at top")
print(" ", obj.top())
print(" peak complete")

print("Popping")
obj.pop()
print(" done")

print("Popping")
obj.pop()
print(" done")

print("Popping")
obj.pop()
print(" done")

# stack should be [] at this point.
print("Hacking stack to observe it (expecting []).")
print(" ", obj.__dict__['stack'])
print(" done")
