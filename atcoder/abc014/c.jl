n = parse(Int, readline())

function solve()
	arr = zeros(Int, 1000002)
	for i in 1:n
		a, b = parse.(Int, split(readline()))
		arr[a+1] += 1
		arr[b+2] -= 1
	end

	for i in 2:1000002
		arr[i] += arr[i-1]
	end

	println(maximum(arr))
end

solve()

