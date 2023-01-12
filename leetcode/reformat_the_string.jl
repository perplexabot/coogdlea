function reformat(s::String)::String
    numbers = Vector{Char}()
    letters = Vector{Char}()
    final = Vector{Char}()

    for c in s
        if isletter(c)
            append!(letters, c)
        else
            append!(numbers, c)
        end
    end

    if (abs(length(numbers) - length(letters)) > 1)
        return ""
    end

    if length(numbers) > length(letters)
        append!(final, pop!(numbers))
        while !isempty(letters)
            append!(final, pop!(letters))
            if !isempty(numbers)
                append!(final, pop!(numbers))
            end
        end
    else
        append!(final, pop!(letters))
        while !isempty(numbers)
            append!(final, pop!(numbers))
            if !isempty(letters)
                append!(final, pop!(letters))
            end
        end
    end
    return join(final)
end

cases = ["a0b1c2", "leetcode", "1229857369"]

for case in cases
    numbers = Vector{Char}()
    letters = Vector{Char}()
    for c in case
        if isletter(c)
            append!(letters, c)
        else
            append!(numbers, c)
        end
    end

    if abs(length(numbers) - length(letters)) > 1
        @assert reformat(case) == ""
    else
        ans = reformat(case)
        if (isletter(case[1]))
            for i in range(1, length(case), step=2)
                @assert isletter(case[i])
            end
            for i in range(2, length(case), step=2)
                @assert isnumeric(case[i])
            end
        else
            for i in range(1, length(case), step=2)
                @assert isnumeric(case[i])
            end
            for i in range(2, length(case), step=2)
                @assert isletter(case[i])
            end
        end
    end
end
