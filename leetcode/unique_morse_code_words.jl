morse_vals = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]
ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
map = Dict(char=>code for (char, code) in zip(ascii_lowercase, morse_vals))

function uniqueMorseRepresentations(words::Vector{String})::Int64
    transformations = Set()
    for word in words
        transformation = []
        for char in word
            append!(transformation, map[char])
        end
        push!(transformations, join(transformation))
    end
    return length(transformations)
end

cases = [(["gin", "zen", "gig", "msg"], 2), (["a"], 1)]

for (case, exp) in cases
    got = uniqueMorseRepresentations(case)
    @assert got == exp "Failed case ($(case)) - expecting ($(exp)), got ($(got))."
end
