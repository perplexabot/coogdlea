mutable struct MyHashSet
    hash::Vector
    add::Function
    remove::Function
    contains::Function

    function MyHashSet()
        return new([-1 for _ in range(1,10^6 + 1)], add, remove, contains)
    end

    function add(hash, key)
        hash[key+1] = key
    end

    function remove(hash, key)
        hash[key+1] = -1
    end

    function contains(hash, key)
        if hash[key+1] != -1
            return true
        else
            return false
        end
    end
end

cases = [
    (
        [
            "MyHashSet",
            "add",
            "add",
            "contains",
            "contains",
            "add",
            "contains",
            "remove",
            "contains",
        ],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
    ),
    (
        [
            "MyHashSet",
            "add",
            "remove",
            "add",
            "remove",
            "remove",
            "add",
            "add",
            "add",
            "add",
            "remove",
        ],
        [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]],
    ),
]

obj = MyHashSet()
for (cmds, keys) in cases
    for (cmd, key) in zip(cmds, keys)


        if cmd == "MyHashSet"
            continue
        end

        key = key[1]
        if cmd == "add"
            if !isempty(key)
                obj.add(obj.hash, key)
                @assert obj.hash[key+1] == key
            end
            continue
        end

        if cmd == "contains"
            ans = obj.contains(obj.hash, key)
            if key in obj.hash
                @assert ans == true
            else
                @assert ans == false
            end
            continue
        end

        if cmd == "remove"
            obj.remove(obj.hash, key)
            @assert obj.hash[key+1] == -1
            continue
        end
    end
end
