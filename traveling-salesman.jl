n = parse(Int, readline())
distances = [Vector{Int64}(undef,n) for _ in 1:n]

for i in 1:n
	dists = parse.(Int, split(readline()))
	println(dists)
	distances[i] = dists
end

println(distances)
