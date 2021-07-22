N, M = readline() |> split .|> x -> parse(Int, x)

K = [parse.(Int, split(readline())) for i in 1:M]
P = parse.(Int, split(readline()))

function solve()
	ans = 0
	for i in 0:2^N-1
		pattern = digits(i, base=2, pad=N)
		# println(pattern)
		ok = true

		for (bulb_i, switches) in enumerate(K)
			# println(switches)
			on_bulbs = count(switch -> (pattern[switches[switch]] == 1), collect(2:length(switches)))
			# println(on_bulbs)
			if mod(on_bulbs, 2) != P[bulb_i] #|| on_bulbs == 0
				ok = false
				break
			end
		end
		
		if ok
			ans += 1
		end
		# println("_____________ $(ok)")
	end

	println(ans)
end

solve()
