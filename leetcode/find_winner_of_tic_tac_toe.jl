function tictactoe(moves::Vector{Vector{Int64}})::String
    board = [["x","x","x"] for _ in range(1,3,step=1)]
    player = "A"
    for move in moves
        board[move[1]][move[2]] = player
        if player == "A"
            player = "B"
        else
            player = "A"
        end
    end

    for row in eachrow(board)
        if count(i->i=="A", row) == 3
            return "A"
        end
        if count(i->i=="B", row) == 3
            return "B"
        end
    end

    for col in eachcol(board)
        if count(i->i=="A", col) == 3
            return "A"
        end
        if count(i->i=="B", col) == 3
            return "B"
        end
    end

    if board[1][1] == board[2][2] == board[3][3] == "A" || board[3][1] == board[2][2] == board[1][3] == "A"
        return "A"
    end

    if board[1][1] == board[2][2] == board[3][3] == "B" || board[3][1] == board[2][2] == board[1][3] == "B"
        return "B"
    end

    if length(moves) == 9
        return "Draw"
    else
        return "Pending"
    end
end

cases = [
    ([[1, 1], [3, 1], [2, 2], [3, 2], [3, 3]], "A"),
    ([[1, 2], [3, 1], [2, 2], [3, 2], [3, 3]], "Pending"),
    ([[1, 1], [2, 2], [1, 2], [1, 3], [2, 1], [3, 1]], "B"),
    ([[1, 1], [2, 2], [3, 1], [2, 1], [2, 3], [3, 2], [1, 2], [1, 3], [3, 3]], "Draw"),
]

for (moves, exp) in cases
    got = tictactoe(moves)
    @assert got == exp "Failed case ($(moves)) - expecting ($(exp)), got ($(got))."
end
