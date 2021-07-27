N, M, X = parse.(Int, split(readline()))

C = [parse.(Int, split(readline())) for i in 1:N]


function solve()
	min_price = Inf
	for i in 0:2^N-1
		pattern = digits(Bool, i, base=2, pad=N)
		algorithms = zeros(Int, M)
		total_book_price = 0
		for book_i in findall(pattern)
			book_price = C[book_i][1]
			algorithms += C[book_i][2:end]
			total_book_price += book_price
		end
		if all(x -> x >= X, algorithms)
			min_price = Int(min(min_price, total_book_price))
		end
	end
	if min_price == Inf
		println(-1)
	else
		println(min_price)
	end
end

solve()
