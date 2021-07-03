N, Q = parse.(Int, split(readline()))
A = parse.(Int, split(readline()))
 
function binarysearch(arr::Vector{T}, needle::T) where T
	low = 1
	high = length(arr)
	while low <= high
		if low == high
			return low
		end
		mid::Integer = (high + low) ÷ 2
		if arr[mid] > needle
			high = mid - 1
		elseif arr[mid] == needle
			return mid
		elseif arr[mid] < needle
			low = mid + 1
		end
	end
end
 
function solve()
	to_add = collect(1:N)
	for i in N:-1:1
		if i == N
			continue
		end
		if A[i] + 1 == A[i+1]
			to_add[i] = to_add[i+1]
		end
	end
 
	for _ in 1:Q
		K = parse(Int, readline())
		if K < A[1]
			println(K)
		else
			i = binarysearch(A, K)
			println(to_add[i]+K)
		end
	end
end
solve()		

