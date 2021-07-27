A, B = parse.(Int, split(readline()))

function C(a, b)
	return ((a-b)/3) + b
end

println(C(A,B))
