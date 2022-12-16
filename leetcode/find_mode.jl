struct TreeNode
    val::Int64
    left::Any
    right::Any

    function TreeNode(val::Int64)
        return new(val, nothing, nothing)
    end

    function TreeNode(val::Int64, left::Any, right::Any)
        return new(val, left, right)
    end

end

function findMode(root)
    if isnothing(root)
        return []
    end

    cnts = Dict()
    Q = [root]
    while ! isempty(Q)
        curr = popfirst!(Q)
        if haskey(cnts, curr.val)
            cnts[curr.val] += 1
        else
            cnts[curr.val] = 1
        end

        if ! isnothing(curr.left)
            append!(Q, [curr.left])
        end
        if ! isnothing(curr.right)
            append!(Q, [curr.right])
        end
    end

    mode = findmax(cnts)[1]
    return [k for (k,v) in cnts if v == mode]
end


T0 = TreeNode(1, nothing, TreeNode(2, TreeNode(2), nothing))
T1 = TreeNode(1, nothing, nothing)
T2 = TreeNode(1, TreeNode(1), TreeNode(1))
T4 = TreeNode(1, TreeNode(2), TreeNode(3))
T5 = TreeNode(0, nothing, TreeNode(0))

T6left = TreeNode(0, TreeNode(0, TreeNode(0), nothing), TreeNode(0))
T6right = TreeNode(1, TreeNode(1), TreeNode(1))
T6 = TreeNode(1, T6left, T6right)

T7left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(2), TreeNode(6)))
T7right = TreeNode(8, TreeNode(7), TreeNode(9))
T7 = TreeNode(6, T7left, T7right)

cases = [
    (T0, [2]),
    (T1, [1]),
    (T2, [1]),
    (T4, [1, 2, 3]),
    (nothing, []),
    (T5, [0]),
    (T6, [0, 1]),
    (T7, [2, 6]),
]

for (root, exp) in cases
    got = findMode(root)
    @assert sort(got) == sort(exp) "Failed with $(root) - got $(got), expecting $(exp)"
end
