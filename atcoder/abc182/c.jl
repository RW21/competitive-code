function arraytoint10_iterative(A)
    n = 0
    l = length(A)
    for i = 1:l
        n = 10n + A[i]
    end
    return n
end


N = parse.(Int, readline())
N_vec = N |> string |> collect .|> x -> parse(Int, x)
k = length(N_vec)

function solve()
	ans = Inf
	for i in 0:2^k-1
		pattern = digits(Bool, i, base=2, pad=k)
		# println(pattern)
		new_N_vec = []
		possible_digits = findall(pattern)

		if length(possible_digits) == 0
			continue
		end

		for digit in possible_digits
			push!(new_N_vec, N_vec[digit])
		end
		new_N = arraytoint10_iterative(new_N_vec)
		# println(new_N)
		# println("_________")
		if mod(new_N, 3) == 0
			ans = Int(min(ans, k - length(possible_digits)))
		end
	end
	if ans == Inf
		println(-1)
	else
		println(ans)
	end
end
solve()

