input = (x -> parse(Int, x)).(split(readline()))
input = (x -> 7-x).(input)
print(sum(input))

