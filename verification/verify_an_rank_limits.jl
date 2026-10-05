using LinearAlgebra

# All numbers here belong to the declared binary/integer projection.
# The index A_n is the rank of the root system, not a stage of DOT exposition.
parity(x::Integer) = count_ones(x) % 2
bit(x, j) = (x >> (j - 1)) & 1
q(x::Integer) = (count_ones(x) ÷ 2) % 2
checks = Ref(0)
function require(value, description)
    checks[] += 1
    value || error(description)
end

println("n | dim_F2 | states | root_classes | radical_dim | q(u) | complement_closed")
for n in 1:8
    N = n + 1
    V = [x for x in 0:(2^N - 1) if parity(x) == 0]
    roots = [x for x in V if count_ones(x) == 2]
    rad = [x for x in V if all(parity(x & y) == 0 for y in V)]
    require(length(V) == 2^n, "A_n: number of binary states")
    require(length(roots) == binomial(N, 2), "A_n: root classes")
    require(length(rad) == (isodd(n) ? 2 : 1), "A_n: radical")
    full = 2^N - 1
    comp = all(xor(x, full) in roots for x in roots)
    require(comp == (n == 3), "Only A3 closes root classes by complement")
    if isodd(n)
        require(full in rad, "Distinguished radical vector")
        require(q(full) == ((n + 1) ÷ 2) % 2, "Norm of radical vector")
    end
    counts = [(k, count(x -> count_ones(x) == k, V)) for k in 0:2:N]
    println(n, " | ", n, " | ", length(V), " | ", length(roots), " | ",
            isodd(n) ? 1 : 0, " | ", isodd(n) ? string(q(full)) : "no u", " | ", comp,
            " ; weight layers ", counts)
end

# A4: ten 2-element supports and five 4-element supports.
# Bilinear form is parity intersection. Edges connect distinct
# orthogonal classes, not neighbors in the real root graph.
N = 5
V = [x for x in 0:(2^N - 1) if parity(x) == 0]
R = [x for x in V if count_ones(x) == 2]
O = [x for x in V if count_ones(x) == 4]
adj(x,y) = x != y && parity(x & y) == 0
require(length(R) == 10 && length(O) == 5, "Partition of A4: 1+10+5")
for x in R
    require(count(y -> adj(x,y), R) == 3, "Petersen: degree 3")
    for y in R
        x == y && continue
        common = count(z -> adj(x,z) && adj(y,z), R)
        require(common == (adj(x,y) ? 0 : 1), "Petersen: parameters (10,3,0,1)")
    end
end
for x in O, y in O
    x == y && continue
    require(parity(x & y) == 1, "Ovoid: pairs are not orthogonal")
end

P = [x for x in V if x != 0]
lines = Set{Tuple{Int,Int,Int}}()
for x in P, y in P
    x < y && parity(x & y) == 0 || continue
    push!(lines, Tuple(sort([x,y,xor(x,y)])))
end
require(length(lines) == 15, "Symplectic geometry: 15 lines")
for l in lines
    require(count(x -> x in O, l) == 1, "Ovoid meets each line exactly once")
end

# Correspondence of A3 to questions on four binary states.
S = [(0,0),(0,1),(1,0),(1,1)]
questions = Set{Int}()
for k in 0:1, a in 0:1, d in 0:1
    mask = sum(xor(k, xor(a*x,d*c)) << (j-1) for (j,(x,c)) in enumerate(S))
    push!(questions, mask)
end
require(questions == Set(x for x in 0:15 if parity(x) == 0), "A3 equals affine questions")

println("Checks completed: ", checks[], "; A4: KG(5,2), ovoid 5, GQ(2,2).")
