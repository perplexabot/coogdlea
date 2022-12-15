""" You are given n numbers as well as n probabilities that sum up to 1. Write a function to
generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and
3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""


def rand_gen(nums, probs):
    from random import uniform

    freq = probs
    while True:
        newFreq = []
        loop = False
        for p in freq:
            p *= 10
            if p != int(p):
                loop = True
            newFreq.append(p)

        freq = newFreq
        if not loop:
            break

    newnums = []
    for n, f in zip(nums, freq):
        newnums.extend([n] * int(f))

    upper = 1
    while upper < len(newnums):
        upper *= 10

    rand_ind = int((uniform(0, 1) * upper)) % len(newnums)
    return newnums[rand_ind]


from collections import Counter

inps = [
    ([1, 2, 3, 4], [0.25] * 4),
    ([1, 2, 3, 4], [0.0, 0.50, 0.25, 0.25]),
    ([1, 2], [0.5, 0.5]),
    ([1, 2, 3, 4, 5], [0.2] * 5),
]

for nums, probs in inps:
    print(f"Randomizing nums {nums} with probs {probs}")
    cnt = Counter()
    for i in range(10000):
        cnt[rand_gen(nums, probs)] += 1

    for key in cnt:
        print(f" Probability of {key}: {cnt[key]/1000}")
