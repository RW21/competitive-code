N, C = parse.(Int, split(readline()))

dists = zeros(Int, N)
cals = zeros(Int, N)

for i in 1:N
	dist, cal = parse.(Int, split(readline()))
	dists[i] = dist
	cals[i] = cal
end

OA = zeros(Int,N)
OB = zeros(Int,N)
dists_rev = reverse(map(i -> C - i, dists))
cals_rev = reverse(cals)
for i in 1:N
	if i == 1
		OA[i] = cals[i] - dists[i]
		OB[i] = cals_rev[i] - dists_rev[i]
	else
		OA[i] = cals[i] - (dists[i] - dists[i-1])
		OB[i] = cals_rev[i] - (dists_rev[i] - dists_rev[i-1])
	end
end

accumulate!(+, OA, OA)
accumulate!(+, OB, OB)

OAOA = OA - dists
OBOB = OB - reverse(dists)

OAOAOB = OAOA[1:end-1] + OB[1:end-1]
OBOBOA = OBOB[1:end-1] + OA[1:end-1]
println(OAOAOB)
println(OBOBOA)

println(maximum(maximum.([OAOAOB, OBOBOA, OBOB, OAOA])))
