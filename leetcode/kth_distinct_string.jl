function kthDistinct(arr, k)
    if isempty(arr) || k > length(arr)
        return ""
    end

    counts = Dict(k=>0 for k in arr)
    for k in arr
        counts[k] += 1
    end

    uniques = Dict(k=>v for (k,v) in counts if v == 1)
    position = sort!([(findall(i->i==char,arr)[1],char) for (char,count) in uniques])
    if k > length(position)
        return ""
    else
        return position[k][2]
    end
end

cases = [
    (["d", "b", "c", "b", "c", "a"], 2, "a"),
    (["aaa", "aa", "a"], 1, "aaa"),
    (["a", "b", "a"], 3, ""),
    ([], 10, ""),
    (["a"], 10, ""),
    (["a", "b", "c", "d"], 1, "a"),
    (["a", "b", "c", "d"], 2, "b"),
    (["a", "b", "c", "d"], 3, "c"),
    (["a", "b", "c", "d"], 4, "d"),
    (["a", "b", "c", "d"], 5, ""),
]

for (arr, k, exp) in cases
    ans = kthDistinct(arr,k)
    @assert ans == exp "Failed with ($(arr), $(k)) - got ($(ans)), expecting ($(exp))"
end
