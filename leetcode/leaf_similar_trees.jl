function leafSimilar(root1, root2)
    function get_lfs_dfs(root, lvs)
        if isnothing(root.left) && isnothing(root.right)
            append!(lvs, root.val)
        end

        if !isnothing(root.left)
            get_lvs_dfs(root.left, lvs)
        end

        if !isnothing(root.right)
            get_lvs_dfs(root.right, lvs)
        end
    end

    lvs1 = []
    get_lvs_dfs(root1, lvs1)
    lvs2 = []
    get_lvs_dfs(root2, lvs2)

    return lvs1 == lvs2
end
