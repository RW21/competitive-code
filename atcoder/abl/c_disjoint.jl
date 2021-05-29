module DisjointSet

mutable struct TreeNode
	parent::Union{TreeNode, Nothing}
	rank::Integer
	val
end

function Base.show(io::IO, n::TreeNode)
	print(io, "$(n.val) -> $(n.parent)")
end

function makeset(val)::TreeNode
	return TreeNode(nothing, 0, val)
end

function link!(x::TreeNode, y::TreeNode)
	if x.rank > y.rank
		y.parent = x
	else
		x.parent = y
		if x.rank == y.rank
			y.rank += 1
		end
	end
end

function findset(x::TreeNode)::TreeNode
	if x.parent === nothing
		return x
	end
	return findset(x.parent)
end

function union!(x::TreeNode, y::TreeNode)
	link!(findset(x), findset(y))
end
end

n, m = parse.(Int, split(readline()))

paths = []

for i in 1:m
	vertex, value = parse.(Int, split(readline()))
	push!(paths, [vertex, value])
end


function solve(paths)
	dsets = [DisjointSet.makeset(i) for i in 1:n]

	for (from, to) in paths
		if DisjointSet.findset(dsets[from]) != DisjointSet.findset(dsets[to])
			DisjointSet.union!(dsets[from], dsets[to])
		end
	end

	println(count(s->(s.parent === nothing), dsets) - 1)
end

solve(paths)

