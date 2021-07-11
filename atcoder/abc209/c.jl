N = parse(Int, readline())
C = parse.(Int, split(readline()))

function solve()
	sort!(C)
	for i in 2:N
		C[i] -= i - 1
	end
	res = 1
	for n in C
		n = max(0, n)
		res = mod(res*n, 1000000007)
	end
	println(res)
end

solve()
	
