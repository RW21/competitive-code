N = parse(Int, readline())
A = parse.(Int, split(readline()))

function solve()
	accumulate!(+, A, A)
	for k in 1:N
		ans = 0
		for i in k:N
			if i == k
				ans = max(ans, A[i])
			else
				ans = max(ans, A[i] - A[i-k])
			end
		end
		println(ans)
	end
end

solve()
