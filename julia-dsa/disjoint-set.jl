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
	x.parent = findset(x.parent)
	return x.parent
end

function union!(x::TreeNode, y::TreeNode)
	link!(findset(x), findset(y))
end

end

# parent = DisjointSet.makeset(1)

# for i in 2:5
# 	newnode = DisjointSet.makeset(i)
# 	DisjointSet.link!(newnode, parent)
# 	println(newnode)
# end

