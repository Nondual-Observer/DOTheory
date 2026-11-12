# =============================================================================
# Исследование 41, Этап 4. Скрипт 10: формальная идентификация и октонионы
#
#  F1. Классы сопряжённости стабилизатора Хоггара (6048) и проверка простоты:
#      простая группа порядка 6048 единственна — PSU3(3).
#  F2. Полная группа симметрий с антиунитарными элементами (C∘K): порядок,
#      центр, индекс 2 над PSU3(3) ⇒ Aut(PSU3(3)) = G2(2).
#  F3. Октонионы над F2 явно: алгебра Цорна (a, v; w, b), v ∈ W = F2^3, w ∈ W*,
#      со сменой знаков, неважной над F2. Проверки: композиционность нормы,
#      альтернативность, неассоциативность. Наивная «таблица Фано»
#      e_i e_j = e_{i⊕j} над F2 — ассоциативна (это групповая алгебра, не октонионы).
#  F4. V = T0/F2·1 ≅ W ⊕ W* = пространство индексов Паули (a_x = v, a_z = w),
#      форма поляризации нормы = симплектическая форма ω. Каждый элемент
#      полной группы симметрий Хоггара поднимается до автоморфизма алгебры Цорна,
#      случайные элементы Sp(6,2) вне группы — нет. ⇒ группа = Aut(октонионов над F2) = G2(2).
#  F5. CNOT-инвариантные векторы образуют 2-мерное пространство span{|0⟩, Σ_{x≠0}|x⟩}.
#      В нём ровно два луча Хоггара: (−1 ± 2i)|0⟩ + Σ_{x≠0}|x⟩ (норма √12) — проверка и
#      сканирование всех лучей вида z|0⟩ + Σ_{x≠0}|x⟩. (Первая версия брала из поисковой
#      сводки (−1±i,1,…,1)/3 — это НЕ SIC; исправлено.)
#
# Запуск: julia 10_ИДЕНТИФИКАЦИЯ_PSU33_И_ОКТОНИОНЫ_ЦОРНА.jl
# =============================================================================
using LinearAlgebra, Printf, Random, JSON

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

# ---------------- Паули и Клиффорд (как в 06) ----------------
const X1 = ComplexF64[0 1; 1 0]; const Z1 = ComplexF64[1 0; 0 -1]; const I1 = Matrix{ComplexF64}(I, 2, 2)
const N = 3; const D = 8; const NA = 64
ax(a) = a & 7; az(a) = (a >> 3) & 7
symp(a, b) = (count_ones(ax(a) & az(b)) + count_ones(az(a) & ax(b))) & 1
Q0(a) = count_ones(ax(a) & az(a)) & 1
pauli(a) = im^(count_ones(ax(a) & az(a)) % 4) * reduce(kron, [X1^((ax(a) >> (j - 1)) & 1) * Z1^((az(a) >> (j - 1)) & 1) for j in 1:N])
const P = [pauli(a) for a in 0:NA-1]
on(j, U) = reduce(kron, [k == j ? U : I1 for k in 1:N])
cnot(c, t) = (on(c, I1) + on(c, Z1)) / 2 + (on(c, I1) - on(c, Z1)) / 2 * on(t, X1)
H1 = ComplexF64[1 1; 1 -1] / sqrt(2); S1 = ComplexF64[1 0; 0 im]
gens = Matrix{ComplexF64}[]
for j in 1:N; push!(gens, on(j, H1)); push!(gens, on(j, S1)); end
for c in 1:N, t in 1:N; c != t && push!(gens, cnot(c, t)); end
function gate_action(g)
    img = zeros(Int, NA); hb = zeros(Int, NA)
    for a in 0:NA-1
        Qm = g * P[a+1] * g'
        for b in 0:NA-1
            z = tr(P[b+1]' * Qm) / D
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
bit(x::UInt64, a) = Int((x >> a) & 1)
println("Перечисление Sp(6,2)…"); flush(stdout)
t0 = time()
group = Dict{UInt64,UInt64}()
k0 = packkey(collect(0:NA-1)); group[k0] = UInt64(0)
frontier = [k0]
while !isempty(frontier)
    nf = UInt64[]
    for k in frontier
        img = imgs_from_key(k); h = group[k]
        for (gimg, gh) in GA
            nimg = [gimg[img[a+1]+1] for a in 0:NA-1]
            nk = packkey(nimg)
            haskey(group, nk) && continue
            group[nk] = h ⊻ hbits([gh[img[a+1]+1] for a in 0:NA-1]); push!(nf, nk)
        end
    end
    global frontier = nf
end
@printf("|Sp(6,2)| = %d ; %.1f с\n", length(group), time() - t0); flush(stdout)

islinear(Dv) = all(Dv[a+1] == reduce(⊻, [Dv[(1<<(i-1))+1] for i in 1:6 if (a >> (i - 1)) & 1 == 1]; init=0) for a in 0:NA-1)
function symmetries(ψ)
    E = [real(dot(ψ, P[a+1] * ψ)) for a in 0:NA-1]
    sb = hbits([E[a+1] < 0 ? 1 : 0 for a in 0:NA-1])
    uni = UInt64[]; anti = UInt64[]
    for (k, h) in group
        img = imgs_from_key(k)
        Dv = [bit(sb, img[a+1]) ⊻ bit(sb, a) ⊻ bit(h, a) for a in 0:NA-1]
        islinear(Dv) && push!(uni, k)
        islinear([Dv[a+1] ⊻ Q0(a) for a in 0:NA-1]) && push!(anti, k)
    end
    uni, anti, E
end
cert06 = JSON.parsefile(joinpath(@__DIR__, "06_СЕРТИФИКАТ_ХОГГАР_ФАНО_ЧЁТНОСТЬ.json"))
fid = cert06["results"]["T4_levi_GL32"]["explicit_fiducial"]
ψp = ComplexF64.(fid["fiducial_real"]) .+ im .* ComplexF64.(fid["fiducial_imag"])
uni, anti, Ep = symmetries(ψp)
@printf("ψ′: унитарный стабилизатор %d, антиунитарных элементов %d, пересечение множеств S: %d\n",
    length(uni), length(anti), length(intersect(Set(uni), Set(anti)))); flush(stdout)

# ---------------- групповые операции на образах ----------------
compose(i1, i2) = [i1[i2[a+1]+1] for a in 0:NA-1]          # (S1∘S2)(a)
function inverse_img(im_)
    inv = zeros(Int, NA)
    for a in 0:NA-1; inv[im_[a+1]+1] = a; end
    inv
end
function elem_order(im_)
    cur = copy(im_); n = 1; id = collect(0:NA-1)
    while cur != id
        cur = compose(im_, cur); n += 1
    end
    n
end
function classes_of(keys)
    imgs = Dict(k => imgs_from_key(k) for k in keys)
    kset = Set(keys)
    rng = MersenneTwister(3)
    # порождающие: случайные элементы, пока не породят всю группу
    allk = collect(keys)
    gens_k = UInt64[]
    while true
        push!(gens_k, allk[rand(rng, 1:length(allk))])
        seen = Set{UInt64}([packkey(collect(0:NA-1))]); fr = collect(seen)
        while !isempty(fr)
            nfr = UInt64[]
            for k in fr, g in gens_k
                nk = packkey(compose(imgs[g], imgs_from_key(k)))
                nk in seen || (push!(seen, nk); push!(nfr, nk))
            end
            fr = nfr
        end
        length(seen) == length(keys) && break
        length(gens_k) > 6 && (empty!(gens_k))
    end
    ginv = Dict(g => inverse_img(imgs[g]) for g in gens_k)
    assigned = Dict{UInt64,Int}(); cls = Vector{Vector{UInt64}}()
    for k in allk
        haskey(assigned, k) && continue
        c = Set([k]); fr = [k]
        while !isempty(fr)
            nfr = UInt64[]
            for x in fr, g in gens_k
                y = packkey(compose(compose(imgs[g], imgs[x]), ginv[g]))
                y in c || (push!(c, y); push!(nfr, y))
            end
            fr = nfr
        end
        push!(cls, collect(c))
        for y in c; assigned[y] = length(cls); end
    end
    cls, imgs, gens_k
end

# =============================================================================
# F1. Классы сопряжённости и простота
# =============================================================================
println("\n== F1. Классы сопряжённости стабилизатора ==")
cls, imgsU, gU = classes_of(uni)
info = sort([(elem_order(imgsU[c[1]]), length(c)) for c in cls])
println("  (порядок, размер класса): ", join(["$(o):$(s)" for (o, s) in info], "  "))
atlas = sort([(1, 1), (2, 63), (3, 56), (3, 672), (4, 63), (4, 63), (4, 378), (6, 504), (7, 864), (7, 864), (8, 756), (8, 756), (12, 504), (12, 504)])
match_atlas = info == atlas
@printf("  число классов %d ; совпадение с таблицей классов PSU3(3) (ATLAS): %s\n", length(cls), match_atlas)
# простота: ⟨C⟩ нормальна для любого класса C; группа проста ⇔ ⟨C⟩ = G для всех C ≠ {1}
function gen_size(genk, imgs)
    seen = Set{UInt64}([packkey(collect(0:NA-1))]); fr = collect(seen)
    while !isempty(fr)
        nfr = UInt64[]
        for k in fr, g in genk
            nk = packkey(compose(imgs[g], imgs_from_key(k)))
            nk in seen || (push!(seen, nk); push!(nfr, nk))
        end
        fr = nfr
    end
    length(seen)
end
idk = packkey(collect(0:NA-1))
normal_found = Int[]
for c in cls
    idk in c && continue
    sz = gen_size(c[1:min(4, length(c))], imgsU)
    sz < 6048 && length(c) > 4 && (sz = gen_size(c[1:min(12, length(c))], imgsU))
    sz < 6048 && push!(normal_found, sz)
end
simple = isempty(normal_found)
@printf("  собственных нетривиальных нормальных подгрупп: %s ⇒ группа простая: %s\n", isempty(normal_found) ? "нет" : string(normal_found), simple)
put!("F1_classes_simplicity", Pair{String,Any}[
    "class_orders_sizes"=>[[o, s] for (o, s) in info], "n_classes"=>length(cls), "matches_ATLAS_U33"=>match_atlas,
    "simple"=>simple,
    "conclusion"=>"Простая группа порядка 6048 единственна (классификация простых групп малого порядка) — PSU3(3) = G2(2)′. Таблица классов совпадает с ATLAS.",
    "status"=>"[Д] при опоре на классификацию простых групп порядка 6048; вычисление исчерпывающее",
])

# =============================================================================
# F2. Полная группа с антиунитарными элементами
# =============================================================================
println("\n== F2. Полная группа симметрий (унитарные + антиунитарные) ==")
full = unique(vcat(uni, anti))
fset = Set(full)
closedF = all(packkey(compose(imgs_from_key(x), imgs_from_key(y))) in fset for x in full[1:200], y in full[1:200])
imgsF = Dict(k => imgs_from_key(k) for k in full)
center = [k for k in full if all(compose(imgsF[k], imgsF[g]) == compose(imgsF[g], imgsF[k]) for g in full[1:300])]
center_true = [k for k in center if all(compose(imgsF[k], imgsF[g]) == compose(imgsF[g], imgsF[k]) for g in full)]
@printf("  |G| = %d ; замкнута (выборочно 200×200): %s ; центр: %d элемент(ов) ; индекс над PSU3(3): %d\n",
    length(full), closedF, length(center_true), length(full) ÷ length(uni))
put!("F2_full_group", Pair{String,Any}[
    "order"=>length(full), "unitary_part"=>length(uni), "antiunitary_part"=>length(anti), "center_size"=>length(center_true),
    "conclusion"=>"G ⊃ PSU3(3) с индексом 2 и тривиальным центром ⇒ G ≅ Aut(PSU3(3)) = PSU3(3):2 ≅ G2(2) (Out(PSU3(3)) = Z2).",
    "status"=>"[Д] (по F1 и стандартным фактам об Aut(U3(3)))",
])

# =============================================================================
# F3. Октонионы над F2: алгебра Цорна
# =============================================================================
println("\n== F3. Октонионы над F2 (алгебра Цорна) ==")
za(x) = x & 1; zv(x) = (x >> 1) & 7; zw(x) = (x >> 4) & 7; zb(x) = (x >> 7) & 1
zel(a, v, w, b) = a | (v << 1) | (w << 4) | (b << 7)
dot3(v, w) = count_ones(v & w) & 1
function cross3(v, w)
    b(x, i) = (x >> (i - 1)) & 1
    c1 = (b(v, 2) & b(w, 3)) ⊻ (b(v, 3) & b(w, 2))
    c2 = (b(v, 3) & b(w, 1)) ⊻ (b(v, 1) & b(w, 3))
    c3 = (b(v, 1) & b(w, 2)) ⊻ (b(v, 2) & b(w, 1))
    c1 | (c2 << 1) | (c3 << 2)
end
function zmul(x, y)
    a, v, w, b = za(x), zv(x), zw(x), zb(x); a2, v2, w2, b2 = za(y), zv(y), zw(y), zb(y)
    A = (a & a2) ⊻ dot3(v, w2)
    V = (a == 1 ? v2 : 0) ⊻ (b2 == 1 ? v : 0) ⊻ cross3(w, w2)
    W = (a2 == 1 ? w : 0) ⊻ (b == 1 ? w2 : 0) ⊻ cross3(v, v2)
    B = (b & b2) ⊻ dot3(w, v2)
    zel(A, V, W, B)
end
znorm(x) = (za(x) & zb(x)) ⊻ dot3(zv(x), zw(x))
ztr(x) = za(x) ⊻ zb(x)
const ONE = zel(1, 0, 0, 1)
MT = [zmul(x, y) for x in 0:255, y in 0:255]
comp_ok = all(znorm(MT[x+1, y+1]) == (znorm(x) & znorm(y)) for x in 0:255, y in 0:255)
unit_ok = all(MT[ONE+1, x+1] == x && MT[x+1, ONE+1] == x for x in 0:255)
alt_ok = all(MT[MT[x+1, x+1]+1, y+1] == MT[x+1, MT[x+1, y+1]+1] && MT[MT[y+1, x+1]+1, x+1] == MT[y+1, MT[x+1, x+1]+1] for x in 0:255, y in 0:255)
nonassoc = count(MT[MT[x+1, y+1]+1, z+1] != MT[x+1, MT[y+1, z+1]+1] for x in 0:255, y in 0:255, z in 0:255)
# наивная «таблица Фано» над F2: e_0 = 1, e_i e_j = e_{i⊕j}
naive(x, y) = reduce(⊻, [UInt8(1) << (i ⊻ j) for i in 0:7 for j in 0:7 if (x >> i) & 1 == 1 && (y >> j) & 1 == 1]; init=UInt8(0))
NT = [Int(naive(x, y)) for x in 0:255, y in 0:255]
naive_nonassoc = count(NT[NT[x+1, y+1]+1, z+1] != NT[x+1, NT[y+1, z+1]+1] for x in 0:255, y in 0:255, z in 0:255)
@printf("  Цорн: норма композиционна %s ; единица %s ; альтернативна %s ; неассоциативных троек %d из %d\n",
    comp_ok, unit_ok, alt_ok, nonassoc, 256^3)
@printf("  наивная «таблица Фано» e_i e_j = e_{i⊕j} над F2: неассоциативных троек %d ⇒ это групповая алгебра F2[F2^3], не октонионы\n", naive_nonassoc)
put!("F3_zorn", Pair{String,Any}[
    "composition"=>comp_ok, "unit"=>unit_ok, "alternative"=>alt_ok, "nonassociative_triples"=>nonassoc,
    "naive_fano_nonassociative_triples"=>naive_nonassoc,
    "note"=>"Над F2 знаки ±1 совпадают, поэтому модель «7 мнимых единиц ↔ 7 точек Фано» вырождается в ассоциативную коммутативную групповую алгебру. Правильная модель октонионов над F2 — алгебра Цорна на W ⊕ W* (векторное произведение), где GL3(2) действует v ↦ gv, w ↦ g^{-T}w — ровно как в Главе 16.",
    "status"=>"[Д] исчерпывающая проверка",
])

# =============================================================================
# F4. Подъём симметрий Хоггара до автоморфизмов Цорна
# =============================================================================
println("\n== F4. Подъём элементов Sp(6,2) до автоморфизмов алгебры Цорна ==")
# V = T0/F2·1, представители (0, v, w, 0) ↔ индекс Паули a = v | (w << 3)
Bpol_ok = all(((znorm(zel(0, ax(a) ⊻ ax(b), az(a) ⊻ az(b), 0)) ⊻ znorm(zel(0, ax(a), az(a), 0)) ⊻ znorm(zel(0, ax(b), az(b), 0))) == symp(a, b)) for a in 0:NA-1, b in 0:NA-1)
idem = [t for t in 0:255 if MT[t+1, t+1] == t && ztr(t) == 1]
const EIDEM = zel(1, 0, 0, 0)
basis8 = [EIDEM, zel(0, 0, 0, 1), [1 << (k + 1) for k in 0:5]...]   # e, 1−e, (0,ε_k,0)
function lifts(im_)
    cnt = 0
    φb = zeros(Int, 8)                       # образ базисного бита i (элемент 1<<i)
    pairs = [(x, y) for x in basis8 for y in basis8]
    for t in idem, cm in 0:63
        φb[1] = t; φb[8] = ONE ⊻ t
        for k in 0:5
            sv = im_[(1<<k)+1]; c = (cm >> k) & 1
            φb[k+2] = zel(c, ax(sv), az(sv), c)
        end
        ok = true
        for (x, y) in pairs
            lhs = 0; xy = MT[x+1, y+1]
            for i in 0:7; (xy >> i) & 1 == 1 && (lhs ⊻= φb[i+1]); end
            fx = φb[trailing_zeros(x)+1]; fy = φb[trailing_zeros(y)+1]
            if lhs != MT[fx+1, fy+1]
                ok = false; break
            end
        end
        ok && (cnt += 1)
    end
    cnt
end
liftsG = [lifts(imgsF[k]) for k in full]
rng = MersenneTwister(11)
allkeys = collect(keys(group))
outside = UInt64[]
while length(outside) < 2000
    k = allkeys[rand(rng, 1:length(allkeys))]
    k in fset || push!(outside, k)
end
liftsOut = [lifts(imgs_from_key(k)) for k in outside]
@printf("  поляризация нормы на V = ω: %s ; идемпотентов следа 1: %d\n", Bpol_ok, length(idem))
@printf("  элементы полной группы Хоггара (%d): поднимаются все: %s (подъёмов на элемент: %s)\n",
    length(full), all(>(0), liftsG), string(sort(unique(liftsG))))
@printf("  2000 случайных элементов Sp(6,2) вне группы: поднимается %d\n", count(>(0), liftsOut))
put!("F4_lift_to_octonions", Pair{String,Any}[
    "polarization_equals_omega"=>Bpol_ok, "trace1_idempotents"=>length(idem),
    "all_hoggar_symmetries_lift"=>all(>(0), liftsG), "lifts_per_element"=>sort(unique(liftsG)),
    "outside_sample"=>length(outside), "outside_lifting"=>count(>(0), liftsOut),
    "conclusion"=>"Полная группа симметрий Хоггара (для ψ′) совпадает с образом Aut(алгебры Цорна над F2) = G2(2) в Sp(V), V = T0/F2·1 ≅ W ⊕ W* — при отождествлении индексов Паули a = (a_x, a_z) с (v, w).",
    "status"=>"[С] исчерпывающе по группе + выборка 2000 вне её; равенство порядков — по |G2(2)| = 12096",
])

# =============================================================================
# F5. Стандартный фидуциал и CNOT-инвариантность
# =============================================================================
println("\n== F5. CNOT-инвариантные фидуциалы Хоггара: z|0⟩ + Σ_{x≠0}|x⟩ ==")
devz(z) = (ψz = normalize(ComplexF64[z, 1, 1, 1, 1, 1, 1, 1]); maximum(abs.(abs.([real(dot(ψz, P[a+1] * ψz)) for a in 1:NA-1]) .- 1 / 3)))
f5 = Pair{String,Any}[]
for (nm, z) in (("−1+2i", -1 + 2im), ("−1−2i", -1 - 2im), ("−1+i (из поисковой сводки)", -1 + im))
    ψs = normalize(ComplexF64[z, 1, 1, 1, 1, 1, 1, 1])
    issic = devz(z) < 1e-12
    cnot_exact = all(norm(cnot(c, t) * ψs - ψs) < 1e-12 for c in 1:N for t in 1:N if c != t)
    u, an, _ = symmetries(ψs)
    @printf("  %-28s: SIC %s (откл. %.2e) ; каждый CNOT оставляет вектор неизменным: %s ; стабилизатор %d, антиунитарных %d\n",
        nm, issic, devz(z), cnot_exact, issic ? length(u) : -1, issic ? length(an) : -1)
    push!(f5, nm => Pair{String,Any}["sic"=>issic, "deviation"=>devz(z), "cnot_fixed_exactly"=>cnot_exact,
        "unitary_stab"=>issic ? length(u) : -1, "antiunitary"=>issic ? length(an) : -1])
end
# сканирование всех z на сетке: SIC только при z = −1 ± 2i
grid_hits = [(re, im_) for re in -4:0.05:4 for im_ in -4:0.05:4 if devz(re + im_ * im) < 1e-9]
@printf("  сетка z ∈ [−4,4]² шаг 0,05: лучи Хоггара найдены при z = %s\n", string(grid_hits))
# совпадает ли ψ′ из Этапа 3 с этим лучом с точностью до оператора Паули?
ψstd = normalize(ComplexF64[-1 - 2im, 1, 1, 1, 1, 1, 1, 1]); ψstd2 = normalize(ComplexF64[-1 + 2im, 1, 1, 1, 1, 1, 1, 1])
ov = maximum(max(abs(dot(P[b+1] * ψstd, ψp)), abs(dot(P[b+1] * ψstd2, ψp))) for b in 0:NA-1)
@printf("  ψ′ (Этап 3) = P_b · ((−1∓2i)|0⟩ + Σ|x⟩)/√12 для некоторого b: max перекрытие %.12f\n", ov)
put!("F5_cnot_invariant_fiducials", Pair{String,Any}[
    "theorem"=>"Пространство векторов, неподвижных при всех обратимых линейных схемах |x⟩ ↦ |gx⟩ (g ∈ GL3(2)), двумерно: span{|0⟩, Σ_{x≠0}|x⟩} (GL3(2) транзитивна на 7 точках Фано). Для ψ = z|0⟩ + Σ_{x≠0}|x⟩: при a_x = 0, a_z ≠ 0 ⟨P_a⟩ ∝ |z|² − 1; при a_x ≠ 0, a_z = 0 — 2Re z + 6; при a_x·a_z чётном, a_z ≠ 0 — 2Re z − 2; при нечётном — 2|Im z|. Равенство всех модулей значению ‖ψ‖²/3 = (|z|²+7)/3 даёт |z|² = 5, Re z = −1, |Im z| = 2: z = −1 ± 2i. Итак, в пространстве CNOT-инвариантных векторов ровно два луча Хоггара (комплексно сопряжённые «близнецы»).",
    "results"=>f5, "grid_hits"=>[[a, b] for (a, b) in grid_hits], "psi_prime_overlap"=>ov,
    "correction"=>"Вектор (−1±i, 1, …, 1)/3 из поисковой сводки не является SIC в стандартном представлении группы Паули трёх кубитов (|⟨P⟩| ∈ {1/9, 2/9, 4/9}).",
    "status"=>"[Д] (явное вычисление в замкнутом виде) + [С] сканирование",
])

out = joinpath(@__DIR__, "10_СЕРТИФИКАТ_ИДЕНТИФИКАЦИИ_И_ОКТОНИОНОВ.json")
open(out, "w") do f
    write(f, tojson(Pair{String,Any}["script"=>basename(@__FILE__), "date"=>"2026-11-01", "results"=>CERT]))
end
println("\nСертификат: ", out)
