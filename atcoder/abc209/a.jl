A, B = parse.(Int, split(readline()))
res = B-A+1

if A == B
	println(0)
elseif res < 0
	println(0)
else
	println(res)
end
