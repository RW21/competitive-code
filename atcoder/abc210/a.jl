function solve()
	N, A, X, Y = parse.(Int, split(readline()))
	if (N - A) <= 0
		rest = 0
	else
		rest = N - A
	end

	if A > N
		A = N
	end

	println(A * X + rest * Y)
end

solve()
