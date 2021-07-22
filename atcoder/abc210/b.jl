N = parse(Int, readline())
S = parse.(Int, split(readline(), ""))

function solve()
	for (i, card) in enumerate(S)
		if card == 1
			if mod(i, 2) == 1
				println("Takahashi")
			else
				println("Aoki")
			end
			return
		end
	end
end

solve()


