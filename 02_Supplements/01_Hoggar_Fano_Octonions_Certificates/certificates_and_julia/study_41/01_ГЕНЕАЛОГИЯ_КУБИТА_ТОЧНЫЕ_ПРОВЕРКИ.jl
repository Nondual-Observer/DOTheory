# =============================================================================
# Исследование 41. Скрипт 01: точные проверки генеалогии кубита
# (что выводится из конечной позиции наблюдателя, а что вводится явно)
#
# Части:
#   A. Фильтр чётности на 16 таблицах Q4 vs положительность эффектов:
#      при каких масштабах λ отображения Уолша — Блоха совпадение точное,
#      и что выделяет λ = 1 (резкость сбалансированных вопросов).
#   B. Т10 как локальная томография: размерности пространств наблюдаемых
#      для «ребитов» (вещественная КМ), для пары ячеек без P+, на W+ и на W-.
#   C. Граница Клиффорд / магия: группа, порождённая дискретной структурой,
#      = октаэдральная группа (24); неклиффордов T выходит за октаэдр;
#      стабилизаторная энтропия Реньи M2 на сфере Блоха; доля стабилизаторного
#      октаэдра в шаре Блоха.
#   D. Число стабилизаторных состояний n кубитов (конечность дискретной части).
#   E. r_min как разбиение Мура / конгруэнция Нероуда на модели скрученного шага.
#
# Запуск:  julia 01_ГЕНЕАЛОГИЯ_КУБИТА_ТОЧНЫЕ_ПРОВЕРКИ.jl
# Выход:   01_СЕРТИФИКАТ_ГЕНЕАЛОГИИ_КУБИТА.json (рядом со скриптом)
# =============================================================================
using LinearAlgebra, Printf

# ---------- минимальный JSON без внешних пакетов ----------
jesc(s::AbstractString) = replace(s, "\\" => "\\\\", "\"" => "\\\"", "\n" => "\\n")
tojson(x::Nothing, i=0) = "null"
tojson(x::Bool, i=0) = x ? "true" : "false"
tojson(x::Integer, i=0) = string(x)
tojson(x::AbstractFloat, i=0) = isfinite(x) ? @sprintf("%.10g", x) : "null"
tojson(x::AbstractString, i=0) = "\"" * jesc(x) * "\""
tojson(x::Symbol, i=0) = tojson(string(x))
function tojson(v::AbstractVector, i=0)
    isempty(v) && return "[]"
    pad = repeat("  ", i + 1)
    "[\n" * join([pad * tojson(e, i + 1) for e in v], ",\n") * "\n" * repeat("  ", i) * "]"
end
function tojson(d::AbstractVector{<:Pair}, i=0)
    pad = repeat("  ", i + 1)
    "{\n" * join([pad * tojson(string(k)) * ": " * tojson(v, i + 1) for (k, v) in d], ",\n") *
    "\n" * repeat("  ", i) * "}"
end

const CERT = Pair{String,Any}[]
put!(k, v) = push!(CERT, k => v)

const σx = ComplexF64[0 1; 1 0]
const σy = ComplexF64[0 -im; im 0]
const σz = ComplexF64[1 0; 0 -1]
const I2 = Matrix{ComplexF64}(I, 2, 2)

# =============================================================================
# A. Фильтр чётности = положительность эффектов
# =============================================================================
println("== A. Фильтр чётности на Q4 и положительность эффектов ==")
states = [(0, 0), (0, 1), (1, 0), (1, 1)]          # s = (x, c)
chars = [(1, 0), (0, 1), (1, 1)]                    # ненулевые характеры a
paulis = [σx, σy, σz]                               # любая биекция: положительность от неё не зависит
tables = [[(k >> (3 - i)) & 1 for i in 0:3] for k in 0:15]   # q = (q(00),q(01),q(10),q(11))
walsh(q, a) = sum(q[i] * (-1)^(a[1] * states[i][1] + a[2] * states[i][2]) for i in 1:4) / 4
parity(q) = sum(q) % 2                               # старший коэффициент Жегалкина e(q)

function effect(q, λ)
    E = walsh(q, (0, 0)) * I2
    for (a, P) in zip(chars, paulis)
        E += λ * walsh(q, a) * P
    end
    E
end
ispos(E; tol=1e-12) = (ev = eigvals(Hermitian(E)); minimum(ev) >= -tol && maximum(ev) <= 1 + tol)

affine_set = Set(k for k in 0:15 if parity(tables[k+1]) == 0)
λgrid = collect(0.0:0.001:1.5)
match = [Set(k for k in 0:15 if ispos(effect(tables[k+1], λ))) == affine_set for λ in λgrid]
λok = λgrid[match]
λlo, λhi = minimum(λok), maximum(λok)
@printf("  совпадение «допустимые эффекты = 8 аффинных таблиц» при λ ∈ [%.3f, %.3f] (теория: (1/√3, 1] = (%.4f, 1])\n", λlo, λhi, 1 / sqrt(3))

# резкость: при каком λ сбалансированные вопросы становятся проекторами
balanced = [k for k in 0:15 if sum(tables[k+1]) == 2]
sharp(λ) = all(begin
    E = effect(tables[k+1], λ); norm(E * E - E) < 1e-12
end for k in balanced)
sharp_λ = [λ for λ in λgrid if sharp(λ)]
@printf("  сбалансированные вопросы — проекторы (резкие измерения) только при λ = %s\n", string(sharp_λ))

# что такое 8 допущенных эффектов при λ=1
stab_effects = [zeros(ComplexF64, 2, 2), I2, [(I2 + s * P) / 2 for P in paulis for s in (1, -1)]...]
adm = [effect(tables[k+1], 1.0) for k in sort(collect(affine_set))]
is_stab = all(any(norm(E - S) < 1e-12 for S in stab_effects) for E in adm)
println("  при λ=1 допущенные 8 эффектов = {0, I, (I±σ_k)/2} (стабилизаторные эффекты): ", is_stab)

odd_eigs = sort(unique(round.(vcat([eigvals(Hermitian(effect(tables[k+1], 1.0))) for k in 0:15 if parity(tables[k+1]) == 1]...), digits=6)))
put!("A_parity_filter", Pair{String,Any}[
    "statement"=>"Линейное отображение Уолша—Блоха E_λ(q)=q̂(0)I+λΣ_a q̂(a)σ_a: множество q с 0≤E_λ(q)≤I совпадает с 8 аффинными (чётными) таблицами тогда и только тогда, когда λ∈(1/√3,1]; λ=1 — единственное значение, при котором 6 сбалансированных вопросов становятся проекторами.",
    "lambda_interval_numeric"=>[λlo, λhi],
    "lambda_interval_theory"=>["1/sqrt(3) (не включая)", "1 (включая)"],
    "sharp_lambda"=>sharp_λ,
    "admitted_equal_stabilizer_effects_at_lambda1"=>is_stab,
    "odd_table_eigenvalues_lambda1"=>odd_eigs,
    "status"=>"[Д] элементарно; классическая опора: аффинные булевы функции ↔ стабилизаторные проекторы (Gross 2006 для нечётных d; Gottesman 1997)",
])

# =============================================================================
# B. T10 = локальная томография
# =============================================================================
println("\n== B. Проектор P+ и локальная томография ==")
J2 = [0.0 -1.0; 1.0 0.0]
J4 = kron(Matrix(1.0I, 2, 2), J2)                    # комплексная структура C^2 ≅ R^4
symbasis(n) = [begin
    M = zeros(n, n); M[i, j] = 1; M[j, i] = 1; M
end for i in 1:n for j in i:n]

# размерность {A симметричная на подпространстве (базис B) : A коммутирует со всеми Js}
function dim_sym_commuting(Bsub, Js)
    k = size(Bsub, 2)
    basis = symbasis(k)
    isempty(Js) && return length(basis)
    Jr = [Bsub' * J * Bsub for J in Js]               # ограничение на подпространство (ортонорм. базис)
    M = hcat([vcat([vec(S * J - J * S) for J in Jr]...) for S in basis]...)
    length(basis) - rank(M; atol=1e-9)
end
orth(P) = (F = svd(P); F.U[:, F.S .> 1e-9])

I4 = Matrix(1.0I, 4, 4); I16 = Matrix(1.0I, 16, 16)
JA = kron(J4, I4); JB = kron(I4, J4)
Pplus = (I16 - JA * JB) / 2
Pminus = (I16 + JA * JB) / 2
Wp = orth(Pplus); Wm = orth(Pminus)

d_cell = dim_sym_commuting(I4, [J4])
d_rebit = dim_sym_commuting(Matrix(1.0I, 2, 2), Matrix{Float64}[])
d_rebit2 = dim_sym_commuting(Matrix(1.0I, 4, 4), Matrix{Float64}[])
d_full_both = dim_sym_commuting(I16, [JA, JB])
d_Wp = dim_sym_commuting(Wp, [JA])
d_Wm = dim_sym_commuting(Wm, [JA])
@printf("  ячейка R^4 с J: dim Sym_J = %d (= Herm(C^2) = 4)\n", d_cell)
@printf("  ребит: %d, пара ребитов: %d  →  %d ≠ %d·%d: локальная томография НАРУШЕНА\n", d_rebit, d_rebit2, d_rebit2, d_rebit, d_rebit)
@printf("  R^4⊗R^4 с J_A и J_B по отдельности (без P+): %d\n", d_full_both)
@printf("  dim W+ = %d, наблюдаемые на W+: %d = 4·4 → локальная томография выполнена\n", size(Wp, 2), d_Wp)
@printf("  dim W- = %d, наблюдаемые на W-: %d (сектор с сопряжённой ориентацией i)\n", size(Wm, 2), d_Wm)

# Порождают ли произведения локальных наблюдаемых всё пространство на W+?
cellbasis = let B = symbasis(4)
    M = hcat([vec(S * J4 - J4 * S) for S in B]...)
    N = nullspace(M)
    [reshape(sum(N[i, c] * vec(B[i]) for i in 1:length(B)), 4, 4) for c in 1:size(N, 2)]
end
prods_Wp = hcat([vec(Wp' * kron(A, B) * Wp) for A in cellbasis for B in cellbasis]...)
rank_prods = rank(prods_Wp; atol=1e-9)
reb = symbasis(2)
rank_reb = rank(hcat([vec(kron(A, B)) for A in reb for B in reb]...); atol=1e-9)
@printf("  ранг произведений A⊗B, сжатых на W+: %d (из %d) ; для ребитов: %d (из %d)\n", rank_prods, d_Wp, rank_reb, d_rebit2)

put!("B_local_tomography", Pair{String,Any}[
    "statement"=>"Запрет внешнего оракула разности фаз (А3*, P+) эквивалентен условию локальной томографии K_AB=K_A·K_B, которое в реконструкциях КМ отделяет комплексную теорию от вещественной (Wootters 1990; Hardy 2001; Hardy–Wootters 2012; Masanes–Müller 2011).",
    "dim_cell_SymJ"=>d_cell,
    "rebit"=>d_rebit, "two_rebits"=>d_rebit2,
    "full_R4xR4_commuting_with_JA_and_JB"=>d_full_both,
    "dim_Wplus"=>size(Wp, 2), "observables_on_Wplus"=>d_Wp,
    "dim_Wminus"=>size(Wm, 2), "observables_on_Wminus"=>d_Wm,
    "rank_local_products_on_Wplus"=>rank_prods,
    "rank_local_products_rebits"=>rank_reb,
    "note"=>"W+ и W- дают изоморфные комплексные двухкубитные пространства (C⊗C и C⊗C̄): выбор P+ — соглашение об относительной ориентации i, а не вывод.",
    "status"=>"[Д] (счёт размерностей); классическое содержание — известный результат о локальной томографии",
])

# =============================================================================
# C. Клиффорд / магия
# =============================================================================
println("\n== C. Граница Клиффорд / магия ==")
function so3(U)            # присоединённое действие на оси Паули
    P = [σx, σy, σz]
    [real(tr(P[i] * U * P[j] * U') / 2) for i in 1:3, j in 1:3]
end
H = [1 1; 1 -1] / sqrt(2) .+ 0im
S = ComplexF64[1 0; 0 im]
T = ComplexF64[1 0; 0 exp(im * π / 4)]
Rtnr = (I2 + (σx * σz)) / sqrt(2)                   # R = (I+J)/√2, J = XZ = -iY
key(M) = Tuple(round.(Int, M))
gens = [so3(H), so3(S)]
group = Dict(key(Matrix(1.0I, 3, 3)) => Matrix(1.0I, 3, 3))
frontier = [Matrix(1.0I, 3, 3)]
while !isempty(frontier)
    nf = Matrix{Float64}[]
    for A in frontier, g in gens
        B = round.(g * A)
        if !haskey(group, key(B))
            group[key(B)] = B; push!(nf, B)
        end
    end
    global frontier = nf
end
poles = [s * e for e in eachcol(Matrix(1.0I, 3, 3)) for s in (1, -1)]
perm_poles = all(all(any(norm(G * p - q) < 1e-9 for q in poles) for p in poles) for G in values(group))
Rso3 = so3(Rtnr)
R_in = haskey(group, key(round.(Rso3))) && norm(Rso3 - round.(Rso3)) < 1e-9
Tso3 = so3(T)
T_pole_image = Tso3 * [1.0, 0, 0]
T_in = norm(Tso3 - round.(Tso3)) < 1e-9
@printf("  |<H,S>| в SO(3) = %d (октаэдральная группа O ≅ S4: 24); переставляет 6 полюсов: %s\n", length(group), perm_poles)
println("  R=(I+J)/√2 ТНР лежит в группе Клиффорда: ", R_in)
@printf("  T: образ полюса +x = (%.4f, %.4f, %.4f) — не полюс; T ∈ Клиффорд: %s\n", T_pole_image..., T_in)
function order_of(M; maxn=64)
    A = copy(M)
    for n in 1:maxn
        norm(A - I) < 1e-9 && return n
        A = A * M
    end
    -1
end
ordR_U2, ordR_SO3 = order_of(Rtnr), order_of(Rso3)
ordT_U2, ordT_SO3 = order_of(T), order_of(Tso3)
@printf("  порядки: R в U(2) = %d, в SO(3) = %d ; T в U(2) = %d, в SO(3) = %d\n", ordR_U2, ordR_SO3, ordT_U2, ordT_SO3)
println("  ⇒ «R⁸ = I» у ТНР — это поворот порядка 4 плюс спинорный знак; восьмёрка T — подлинный поворот на π/4 (неклиффордов)")

M2(r) = -log2((1 + sum(r .^ 4)) / 2)           # стабилизаторная энтропия Реньи (Leone–Oliviero–Hamma 2022), чистый кубит
best = (0.0, [0.0, 0, 0])
for θ in range(0, π, length=721), φ in range(0, 2π, length=1441)
    r = [sin(θ) * cos(φ), sin(θ) * sin(φ), cos(θ)]
    m = M2(r)
    m > best[1] && (global best = (m, r))
end
zero_at_poles = all(abs(M2(p)) < 1e-12 for p in poles)
@printf("  M2 = 0 ровно на 6 полюсах: %s; max M2 = %.6f (теория log2(3/2) = %.6f) при r ≈ (%.3f, %.3f, %.3f)\n",
    zero_at_poles, best[1], log2(1.5), abs.(best[2])...)
frac_oct = (4 / 3) / (4π / 3)
@printf("  доля стабилизаторного октаэдра |x|+|y|+|z|≤1 в шаре Блоха = 1/π = %.4f\n", frac_oct)

put!("C_clifford_magic", Pair{String,Any}[
    "statement"=>"Дискретная (над F2) часть конструкции порождает ровно клиффордову группу одного кубита (октаэдральная группа, 24 поворота), чьи орбиты — 6 полюсов октаэдра ТНР = 6 стабилизаторных состояний. Всё, что вне октаэдра, — «магия» (неклиффордов ресурс), который из конечной F2-структуры не выводится.",
    "clifford_group_order_SO3"=>length(group),
    "permutes_six_poles"=>perm_poles,
    "tnr_R_is_clifford"=>R_in,
    "T_is_clifford"=>T_in,
    "order_R_U2"=>ordR_U2, "order_R_SO3"=>ordR_SO3, "order_T_U2"=>ordT_U2, "order_T_SO3"=>ordT_SO3,
    "M2_zero_exactly_at_poles"=>zero_at_poles,
    "M2_max_numeric"=>best[1], "M2_max_theory"=>log2(1.5),
    "stabilizer_octahedron_volume_fraction"=>frac_oct,
    "status"=>"[Д]; классическая опора: Gottesman–Knill; Bravyi–Kitaev 2005 (magic states); Howard–Wallman–Veitch–Emerson 2014 (contextuality supplies the magic)",
])

# =============================================================================
# D. Конечность дискретной части: число стабилизаторных состояний
# =============================================================================
nstab(n) = big(2)^n * prod(big(2)^k + 1 for k in 1:n)
counts = [string(nstab(n)) for n in 1:6]
println("\n== D. Число стабилизаторных состояний n кубитов: ", join(counts, ", "))
put!("D_stabilizer_counts", Pair{String,Any}["n_1_to_6"=>counts, "formula"=>"2^n ∏_{k=1..n}(2^k+1) (Aaronson–Gottesman 2004)"])

# =============================================================================
# E. r_min = разбиение Мура (конгруэнция Нероуда)
# =============================================================================
println("\n== E. r_min как разбиение Мура на модели скрученного шага ==")
# состояния (v,s) ∈ F2^2, шаг V(v,s) = (v⊕1, s⊕v)
st = [(v, s) for v in 0:1 for s in 0:1]
Vstep(x) = (x[1] ⊻ 1, x[2] ⊻ x[1])
function moore(states, step, q)
    # начальное разбиение по ответу q, затем уточнение по классу образа
    cls = Dict(x => q(x) for x in states)
    while true
        sig = Dict(x => (cls[x], cls[step(x)]) for x in states)
        labels = Dict(v => i for (i, v) in enumerate(unique(values(sig))))
        new = Dict(x => labels[sig[x]] for x in states)
        length(unique(values(new))) == length(unique(values(cls))) && return new
        cls = new
    end
end
rv = moore(st, Vstep, x -> x[1]); rs = moore(st, Vstep, x -> x[2])
nv, ns = length(unique(values(rv))), length(unique(values(rs)))
@printf("  вопрос «видимый бит v»: |r_min| = %d ; вопрос «бит листа s»: |r_min| = %d\n", nv, ns)
period = let x = (0, 0), n = 0
    while true
        x = Vstep(x); n += 1
        x == (0, 0) && break
    end
    n
end
@printf("  порядок скрученного шага V: %d (V² ≠ id, V⁴ = id)\n", period)
put!("E_rmin_moore", Pair{String,Any}[
    "statement"=>"Минимальная достаточная память r_min относительно будущих вопросов q∘T^n — это разбиение Мура / конгруэнция Нероуда (Moore 1956; Nerode 1958; в теории управления — фактор наблюдаемости Калмана). Она зависит от библиотеки вопросов, а не только от динамики.",
    "rmin_size_question_v"=>nv, "rmin_size_question_s"=>ns, "order_of_V"=>period,
    "status"=>"[Д]; классическое совпадение",
])

# =============================================================================
# F. Сцена S = F2^2, прочитанная тремя сбалансированными вопросами, = SIC-POVM кубита
# =============================================================================
println("\n== F. Сцена из 4 состояний через вопросы (x, c, β=x⊕c) = тетраэдр SIC на сфере Блоха ==")
vs = [[(-1.0)^x, (-1.0)^c, (-1.0)^(x ⊻ c)] / sqrt(3) for (x, c) in states]
dots = [dot(vs[i], vs[j]) for i in 1:4 for j in 1:4 if i < j]
overlaps = [(1 + d) / 2 for d in dots]                  # |<ψ_i|ψ_j>|² для чистых состояний
povm = [(I2 + sum(v[k] * paulis[k] for k in 1:3)) / 4 for v in vs]
povm_sum_ok = norm(sum(povm) - I2) < 1e-12
# информационная полнота: 4 эффекта линейно независимы в 4-мерном Herm(C^2)
ic_rank = rank(hcat([vcat(real(vec(E)), imag(vec(E))) for E in povm]...); atol=1e-12)
m2s = [M2(v) for v in vs]
parity_prod = [prod(sign.(v)) for v in vs]
qprob = [(1 + 1 / sqrt(3)) / 2]
@printf("  попарные скалярные произведения: %s (правильный тетраэдр: −1/3)\n", string(round.(unique(round.(dots, digits=12)), digits=6)))
@printf("  перекрытия |<ψi|ψj>|² = %s (SIC: 1/3); ΣE_s = I: %s; ранг эффектов = %d (информационно полна)\n",
    string(round.(unique(round.(overlaps, digits=12)), digits=6)), povm_sum_ok, ic_rank)
@printf("  M2 каждого состояния сцены = %s (максимум магии log2(3/2)); произведение знаков = %s\n",
    string(round.(unique(round.(m2s, digits=9)), digits=6)), string(unique(parity_prod)))
@printf("  каждое состояние сцены отвечает на все три вопроса с вероятностью (1+1/√3)/2 = %.4f\n", qprob[1])
put!("F_scene_is_SIC", Pair{String,Any}[
    "statement"=>"Четыре состояния минимальной сцены S=F2^2, прочитанные тремя сбалансированными вопросами (x, c, β=x⊕c) как векторы Блоха ((−1)^x,(−1)^c,(−1)^(x⊕c))/√3, образуют правильный тетраэдр = SIC-POVM кубита: перекрытия 1/3, ΣE=I, информационная полнота; каждое состояние имеет максимальную стабилизаторную энтропию log2(3/2). Условие β=x⊕c (борромеево замыкание) выбирает один из двух дуальных тетраэдров; другой отвечает β̄.",
    "pairwise_dots"=>unique(round.(dots, digits=12)),
    "overlaps"=>unique(round.(overlaps, digits=12)),
    "povm_sums_to_identity"=>povm_sum_ok,
    "informationally_complete_rank"=>ic_rank,
    "M2_scene_states"=>unique(round.(m2s, digits=9)),
    "sign_product"=>unique(parity_prod),
    "answer_probability_each_question"=>qprob[1],
    "interpretation"=>"Вопросы ТНР (октаэдр) — стабилизаторный, клиффордов слой; состояния сцены (тетраэдр), увиденные через все три вопроса сразу, — максимально магический SIC-слой. Октаэдр и вписанный в куб тетраэдр — двойственные многогранники: шов Клиффорд/магия в ТНР — это шов «вопросы/сцена».",
    "status"=>"[Д]; классическая опора: Renes–Blume-Kohout–Scott–Caves 2004 (SIC-POVM), Fuchs–Schack (QBism, SIC как опорное измерение), Bravyi–Kitaev 2005 (T-тип магических состояний)",
])

out = joinpath(@__DIR__, "01_СЕРТИФИКАТ_ГЕНЕАЛОГИИ_КУБИТА.json")
open(out, "w") do f
    write(f, tojson(Pair{String,Any}["script"=>basename(@__FILE__), "date"=>"2026-11-01", "results"=>CERT]))
end
println("\nСертификат: ", out)
