A, B, C = parse.(Int, split(readline()))
println(maximum([A+B, B+C, C+A]))
