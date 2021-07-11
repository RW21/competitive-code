A, B, C, D = parse.(Int, split(readline()))

function solve()
	res = -1


	bl = A
	re = 0

	for i in 1:A
		bl += B
		re += C
		if bl <= re * D
			println(i)
			return
		end
	end
	println(-1)
end

solve()



