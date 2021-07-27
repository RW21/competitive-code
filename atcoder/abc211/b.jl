S = Set([readline() for i in 1:4])
proper = Set(["H" , "2B" , "3B" , "HR"])

function solve()
	if S == proper
		println("Yes")
	else
		println("No")
	end
end
solve()
