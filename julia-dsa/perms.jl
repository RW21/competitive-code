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


