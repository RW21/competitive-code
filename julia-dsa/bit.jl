module Tree

mutable struct Bit{T, N} <: AbstractArray{T, N}
	arr::Array{T}

	function Bit(arr::Vector)
		n = length(arr)
		b = new{typeof(arr[1]), n}(arr)
		for (i, x) in enumerate(arr)
			# b[i] = x
			add!(b, x, i)
		end
		return b
		# return new{typeof(arr[1]), length(arr)}(arr)
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

function Base.sum(B::Bit, l, r)
	return sum(B, r) - sum(B, l)
end

function Base.sum(B::Bit, i)
	s = 0
	while i > 0
		s += B.arr[i]
		i -= (i & -i)
	end
	return s
end
end

a = Tree.Bit([i for i in 0:7])
b = Tree.sum(a, 2, 4)
println(b)

