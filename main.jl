n = parse(Int, readline())

function solve()
	arr =  [0 for i in 1:1000002]
	for i in 1:n
		a, b = parse.(Int, split(readline()))
		arr[a + 1] += 1
		arr[b + 1 + 1] -= 1
	end

	for i in 2:1000001
		arr[i] = arr[i] + arr[i-1]
	end

	println(maximum(arr))
end

solve()
		

