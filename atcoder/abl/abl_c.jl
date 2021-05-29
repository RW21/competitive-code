n, m = parse.(Int, split(readline()))

paths = [[] for i in 1:n]

for i in 1:m
	vertex, value = parse.(Int, split(readline()))
	append!(paths[vertex], value)
end

function solve(paths)
	visited = fill(false, n)
	count = 0

	for v in 1:n
		println(visited)
		if !visited[v]
			count += 1
		end
		stack = [v]
		while !isempty(stack)
			current = pop!(stack)
			if !visited[current]
				visited[current] = true
				for next in paths[current]
					push!(stack, next)
				end
			end
		end
	end

	println(count-1)
end

solve(paths)

