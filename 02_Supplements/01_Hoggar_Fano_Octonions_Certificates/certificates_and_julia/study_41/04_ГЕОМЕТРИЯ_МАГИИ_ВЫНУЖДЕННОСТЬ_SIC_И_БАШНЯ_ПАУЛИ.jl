# =============================================================================
# Исследование 41, Этап 2. Скрипт 04: геометрия магии за октаэдром
#
#  P1. Полярная двойственность: нижний порог λ = 1/√3 из Г4 = радиус вписанной
#      сферы октаэдра = радиус выхода направления T из стабилизаторного октаэдра
#      = полуребро куба, вписанного в шар Блоха.
#  P2. Теорема о вынужденности вложения сцены s ↦ v_s: эквивариантность
#      относительно группы симметрий трёх вопросов (A4 или полная Td, 24)
#      оставляет одномерное пространство F(r) = α·r; резкость ⇒ α = ±1/√3.
#  P3. Дистилляция Бравого — Китаева (5-кубитный код) на оси T: порог,
#      и разбиение 68 % шара на «дистиллируемую» и «связанную» магию
#      для этого протокола.
#  P4. Башня рангов F2^(2n): существует ли SIC, ковариантная относительно
#      n-кубитной группы Паули (= группы Гейзенберга ТНР; при n = 3 это H_128)?
#      Численный поиск фидуциалов для n = 1, 2, 3 и алгебраическая степень
#      таблицы знаков ⟨P_a⟩ (полином Жегалкина).
#
# Запуск: julia 04_ГЕОМЕТРИЯ_МАГИИ_ВЫНУЖДЕННОСТЬ_SIC_И_БАШНЯ_ПАУЛИ.jl
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

const σx = ComplexF64[0 1; 1 0]; const σy = ComplexF64[0 -im; im 0]; const σz = ComplexF64[1 0; 0 -1]
const I2 = Matrix{ComplexF64}(I, 2, 2)

# =============================================================================
# P1. Полярная двойственность
# =============================================================================
println("== P1. Полярная двойственность октаэдр ↔ куб ==")
inr = 1 / norm([1, 1, 1])            # расстояние от 0 до грани x+y+z=1
λmin_G4 = 1 / sqrt(3)
r_exit_T = 1 / sqrt(3)                 # r·(1,1,1)/√3 имеет ‖·‖₁ = r√3
r_exit_H = 1 / sqrt(2)                 # r·(1,1,0)/√2 имеет ‖·‖₁ = r√2
cube_in_ball = 1 / sqrt(3)             # куб [-λ,λ]^3 ⊂ шар ⇔ λ√3 ≤ 1
# численная проверка через опорные функции: B(r) ⊆ O ⇔ O° ⊆ B(1/r), O° = [-1,1]^3
rng = MersenneTwister(1)
dirs = [normalize(randn(rng, 3)) for _ in 1:200000]
inr_num = minimum(1 / sum(abs.(d)) for d in dirs)   # радиальная функция октаэдра 1/‖d‖₁
circ_cube = maximum(sum(abs.(d)) for d in dirs)                                   # опорная функция куба = ‖d‖₁
@printf("  радиус вписанной сферы октаэдра: %.6f (числ. %.6f); описанной сферы куба [-1,1]^3: %.6f (числ. %.6f); произведение = 1\n",
    inr, inr_num, sqrt(3), circ_cube)
@printf("  порог Г4 λ_min = %.6f ; выход оси T из октаэдра r = %.6f ; оси H r = %.6f ; куб внутри шара при λ ≤ %.6f\n",
    λmin_G4, r_exit_T, r_exit_H, cube_in_ball)
put!("P1_polar_duality", Pair{String,Any}[
    "statement"=>"λ_min(Г4) = 1/√3 = радиус вписанной сферы октаэдра = радиус, на котором направление T (центр грани) выходит из стабилизаторного октаэдра = полуребро куба, вписанного в шар. Все четыре — одно утверждение по полярной двойственности: B(r) ⊆ O ⇔ O° = [-1,1]^3 ⊆ B(1/r). В Г4 нечётные таблицы имеют нормированный вектор λ(±1,±1,±1) (вершины куба), сбалансированные — λe_k (вершины октаэдра): интервал (1/√3, 1] — это «вершины октаэдра в шаре, вершины куба вне шара».",
    "inradius_octahedron"=>inr, "inradius_numeric"=>inr_num, "circumradius_cube"=>sqrt(3), "circumradius_numeric"=>circ_cube,
    "lambda_min_G4"=>λmin_G4, "exit_radius_T"=>r_exit_T, "exit_radius_H"=>r_exit_H,
    "status"=>"[Д]; элементарная выпуклая геометрия",
])

# =============================================================================
# P2. Вынужденность вложения сцены
# =============================================================================
println("\n== P2. Эквивариантность вынуждает v_s = α·r(s) ==")
using Base.Iterators: product
perms = [[1, 2, 3], [2, 3, 1], [3, 1, 2], [1, 3, 2], [3, 2, 1], [2, 1, 3]]
signs_even = [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]
pm(p, s) = (M = zeros(3, 3); for i in 1:3; M[i, p[i]] = s[i]; end; M)
G24 = [pm(p, s) for p in perms for s in signs_even]
G12 = [g for g in G24 if det(g) > 0]
C3K = [pm(p, s) for p in perms[1:3] for s in signs_even]                  # циклы вопросов + чётные отрицания
verts = [Float64[(-1)^x, (-1)^c, (-1)^(x ⊻ c)] for x in 0:1 for c in 0:1]  # r(s): ответы трёх вопросов
vidx(v) = findfirst(w -> norm(w - v) < 1e-9, verts)
function equivariant_dim(G)
    # неизвестные F(v_i) ∈ R^3, i=1..4 → 12 чисел; условие F(g v) = g F(v)
    rows = Vector{Vector{Float64}}()
    for g in G, i in 1:4
        j = vidx(g * verts[i]); j === nothing && error("группа не сохраняет тетраэдр")
        for k in 1:3
            row = zeros(12)
            row[3(j-1)+k] += 1
            for l in 1:3
                row[3(i-1)+l] -= g[k, l]
            end
            push!(rows, row)
        end
    end
    A = reduce(vcat, permutedims.(rows))
    N = nullspace(A)
    size(N, 2), N
end
results = Pair{String,Any}[]
for (name, G) in (("Td (24: все перестановки вопросов + чётные отрицания)", G24), ("T (12: только повороты)", G12), ("C3 вопросов + чётные отрицания (12)", C3K))
    d, N = equivariant_dim(G)
    prop = d == 1 ? begin
        F = reshape(N[:, 1], 3, 4)
        α = F[:, 1] ⋅ verts[1] / 3
        maximum(norm(F[:, i] - α * verts[i]) for i in 1:4) < 1e-9
    end : false
    @printf("  %-55s |G| = %2d : dim{эквивариантных F} = %d ; F ∝ r: %s\n", name, length(G), d, prop)
    push!(results, name => Pair{String,Any}["order"=>length(G), "dim"=>d, "proportional_to_r"=>prop])
end
αsharp = 1 / sqrt(3)
@printf("  резкость ‖v_s‖ = 1 ⇒ α = ±%.6f ; α < 0 переводит чётный тетраэдр в нечётный (ориентация β̄)\n", αsharp)
put!("P2_forced_embedding", Pair{String,Any}[
    "theorem"=>"Пусть сцена S=F2^2 читается тремя сбалансированными вопросами r(s)=((−1)^x,(−1)^c,(−1)^(x⊕c)) ∈ {±1}^3 (четыре чётные вершины куба), и вложение F: S → R^3 (вектор Блоха) эквивариантно относительно группы G, действующей перестановками вопросов и одновременным обращением пар ответов (на осях Блоха — соответствующими знаковыми перестановками). Если G транзитивна на S и стабилизатор вершины содержит цикл длины 3 вопросов, то F(s) = α·r(s). Требование резкости (чистые состояния, ‖F(s)‖=1) даёт α = ±1/√3: чётный (β) или нечётный (β̄) тетраэдр SIC. Борромеево тождество q1⊕q2⊕q3=0 не является отдельной посылкой: оно встроено в β = x⊕c.",
    "groups"=>results, "alpha"=>αsharp,
    "status"=>"[Д] (линейная алгебра + лемма о неподвижных векторах C3); снимает оговорку «вложение выбрано вручную» из Г5′ при посылке симметрии вопросов",
])

# =============================================================================
# P3. Дистилляция Бравого — Китаева (5-кубитный код)
# =============================================================================
println("\n== P3. Дистилляция магии (Bravyi–Kitaev 2005, 5→1, ось T) ==")
kronall(ms) = reduce(kron, ms)
P1 = Dict('I' => I2, 'X' => σx, 'Y' => σy, 'Z' => σz)
pauli(str) = kronall([P1[c] for c in str])
stabs = ["XZZXI", "IXZZX", "XIXZZ", "ZXIXZ"]
Pcode = prod((Matrix{ComplexF64}(I, 32, 32) + pauli(s)) / 2 for s in stabs)
Xl, Zl = pauli("XXXXX"), pauli("ZZZZZ")
Yl = im * Xl * Zl
# базис кодового пространства
v0 = Pcode * (e = zeros(ComplexF64, 32); e[1] = 1; e); v0 /= norm(v0)
v1 = Xl * v0; v1 /= norm(v1)
V = hcat(v0, v1)
@assert norm(V' * V - I) < 1e-10
function bk_step(r::Vector{Float64})
    ρ = (I2 + r[1] * σx + r[2] * σy + r[3] * σz) / 2
    ρ5 = kronall(fill(ρ, 5))
    M = V' * Pcode * ρ5 * Pcode * V
    p = real(tr(M))
    M /= p
    [real(tr(M * σx)), real(tr(M * σy)), real(tr(M * σz))], p
end
tdir = [1, 1, 1] / sqrt(3)
function out_along_T(r)
    ro, p = bk_step(r * tdir)
    # выход — состояние T-типа с точностью до клиффорда: берём лучшую из 8 диагоналей
    best = (abs(ro[1]) + abs(ro[2]) + abs(ro[3])) / sqrt(3)
    best, p, ro
end
# порог: r_out(r) = r
lo, hi = 0.58, 0.99
for _ in 1:60
    mid = (lo + hi) / 2
    o, _, _ = out_along_T(mid)
    o > mid ? (global hi = mid) : (global lo = mid)
end
rth = (lo + hi) / 2
o1, p1, ro1 = out_along_T(1.0)
o_half, _, ro_half = out_along_T(0.9)
@printf("  порог по радиусу на оси T: r* = %.6f ; теория √(3/7) = %.6f ; верность F* = (1+r*)/2 = %.6f (порог ошибки ε* = %.4f; BK: (1−√(3/7))/2 ≈ 0.173)\n", rth, sqrt(3 / 7), (1 + rth) / 2, (1 - rth) / 2)
@printf("  пример: r = 0.90 → выход %.4f, вектор (%.4f, %.4f, %.4f) — диагональ T с точностью до знаков\n", o_half, ro_half...)
@printf("  граница стабилизаторного октаэдра на оси T: r = %.6f ; «связанная» для BK полоса: (%.4f, %.4f]\n", 1 / sqrt(3), 1 / sqrt(3), rth)
# доли объёма шара (по T-скручиванию в лучший октант: дистиллируемо, если ‖r‖₁/√3 > r*)
Lth = sqrt(3) * rth
N = 4_000_000
cnt_stab = 0; cnt_bound = 0; cnt_dist = 0
for _ in 1:N
    v = 2 .* rand(rng, 3) .- 1
    norm(v) > 1 && continue
    l1 = sum(abs, v)
    if l1 <= 1
        global cnt_stab += 1
    elseif l1 <= Lth
        global cnt_bound += 1
    else
        global cnt_dist += 1
    end
end
tot = cnt_stab + cnt_bound + cnt_dist
fs, fb, fd = cnt_stab / tot, cnt_bound / tot, cnt_dist / tot
@printf("  доли шара Блоха: стабилизаторные %.2f%% (1/π = %.2f%%), не дистиллируемые протоколом BK-5 %.2f%%, дистиллируемые %.2f%%\n",
    100fs, 100 / π, 100fb, 100fd)
put!("P3_bravyi_kitaev", Pair{String,Any}[
    "threshold_radius_T"=>rth, "theory_sqrt_3_7"=>sqrt(3 / 7), "threshold_fidelity"=>(1 + rth) / 2,
    "stabilizer_face_radius_T"=>1 / sqrt(3),
    "ball_fraction_stabilizer"=>fs, "ball_fraction_not_BK_distillable_nonstabilizer"=>fb, "ball_fraction_BK_distillable"=>fd,
    "note"=>"Доля «дистиллируемых» дана для одного протокола (5-кубитный код с T-скручиванием в лучший октант); другие протоколы (Reichardt; Campbell–Browne о «связанной магии») дают иные границы. Состояния сцены (чистые SIC, r=1) — неподвижная точка: 5→1 сохраняет r=1.",
    "pure_scene_state_output"=>o1, "success_probability_pure"=>p1,
    "status"=>"[С] (численный расчёт протокола); [Кл] Bravyi–Kitaev 2005",
])

# =============================================================================
# P4. Башня Паули: SIC, ковариантные относительно n-кубитной группы Паули
# =============================================================================
println("\n== P4. SIC, ковариантные относительно группы Паули F2^(2n) (n = 1, 2, 3) ==")
function paulis_n(n)
    out = Tuple{Vector{Int},Matrix{ComplexF64}}[]
    for k in 1:(4^n-1)
        ax = [(k >> (2(j - 1))) & 1 for j in 1:n]; az = [(k >> (2(j - 1) + 1)) & 1 for j in 1:n]
        M = kronall([(σx^ax[j]) * (σz^az[j]) for j in 1:n])
        ph = im^(dot(ax, az) % 4)                   # P_a = i^{ax·az} X^ax Z^az — эрмитов
        push!(out, (vcat(ax, az), ph * M))
    end
    out
end
function sic_search(n; restarts=60, iters=4000, seed=7)
    d = 2^n; c = 1 / (d + 1)
    Ps = [P for (_, P) in paulis_n(n)]
    rng = MersenneTwister(seed)
    best = (Inf, zeros(ComplexF64, d))
    for _ in 1:restarts
        ψ = normalize(randn(rng, ComplexF64, d))
        m = zeros(ComplexF64, d); v = zeros(d); β1, β2, lr = 0.9, 0.999, 0.02
        f = Inf
        for t in 1:iters
            ψ = normalize(ψ)
            g = zeros(ComplexF64, d); f = 0.0
            for P in Ps
                Pψ = P * ψ; e = real(dot(ψ, Pψ))
                f += (e^2 - c)^2
                g .+= 4 * (e^2 - c) * e .* Pψ
            end
            g .-= real(dot(ψ, g)) .* ψ               # касательная к сфере
            m .= β1 .* m .+ (1 - β1) .* g; v .= β2 .* v .+ (1 - β2) .* abs2.(g)
            ψ = ψ .- lr .* (m ./ (1 - β1^t)) ./ (sqrt.(v ./ (1 - β2^t)) .+ 1e-12)
            f < 1e-26 && break
        end
        f < best[1] && (best = (f, normalize(ψ)))
        best[1] < 1e-24 && break
    end
    best
end
# алгебраическая нормальная форма (Жегалкин) булевой функции на F2^m
function anf_degree(tbl::Vector{Int}, m)
    a = copy(tbl)
    for i in 0:m-1, x in 0:(2^m-1)
        if (x >> i) & 1 == 1
            a[x+1] ⊻= a[(x ⊻ (1 << i))+1]
        end
    end
    maximum([count_ones(x) for x in 0:(2^m-1) if a[x+1] == 1]; init=0)
end
p4 = Pair{String,Any}[]
for n in 1:3
    t0 = time()
    f, ψ = sic_search(n; restarts=(n == 3 ? 40 : 80), iters=(n == 3 ? 6000 : 4000))
    d = 2^n
    evs = [real(dot(ψ, P * ψ)) for (_, P) in paulis_n(n)]
    exists = f < 1e-12
    rec = Pair{String,Any}["n"=>n, "d"=>d, "min_objective"=>f, "covariant_SIC_found"=>exists,
        "max_abs_dev_from_1_over_sqrt_dplus1"=>maximum(abs.(abs.(evs) .- 1 / sqrt(d + 1)))]
    if exists
        # таблица знаков ε_a = sign⟨P_a⟩ как булева функция f(a) на F2^(2n), f(0)=0
        tbl = zeros(Int, 4^n)
        for (k, (a, P)) in enumerate(paulis_n(n))
            idx = sum(a[j] << (j - 1) for j in 1:2n)
            tbl[idx+1] = real(dot(ψ, P * ψ)) < 0 ? 1 : 0
        end
        deg = anf_degree(tbl, 2n)
        push!(rec, "sign_table_ANF_degree" => deg)
        @printf("  n=%d (d=%d): SIC найдена, min f = %.2e, |⟨P⟩| = 1/√%d для всех %d Паули; степень Жегалкина таблицы знаков = %d ; %.1f с\n",
            n, d, f, d + 1, 4^n - 1, deg, time() - t0)
    else
        @printf("  n=%d (d=%d): ковариантная SIC НЕ найдена, min f = %.3e (по всем перезапускам); %.1f с\n", n, d, f, time() - t0)
    end
    push!(p4, "n=$n" => rec)
end
# --- P5. Инвариант чётности таблицы знаков (А3*) по многим фидуциалам ---
function sign_table(n, ψ)
    tbl = zeros(Int, 4^n)
    for (a, P) in paulis_n(n)
        idx = sum(a[j] << (j - 1) for j in 1:2n)
        tbl[idx+1] = real(dot(ψ, P * ψ)) < 0 ? 1 : 0
    end
    tbl
end
p5 = Pair{String,Any}[]
for n in (1, 3)
    degs = Int[]; es = Int[]; found = 0
    for seed in 101:124
        f, ψ = sic_search(n; restarts=10, iters=(n == 3 ? 6000 : 3000), seed=seed)
        f < 1e-12 || continue
        found += 1
        tbl = sign_table(n, ψ)
        push!(degs, anf_degree(tbl, 2n)); push!(es, sum(tbl) % 2)
    end
    @printf("  P5 n=%d: найдено %d фидуциалов; степени Жегалкина %s; чётность числа минусов e = %s\n", n, found, string(sort(unique(degs))), string(sort(unique(es))))
    push!(p5, "n=$n" => Pair{String,Any}["fiducials"=>found, "anf_degrees"=>sort(unique(degs)), "odd_minus_parity_values"=>sort(unique(es))])
end
put!("P5_sign_parity_invariant", Pair{String,Any}[
    "statement"=>"Таблица знаков ⟨P_a⟩ фидуциала как булева функция на F2^(2n). Клиффордовы преобразования меняют её линейной заменой a ↦ Sa и прибавлением квадратичной формы; поэтому при 2n ≥ 3 старший коэффициент Жегалкина (= чётность числа отрицательных ⟨P_a⟩) — клиффордов инвариант. При n=1 он не инвариантен (клиффордовы повороты меняют местами два тетраэдра).",
    "results"=>p5,
    "status"=>"[С] по найденным фидуциалам; инвариантность старшего коэффициента — [Д] (линейная замена сохраняет старший моном с множителем det=1, квадратичная добавка его не затрагивает при 2n≥3)",
])

put!("P4_pauli_covariant_SIC_tower", Pair{String,Any}[
    "statement"=>"Для башни F2^(2n) (n-кубитная группа Паули = группа Гейзенберга ТНР; n=3 ↔ H_128 Глав 15–16) ищется фидуциал ψ с |⟨ψ|P|ψ⟩|² = 1/(d+1) для всех неединичных P — тогда орбита ψ под группой Паули есть SIC из d² состояний, а сцена F2^(2n) «читается всеми вопросами с равной уверенностью».",
    "results"=>p4,
    "classical_reference"=>"Godsil–Roy 2009: SIC, ковариантные относительно n-кубитной группы Паули, существуют только при n=1 и n=3 (линии Хоггара, 64 линии в C^8).",
    "status"=>"[С] численный поиск (отсутствие при n=2 — численное свидетельство, доказательство — у Godsil–Roy)",
])

out = joinpath(@__DIR__, "04_СЕРТИФИКАТ_ГЕОМЕТРИИ_МАГИИ_И_БАШНИ_ПАУЛИ.json")
open(out, "w") do f
    write(f, tojson(Pair{String,Any}["script"=>basename(@__FILE__), "date"=>"2026-11-01", "results"=>CERT]))
end
println("\nСертификат: ", out)
