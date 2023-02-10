function flipAndInvertImage(image::Matrix{Bool})::Matrix{Bool}
    return .!reverse!(image,dims=2)
end

cases = [
    ([true true false; true false true; false false false], [true false false; false true false; true true true]),
    (
        [true true false false; true false false true; false true true true; true false true false],
        [true true false false; false true true false; false false false true; true false true false],
    ),
    (hcat(true), hcat(false)),
]

for (image, exp) in cases
    got = flipAndInvertImage(image)
    @assert got == exp "Failed case ($(image)) - expecting ($(exp)), got ($(got))."
end
