N = parse(Int, readline())
towns = [parse.(Int, split(readline())) for i in 1:N]

function unique_permutations(x::T, prefix=T()) where T
   if length(x) == 1
	   return [[prefix; x]]
   else
	   t = T[]
	   for i in eachindex(x)
		   if i > firstindex(x) && x[i] == x[i-1]
			   continue
		   end
		   append!(t, unique_permutations([x[begin:i-1];x[i+1:end]], [prefix; x[i]]))
	   end
	   return t
   end
end



using Statistics

function solve()
	perms = unique_permutations(collect(1:N))
	# println(perms)
	# println(towns)
	possible_distances = [] 
	for town_perm in perms
		distance = 0
		for j in 1:N-1
			town_i_i = town_perm[j]
			town_j_i = town_perm[j + 1]
			distance += sqrt((towns[town_i_i][1] - towns[town_j_i][1])^2 + (towns[town_i_i][2]- towns[town_j_i][2])^2)
			# println(distance)
		end
		push!(possible_distances, distance)
	end
	# println(possible_distances)
	println(mean(possible_distances))
end

solve()

