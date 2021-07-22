N = parse(Int, readline())

function solve()
	ans = 0
	for i in 1:N
		count = 0
		if mod(i, 2) != 1
			continue
		end
			for j in 1:i
				if mod(i, j) == 0
					count += 1
				end
			end
			if count == 8 
				ans += 1
			end
		end
	println(ans)
end

solve()

