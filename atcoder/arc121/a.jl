n = parse(Int, readline())

house = []

struct House
	x::Int
	y::Int
	order::Int
end


for i in 1:n
	x, y = parse.(Int, split(readline()))
	push!(house, House(x,y,i))
end

chevi(a, b) = max(abs(a[1] - b[1]), abs(a[2] - b[2]))
chevi(a::House, b::House) = max(abs(a.x - a.y), abs(b.x - b.y))

function solve()

	# distances = sort(map((v) -> distance(v[1], v[2]), [[house[a],house[b]] for a in 1:n for b in 1:a if a != b]), rev=true)
	# println(distances[2])
	#
	# furthest = 0
	# second_furthest = 0
	# for a in 1:n, b in 1:a
	# 	if a == b
	# 		continue
	# 	end
	# 	distance = chevi(house[a], house[b])
	# 	if distance > second_furthest
	# 		second_furthest = distance
	# 	end
	# 	if second_furthest > furthest
	# 		furthest, second_furthest = second_furthest, furthest
	# 	end

	# end
	sortedx = sort(house, by=h->(h.x), rev=true)
	sortedy = sort(house, by=h->(h.y), rev=true)

	possibilities::Array{House} = [sortedx[1], sortedx[2], sortedx[end], sortedx[end-1],
					 sortedy[1], sortedy[2], sortedy[end], sortedy[end-1]]

	saw = Set()
	distances = []
	for a in 1:8, b in 1:a
		if !([possibilities[a].order, possibilities[b].order] in saw)
			push!(saw, [possibilities[a].order, possibilities[b].order])
			push!(distances, chevi(possibilities[a], possibilities[b]))
		end
	end

	println(distances)

	println(sort(distances, rev=true)[2])

end
solve()

