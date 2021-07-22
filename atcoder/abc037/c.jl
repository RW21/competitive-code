N, K = parse.(Int, split(readline()))
A = parse.(Int, split(readline()))

accumulate!(+, A, A)

function solve()
	res = 0
	last = K
	start = 0
	while last <= N
		if start == 0
			res += A[last]
		else
			res += A[last] - A[start]
		end
		start += 1
		last += 1
	end

	println(res)
end

solve()
