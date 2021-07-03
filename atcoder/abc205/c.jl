function solve()
	A, B, C = parse.(Int, split(readline()))
	if C % 2 == 0
		A, B = abs(A), abs(B)
	end
	# x = A^C
	# y = B^C

	if A > B
		println(">")
	elseif A == B
		println("=")
	else
		println("<")
	end
	# if x > y
	# 	println(">")
	# elseif x == y
	# 	println("=")
	# else
	# 	println("<")
	# end
end

solve()

