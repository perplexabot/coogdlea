function getCommon(nums1, nums2)::Int64
    intersection = intersect(Set(nums1), Set(nums2))
    if isempty(intersection)
        return -1
    else
        return minimum(intersection)
    end
end

cases = [
    ([1, 2, 3], [2, 4], 2),
    ([1, 2, 3, 6], [2, 3, 4, 5], 2),
    ([], [1], -1),
    ([1], [], -1),
    ([1], [2], -1),
    ([-1, 100], [-1, 200], -1),
    ([1, 2], [1, 2], 1),
]

for (nums1, nums2, exp) in cases
    got = getCommon(nums1, nums2)
    @assert got == exp "Failed case ($(nums1), $(nums2)) - expecting ($(exp)), got ($(got))."
end
