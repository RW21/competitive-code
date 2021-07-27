N = parse(Int, readline())
S = split(readline(), "") .|> only

function solve()
	if N == 1
		println(0)
		return
	end

	function acc_c(c)
		function acc(prev, curr)
			if curr == c
				prev += 1
			end
			return prev
		end
	end
	black_from_left = accumulate(acc_c('#'), S; init=0)
	white_from_right = reverse(accumulate(acc_c('.'), reverse(S); init=0))
	println(minimum(black_from_left + white_from_right) - 1)
end

solve()
