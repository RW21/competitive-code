
function solve()
	N = parse(Int, readline())
	A = parse.(Int, split(readline()))
	A = Set(A)
	for i in 1:N
		if !(i in A)
			println("No")
			return
		end
	end
	println("Yes")
end

solve()
