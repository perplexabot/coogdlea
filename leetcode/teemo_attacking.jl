function findPoisonedDuration(timeSeries, duration)
    if isempty(timeSeries) || iszero(duration)
        return 0
    end

    if length(timeSeries) < 2
        return duration
    end

    total = 0
    for i in range(2, length(timeSeries))
        total += timeSeries[i] - timeSeries[i-1] > duration ? duration : timeSeries[i] - timeSeries[i-1]
    end
    return total + duration
end

cases = [
    ([1, 4], 2, 4),
    ([1, 2], 2, 3),
    ([1, 2, 4, 6, 9], 2, 9),
    ([1, 2, 3], 5, 7),
    ([], 10, 0),
    ([1, 2, 3], 0, 0),
    ([1], 10, 10),
    ([1], 0, 0),
    ([1, 2], 10, 11),
]

for (timeSeries, duration, exp) in cases
    got = findPoisonedDuration(timeSeries, duration)
    @assert got == exp "Failed ($(timeSeries), $(duration)) - expecting ($(exp)), got ($(got))"
end
