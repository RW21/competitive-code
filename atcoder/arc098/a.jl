N = parse(Int, readline())
S = split(readline(), "") .|> only

function solve()
	function acc_char(c)
		function acc(prev, x)
			if x == c
				prev +=1
			end
			return prev
		end
		return acc
	end

	w_from_left = accumulate(acc_char('W'), S; init=0)
	e_from_right = reverse(accumulate(acc_char('E'), reverse(S); init=0))

	println(minimum(w_from_left+e_from_right) - 1)
end
solve()


