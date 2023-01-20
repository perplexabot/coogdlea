# julia is 1 based indexing, so things go crazy.
function decrypt(code::Vector{Int64}, k::Int64)::Vector{Int64}
    n = length(code)
    ncode = Vector{Int64}()
    if k > 0
        for i in range(1,n,step=1)
            elems_to_sum = Vector{Int64}()
            for j in range(1,k,step=1)
                t = i + j
                if t > n
                    index = t % n
                else
                    index = t
                end
                append!(elems_to_sum, code[index])
            end
            append!(ncode, sum(elems_to_sum))
        end
    elseif k < 0
        for i in range(1,n,step=1)
            elems_to_sum = Vector{Int64}()
            for j in range(1,abs(k),step=1)
                t = i - j
                if t > 0
                    index = t
                elseif t == 0
                    index = n
                else
                    index = n -(abs(t) % (n+1))
                    if iszero(index)
                        index = 1
                    end
                end
                append!(elems_to_sum, code[index])
            end
            append!(ncode, sum(elems_to_sum))
        end
    else
        append!(ncode, [0 for i in range(1,n)])
    end
    return ncode
end

cases = [
    ([5, 7, 1, 4], 3, [12, 10, 16, 13]),
    ([1, 2, 3, 4], 0, [0, 0, 0, 0]),
    ([2, 4, 9, 3], -2, [12, 5, 6, 13]),
]

for (code, k, exp) in cases
    got = decrypt(code, k)
    @assert got == exp "Failed case ($(code), $(k)) - expecting ($(exp)), got ($(got))."
end
