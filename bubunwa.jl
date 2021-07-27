N, X = parse.(Int, split(readline()))
A = parse.(Int, split(readline()))

function solve()
	for i in 0:2^N-1
		pattern = digits(Bool, i, base=2, pad=N)
		where_i = findall(pattern)
		s = 0
		if length(where_i) > 0
			s = sum(A[use_i] for use_i in findall(pattern))
		end

		if s == X
			println("Yes")
			return
		end
	end
	println("No")
end

solve()


