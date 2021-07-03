module primes

function sieve_eratosthenues(n::Int)
	prime = fill(true, n)
	prime[1] = false
	p = 2
	for i in 2:Int(round(sqrt(n)))
		if prime[i]
			for j in (i*i):i:n
				prime[j] = false
			end
		end
	end
	findall(prime)
end
end

