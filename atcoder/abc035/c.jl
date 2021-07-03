N, Q = parse.(Int, split(readline()))

function solve()
	row = zeros(Int, N+1)

	for i in 1:Q
		l, r = parse.(Int, split(readline()))
		row[l] += 1
		row[r+1] -= 1
	end

	accumulate!(+, row, row)

	for i in 1:N
		print(mod(row[i], 2))
	end
	print('\n')

end

solve()
	
