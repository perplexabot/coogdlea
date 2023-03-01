mutable struct ListNode
    val::Int64
    next

    function ListNode(val::Int64, next=nothing)
        new(val, next)
    end
end

function removeElements(head, val)
    if isnothing(head)
        return head
    end

    if isnothing(head.next)
        if head.val == val
            return nothing
        else
            return head
        end
    end

    curr = head
    prev = nothing
    while !isnothing(curr)
        if curr.val == val
            if isnothing(prev)
                head = curr.next
            else
                prev.next = curr.next
            end
        else
            prev = curr
        end
        curr = curr.next
    end
    return head
end

cases = [
    (
        ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))),
        6,
        [1, 2, 3, 4, 5],
    ),
    (nothing, 1, []),
    (ListNode(1), 1, []),
    (ListNode(1, ListNode(1)), 1, []),
    (ListNode(1, ListNode(2, ListNode(3))), 1, [2, 3]),
    (ListNode(3, ListNode(2, ListNode(1))), 1, [3, 2]),
    (ListNode(1, ListNode(1, ListNode(1))), 1, []),
    (ListNode(7, ListNode(7, ListNode(7, ListNode(7)))), 7, []),
]

for (ind, (root, val, exp)) in enumerate(cases)
    got = removeElements(root, val)

    got_vals = []
    curr = got
    while !isnothing(curr)
        append!(got_vals, curr.val)
        curr = curr.next
    end

    @assert got_vals == exp "Failed case ($(ind)) - expecting ($(exp)), got ($(got_vals))"
end
