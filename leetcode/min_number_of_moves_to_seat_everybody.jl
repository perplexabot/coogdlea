function minMovesToSeat(seats::Vector{Int64}, students::Vector{Int64})::Int64
    sort!(seats)
    sort!(students)
    return sum(abs(seat - student) for (seat, student) in zip(seats, students))
end

cases = [
    ([3, 1, 5], [2, 7, 4], 4),
    ([4, 1, 5, 9], [1, 3, 2, 6], 7),
    ([2, 2, 6, 6], [1, 3, 2, 6], 4),
    ([1], [1], 0),
    ([1, 2], [2, 1], 0),
    ([2, 3], [1, 4], 2),
    ([2, 3], [4, 1], 2),
]

for (seats, students, exp) in cases
    got = minMovesToSeat(seats, students)
    @assert got == exp "Failed case ($(seats), $(students)) - expecting ($(exp)), got ($(got))"
end
