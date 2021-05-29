combination(n, r) = factorial(big(n)) / (factorial(big(r)) * factorial(big(n-r)))

function solve(a, b, k)
	if a == 0 && b == 1
		print('b')
		return
	elseif a == 1 && b == 0
		print('a')
		return
	end


	num_of_a = combination((a - 1) + b, b)
	if num_of_a == Nan
		println("$a $b $k $num_of_a")
	end


	if k > num_of_a
		print('b')
		b -= 1
	else
		print('a')
		a -= 1
	end
	
	solve(a, b, mod(k, num_of_a))
end

A, B, K = parse.(Int64, split(readline()))
solve(A, B, K)

