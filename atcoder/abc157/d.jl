module DisjointSet

mutable struct TreeNode
	parent::Union{TreeNode, Nothing}
	child::Union{TreeNode, Nothing}
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
n, m, k = parse.(Int, split(readline()))

friends = [[] for i in 1:m]
# friends = [parse.(Int, split(readline())) for i in 1:m]
blocks = [[] for i in 1:k]
# blocks = [parse.(Int, split(readline())) for i in 1:k]
for i in 1:m
	from, to = parse.(Int, split(readline()))
	push!(friends[from], to)
end
for i in 1:k
	from, to = parse.(Int, split(readline()))
	push!(blocks[from], to)
end


function solve()
	dsets = [DisjointSet.makeset(i) for i in 1:n]

	for from in 1:m, to in friends[from]
		DisjointSet.union!(dsets[from], dsets[to])
	end

	end

	for person in dsets



