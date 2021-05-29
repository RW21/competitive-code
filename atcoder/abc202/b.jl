S = readline()

function angle(s::Char)
	if s == '6'
		return '9'
	elseif s == '9'
		return '6'
	else
		return s
	end
end

print(map(angle, reverse(S)))


