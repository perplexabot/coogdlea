struct ListNode
    val::Int64
    next

    function ListNode(val=0, next=nothing)
        new(val, next)
    end
end

l = ListNode(0, ListNode(1))

function middleNode(head::ListNode)::ListNode
    if isnothing(head)
        return None
    end

    if isnothing(head.next)
        return head
    end

    l = []
    global curr = head
    while !isnothing(curr)
        global curr
        append!(l, [curr])
        curr = curr.next
    end

    return l[floor(Int64, length(l)/2)+1]
end

expected0 = ListNode(3, ListNode(4, ListNode(5)))
expected1 = ListNode(4, ListNode(5, ListNode(6)))
expected2 = ListNode(1)
expected3 = ListNode(1)

cases = [
    (ListNode(1, ListNode(2, expected0)), expected0),
    (ListNode(1, ListNode(2, ListNode(3, expected1))), expected1),
    (expected2, expected2),
    (ListNode(0, expected3), expected3)
]

for (index, (head, exp)) in enumerate(cases)
    ans = middleNode(head)
    @assert  ans == exp "Failed case $(index) - got value $(ans.val), expecting value $(exp.val)"
end
