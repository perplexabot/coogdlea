"""
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets
    poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is
    poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before
    the poison effect ends, the timer for it is reset, and the poison effect will end duration
    seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo
    attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Example 1:
    Input: timeSeries = [1,4], duration = 2
    Output: 4
    Explanation: Teemo's attacks on Ashe go as follows:
    - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
    - At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
    Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:
    Input: timeSeries = [1,2], duration = 2
    Output: 3
    Explanation: Teemo's attacks on Ashe go as follows:
    - At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
    - At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for
        seconds 2 and 3.
    Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

Constraints:
    1 <= timeSeries.length <= 10**4
    0 <= timeSeries[i], duration <= 10**7
    timeSeries is sorted in non-decreasing order.

A:
    empty timeSeries        ->  return 0
    duration = 0            ->  return 0
    len(timeSeries) == 1    ->  return duration

D:
    timeSeries = [1,2,4,6,9], d = 2
        total = 0
        2 - 1 = 1 <= d -> total += 1
        4 - 2 = 2 <= d -> total += 2
        6 - 4 = 2 <= d -> total += 2
        9 - 6 = 3  > d -> total += d
        total = 7 + d = 9

    timeSeries = [1,4], d = 2
        total = 0
        4 - 1 = 3 >  d -> total += d
        total = 2 + d = 4

    timeSeries = [1,2], d = 2
        total = 0
        2 - 1 = 1 <= d -> total += 1
        total = 1 + d = 3

    timeSeries = [1,2,3], d = 5
        total = 0
        2 - 1 = 1 <= d -> total += 1
        3 - 2 = 1 <= d -> total += 1
        total = 2 + 5 = 7

P:
    if not timeSeries or not d:
        return 0

    if len(timeSeries) < 2:
        return d

    total = 0
    for i in range(1, len(timeSeries)):
        total += d if timeSeries[i] - timeSeries[i-1] > d else timeSeries[i] - timeSeries[i-1]
    return total + d
"""


def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
    if not timeSeries or not duration:
        return 0

    if len(timeSeries) < 2:
        return duration

    total = 0
    for i in range(1, len(timeSeries)):
        total += (
            duration
            if timeSeries[i] - timeSeries[i - 1] > duration
            else timeSeries[i] - timeSeries[i - 1]
        )
    return total + duration


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

for (timeSeries, duration, exp) in cases:
    assert (
        got := findPoisonedDuration(timeSeries, duration)
    ) == exp, f"Failed ({timeSeries}, {duration}) - expecting ({exp}), got ({got})"
