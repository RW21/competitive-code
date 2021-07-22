N, K = parse.(Int, split(readline()))
C = parse.(Int, split(readline()))

using DataStructures

function solve()
	if K == 1
		println(1)
		return
	end

	dict = DataStructures.DefaultDict(0)
	res = 0
	uniques = 0
	
	for i in 1:K
		dict[C[i]] += 1
	end
	uniques = length(dict)
	res = uniques
	for i in K+1:N
		if dict[C[i-K]] == 1
			uniques -= 1
		end
		dict[C[i-K]] -= 1
		
		if dict[C[i]] == 0
			uniques += 1
		end
		dict[C[i]] += 1
		res = max(res, uniques)
	end

	# if N >= 2
	# 	for l in 2:N-K+1
	# 		r = l + K - 1
	# 		if dict[C[l-1]] == 1
	# 			uniques -= 1
	# 		end
	# 		dict[C[l-1]] -=1

	# 		if dict[C[r]] == 0
	# 			uniques += 1
	# 		end
	# 		dict[C[r]] += 1
	# 		res = max(uniques, res)
	# 	end
	# end
	println(res)
end

solve()

