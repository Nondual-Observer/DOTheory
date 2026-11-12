# =============================================================================
# Исследование 41, Этап 3. Скрипт 06: Хоггар, Фано и чётность
#
#  T1. Теорема (элементарное доказательство необходимости, Godsil–Roy):
#      Паули-ковариантная SIC в d = 2^n возможна только при n = 1 или n = 3.
#      Проверка ключевого тождества на найденных фидуциалах.
#  T2. Теорема о чётности: e ≡ 1 + K (mod 2), где K — константа фазовой
#      структуры группы Паули (не зависит от фидуциала). Вычисление K.
#  T3. Группа клиффордовых симметрий фидуциала Хоггара: перечисление Sp(6,2)
#      (1 451 520 элементов) с фазовыми функциями, отбор стабилизатора,
#      порядок, орбиты на 63 ненулевых векторах.
#  T4. Содержит ли стабилизатор GL3(2), действующую как в Главе 16 ТНР
#      (подгруппа Леви: (u,s) ↦ (g^{-T}u, g s), т. е. обратимые линейные схемы
#      из CNOT)? Поиск пар дополнительных лагранжевых подпространств,
#      явная сборка фидуциала, инвариантного относительно всех CNOT-схем.
#
# Запуск: julia 06_ХОГГАР_ФАНО_И_ЧЁТНОСТЬ.jl
# =============================================================================
using LinearAlgebra, Printf, Random, Statistics

jesc(s::AbstractString) = replace(s, "\\" => "\\\\", "\"" => "\\\"", "\n" => "\\n")
tojson(x::Nothing, i=0) = "null"
tojson(x::Bool, i=0) = x ? "true" : "false"
tojson(x::Integer, i=0) = string(x)
tojson(x::AbstractFloat, i=0) = isfinite(x) ? @sprintf("%.10g", x) : "null"
tojson(x::AbstractString, i=0) = "\"" * jesc(x) * "\""
function tojson(v::AbstractVector, i=0)
    isempty(v) && return "[]"
    pad = repeat("  ", i + 1)
    "[\n" * join([pad * tojson(e, i + 1) for e in v], ",\n") * "\n" * repeat("  ", i) * "]"
end
function tojson(d::AbstractVector{<:Pair}, i=0)
    pad = repeat("  ", i + 1)
    "{\n" * join([pad * tojson(string(k)) * ": " * tojson(v, i + 1) for (k, v) in d], ",\n") * "\n" * repeat("  ", i) * "}"
end
const CERT = Pair{String,Any}[]
put!(k, v) = push!(CERT, k => v)

const X1 = ComplexF64[0 1; 1 0]; const Z1 = ComplexF64[1 0; 0 -1]; const I1 = Matrix{ComplexF64}(I, 2, 2)
const N = 3; const D = 8; const NA = 64
# индекс a: биты 0..2 — a_x (кубиты 1..3), биты 3..5 — a_z
ax(a) = a & 7; az(a) = (a >> 3) & 7
symp(a, b) = (count_ones(ax(a) & az(b)) + count_ones(az(a) & ax(b))) & 1
function pauli(a)
    M = reduce(kron, [X1^((ax(a) >> (j - 1)) & 1) * Z1^((az(a) >> (j - 1)) & 1) for j in 1:N])
    im^(count_ones(ax(a) & az(a)) % 4) * M
end
const P = [pauli(a) for a in 0:NA-1]
@assert all(norm(P[a+1] - P[a+1]') < 1e-12 for a in 0:NA-1)

# ---------- фидуциал Хоггара (численный поиск) ----------
function sic_search(Ps, d; restarts=40, iters=6000, seed=7)
    c = 1 / (d + 1); rng = MersenneTwister(seed); best = (Inf, zeros(ComplexF64, d))
    for _ in 1:restarts
        ψ = normalize(randn(rng, ComplexF64, d)); m = zeros(ComplexF64, d); v = zeros(d)
        f = Inf
        for t in 1:iters
            ψ = normalize(ψ); g = zeros(ComplexF64, d); f = 0.0
            for Pm in Ps
                Pψ = Pm * ψ; e = real(dot(ψ, Pψ)); f += (e^2 - c)^2; g .+= 4 * (e^2 - c) * e .* Pψ
            end
            g .-= real(dot(ψ, g)) .* ψ
            m .= 0.9 .* m .+ 0.1 .* g; v .= 0.999 .* v .+ 0.001 .* abs2.(g)
            ψ = ψ .- 0.02 .* (m ./ (1 - 0.9^t)) ./ (sqrt.(v ./ (1 - 0.999^t)) .+ 1e-12)
            f < 1e-28 && break
        end
        f < best[1] && (best = (f, normalize(ψ)))
        best[1] < 1e-26 && break
    end
    best
end
f, ψ = sic_search(P[2:end], D)
E = [real(dot(ψ, P[a+1] * ψ)) for a in 0:NA-1]
@printf("Фидуциал Хоггара: невязка %.2e ; max | |E|−1/3 | = %.2e\n", f, maximum(abs.(abs.(E[2:end]) .- 1 / 3)))
s_of = [E[a+1] < 0 ? 1 : 0 for a in 0:NA-1]
e_par = sum(s_of) % 2

# =============================================================================
# T1. Необходимое условие существования
# =============================================================================
println("\n== T1. Тождество чистоты и необходимое условие ==")
# фаза произведения коммутирующих операторов: P_a P_b = φ(a,b) P_{a+b}, φ = ±1
φ = zeros(Int, NA, NA)
for a in 0:NA-1, b in 0:NA-1
    symp(a, b) == 0 || continue
    z = tr(P[(a⊻b)+1]' * P[a+1] * P[b+1]) / D
    φ[a+1, b+1] = round(Int, real(z))
end
# проверка: для каждого c ≠ 0 сумма по 15 парам {a, a+c} ⊂ c^⊥ \ {0,c} знаков t = sgnE(a) sgnE(a+c) φ равна 9·sgnE(c)
ok_T1 = true; minus_counts = Int[]
for c in 1:NA-1
    tot = 0; nminus = 0
    for a in 1:NA-1
        (a == c || symp(a, c) == 1) && continue
        a < (a ⊻ c) || continue
        t = sign(E[a+1]) * sign(E[(a⊻c)+1]) * φ[a+1, (a⊻c)+1]
        tot += Int(t); t < 0 && (nminus += 1)
    end
    push!(minus_counts, nminus)
    tot == 9 * Int(sign(E[c+1])) || (global ok_T1 = false)
end
@printf("  для всех 63 c: Σ по 15 парам = 9·sgn E(c): %s ; число минусов по парам ∈ %s\n", ok_T1, string(sort(unique(minus_counts))))
nec = [(n, 2^n, (2^n - 2) * sqrt(2^n + 1) / 2) for n in 1:8]
println("  требуемая сумма (d−2)√(d+1)/2 должна быть целой: ", join([@sprintf("n=%d: %.4f", n, v) for (n, _, v) in nec], "; "))
put!("T1_existence", Pair{String,Any}[
    "theorem"=>"Пусть ψ ∈ C^d, d = 2^n, и |⟨ψ|P_a|ψ⟩|² = 1/(d+1) для всех неединичных Паули. Из ρ² = ρ для коэффициента при P_c (c ≠ 0) антикоммутирующие пары сокращаются, и для 'd²/4−1' пар {a, a+c} ⊂ c^⊥\\{0,c} сумма знаков t_p = sgnE(a)·sgnE(a+c)·φ(a,a+c) равна (d−2)√(d+1)/2·sgnE(c). Она целая только если n = 1 (тогда пар нет) или d+1 — полный квадрат; 2^n+1 = m² ⇔ (m−1)(m+1) = 2^n ⇔ n = 3. Итак, Паули-ковариантная SIC возможна только при n ∈ {1, 3}; обе существуют (тетраэдр сцены и линии Хоггара).",
    "identity_verified_on_fiducial"=>ok_T1, "minus_counts_per_c"=>sort(unique(minus_counts)),
    "required_sums"=>[v for (_, _, v) in nec],
    "status"=>"[Д]; необходимость — элементарное доказательство (результат Godsil–Roy 2009), существование — классика",
])

# =============================================================================
# T2. Чётность e ≡ 1 + K (mod 2)
# =============================================================================
println("\n== T2. Теорема о чётности ==")
K = 0
for a in 1:NA-1, b in a+1:NA-1
    symp(a, b) == 0 || continue
    φ[a+1, b+1] < 0 && (global K += 1)
end
@printf("  K = число коммутирующих пар {a,b} (a≠b, ненулевые) с P_aP_b = −P_{a+b}: %d ; предсказание e = 1 + K mod 2 = %d ; у фидуциала e = %d\n",
    K, (1 + K) % 2, e_par)
put!("T2_parity", Pair{String,Any}[
    "theorem"=>"Для любого Паули-ковариантного SIC-фидуциала в d = 8 чётность числа отрицательных ⟨P_a⟩ равна e ≡ 1 + K (mod 2), где K — число коммутирующих пар различных ненулевых a, b с P_aP_b = −P_{a+b} (зависит только от соглашения о фазах Паули). Доказательство: из T1 число минусов по парам для данного c равно 3 (E(c)>0) или 12 (E(c)<0), т. е. ≡ 1 + s(c); суммируя по c, слагаемые s(a) входят по 30 раз (чётно), остаётся Σ_pairs e(a,b) = K ≡ 63 + e.",
    "convention"=>"P_a = i^{a_x·a_z} X^{a_x} Z^{a_z}",
    "K"=>K, "predicted_e"=>(1 + K) % 2, "fiducial_e"=>e_par,
    "status"=>"[Д]",
])

# =============================================================================
# T3. Стабилизатор в Sp(6,2)
# =============================================================================
println("\n== T3. Перечисление Sp(6,2) с фазовыми функциями ==")
# порядок кубитов в kron: кубит 1 — старший множитель; индекс базиса x: бит (N - j) ↔ кубит j
# чтобы не путаться, строим однокубитные вентили тем же kron, а CNOT — через сопряжение Паули
on(j, U) = reduce(kron, [k == j ? U : I1 for k in 1:N])
H1 = ComplexF64[1 1; 1 -1] / sqrt(2); S1 = ComplexF64[1 0; 0 im]
function cnot(c, t)   # CNOT как 1/2(I+Z_c) + 1/2(I−Z_c)X_t
    (on(c, I1) + on(c, Z1)) / 2 + (on(c, I1) - on(c, Z1)) / 2 * on(t, X1)
end
gens = Matrix{ComplexF64}[]
for j in 1:N; push!(gens, on(j, H1)); push!(gens, on(j, S1)); end
for c in 1:N, t in 1:N; c != t && push!(gens, cnot(c, t)); end
# действие вентиля: g P_a g† = (−1)^h P_{S a}
function gate_action(g)
    img = zeros(Int, NA); hb = zeros(Int, NA)
    for a in 0:NA-1
        Q = g * P[a+1] * g'
        for b in 0:NA-1
            z = tr(P[b+1]' * Q) / D
            if abs(abs(z) - 1) < 1e-9
                img[a+1] = b; hb[a+1] = real(z) < 0 ? 1 : 0; break
            end
        end
    end
    img, hb
end
GA = [gate_action(g) for g in gens]
packkey(img) = reduce(|, [UInt64(img[1<<(i-1)+1]) << (6(i - 1)) for i in 1:6])
function imgs_from_key(k)
    basis = [Int((k >> (6(i - 1))) & 63) for i in 1:6]
    [reduce(⊻, [basis[i] for i in 1:6 if (a >> (i - 1)) & 1 == 1]; init=0) for a in 0:NA-1]
end
hbits(hv) = reduce(|, [UInt64(hv[a+1]) << a for a in 0:NA-1])
id_img = collect(0:NA-1)
t0 = time()
group = Dict{UInt64,Tuple{UInt64,UInt64,Int8}}()     # ключ S → (h, ключ родителя, номер вентиля)
k0 = packkey(id_img)
group[k0] = (UInt64(0), k0, Int8(0))
frontier = [k0]
while !isempty(frontier)
    nf = UInt64[]
    for k in frontier
        img = imgs_from_key(k); h = group[k][1]
        for (gi, (gimg, gh)) in enumerate(GA)
            nimg = [gimg[img[a+1]+1] for a in 0:NA-1]
            nk = packkey(nimg)
            haskey(group, nk) && continue
            nh = h ⊻ hbits([gh[img[a+1]+1] for a in 0:NA-1])
            group[nk] = (nh, k, Int8(gi)); push!(nf, nk)
        end
    end
    global frontier = nf
end
@printf("  |Sp(6,2)| найдено: %d (теория 1 451 520) ; %.1f с\n", length(group), time() - t0)

sbits = hbits(s_of)
bit(x::UInt64, a) = Int((x >> a) & 1)
stab = UInt64[]
for (k, (h, _, _)) in group
    img = imgs_from_key(k)
    Dv = [bit(sbits, img[a+1]) ⊻ bit(sbits, a) ⊻ bit(h, a) for a in 0:NA-1]
    lin = all(Dv[a+1] == reduce(⊻, [Dv[(1<<(i-1))+1] for i in 1:6 if (a >> (i - 1)) & 1 == 1]; init=0) for a in 0:NA-1)
    lin && push!(stab, k)
end
@printf("  стабилизатор фидуциала (образ в Sp(6,2)): порядок %d ; полная группа симметрий SIC в клиффордовой = 64 × %d = %d\n",
    length(stab), length(stab), 64 * length(stab))
# орбиты на ненулевых векторах
stab_imgs = [imgs_from_key(k) for k in stab]
seen = falses(NA); orbs = Int[]
for v in 1:NA-1
    seen[v+1] && continue
    orb = Set{Int}([v]); fr = [v]
    while !isempty(fr)
        nfr = Int[]
        for x in fr, im_ in stab_imgs
            y = im_[x+1]; y in orb || (push!(orb, y); push!(nfr, y))
        end
        fr = nfr
    end
    for y in orb; seen[y+1] = true; end
    push!(orbs, length(orb))
end
# порядки элементов
function elem_order(im_)
    cur = copy(im_); n = 1
    while cur != id_img
        cur = [im_[cur[a+1]+1] for a in 0:NA-1]; n += 1
    end
    n
end
ords = [elem_order(im_) for im_ in stab_imgs]
ordhist = sort([(o, count(==(o), ords)) for o in unique(ords)])
@printf("  орбиты на 63 ненулевых векторах: %s ; порядки элементов: %s\n", string(sort(orbs)), join(["$o:$c" for (o, c) in ordhist], " "))
put!("T3_stabilizer", Pair{String,Any}[
    "Sp62_order_found"=>length(group), "stabilizer_order"=>length(stab), "full_symmetry_order"=>64 * length(stab),
    "orbits_on_nonzero_vectors"=>sort(orbs), "element_orders"=>[[o, c] for (o, c) in ordhist],
    "note"=>"Порядок 12096 = |G2(2)| = |U3(3):2|; G2(2) — группа автоморфизмов октонионов над F2 (Stacey 2017: «Sporadic SICs and the normed division algebras»; Zhu 2015).",
    "status"=>"[С] исчерпывающее перечисление",
])

# =============================================================================
# T4. Подгруппа Леви GL3(2) (как в Главе 16)
# =============================================================================
println("\n== T4. GL3(2) в стабилизаторе: тип Леви (3 ⊕ 3*) как в Главе 16 ==")
# лагранжевы подпространства: 3-мерные вполне изотропные
lagr = UInt64[]
for a in 1:NA-1, b in a+1:NA-1, c in b+1:NA-1
    (symp(a, b) | symp(a, c) | symp(b, c)) == 0 || continue
    span = Set([0, a, b, c, a ⊻ b, a ⊻ c, b ⊻ c, a ⊻ b ⊻ c])
    length(span) == 8 || continue
    push!(lagr, reduce(|, [UInt64(1) << x for x in span]))
end
lagr = unique(lagr)
members(m) = [x for x in 0:NA-1 if (m >> x) & 1 == 1]
@printf("  лагранжевых подпространств: %d (теория 135)\n", length(lagr))
Lx = reduce(|, [UInt64(1) << x for x in 0:7])                    # a_z = 0
Lz = reduce(|, [UInt64(1) << (x << 3) for x in 0:7])             # a_x = 0
maps_to(im_, m) = all(((m >> im_[x+1]) & 1) == 1 for x in members(m))
levi_pairs = Tuple{UInt64,UInt64,Int}[]
for L1 in lagr, L2 in lagr
    (L1 & L2) == UInt64(1) || continue                           # пересечение только {0}
    L1 < L2 || continue
    sub = [im_ for im_ in stab_imgs if maps_to(im_, L1) && maps_to(im_, L2)]
    length(sub) >= 168 || continue
    restr = unique([[im_[x+1] for x in members(L1)] for im_ in sub])
    push!(levi_pairs, (L1, L2, length(restr)))
end
nfull = count(t -> t[3] == 168, levi_pairs)
@printf("  пар дополнительных лагранжевых (L1, L2), чей общий стабилизатор в Stab действует на L1 как вся GL3(2): %d\n", nfull)
std_sub = count(im_ -> maps_to(im_, Lx) && maps_to(im_, Lz), stab_imgs)
@printf("  у найденного фидуциала стабилизатор ∩ стандартная Леви (CNOT-схемы): %d элементов\n", std_sub)

explicit = Pair{String,Any}[]
if nfull > 0
global explicit = let
    (L1, L2, _) = first(filter(t -> t[3] == 168, levi_pairs))
    # ищем S0 ∈ Sp(6,2): S0(Lx) = L1, S0(Lz) = L2
    local k0s = nothing
    for (k, _) in group
        im_ = imgs_from_key(k)
        if all(((L1 >> im_[x+1]) & 1) == 1 for x in members(Lx)) && all(((L2 >> im_[x+1]) & 1) == 1 for x in members(Lz))
            k0s = k; break
        end
    end
    # восстановление слова и унитарного оператора
    word = Int[]; local k = k0s
    while group[k][3] != 0
        push!(word, group[k][3]); k = group[k][2]
    end
    local U0 = Matrix{ComplexF64}(I, D, D)
    for gi in reverse(word)
        U0 = gens[gi] * U0
    end
    ψ2 = U0' * ψ
    # проверка: каждый CNOT отображает ψ2 в P_b ψ2 (с точностью до фазы)
    function in_orbit(φv)
        maximum(abs(dot(P[b+1] * ψ2, φv)) for b in 0:NA-1)
    end
    cn_ok = [in_orbit(cnot(c, t) * ψ2) for c in 1:N for t in 1:N if c != t]
    E2 = [real(dot(ψ2, P[a+1] * ψ2)) for a in 0:NA-1]
    @printf("  явный фидуциал ψ' = U0†ψ: все |⟨P⟩| = 1/3: %s ; инвариантность под 6 CNOT (max перекрытие с орбитой Паули): %s\n",
        maximum(abs.(abs.(E2[2:end]) .- 1 / 3)) < 1e-9, string(round.(cn_ok, digits=10)))
    # стабилизатор ψ' ⊇ стандартная Леви?
    s2 = hbits([E2[a+1] < 0 ? 1 : 0 for a in 0:NA-1])
    local cnt_levi = 0
    for (k, (h, _, _)) in group
        im_ = imgs_from_key(k)
        (maps_to(im_, Lx) && maps_to(im_, Lz)) || continue
        Dv = [bit(s2, im_[a+1]) ⊻ bit(s2, a) ⊻ bit(h, a) for a in 0:NA-1]
        lin = all(Dv[a+1] == reduce(⊻, [Dv[(1<<(i-1))+1] for i in 1:6 if (a >> (i - 1)) & 1 == 1]; init=0) for a in 0:NA-1)
        lin && (cnt_levi += 1)
    end
    @printf("  у ψ' стабилизатор ∩ стандартная Леви = %d (вся GL3(2) = 168)\n", cnt_levi)
    Pair{String,Any}["word_length"=>length(word), "cnot_invariance_overlaps"=>cn_ok, "levi_in_stabilizer"=>cnt_levi,
        "fiducial_real"=>real.(ψ2), "fiducial_imag"=>imag.(ψ2)]
end
end
put!("T4_levi_GL32", Pair{String,Any}[
    "question"=>"Содержит ли стабилизатор Хоггар-фидуциала подгруппу GL3(2), действующую на F2^6 = W* ⊕ W как (g^{-T}, g) — так, как GL3(2) действует в Главе 16 ТНР (НС-09)? Такие подгруппы — в точности общие стабилизаторы пар дополнительных лагранжевых подпространств, действующие на них полностью.",
    "lagrangians"=>length(lagr), "levi_type_GL32_subgroups"=>nfull, "found_fiducial_std_levi_intersection"=>std_sub,
    "explicit_fiducial"=>explicit,
    "status"=>"[С] исчерпывающая проверка",
])

# =============================================================================
# T5. 36 подгрупп Леви ↔ 36 квадратичных форм плюс-типа (разбиение 36/28 док. 97)
# =============================================================================
println("\n== T5. Подгруппы Леви и квадратичные формы плюс-типа ==")
function qform(L1, L2)
    Q = zeros(Int, NA)
    for x1 in members(L1), x2 in members(L2)
        Q[(x1 ⊻ x2)+1] = symp(x1, x2)
    end
    Q
end
forms = [qform(L1, L2) for (L1, L2, r) in levi_pairs if r == 168]
uniqf = unique(forms)
polar_ok = all(all((Q[(x⊻y)+1] ⊻ Q[x+1] ⊻ Q[y+1]) == symp(x, y) for x in 0:NA-1 for y in 0:NA-1) for Q in uniqf)
Q0 = [count_ones(ax(a) & az(a)) & 1 for a in 0:NA-1]          # форма док. 97: чётность ⟨u,s⟩ (36 симметричных Паули)
allforms = [[Q0[a+1] ⊻ symp(c, a) for a in 0:NA-1] for c in 0:NA-1]
plusf = unique([Q for Q in allforms if count(==(0), Q) == 36])
bij = Set(uniqf) == Set(plusf)
# орбита формы под стабилизатором: (S·Q)(S a) = Q(a)
orbitQ = Set([uniqf[1]]); frQ = [uniqf[1]]
while !isempty(frQ)
    nfr = Vector{Vector{Int}}()
    for Q in frQ, im_ in stab_imgs
        Q2 = zeros(Int, NA)
        for a in 0:NA-1; Q2[im_[a+1]+1] = Q[a+1]; end
        Q2 in orbitQ || (push!(orbitQ, Q2); push!(nfr, Q2))
    end
    global frQ = nfr
end
@printf("  различных форм у 36 подгрупп Леви: %d ; все поляризуются в ω: %s ; форм плюс-типа всего: %d ; биекция: %s ; орбита стабилизатора на формах: %d\n",
    length(uniqf), polar_ok, length(plusf), bij, length(orbitQ))
@printf("  форма Q0(a) = a_x·a_z (36 симметричных / 28 кососимметричных операторов док. 97) среди них: %s\n", Q0 in uniqf)
put!("T5_levi_vs_plus_forms", Pair{String,Any}[
    "statement"=>"Каждая пара дополнительных лагранжевых (L1,L2) задаёт квадратичную форму Q(x1+x2)=ω(x1,x2) плюс-типа, поляризующуюся в ω. Проверяется: 36 подгрупп Леви GL3(2) в стабилизаторе Хоггара дают 36 различных форм = все 36 форм плюс-типа (чётные тэта-характеристики Sp(6,2)), и стабилизатор транзитивен на них. Форма Q0 = a_x·a_z — это ровно разбиение 36/28 из док. 97.",
    "distinct_forms"=>length(uniqf), "polarize_to_omega"=>polar_ok, "plus_type_total"=>length(plusf),
    "bijection"=>bij, "stabilizer_orbit_on_forms"=>length(orbitQ), "Q0_doc97_among"=>(Q0 in uniqf),
    "status"=>"[С] исчерпывающая проверка",
])

out = joinpath(@__DIR__, "06_СЕРТИФИКАТ_ХОГГАР_ФАНО_ЧЁТНОСТЬ.json")
open(out, "w") do f
    write(f, tojson(Pair{String,Any}["script"=>basename(@__FILE__), "date"=>"2026-11-01", "results"=>CERT]))
end
println("\nСертификат: ", out)
