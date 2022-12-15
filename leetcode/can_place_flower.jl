function canPlaceFlowers(flowerbed, n)
    fb = copy(flowerbed)
    for i in range(1,length(fb))
        if fb[i] == 1
            continue
        end

        prv = i > 1 ? fb[i-1] : nothing
        nxt = i + 1 <= length(fb) ? fb[i+1] :  nothing

        if prv != 1 && nxt != 1
            fb[i] = 1
        end

    end
    return count(i->i==1, fb) - count(i->i==1, flowerbed) >= n
end

cases = [
    ([1, 0, 0, 0, 1], 1, true),
    ([1, 0, 0, 0, 1], 2, false),
    ([], 1, false),
    ([1], 1, false),
    ([0], 1, true),
    ([0, 1], 1, false),
    ([0, 1], 4, false),
    ([1, 0], 1, false),
    ([1, 0], 0, true),
    ([0, 1, 0], 1, false),
    ([0, 1, 0], 0, true),
    ([1, 0, 1], 1, false),
    ([1, 0, 1], 0, true),
    ([1, 0, 1], 10, false),
    ([0, 0], 1, true),
    ([0, 0], 2, false),
    ([0, 0, 0], 1, true),
    ([0, 0, 0], 2, true),
    ([0, 0, 0], 3, false),
]

for (flowerbed, n, exp) in cases
    got = canPlaceFlowers(flowerbed, n)
    @assert got == exp "Failed ($(flowerbed), $(n)) - expecting ($(exp)), got ($(got))"
end
