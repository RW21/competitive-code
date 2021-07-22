N = parse(Int, readline())

A = parse.(Int, split(readline()))
sort!(A)
B = parse.(Int, split(readline()))
C = parse.(Int, split(readline()))
sort!(C)

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



function solve()
	res = 0
	for n in B
		AB = bisect_left(A, n) - 1
		BC = N - (bisect_right(C, n) - 1)
		res += AB * BC
	end
	println(res)
end
		
solve()

