# Самостоятельная конечная проверка A3, вопросов и графового накрытия.
# Запуск: julia --startup-file=no verify_a3_cover.jl
# Скрипт не читает и не изменяет корпус; внешние пакеты не нужны.

function permutations_of(n::Int)
    result = Vector{Vector{Int}}()
    current = zeros(Int, n)
    used = falses(n)
    function visit(position)
        if position > n
            push!(result, copy(current))
            return
        end
        for value in 1:n
            if !used[value]
                used[value] = true
                current[position] = value
                visit(position + 1)
                used[value] = false
            end
        end
    end
    visit(1)
    result
end

bit_at(mask, i) = (mask >> (i - 1)) & 1
pair_mask(i, j) = (1 << (i - 1)) | (1 << (j - 1))
parity_mask(z) = sum(mod(z[i], 2) << (i - 1) for i in 1:4)
function permute_mask(mask, permutation)
    sum(bit_at(mask, i) << (permutation[i] - 1) for i in 1:4)
end
function apply_binary_matrix(columns, vector)
    result = 0
    for i in 1:3
        if bit_at(vector, i) == 1
            result = xor(result, columns[i])
        end
    end
    result
end
function components(nodes, adjacency)
    remaining = Set(nodes)
    sizes = Int[]
    while !isempty(remaining)
        reached = Set([first(remaining)])
        pending = collect(reached)
        while !isempty(pending)
            a = pop!(pending)
            for b in nodes
                if adjacency(a, b) && !(b in reached)
                    push!(reached, b)
                    push!(pending, b)
                end
            end
        end
        push!(sizes, length(reached))
        setdiff!(remaining, reached)
    end
    sort(sizes)
end

function main()
    u = 0b1111
    V = [q for q in 0:15 if iseven(count_ones(q))]
    balanced = [q for q in V if count_ones(q) == 2]
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    affine_table(k, a, d) = sum(
        xor(xor(k, a * states[i][1]), d * states[i][2]) << (i - 1)
        for i in 1:4)
    question_tables = Set(affine_table(k, a, d)
                          for k in 0:1 for a in 0:1 for d in 0:1)
    @assert length(V) == 8 && Set(V) == question_tables
    @assert length(balanced) == 6 && Set(V) == Set([0, u, balanced...])

    # Базис e_i-e_4 даёт все восемь чётнопаритетных таблиц.
    lattice_basis = [(1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1)]
    basis_masks = parity_mask.(lattice_basis)
    @assert basis_masks == [0b1001, 0b1010, 0b1100]
    basis_span = Set(
        xor(xor(a == 1 ? basis_masks[1] : 0,
                b == 1 ? basis_masks[2] : 0),
                c == 1 ? basis_masks[3] : 0)
        for a in 0:1 for b in 0:1 for c in 0:1
    )
    @assert basis_span == Set(V)
    lattice_sample = [(a, b, c, d) for a in -2:2 for b in -2:2
                      for c in -2:2 for d in -2:2 if a + b + c + d == 0]
    @assert Set(parity_mask.(lattice_sample)) == Set(V)
    @assert all(sum(z) == 0 && all(iseven, z) for z in lattice_sample
                if parity_mask(z) == 0)
    @assert all(sum(z .÷ 2) == 0 for z in lattice_sample if parity_mask(z) == 0)

    # Полярная форма — обычное скалярное произведение таблиц mod 2.
    bilinear(a, b) = count_ones(a & b) % 2
    quadratic(q) = (count_ones(q) ÷ 2) % 2
    radical = [a for a in V if all(bilinear(a, b) == 0 for b in V)]
    @assert radical == [0, u]
    @assert quadratic(u) == 0 && all(quadratic(q) == 1 for q in balanced)
    @assert all(quadratic(xor(a, b)) ==
                xor(xor(quadratic(a), quadratic(b)), bilinear(a, b))
                for a in V for b in V)

    directed = [(i, j) for i in 1:4 for j in 1:4 if i != j]
    roots = [ntuple(k -> Int(k == j) - Int(k == i), 4) for (i, j) in directed]
    lower(d) = pair_mask(d...)
    reverse_direction(d) = (d[2], d[1])
    complement(q) = xor(q, u)
    @assert length(Set(roots)) == 12
    @assert all(sum(r) == 0 && sum(abs2, r) == 2 for r in roots)
    @assert Set(parity_mask.(roots)) == Set(balanced)
    @assert all(count(r -> parity_mask(r) == q, roots) == 2 for q in balanced)
    @assert all(parity_mask(ntuple(k -> -r[k], 4)) == parity_mask(r) for r in roots)
    @assert all(lower(reverse_direction(d)) == lower(d) for d in directed)
    @assert all(complement(lower(d)) != lower(d) for d in directed)
    @assert all(count_ones(q & complement(q)) == 0 for q in balanced)
    @assert all(complement(complement(q)) == q for q in V)

    # Перестановки четырёх состояний совпадают со стабилизатором u.
    permutations4 = permutations_of(4)
    matrices = [(a, b, c) for a in 1:7 for b in 1:7 for c in 1:7
                if length(Set([0, a, b, c, xor(a, b), xor(a, c),
                               xor(b, c), xor(xor(a, b), c)])) == 8]
    stabilizer = Set(M for M in matrices if apply_binary_matrix(M, 7) == 7)
    represented = Set(
        Tuple(permute_mask(basis_masks[i], p) & 7 for i in 1:3)
        for p in permutations4
    )
    @assert length(matrices) == 168 && length(stabilizer) == 24
    @assert represented == stabilizer
    @assert all(permute_mask(u, p) == u for p in permutations4)
    @assert all(permute_mask(xor(a, b), p) ==
                xor(permute_mask(a, p), permute_mask(b, p))
                for p in permutations4 for a in V for b in V)
    @assert all(bilinear(permute_mask(a, p), permute_mask(b, p)) == bilinear(a, b)
                for p in permutations4 for a in V for b in V)
    @assert Set(a for a in V if all(permute_mask(a, p) == a for p in permutations4)) ==
            Set(radical)
    for i in 1:4, j in (i + 1):4
        reflection = collect(1:4)
        reflection[i], reflection[j] = reflection[j], reflection[i]
        alpha = pair_mask(i, j)
        @assert all(permute_mask(v, reflection) ==
                    xor(v, bilinear(v, alpha) == 1 ? alpha : 0) for v in V)
    end

    # Все 24 аффинных действия s↦As+b на четырёх состояниях.
    matrices2 = [(a, b) for a in 1:3 for b in 1:3 if a != b]
    affine_permutations = Set{NTuple{4, Int}}()
    for A in matrices2, translation in 0:3
        images = ntuple(4) do i
            s = states[i]
            v = s[1] | (s[2] << 1)
            image = xor(xor(bit_at(v, 1) == 1 ? A[1] : 0,
                            bit_at(v, 2) == 1 ? A[2] : 0), translation)
            point = (bit_at(image, 1), bit_at(image, 2))
            something(findfirst(==(point), states))
        end
        push!(affine_permutations, images)
        for k in 0:1, a in 0:1, d in 0:1
            coefficient = a | (d << 1)
            dot2(v, w) = count_ones(v & w) % 2
            transformed = affine_table(xor(k, dot2(coefficient, translation)),
                                       dot2(coefficient, A[1]), dot2(coefficient, A[2]))
            original = affine_table(k, a, d)
            pulled_back = sum(bit_at(original, images[i]) << (i - 1) for i in 1:4)
            @assert transformed == pulled_back
        end
    end
    @assert length(affine_permutations) == 24
    @assert affine_permutations == Set(Tuple(p) for p in permutations4)

    lower_adjacent(a, b) = a != b && count_ones(a & b) == 1
    upper_adjacent(d, e) = d != e && (d[1] == e[1] || d[2] == e[2])
    @assert sum(lower_adjacent(balanced[i], balanced[j])
                for i in 1:6 for j in (i + 1):6) == 12
    @assert sum(upper_adjacent(directed[i], directed[j])
                for i in 1:12 for j in (i + 1):12) == 24
    @assert all(count(e -> upper_adjacent(d, e), directed) == 4 for d in directed)
    @assert components(directed, upper_adjacent) == [12]
    for d in directed
        images = [lower(e) for e in directed if upper_adjacent(d, e)]
        expected = [q for q in balanced if lower_adjacent(lower(d), q)]
        @assert length(images) == length(Set(images)) == 4
        @assert Set(images) == Set(expected)
    end

    triangles = [(balanced[i], balanced[j], balanced[k])
                 for i in 1:6 for j in (i + 1):6 for k in (j + 1):6
                 if lower_adjacent(balanced[i], balanced[j]) &&
                    lower_adjacent(balanced[i], balanced[k]) &&
                    lower_adjacent(balanced[j], balanced[k])]
    stars = [tr for tr in triangles if xor(xor(tr[1], tr[2]), tr[3]) == u]
    cycles = [tr for tr in triangles if xor(xor(tr[1], tr[2]), tr[3]) == 0]
    @assert length(triangles) == 8 && length(stars) == length(cycles) == 4
    for tr in stars
        @assert components([d for d in directed if lower(d) in tr], upper_adjacent) == [3, 3]
    end
    for tr in cycles
        @assert components([d for d in directed if lower(d) in tr], upper_adjacent) == [6]
    end
    @assert Set(Tuple(sort(complement.(collect(tr)))) for tr in stars) ==
            Set(Tuple(sort(collect(tr))) for tr in cycles)

    # Из (V,u,+) восстанавливаются состояния-свидетели и все 12 флагов.
    recovered_stars = [(balanced[i], balanced[j], balanced[k])
                       for i in 1:6 for j in (i + 1):6 for k in (j + 1):6
                       if xor(xor(balanced[i], balanced[j]), balanced[k]) == u]
    @assert Set(recovered_stars) == Set(stars)
    witnesses = [something(findfirst(i -> all(bit_at(q, i) == 1 for q in tr), 1:4))
                 for tr in recovered_stars]
    @assert Set(witnesses) == Set(1:4)
    @assert all(count(tr -> q in tr, recovered_stars) == 2 for q in balanced)
    flags = [(q, f) for q in balanced for f in 1:4 if q in recovered_stars[f]]
    flag_direction = Dict(flag =>
        (witnesses[flag[2]], only(i for i in 1:4
                                if bit_at(flag[1], i) == 1 && i != witnesses[flag[2]]))
        for flag in flags)
    @assert length(flags) == 12 && Set(values(flag_direction)) == Set(directed)
    @assert all(lower(flag_direction[flag]) == flag[1] for flag in flags)
    @assert all(bit_at(lower(d), d[1]) == 1 for d in directed)

    # Геометрическое осуществление и нелинейная свёртка направления.
    tetrahedron = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    geometric_root(d) = ntuple(k ->
        (tetrahedron[d[2]][k] - tetrahedron[d[1]][k]) ÷ 2, 3)
    geometric_midpoint(q) = ntuple(k ->
        sum(bit_at(q, i) * tetrahedron[i][k] for i in 1:4) ÷ 2, 3)
    mu(r) = (r[2] * r[3], r[1] * r[3], r[1] * r[2])
    @assert length(Set(geometric_root.(directed))) == 12
    @assert length(Set(geometric_midpoint.(balanced))) == 6
    @assert all(mu(geometric_root(d)) == geometric_midpoint(lower(d)) for d in directed)
    @assert all(upper_adjacent(d, e) ==
                (sum((geometric_root(d)[k] - geometric_root(e)[k])^2 for k in 1:3) == 2)
                for d in directed for e in directed)

    # Полная нижняя группа: S4 и дополнительная центральная симметрия.
    lower_maps = [Tuple(permute_mask(q, p) for q in balanced) for p in permutations4]
    lower_maps_with_complement = [Tuple(complement(permute_mask(q, p)) for q in balanced)
                                  for p in permutations4]
    all_lower_maps = [lower_maps; lower_maps_with_complement]
    @assert length(Set(all_lower_maps)) == 48
    @assert !(Tuple(complement.(balanced)) in Set(lower_maps))
    @assert all(lower_adjacent(balanced[i], balanced[j]) == lower_adjacent(g[i], g[j])
                for g in all_lower_maps for i in 1:6 for j in 1:6)
    quotient_class(q) = min(q, complement(q))
    quotient_points = sort(unique(quotient_class.(balanced)))
    @assert length(quotient_points) == 3
    quotient_actions = [Tuple(quotient_class(permute_mask(q, p)) for q in quotient_points)
                        for p in permutations4]
    @assert length(Set(quotient_actions)) == 6
    @assert count(==(Tuple(quotient_points)), quotient_actions) == 4

    # Для каждой из 48 нижних симметрий перебираются все 2^6 выбора подъёма.
    fibers = [[d for d in directed if lower(d) == q] for q in balanced]
    lift_counts = Int[]
    for g in all_lower_maps
        number = 0
        for flip in 0:63
            mapping = Dict{Tuple{Int, Int}, Tuple{Int, Int}}()
            for i in 1:6
                targets = [d for d in directed if lower(d) == g[i]]
                @assert length(targets) == 2
                for side in 1:2
                    chosen = 1 + mod(side - 1 + bit_at(flip, i), 2)
                    mapping[fibers[i][side]] = targets[chosen]
                end
            end
            if all(upper_adjacent(d, e) == upper_adjacent(mapping[d], mapping[e])
                   for d in directed for e in directed)
                number += 1
            end
        end
        push!(lift_counts, number)
    end
    @assert lift_counts[1:24] == fill(2, 24)
    @assert lift_counts[25:48] == fill(0, 24)
    @assert sum(lift_counts) == 48

    upper_maps = [Tuple(swap ? (p[d[2]], p[d[1]]) : (p[d[1]], p[d[2]]) for d in directed)
                  for p in permutations4 for swap in (false, true)]
    @assert length(Set(upper_maps)) == 48
    @assert all(upper_adjacent(directed[i], directed[j]) == upper_adjacent(g[i], g[j])
                for g in upper_maps for i in 1:12 for j in 1:12)

    # Полнота верхней группы: максимальные треугольники образуют куб.
    cliques = [[d for d in directed if d[1] == i] for i in 1:4]
    append!(cliques, [[d for d in directed if d[2] == i] for i in 1:4])
    all_upper_triangles = [Set([directed[i], directed[j], directed[k]])
                          for i in 1:12 for j in (i + 1):12 for k in (j + 1):12
                          if upper_adjacent(directed[i], directed[j]) &&
                             upper_adjacent(directed[i], directed[k]) &&
                             upper_adjacent(directed[j], directed[k])]
    @assert length(all_upper_triangles) == 8
    @assert Set(all_upper_triangles) == Set(Set(c) for c in cliques)
    clique_adjacent(i, j) = i != j && !isempty(intersect(cliques[i], cliques[j]))
    @assert all(count(j -> clique_adjacent(i, j), 1:8) == 3 for i in 1:8)
    cube_automorphisms = count(p ->
        all(clique_adjacent(i, j) == clique_adjacent(p[i], p[j])
            for i in 1:8 for j in (i + 1):8), permutations_of(8))
    @assert cube_automorphisms == 48
    @assert all(count(c -> d in c, cliques) == 2 for d in directed)
    @assert all(length(intersect(cliques[i], cliques[j])) <= 1
                for i in 1:8 for j in (i + 1):8)

    println("Все утверждения проверены.")
    println("A3/2A3: 8 чётнопаритетных таблиц = 8 аффинных вопросов; радикал {0,u}.")
    println("12 корней дают 6 вопросов; обращение направления склеивается, дополнение не склеивается.")
    println("GL(3,2): 168; стабилизатор u = образ S4 = AGL(2,2): 24.")
    println("Графовое накрытие: 12 вершин / 24 ребра → 6 вершин / 12 рёбер.")
    println("4 тройки с XOR=u: два C3; 4 тройки с XOR=0: один C6.")
    println("Из (V,u,+) восстановлены 4 состояния и 12 направленных флагов.")
    println("Нижняя группа: 48; поднимаются ровно 24 элемента, каждый двумя способами.")
    println("Проверено 48×64 кандидата подъёма; у глобального дополнения подъёмов нет.")
    println("Полная верхняя группа: 48; её ядро над нижним графом — обращение направления.")
end

main()
