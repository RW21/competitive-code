

# function solve()
# 	P = parse(Int, readline())
# 	coins = [factorial(i) for i in 1:10]

# 	res = 0
# 	for i in 1:10
# 		div = factorial(i)

function solve()
	P = parse(Int, readline())
	res = 0
	for i in 10:-1:1
		while factorial(i) <= P
			res += 1
			P -= factorial(i)
		end
	end
	println(res)
end

		
solve()

