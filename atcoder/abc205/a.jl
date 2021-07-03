A, B = parse.(Int, split(readline()))

function solve()
	println(A/100 * B)
end

solve()
