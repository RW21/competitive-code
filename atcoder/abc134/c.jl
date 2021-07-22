N = parse(Int, readline())

A = zeros(Int, N)

for i in 1:N
	a = parse(Int, readline())
	A[i] = a
end

function solve()
	max1 = 0
	max2 = 0
	for a in A
		if max2 <= a
			if max1 <= a
				max2 = max1
				max1 = a
			else
				max2 = a
			end
		end
	end

	for a in A
		if a == max1
			println(max2)
		else
			println(max1)
		end
	end
end

solve()

