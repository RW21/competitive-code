module primes

function sieve_eratosthenues(n::Int)
	prime = fill(1, n)
	prime[1] = 0
	p = 2
	for i in 2:Int(round(sqrt(n)))
		if prime[i] == 1
			for j in (i*i):i:n
				prime[j] = 0
			end
		end
	end
	prime
end
end
 
Q = parse(Int, readline())

function solve()
	size = 100000
	# size = 100
	prime = primes.sieve_eratosthenues(size)
	prime_2017 = fill(0, size)
	for (i, p) in enumerate(prime)
		if p == 1 && isodd(i) && prime[Int((i+1)/2)] == 1
			prime_2017[i] = 1
		end
	end

	accumulate!(+, prime_2017, prime_2017)

	 for i in 1:Q
	 	l, r = parse.(Int, split(readline()))
		if l == 1
			ans = prime_2017[r] - prime_2017[l]
		else
			ans = prime_2017[r] - prime_2017[l-1]
		end
		println(ans)
	end

end

solve()
		

