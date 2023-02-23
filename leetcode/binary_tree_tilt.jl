using DataStructures

struct TreeNode
    val::Int64
    left
    right

    function TreeNode(val=0, left=nothing, right=nothing)
        new(val, left, right)
    end
end

function treeSum(node::TreeNode)::Int64
    total = 0
    q = DataStructures.Deque{TreeNode}()
    push!(q, node)
    while ! isempty(q)
        curr = popfirst!(q)
        total += curr.val
        if ! isnothing(curr.left)
            push!(q, curr.left)
        end
        if ! isnothing(curr.right)
            push!(q, curr.right)
        end
    end
    return total
end

function allTilts(node::TreeNode)::Vector{Int64}
    q = DataStructures.Deque{TreeNode}()
    push!(q, node)
    tilts = []
    while ! isempty(q)
        curr = popfirst!(q)
        if isnothing(curr.left) && isnothing(curr.right)
            append!(tilts, 0)
        elseif isnothing(curr.left) && ! isnothing(curr.right)
            append!(tilts, abs(0 - treeSum(curr.right)))
            push!(q, curr.right)
        elseif isnothing(curr.right) && ! isnothing(curr.left)
            append!(tilts, abs(treeSum(curr.left) - 0))
            push!(q, curr.left)
        else
            append!(tilts, abs(treeSum(curr.left) - treeSum(curr.right)))
            push!(q, curr.right)
            push!(q, curr.left)
        end
    end
    return tilts
end

function findTilt(root::TreeNode)::Int64
    if isnothing(root)
        return 0
    end

    return sum(allTilts(root))
end

cases = [
    (TreeNode(1, TreeNode(2), TreeNode(3)), 1),
    (TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(5)), TreeNode(9, nothing, TreeNode(7))), 15),
]

for (index, (root, exp)) in enumerate(cases)
    got = findTilt(root)
    @assert got == exp "Failed case $(index) - expecting $(exp), got $(got)."
end
