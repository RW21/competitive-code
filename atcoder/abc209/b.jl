N, X = parse.(Int, split(readline()))

products = parse.(Int, split(readline()))

function solve()
	for i in 1:N
		if mod(i, 2) == 0
			products[i] -= 1
		end
	end
	if (sum(products)) > X
		println("No")
	else
		println("Yes")
	end
end

solve()

