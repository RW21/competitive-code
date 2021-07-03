module bs

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

end

a = [2,3,5]
for i in 1:10
	print("$i ")
	println(bs.binarysearch(a, i))
end

