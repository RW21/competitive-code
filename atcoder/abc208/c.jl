N, K = parse.(Int, split(readline()))

function solve()
	a = parse.(Int, readline())
	sort!(a)
	if N >= K
		println(1)
	end

