N = parse(Int, readline())
A = (x -> parse(Int, x)).(split(readline()))
B = (x -> parse(Int, x)).(split(readline()))
C = (x -> parse(Int, x)).(split(readline()))

exists = Dict() 

for n in A
	exists[n] = 0
end

for j in 1:N
	num = B[C[j]]
	if !haskey(exists, num)
		exists[num] = 0
	end
	exists[num] += 1
end

print(sum([exists[A[i]] for i in 1:N]))

