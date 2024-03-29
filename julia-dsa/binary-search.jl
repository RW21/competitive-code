module bs

# Alternatives
# findfirst
# findlast
# searchsorted

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

function bisect_left(a, x, lo = 1, hi = nothing)
    if lo < 1
        throw(BoundsError(a, lo))
    end
    if hi === nothing
        hi = length(a) + 1  # It's not `length(a)`!
    end
    while lo < hi
        mid = (lo + hi) ÷ 2
        a[mid] < x ? lo = mid + 1 : hi = mid
    end
    return lo
end

function bisect_right(a, x, lo = 1, hi = nothing)
    if lo < 1
        throw(BoundsError(a, lo))
    end
    if hi === nothing
        hi = length(a) + 1  # It's not `length(a)`!
    end
    while lo < hi
        mid = (lo + hi) ÷ 2
        x < a[mid] ? hi = mid : lo = mid + 1
    end
    return lo
end
end


a = [1,1,1]

println(bs.bisect_right(a, 2))
println(bs.bisect_left(a, 2))

