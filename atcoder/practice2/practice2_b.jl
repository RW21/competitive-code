module Tree
mutable struct Bit{T, N} <: AbstractArray{T, N}
	arr::Array{T}
	# Bit() = (x = new(){}; x.arr = [])
	#
	function Bit(arr::Vector)
		n = length(arr)
		b = new{typeof(arr[1]), n}(arr)
		# b.arr = zeros(n)
		for (i, x) in enumerate(arr)
			b[i] = x
			add!(b, x, i)
		end
		return b
	end
end

function Base.show(io::IO, B::Bit)
	print(io, "$(B.arr)")
end

function Base.size(B::Bit)
	return length(B.arr)
end

function Base.getindex(B::Bit, i::Integer)
	return B.arr[i]
end

function add!(B::Bit, x, i::Integer)
	while i < length(B)
		B.arr[i] += x
		i += (i & -i)
	end
end

function Base.setindex!(B::Bit, x, i::Integer)
	B.arr[i] = x
end

function Base.sum(B::Bit, i, f=+)
	s = 0
	while i > 0
		s += f(s, B.arr[i])
		i -= (i & -i)
	end
	return s
end
end

N, Q = parse.(Int, split(readline()))

fun
