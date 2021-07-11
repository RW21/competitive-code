R, C, K = parse.(Int, split(readline()))

# board = Vector{Vector{Bool, C}, R}
board = Array{Bool}(undef, R, C)
function solve()
	for i in 1:R
		row = collect(readline())
		row = map(c -> c == 'o', row)
		# push!(board, row)
		# board[i] = row
		for c in 1:C
			board[i, c] = row[c]
		end
	end

	for c in 1:(K-1)
		ref = copy(board)
		for i in 1:R
			for j in 1:C
				if !ref[i, j]
					continue
				end

				try
					up = ref[i+1, j]
					down = ref[i-1, j]
					right = ref[i, j+1]
					left = ref[i, j-1]
					cell = up && down && left && right
					board[i, j] = cell
				catch BoundsError
					cell = false
					board[i, j] = cell
				end
			end
		end
	end
	println(sum(length.(findall.(board))))
end
solve()
