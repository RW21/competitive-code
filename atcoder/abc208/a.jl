A, B = parse.(Int, split(readline()))

function solve()
	min_ = A
	max_ = A * 6
	if min_ <= B <= max_
		println("Yes")
		return
	end
	println("No")
end
solve()

