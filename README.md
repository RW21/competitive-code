# Competitive Programming

## Julia

```
use Revise
includet("sourcefile")
```

### bits
```julia
N = 4
for i in 0:2^N - 1
   pattern = digits(Bool, i, base=2, pad=N)
```

```
all_perm(xs, n) = vec(map(collect, Iterators.product(ntuple(_ -> xs, n)...)))
```

```
function next_perm!(itr)::Bool                      
    (isempty(itr) || length(itr) == 1) && return false
        
    i = findlast(idx -> itr[idx + 1] > itr[idx], 1:lastindex(itr) - 1)             
    isnothing(i) && (reverse!(itr); return false)
      
    j = findlast(idx -> itr[idx] > itr[i], i+1:lastindex(itr)) + i
    itr[i], itr[j] = itr[j], itr[i] 
    reverse!(itr, i + 1)
    return true
end

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

```

