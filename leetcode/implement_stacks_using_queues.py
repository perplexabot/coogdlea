"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should
support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
    You must use only standard operations of a queue, which means that only push to back, peek/pop
    from front, size and is empty operations are valid. Depending on your language, the queue may
    not be supported natively. You may simulate a queue using a list or deque (double-ended queue)
    as long as you use only a queue's standard operations.

Example 1:
    Input
    ["MyStack", "push", "push", "top", "pop", "empty"]
    [[], [1], [2], [], [], []]
    Output
    [null, null, null, 2, 2, false]
    Explanation
    MyStack myStack = new MyStack();
    myStack.push(1);
    myStack.push(2);
    myStack.top(); // return 2
    myStack.pop(); // return 2
    myStack.empty(); // return False

Constraints:
    1 <= x <= 9
    At most 100 calls will be made to push, pop, top, and empty.
    All the calls to pop and top are valid.
 
Follow-up: Can you implement the stack using only one queue?

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

A:
    elements are ints only
    pop empty stack -> no error
    top of empty stack -> None
"""


class MyStack:
    def __init__(self):
        from collections import deque

        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


cases = [
    (
        ["MyStack", "push", "push", "top", "pop", "empty"],
        [[], [1], [2], [], [], []],
    )
]

s = MyStack()
for (cmds, values) in cases:
    for (cmd, value) in zip(cmds, values):
        print(f'doing cmd: {cmd}')
        if cmd == "MyStack":
            continue

        val = value[0] if value else None

        ans = None
        if cmd == 'push':
            cnt = len(s.stack)

            s.push(val)

            assert s.stack[-1] == val and len(s.stack) == cnt + 1
        elif cmd == 'pop':
            last = s.stack[-1]
            cnt = len(s.stack)

            ans = s.pop()

            assert ans == last and len(s.stack) == cnt - 1
        elif cmd == 'top':
            last = s.stack[-1]
            cnt = len(s.stack)

            ans = s.top()

            assert ans == last and cnt == len(s.stack)
        elif cmd == 'empty':
            ans = s.empty()

            if len(s.stack):
                assert ans == False
            else:
                assert ans == True
