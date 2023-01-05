struct MyStack
    stack::Vector{Int64}
    push::Function
    pop::Function
    top::Function
    empty::Function

    function MyStack()
        new(Vector{Int64}(), push, pop, top, empty)
    end

    function push(stack::Vector{Int}, elem::Int64)
        append!(stack, elem)
    end

    function pop(stack::Vector{Int})::int64
        pop!(stack)
    end

    function top(stack::Vector{Int})::int64
        stack[end]
    end

    function empty(stack::Vector{Int})::boolean
        isempty(stack)
    end
end
               
cases = [
    (
        ["MyStack", "push", "push", "top", "pop", "empty"],
        [[], [1], [2], [], [], []],
    )
]

s = MyStack()
for (cmds, values) in cases
    for (cmd, value) in zip(cmds, values)
        if (cmd == "MyStack")
            continue
        end

        if !isempty(value)
            val = value[1]
        end

        if cmd == "push"
            cnt = length(s.stack)

            s.push(s.stack, val)

            @assert s.stack[end] == val and length(s.stack) == cnt + 1
        elseif cmd == "pop"
            last = s.stack[end]
            cnt = length(s.stack)

            ans = s.pop(s.stack)

            @assert ans == last and length(s.stack) == cnt - 1
        elseif cmd == "top"
            last = s.stack[end]
            cnt = length(s.stack)

            ans = s.top(s.stack)

            @assert ans == last and cnt == length(s.stack)
        elseif cmd == "empty"
            ans = s.empty(s.stack)

            if isempty(s.stack)
                @assert ans == true
            else
                @assert ans == false
            end
        end
    end
end
