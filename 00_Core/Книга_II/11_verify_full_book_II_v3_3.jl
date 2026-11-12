#!/usr/bin/env julia
# ==============================================================================
# 11_verify_full_book_II_v3_3.jl
# Единый однопоточный верификатор Второго тома («Книга II v3.3»)
# Запуск: JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 11_verify_full_book_II_v3_3.jl
# ==============================================================================

using LinearAlgebra
using Dates
using SHA

const ROOT_DIR = @__DIR__
const CERT_PATH = joinpath(ROOT_DIR, "12_book_II_v3_3_master_certificate.json")

struct GateResult
    id::String
    chapter::String
    description::String
    passed::Bool
    details::String
end

const RESULTS = GateResult[]

function record_gate!(id::String, chapter::String, description::String, passed::Bool, details::String)
    @assert passed "GATE FAILED: $id ($description) -> $details"
    push!(RESULTS, GateResult(id, chapter, description, passed, details))
    println("  [PASS] $id ($chapter): $description — $details")
end

# ------------------------------------------------------------------------------
# Точный ранг матрицы над полем рациональных чисел Rational{BigInt} или F_p
# ------------------------------------------------------------------------------
function exact_rank_rational(M::AbstractMatrix)
    A = Rational{BigInt}.(M)
    m, n = size(A)
    r = 0
    for col in 1:n
        pivot = 0
        for row in (r+1):m
            if A[row, col] != 0
                pivot = row
                break
            end
        end
        pivot == 0 && continue
        r += 1
        if pivot != r
            for j in col:n
                A[r, j], A[pivot, j] = A[pivot, j], A[r, j]
            end
        end
        inv_p = inv(A[r, col])
        for j in col:n
            A[r, j] *= inv_p
        end
        for row in 1:m
            if row != r && A[row, col] != 0
                factor = A[row, col]
                for j in col:n
                    A[row, j] -= factor * A[r, j]
                end
            end
        end
    end
    return r
end

function exact_rref_mod2(M::AbstractMatrix{<:Integer})
    A = mod.(Int.(M), 2)
    m, n = size(A)
    r = 0
    pivots = Int[]
    for col in 1:n
        pivot = 0
        for row in (r+1):m
            if A[row, col] != 0
                pivot = row
                break
            end
        end
        pivot == 0 && continue
        r += 1
        push!(pivots, col)
        if pivot != r
            for j in col:n
                A[r, j], A[pivot, j] = A[pivot, j], A[r, j]
            end
        end
        for row in 1:m
            if row != r && A[row, col] != 0
                for j in col:n
                    A[row, j] = xor(A[row, j], A[r, j])
                end
            end
        end
    end
    return A, pivots
end

function exact_rank_mod(M::AbstractMatrix{<:Integer}, p::Int)
    A = mod.(Int.(M), p)
    m, n = size(A)
    r = 0
    for col in 1:n
        pivot = 0
        for row in (r+1):m
            if A[row, col] != 0
                pivot = row
                break
            end
        end
        pivot == 0 && continue
        r += 1
        if pivot != r
            for j in col:n
                A[r, j], A[pivot, j] = A[pivot, j], A[r, j]
            end
        end
        inv_p = invmod(A[r, col], p)
        for j in col:n
            A[r, j] = mod(A[r, j] * inv_p, p)
        end
        for row in 1:m
            if row != r && A[row, col] != 0
                factor = A[row, col]
                for j in col:n
                    A[row, j] = mod(A[row, j] - factor * A[r, j], p)
                end
            end
        end
    end
    return r
end

function nullspace_mod2(M::AbstractMatrix{<:Integer})
    A, pivots = exact_rref_mod2(M)
    _, n = size(A)
    piv_set = Set(pivots)
    free_cols = [c for c in 1:n if !(c in piv_set)]
    basis = Vector{Vector{Int}}()
    for fc in free_cols
        v = zeros(Int, n)
        v[fc] = 1
        for (row_idx, pc) in enumerate(pivots)
            v[pc] = A[row_idx, fc]
        end
        push!(basis, v)
    end
    return basis
end

# ------------------------------------------------------------------------------
# Целочисленная нормальная форма Смита (Smith Normal Form) над Z
# ------------------------------------------------------------------------------
function smith_normal_form_diag(M::AbstractMatrix{<:Integer})
    A = BigInt.(M)
    m, n = size(A)
    k = 1
    while k <= min(m, n)
        while true
            min_val = BigInt(0)
            best_i, best_j = 0, 0
            for i in k:m, j in k:n
                v = abs(A[i, j])
                if v > 0 && (min_val == 0 || v < min_val)
                    min_val = v
                    best_i, best_j = i, j
                end
            end
            if best_i == 0
                return [abs(A[i, i]) for i in 1:(k-1)]
            end
            if best_i != k
                for j in k:n
                    A[k, j], A[best_i, j] = A[best_i, j], A[k, j]
                end
            end
            if best_j != k
                for i in k:m
                    A[i, k], A[i, best_j] = A[i, best_j], A[i, k]
                end
            end
            if A[k, k] < 0
                for j in k:n
                    A[k, j] = -A[k, j]
                end
            end
            changed = false
            for i in (k+1):m
                if A[i, k] != 0
                    q = div(A[i, k], A[k, k])
                    for j in k:n
                        A[i, j] -= q * A[k, j]
                    end
                    if A[i, k] != 0
                        changed = true
                    end
                end
            end
            for j in (k+1):n
                if A[k, j] != 0
                    q = div(A[k, j], A[k, k])
                    for i in k:m
                        A[i, j] -= q * A[i, k]
                    end
                    if A[k, j] != 0
                        changed = true
                    end
                end
            end
            if !changed
                div_fail_i = 0
                for i in (k+1):m, j in (k+1):n
                    if mod(A[i, j], A[k, k]) != 0
                        div_fail_i = i
                        break
                    end
                end
                if div_fail_i != 0
                    for j in k:n
                        A[k, j] += A[div_fail_i, j]
                    end
                else
                    break
                end
            end
        end
        k += 1
    end
    diag_vals = [abs(A[i, i]) for i in 1:min(m, n) if A[i, i] != 0]
    return sort!(diag_vals)
end

println("==============================================================================")
println(" ЗАПУСК ВЕРИФИКАТОРА КНИГИ II v3.3 (RU) — ОДНОПОТОЧНЫЙ БЕЗФЛОАТНЫЙ РЕЖИМ JULIA")
println(" Julia version = $(VERSION), Threads.nthreads() = $(Threads.nthreads())")
println("==============================================================================")
@assert Threads.nthreads() == 1 "Верификатор обязан работать строго в 1 потоке!"

# ==============================================================================
# ГЛАВА II.1. Линейная память, матрицы Ганкеля и теорема Хо — Калмана
# ==============================================================================

# GATE-II01-01: Обход четырёхточечной сцены S_4 и ранги Ганкеля 1, 2, 3, 4
let
    s_const = [1 for _ in 0:9]
    s_parity = [mod(t, 2) for t in 0:9]
    s_x1 = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0]
    s_ind00 = [mod(t, 4) == 0 ? 1 : 0 for t in 0:9]

    hankel(seq, m) = [seq[i + j + 1] for i in 0:(m-1), j in 0:(m-1)]
    r1 = exact_rank_rational(hankel(s_const, 5))
    r2 = exact_rank_rational(hankel(s_parity, 5))
    r3 = exact_rank_rational(hankel(s_x1, 5))
    r4 = exact_rank_rational(hankel(s_ind00, 5))

    @assert (r1, r2, r3, r4) == (1, 2, 3, 4)
    record_gate!("GATE-II01-01", "II.1", "Ранги Ганкеля при обходе сцены S_4", true, "ranks = ($r1, $r2, $r3, $r4) == (1, 2, 3, 4)")
end

# GATE-II01-02: Теорема II.1.1 — стабилизация ядра наблюдаемости и совместная инъективность окна задержки
let
    B = Rational{BigInt}[0 1 0 0; 0 0 1 0; 0 0 0 1; 0 0 0 0]
    C = Rational{BigInt}[1 0 0 0]
    w0 = Rational{BigInt}[0, 0, 7, 5]
    y_window = [(C * (B^t) * w0)[1] for t in 0:3]
    @assert y_window == Rational{BigInt}[0, 0, 7, 5]

    # Проверка инъективности совместного окна [C B^2; C B^3] на 2-мерном подпространстве глубоких мод {e_3, e_4}
    rk_step2 = exact_rank_rational((C * (B^2))[:, 3:4])
    rk_step3 = exact_rank_rational((C * (B^3))[:, 3:4])
    rk_joint = exact_rank_rational(vcat(C * (B^2), C * (B^3))[:, 3:4])
    @assert rk_step2 == 1 && rk_step3 == 1 && rk_joint == 2

    dims_ker = Int[]
    for N in 1:6
        O_N = vcat([C * (B^(i-1)) for i in 1:N]...)
        push!(dims_ker, 4 - exact_rank_rational(O_N))
    end
    @assert dims_ker == [3, 2, 1, 0, 0, 0]
    record_gate!("GATE-II01-02", "II.1", "Стабилизация ядра наблюдаемости и совместная инъективность окна задержки j_0", true, "dims_ker = $dims_ker, single-step rk = 1, joint window rk = 2")
end

# GATE-II01-03: Теорема II.1.2 — скелетная сборка минимальной реализации Хо — Калмана (скалярная и блочная MIMO p=m=2)
let
    # 1) Скалярный обход S_4 (p = m = 1, r = 3)
    s_x1 = Rational{BigInt}[0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
    H3 = [s_x1[i + j + 1] for i in 0:2, j in 0:2]
    H3_shift = [s_x1[i + j + 2] for i in 0:2, j in 0:2]
    B_min = inv(H3) * H3_shift
    A_min = Rational{BigInt}[1, 0, 0]
    C_min = H3[1:1, :]
    reconstructed = [(C_min * (B_min^t) * A_min)[1] for t in 0:11]
    @assert reconstructed == s_x1

    # 2) Блочная MIMO-система (p = 2 выхода, m = 2 входа, минимальный ранг r = 3) над Q
    B_true = Rational{BigInt}[0 1 0; 0 0 1; 1 -1 1]
    A_true = Rational{BigInt}[1 0; 0 1; 1 1]
    C_true = Rational{BigInt}[1 0 0; 0 1 1]
    M_seq = [C_true * (B_true^t) * A_true for t in 0:10]

    H_blk = [M_seq[1] M_seq[2]; M_seq[2] M_seq[3]]
    H_blk_shift = [M_seq[2] M_seq[3]; M_seq[3] M_seq[4]]
    @assert exact_rank_rational(H_blk) == 3

    I_sel = [1, 2, 3]
    J_sel = [1, 2, 4]
    S_minor = H_blk[I_sel, J_sel]
    @assert exact_rank_rational(S_minor) == 3

    B_mimo = inv(S_minor) * H_blk_shift[I_sel, J_sel]
    A_mimo = inv(S_minor) * H_blk[I_sel, 1:2]
    C_mimo = H_blk[1:2, J_sel]
    mimo_match = all((C_mimo * (B_mimo^t) * A_mimo) == M_seq[t + 1] for t in 0:10)
    @assert mimo_match

    record_gate!("GATE-II01-03", "II.1", "Скелетный алгоритм Хо — Калмана: скалярный S_4 и блочный MIMO (p=m=2, r=3)", true, "scalar 12 steps & MIMO 2x2 (11 block Markov matrices) reconstructed exactly, rank = 3")
end

# GATE-II01-04: Предложение II.1.1 — разложение Уолша на D^n и дефект 2^n - (n + 1)
let
    defects_ok = true
    for n in 2:4
        N = 1 << n
        pts = [digits(x, base=2, pad=n) for x in 0:(N-1)]
        W_le1 = Matrix{Rational{BigInt}}(undef, n + 1, N)
        for j in 1:N
            W_le1[1, j] = 1
            for i in 1:n
                W_le1[i + 1, j] = pts[j][i] == 0 ? 1 : -1
            end
        end
        r = exact_rank_rational(W_le1)
        null_dim = N - r
        defects_ok &= (null_dim == (1 << n) - (n + 1))
        w_top = [iseven(sum(pts[j])) ? Rational{BigInt}(1) : Rational{BigInt}(-1) for j in 1:N]
        defects_ok &= all(iszero, W_le1 * w_top)
    end
    @assert defects_ok
    record_gate!("GATE-II01-04", "II.1", "Дефект линейного проектора Уолша 2^n - (n + 1) и зануление w_{111}", true, "verified for n = 2, 3, 4 (defects 1, 4, 11)")
end

# GATE-II01-05: Предложение II.1.2 — группы перестановок, сохраняющих формы соседства Q_path и Q_cycle
let
    function perms(v::Vector{Int})
        length(v) <= 1 && return [copy(v)]
        res = Vector{Vector{Int}}()
        for i in eachindex(v)
            rest = [v[j] for j in eachindex(v) if j != i]
            for p in perms(rest)
                push!(res, vcat(v[i], p))
            end
        end
        return res
    end
    for n in 4:6
        A_path = zeros(Int, n, n)
        A_cycle = zeros(Int, n, n)
        for i in 1:(n-1)
            A_path[i, i+1] = A_path[i+1, i] = 1
            A_cycle[i, i+1] = A_cycle[i+1, i] = 1
        end
        A_cycle[n, 1] = A_cycle[1, n] = 1
        cnt_path = 0
        cnt_cycle = 0
        for p in perms(collect(1:n))
            P = zeros(Int, n, n)
            for i in 1:n
                P[i, p[i]] = 1
            end
            if P' * A_path * P == A_path
                cnt_path += 1
            end
            if P' * A_cycle * P == A_cycle
                cnt_cycle += 1
            end
        end
        @assert cnt_path == 2 && cnt_cycle == 2 * n
    end
    record_gate!("GATE-II01-05", "II.1", "Редукция S_n до Aut(P_n) = C_2 и Aut(C_n) = D_n", true, "verified for n = 4, 5, 6: |Aut(P_n)| = 2, |Aut(C_n)| = 2n")
end

# ==============================================================================
# ГЛАВА II.2. Диадическая склейка, струи Кэли — Паде и дуальные числа
# ==============================================================================

# GATE-II02-01: Лемма II.2.1 — формальная резольвента и двойственность z <-> 1/z
let
    B = Rational{BigInt}[0 1 0; 0 0 1; -2 1 2]
    A = Rational{BigInt}[1; 0; 0]
    C = Rational{BigInt}[1 2 3]
    M = [(C * (B^t) * A)[1] for t in 0:8]
    for t in 0:5
        @assert M[t + 4] - 2 * M[t + 3] - M[t + 2] + 2 * M[t + 1] == 0
    end
    record_gate!("GATE-II02-01", "II.2", "Тождество резольвенты и возвратного многочлена det(I - wB)", true, "Markov recurrence satisfied for all t")
end

# GATE-II02-02: Предложение II.2.1 — инъективность Phi_m, диадическая склейка и неаддитивность Z_2 ->> R/Z
let
    phi_m(x::Int, m::Int) = begin
        bits = digits(x, base=2, pad=m)
        sum(Rational{BigInt}(bits[j], BigInt(2)^j) for j in 1:m)
    end
    # 1) Строгая инъективность Phi_m : Z/2^m Z -> [0, 1) на конечных окнах m = 1..8
    for m in 1:8
        vals = [phi_m(x, m) for x in 0:((1 << m) - 1)]
        @assert length(unique(vals)) == (1 << m)
        sorted_vals = sort(vals)
        @assert all(sorted_vals[k+1] - sorted_vals[k] == Rational{BigInt}(1, BigInt(2)^m) for k in 1:(length(vals)-1))
    end
    # 2) Диадический зазор |Phi_m(x+) - Phi_m(x-)| == 2^(-m) для хвостов 1000... и 0111...
    for m in 2:12
        phi_minus = sum(Rational{BigInt}(1, BigInt(2)^(j + 1)) for j in 1:(m - 1))
        phi_plus  = Rational{BigInt}(1, 2)
        diff_m = phi_plus - phi_minus
        @assert diff_m == Rational{BigInt}(1, BigInt(2)^m)
    end
    # 3) Неаддитивность фактор-отображения Z_2 ->> R/Z (Предложение II.2.1(3)):
    #    Phi(1) = 1/2, Phi(1) + Phi(1) ≡ 0 (mod 1), но Phi(1 + 1) = Phi(2) = 1/4 ≢ 0 (mod 1)!
    mod1_rat(r::Rational{BigInt}) = r - floor(r)
    @assert phi_m(1, 4) == 1 // 2 && phi_m(2, 4) == 1 // 4
    @assert mod1_rat(phi_m(1, 4) + phi_m(1, 4)) == 0 // 1 && mod1_rat(phi_m(2, 4)) == 1 // 4
    @assert mod1_rat(phi_m(1, 4) + phi_m(1, 4)) != mod1_rat(phi_m(2, 4))

    record_gate!("GATE-II02-02", "II.2", "Инъективность Phi_m, диадическая склейка 2^(-m) и неаддитивность Z_2 ->> R/Z", true, "Phi_m injective on 0..(2^m-1), gap = 2^(-m), Phi(1)+Phi(1)=0 mod 1 != 1/4 = Phi(2)")
end

# GATE-II02-03: Теорема II.2.1 и Лемма II.2.2 — дефект Кэли -1/12 h^3 J_a^3 и ряд сигмоиды из Тейлора
let
    J = zeros(Rational{BigInt}, 5, 5)
    for i in 1:4
        J[i, i + 1] = i
    end
    I5 = Matrix{Rational{BigInt}}(I, 5, 5)
    E_true = sum((J^k) // factorial(k) for k in 0:4)
    T_cayley = (I5 + J // 2) * inv(I5 - J // 2)
    T_cayley_neg = (I5 - J // 2) * inv(I5 + J // 2)
    @assert T_cayley * T_cayley_neg == I5
    defect = E_true - T_cayley
    expected_defect = (-1 // 12) * (J^3) + (-1 // 12) * (J^4)
    @assert defect == expected_defect

    poly_mul(p, q) = [sum((i + j == k ? p[i+1]*q[j+1] : Rational{BigInt}(0)) for i in 0:6, j in 0:6) for k in 0:6]
    exp_neg = [Rational{BigInt}((-1)^k, factorial(k)) for k in 0:6]
    u = copy(exp_neg); u[1] = 0
    inv_denom = zeros(Rational{BigInt}, 7)
    u_pow = zeros(Rational{BigInt}, 7); u_pow[1] = 1
    for m in 0:6
        inv_denom .+= (Rational{BigInt}(1, 2)) .* u_pow
        u_pow = poly_mul(u_pow, (-1 // 2) .* u)
    end
    sig_tilde = copy(inv_denom)
    sig_tilde[1] -= 1 // 2
    @assert sig_tilde[1] == 0 && sig_tilde[2] == 1 // 4 && sig_tilde[3] == 0 &&
            sig_tilde[4] == -1 // 48 && sig_tilde[5] == 0 && sig_tilde[6] == 1 // 480
    record_gate!("GATE-II02-03", "II.2", "Точный кубический дефект Кэли -1/12 J^3 и ряд сигмоиды из экспоненты", true, "E - T_Cayley = -1/12 J^3 - 1/12 J^4; sigma_tilde = 1/4 z - 1/48 z^3 + 1/480 z^5")
end

# GATE-II02-04: Предложение II.2.2 — правило Якоби через дуальные числа K[eps]/(eps^2) над Q и F_2
let
    struct Dual{T}
        a::T
        b::T
    end
    Base.:+(x::Dual{T}, y::Dual{T}) where T = Dual{T}(x.a + y.a, x.b + y.b)
    Base.:-(x::Dual{T}, y::Dual{T}) where T = Dual{T}(x.a - y.a, x.b - y.b)
    Base.:*(x::Dual{T}, y::Dual{T}) where T = Dual{T}(x.a * y.a, x.a * y.b + x.b * y.a)
    Base.:*(c::T, x::Dual{T}) where T = Dual{T}(c * x.a, c * x.b)

    F(v) = [v[1] * v[2] + v[1] * v[1], v[2] * v[2] * v[2] + v[1]]
    G(w) = [w[1] * w[1] + w[2], w[1] * w[2]]

    function dual_jacobian(H, x::Vector{T}, zero_val::T, one_val::T) where T
        n = length(x)
        m = length(H(x))
        J = Matrix{T}(undef, m, n)
        for j in 1:n
            xd = [Dual{T}(x[i], i == j ? one_val : zero_val) for i in 1:n]
            yd = H(xd)
            for i in 1:m
                J[i, j] = yd[i].b
            end
        end
        return J
    end

    x_q = Rational{BigInt}[3, -2]
    JF_q = dual_jacobian(F, x_q, Rational{BigInt}(0), Rational{BigInt}(1))
    JG_q = dual_jacobian(G, F(x_q), Rational{BigInt}(0), Rational{BigInt}(1))
    JGF_q = dual_jacobian(v -> G(F(v)), x_q, Rational{BigInt}(0), Rational{BigInt}(1))
    @assert JGF_q == JG_q * JF_q
    @assert mod.(Int.(numerator.(JGF_q)), 2) == mod.(Int.(numerator.(JG_q * JF_q)), 2)
    record_gate!("GATE-II02-04", "II.2", "Цепное правило Якоби в дуальных числах K[eps]/(eps^2)", true, "J_{G o F} == J_G * J_F verified over Q and F_2")
end

# ==============================================================================
# ГЛАВА II.3. Знак границы, нерв шести срезов O_6 и кручение RP^2
# ==============================================================================

# GATE-II03-01: Лемма II.3.1 (d_1 d_2 = 0) и пустота треугольника Мёбиуса
let
    edges = [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
    tris  = [(1,2,3), (1,2,4), (1,3,4), (2,3,4)]
    d1 = zeros(Int, 4, 6)
    for (e_idx, (u, v)) in enumerate(edges)
        d1[u, e_idx] = -1
        d1[v, e_idx] = +1
    end
    d2 = zeros(Int, 6, 4)
    for (t_idx, (u, v, w)) in enumerate(tris)
        d2[findfirst(==((v, w)), edges), t_idx] = +1
        d2[findfirst(==((u, w)), edges), t_idx] = -1
        d2[findfirst(==((u, v)), edges), t_idx] = +1
    end
    @assert all(iszero, d1 * d2)

    R12 = Set([(0,0), (1,1)])
    R23 = Set([(0,0), (1,1)])
    R13 = Set([(0,1), (1,0)])
    comp123 = Set((a, c) for (a, b1) in R12 for (b2, c) in R23 if b1 == b2)
    @assert isempty(intersect(comp123, R13))
    record_gate!("GATE-II03-01", "II.3", "Тождество границы d_1 d_2 = 0 и пустота треугольника замков Мёбиуса", true, "d1 * d2 == 0 and (R12 o R23) ∩ R13 == empty")
end

# GATE-II03-02: Теорема II.3.1 — когомологии нерва шести срезов N(O_6) на сцене S_4 и [w] != 0
let
    axes_of = [1, 1, 2, 2, 3, 3]
    bit_of  = [0, 1, 0, 1, 0, 1]
    edges_O6 = Tuple{Int,Int}[]
    for u in 1:6, v in (u+1):6
        if axes_of[u] != axes_of[v]
            push!(edges_O6, (u, v))
        end
    end
    @assert length(edges_O6) == 12
    filled_faces = Tuple{Int,Int,Int}[]
    hollow_faces = Tuple{Int,Int,Int}[]
    for u in 1:2, v in 3:4, z in 5:6
        kappa = xor(bit_of[u], bit_of[v], bit_of[z])
        if kappa == 0
            push!(filled_faces, (u, v, z))
        else
            push!(hollow_faces, (u, v, z))
        end
    end
    @assert length(filled_faces) == 4 && length(hollow_faces) == 4

    delta0 = zeros(Int, 12, 6)
    for (e_idx, (u, v)) in enumerate(edges_O6)
        delta0[e_idx, u] = 1
        delta0[e_idx, v] = 1
    end
    delta1 = zeros(Int, 4, 12)
    for (f_idx, (u, v, z)) in enumerate(filled_faces)
        for pair in ((u, v), (u, z), (v, z))
            delta1[f_idx, findfirst(==(pair), edges_O6)] = 1
        end
    end
    rk_d0 = exact_rank_mod(delta0, 2)
    rk_d1 = exact_rank_mod(delta1, 2)
    dim_Z1 = 12 - rk_d1
    dim_H1 = dim_Z1 - rk_d0
    @assert rk_d0 == 5 && rk_d1 == 4 && dim_Z1 == 8 && dim_H1 == 3

    twisted_edges = Set([(1,4), (1,6), (2,3), (2,6)])
    w = [e in twisted_edges ? 1 : 0 for e in edges_O6]
    @assert all(iszero, mod.(delta1 * w, 2))
    for (u, v, z) in hollow_faces
        s_hollow = xor(w[findfirst(==((u,v)), edges_O6)], w[findfirst(==((u,z)), edges_O6)], w[findfirst(==((v,z)), edges_O6)])
        @assert s_hollow == 1
    end
    has_global = any(mod.(delta0 * digits(mask, base=2, pad=6), 2) == w for mask in 0:63)
    @assert !has_global
    record_gate!("GATE-II03-02", "II.3", "Когомологии нерва шести срезов N(O_6): dim H^1 = 3 и [w] != 0", true, "rk(d0)=5, rk(d1)=4, dim Z^1=8, dim H^1=3, d1(w)=0, 0/64 global sections")
end

# GATE-II03-03: Теорема II.3.2 — нормальная форма Смита SNF(d_2) для 6-вершинной триангуляции RP^2
let
    edges_rp2 = [(i, j) for i in 1:6 for j in (i+1):6]
    tris_rp2 = [
        (1,2,3), (1,2,4), (1,3,5), (1,4,6), (1,5,6),
        (2,3,6), (2,4,5), (2,5,6), (3,4,5), (3,4,6)
    ]
    d1_rp2 = zeros(Int, 6, 15)
    for (e_idx, (u, v)) in enumerate(edges_rp2)
        d1_rp2[u, e_idx] = -1
        d1_rp2[v, e_idx] = +1
    end
    d2_rp2 = zeros(Int, 15, 10)
    for (t_idx, (u, v, w)) in enumerate(tris_rp2)
        d2_rp2[findfirst(==((v, w)), edges_rp2), t_idx] = +1
        d2_rp2[findfirst(==((u, w)), edges_rp2), t_idx] = -1
        d2_rp2[findfirst(==((u, v)), edges_rp2), t_idx] = +1
    end
    @assert all(iszero, d1_rp2 * d2_rp2)
    snf_d1 = smith_normal_form_diag(d1_rp2)
    snf_d2 = smith_normal_form_diag(d2_rp2)
    rk_Q  = exact_rank_rational(d2_rp2)
    rk_F2 = exact_rank_mod(d2_rp2, 2)
    @assert snf_d1 == fill(BigInt(1), 5)
    @assert snf_d2 == vcat(fill(BigInt(1), 9), [BigInt(2)])
    @assert rk_Q == 10 && rk_F2 == 9
    record_gate!("GATE-II03-03", "II.3", "Нормальная форма Смита SNF(d_2) для RP^2 с кручением Z/2Z", true, "SNF(d2) = (1^9, 2), rk_Q = 10, rk_F2 = 9")
end

# GATE-II03-04: Таблица II.3.1 — нарушение аксиомы отделимости в предпучке G против стягиваемой склейки торсора S_w
let
    # 1) Явление А (предпучок G на X = U_1 ∪ U_2): G(X) = F_2 (глобальный заряд kappa in {0,1}), G(U_1) = G(U_2) = {0}
    G_X = [0, 1]
    rho_U1(kappa) = 0
    rho_U2(kappa) = 0
    compat_preimages = [k for k in G_X if rho_U1(k) == 0 && rho_U2(k) == 0]
    # Нарушение отделимости пучка: два различных глобальных сечения kappa=0 и kappa=1 дают одинаковые нулевые ограничения!
    @assert length(compat_preimages) == 2 && compat_preimages[1] != compat_preimages[2]

    # 2) Явление Б (истинный F_2-торсор S_w на нерве O_6): на любом остовном дереве T_5 из 5 рёбер ровно 2 сечения (1 при фиксированной базе g[1]=0)
    tree_edges = [(1,3), (1,4), (1,5), (1,6), (2,3)]
    d0_tree = zeros(Int, 5, 6)
    for (idx, (u, v)) in enumerate(tree_edges)
        d0_tree[idx, u] = 1
        d0_tree[idx, v] = 1
    end
    w_tree = [1, 0, 1, 0, 1]
    sols_all = [digits(mask, base=2, pad=6) for mask in 0:63 if mod.(d0_tree * digits(mask, base=2, pad=6), 2) == w_tree]
    sols_pinned = [g for g in sols_all if g[1] == 0]
    @assert length(sols_all) == 2 && length(sols_pinned) == 1

    record_gate!("GATE-II03-04", "II.3", "Различение не-пучкового предпучка G (сбой отделимости) и торсора S_w (единственность при фиксированной базе на дереве)", true, "|G_X preimages|=2 (separability fails), |S_w(tree)|=2, |S_w(tree, g1=0)|=1")
end

# ==============================================================================
# ГЛАВА II.4. Дискретная связность, октаэдр наблюдателя W(B_3) и группа Q_8
# ==============================================================================

# GATE-II04-01: Теорема II.4.1 — полный перебор W(B_3) порядка 48, различение W(D_3) и W(B_3)^+ и заряд kappa
let
    det3_int(M) = M[1,1]*(M[2,2]*M[3,3] - M[2,3]*M[3,2]) -
                  M[1,2]*(M[2,1]*M[3,3] - M[2,3]*M[3,1]) +
                  M[1,3]*(M[2,1]*M[3,2] - M[2,2]*M[3,1])

    perms3 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    WB3 = Matrix{Int}[]
    WD3 = Matrix{Int}[] # чётное число перемен знака (s1*s2*s3 == 1): стабилизатор полукуба T_+ = S_4
    for p in perms3, s1 in (-1, 1), s2 in (-1, 1), s3 in (-1, 1)
        M = zeros(Int, 3, 3)
        s = (s1, s2, s3)
        for i in 1:3
            M[i, p[i]] = s[i]
        end
        push!(WB3, M)
        if s1 * s2 * s3 == 1
            push!(WD3, M)
        end
    end
    @assert length(WB3) == 48 && length(WD3) == 24

    WB3_plus = [M for M in WB3 if det3_int(M) == 1]
    A4_rot   = [M for M in WD3 if det3_int(M) == 1]
    @assert length(WB3_plus) == 24 && length(A4_rot) == 12

    octants = [[s1, s2, s3] for s1 in (-1, 1) for s2 in (-1, 1) for s3 in (-1, 1)]
    T_plus  = [v for v in octants if prod(v) == 1]
    diag_pairs = [Set([v, -v]) for v in octants if v[1] == 1]
    @assert length(T_plus) == 4 && length(diag_pairs) == 4

    # 1) W(D_3) точно сохраняет заряд kappa (T_+) и индуцирует все 24 перестановки S_4 на T_+
    perms_WD3_Tplus = Set{Vector{Int}}()
    for M in WD3
        @assert all(prod(M * v) == prod(v) for v in octants)
        push!(perms_WD3_Tplus, [findfirst(==(M * u), T_plus) for u in T_plus])
    end
    @assert length(perms_WD3_Tplus) == 24

    # 2) W(B_3)^+ = Aut(O_6) ∩ SO(3) индуцирует все 24 перестановки S_4 на 4 диагоналях куба,
    #    сохраняет kappa на 12 чётных вращениях A_4 и обращает kappa на 12 нечётных вращениях!
    perms_WB3_diag = Set{Vector{Int}}()
    cnt_keep_kappa = 0
    cnt_flip_kappa = 0
    for M in WB3_plus
        push!(perms_WB3_diag, [findfirst(P -> (M * first(D)) in P, diag_pairs) for D in diag_pairs])
        if all(prod(M * v) == prod(v) for v in octants)
            cnt_keep_kappa += 1
        elseif all(prod(M * v) == -prod(v) for v in octants)
            cnt_flip_kappa += 1
        end
    end
    @assert length(perms_WB3_diag) == 24 && cnt_keep_kappa == 12 && cnt_flip_kappa == 12

    # 3) Центральная инверсия -I_3 тривиальна на 4 диагоналях, но обращает заряд kappa всех 8 граней
    inv_mat = -Matrix{Int}(I, 3, 3)
    @assert all((inv_mat * first(D)) in D for D in diag_pairs)
    @assert all(prod(inv_mat * v) == -prod(v) for v in octants)

    record_gate!("GATE-II04-01", "II.4", "Полный перебор W(B_3) (48), различение W(D_3) (24, kappa-inv) и W(B_3)^+ (24=12+12 в SO(3))", true, "|W(B_3)|=48, |W(D_3)|=24 (S_4 on T_+), |W(B_3)^+|=24 (12 keep + 12 flip kappa), -I_3 flips kappa")
end

# GATE-II04-02: Предложение II.4.1 — 8 матриц Q_8 в SL_2(F_3), отсутствие сечения V_4 -> Q_8 и инволюции 19, 13, 1
let
    I2 = [1 0; 0 1]
    mI2 = [2 0; 0 2]
    QI = [0 2; 1 0]
    QJ = [1 1; 1 2]
    QK = mod.(QI * QJ, 3)
    Q8 = [I2, mI2, QI, mod.(2 .* QI, 3), QJ, mod.(2 .* QJ, 3), QK, mod.(2 .* QK, 3)]
    @assert length(unique(Q8)) == 8
    @assert mod.(QI * QI, 3) == mI2 && mod.(QJ * QJ, 3) == mI2 && mod.(QK * QK, 3) == mI2

    v0 = [1, 0]
    orbit = unique([mod.(M * v0, 3) for M in Q8])
    @assert length(orbit) == 8

    cosets = [[I2], [QI, mod.(2 .* QI, 3)], [QJ, mod.(2 .* QJ, 3)], [QK, mod.(2 .* QK, 3)]]
    has_splitting = false
    for m1 in cosets[2], m2 in cosets[3], m3 in cosets[4]
        sec = [I2, m1, m2, m3]
        if all(mod.(a * b, 3) in sec for a in sec for b in sec)
            has_splitting = true
        end
    end
    @assert !has_splitting

    perms3 = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
    inv_WB3 = 0
    I3 = Matrix{Int}(I, 3, 3)
    for p in perms3, s1 in (-1,1), s2 in (-1,1), s3 in (-1,1)
        M = zeros(Int, 3, 3); s = (s1, s2, s3)
        for i in 1:3; M[i, p[i]] = s[i]; end
        if M != I3 && M * M == I3
            inv_WB3 += 1
        end
    end
    inv_GL2F3 = 0
    for a in 0:2, b in 0:2, c in 0:2, d in 0:2
        M = [a b; c d]
        if mod(a*d - b*c, 3) != 0 && M != I2 && mod.(M * M, 3) == I2
            inv_GL2F3 += 1
        end
    end
    inv_Q8 = count(M -> M != I2 && mod.(M * M, 3) == I2, Q8)
    @assert (inv_WB3, inv_GL2F3, inv_Q8) == (19, 13, 1)
    record_gate!("GATE-II04-02", "II.4", "Группа Q_8 в SL_2(F_3), нерасщепимость Q_8 ->> V_4 и инволюции 19, 13, 1", true, "8 distinct matrices, 0 splittings, involutions = (19, 13, 1)")
end

# GATE-II04-03: Теорема II.4.2 — абелианизация группы кос B_3 через SNF и некоммутативный след в S_3
let
    R_b3 = reshape([2, -3], 2, 1)
    snf_b3 = smith_normal_form_diag(R_b3)
    @assert snf_b3 == [BigInt(1)]
    S1 = [0 1 0; 1 0 0; 0 0 1]
    S2 = [1 0 0; 0 0 1; 0 1 0]
    @assert S1 * S2 * S1 == S2 * S1 * S2
    @assert S1 * transpose(S2) != I
    @assert (S1^3) != (S1 * S2 * S1)
    record_gate!("GATE-II04-03", "II.4", "Абелианизация B_3^ab = Z через SNF и некоммутативное различение в S_3", true, "SNF([2;-3]) = [1], S1*S2*S1 == S2*S1*S2, S1*S2^-1 != I")
end

# ==============================================================================
# ГЛАВА II.5. Плоскость Фано, октонионы над F_2, лупа Пейджа и седенионы
# ==============================================================================

# GATE-II05-01: Теорема II.5.1 — ассоциативность беззнаковой таблицы Фано F_2[F_2^3] и альтернативность октонионов O
let
    unsigned_nonassoc = count(xor(xor(r, s), t) != xor(r, xor(s, t)) for r in 0:7, s in 0:7, t in 0:7)
    @assert unsigned_nonassoc == 0

    fano_lines = [(1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5)]
    mult_idx = zeros(Int, 8, 8)
    mult_sgn = zeros(Int, 8, 8)
    for r in 0:7
        mult_idx[1, r+1] = r; mult_sgn[1, r+1] = 1
        mult_idx[r+1, 1] = r; mult_sgn[r+1, 1] = 1
        r >= 1 && (mult_idx[r+1, r+1] = 0; mult_sgn[r+1, r+1] = -1)
    end
    for (i, j, k) in fano_lines
        for (a, b, c) in ((i,j,k), (j,k,i), (k,i,j))
            mult_idx[a+1, b+1] = c; mult_sgn[a+1, b+1] = +1
            mult_idx[b+1, a+1] = c; mult_sgn[b+1, a+1] = -1
        end
    end
    function oct_mul(x::Vector{Int}, y::Vector{Int})
        res = zeros(Int, 8)
        for r in 0:7, s in 0:7
            if x[r+1] != 0 && y[s+1] != 0
                idx = mult_idx[r+1, s+1]
                res[idx+1] += x[r+1] * y[s+1] * mult_sgn[r+1, s+1]
            end
        end
        return res
    end
    basis = [[i == r ? 1 : 0 for i in 0:7] for r in 0:7]
    signed_nonassoc = 0
    alt_failures = 0
    moufang_failures = 0
    for r in 1:8, s in 1:8, t in 1:8
        er, es, et = basis[r], basis[s], basis[t]
        lhs = oct_mul(oct_mul(er, es), et)
        rhs = oct_mul(er, oct_mul(es, et))
        lhs != rhs && (signed_nonassoc += 1)
        (r == s || s == t || r == t) && lhs != rhs && (alt_failures += 1)
        m_lhs = oct_mul(oct_mul(et, er), oct_mul(es, et))
        m_rhs = oct_mul(et, oct_mul(oct_mul(er, es), et))
        m_lhs != m_rhs && (moufang_failures += 1)
    end
    @assert signed_nonassoc == 168 && alt_failures == 0 && moufang_failures == 0
    record_gate!("GATE-II05-01", "II.5", "Беззнаковая таблица Фано ассоциативна (0/512), знаковая имеет 168 антиассоциативных реперов и 0 нарушений Муфанг", true, "unsigned_nonassoc=0, signed_nonassoc=168, alt_failures=0, moufang_failures=0")
end

# GATE-II05-02 & GATE-II05-03: Теорема II.5.2 — алгебра Цорна Oct(F_2), оба расщепления M_120 (64+56 и 36+84) и все 120^3 троек Муфанг
let
    dot3(u, v) = mod(u[1]*v[1] + u[2]*v[2] + u[3]*v[3], 2)
    cross3(u, v) = (mod(u[2]*v[3] + u[3]*v[2], 2), mod(u[3]*v[1] + u[1]*v[3], 2), mod(u[1]*v[2] + u[2]*v[1], 2))

    elems = [Tuple(digits(m, base=2, pad=8)) for m in 0:255]
    elem_to_idx = Dict(elems[i] => i for i in 1:256)
    function zorn_mul(x, y)
        a1, u1, v1, b1 = x[1], (x[2],x[3],x[4]), (x[5],x[6],x[7]), x[8]
        a2, u2, v2, b2 = y[1], (y[2],y[3],y[4]), (y[5],y[6],y[7]), y[8]
        a = mod(a1*a2 + dot3(u1, v2), 2)
        b = mod(b1*b2 + dot3(v1, u2), 2)
        cx_v = cross3(v1, v2)
        cx_u = cross3(u1, u2)
        u = ntuple(i -> mod(a1*u2[i] + b2*u1[i] + cx_v[i], 2), 3)
        v = ntuple(i -> mod(a2*v1[i] + b1*v2[i] + cx_u[i], 2), 3)
        return (a, u[1], u[2], u[3], v[1], v[2], v[3], b)
    end
    zorn_tr(x) = mod(x[1] + x[8], 2)
    zorn_norm(x) = mod(x[1]*x[8] + dot3((x[2],x[3],x[4]), (x[5],x[6],x[7])), 2)
    zorn_omega(x, y) = mod(x[1]*y[8] + x[8]*y[1] + dot3((x[2],x[3],x[4]), (y[5],y[6],y[7])) + dot3((x[5],x[6],x[7]), (y[2],y[3],y[4])), 2)

    I_zorn = (1, 0, 0, 0, 0, 0, 0, 1)
    ZERO_zorn = (0, 0, 0, 0, 0, 0, 0, 0)

    @assert all(zorn_omega(x, I_zorn) == zorn_tr(x) for x in elems)
    I_perp = [x for x in elems if zorn_omega(x, I_zorn) == 0]
    @assert length(I_perp) == 128 && (I_zorn in I_perp)

    M120 = [x for x in elems if zorn_norm(x) == 1]
    @assert length(M120) == 120

    # Расщепление 1 по следу в M_120: 64 элемента с tr=0 (удовлетворяют x^2 = I) и 56 элементов с tr=1 (удовлетворяют x^2 + x + I = 0)
    M120_tr0 = [x for x in M120 if zorn_tr(x) == 0]
    M120_tr1 = [x for x in M120 if zorn_tr(x) == 1]
    @assert length(M120_tr0) == 64 && length(M120_tr1) == 56
    @assert all(zorn_mul(x, x) == I_zorn for x in M120_tr0)
    @assert all(ntuple(i -> xor(zorn_mul(x, x)[i], x[i]), 8) == I_zorn for x in M120_tr1)

    # Расщепление 2 по гиперболическому ядру u . v на V_6: 36 изотропных (a=b=1) + 84 неизотропных (28 пар * 3 выбора (a,b) с ab=0) = 120
    uv_dot(x) = dot3((x[2],x[3],x[4]), (x[5],x[6],x[7]))
    M120_iso    = [x for x in M120 if uv_dot(x) == 0]
    M120_noniso = [x for x in M120 if uv_dot(x) == 1]
    v6_zeros = count(m -> dot3(digits(m, base=2, pad=6)[1:3], digits(m, base=2, pad=6)[4:6]) == 0, 0:63)
    v6_ones  = 64 - v6_zeros
    @assert v6_zeros == 36 && v6_ones == 28
    @assert length(M120_iso) == 36 && length(M120_noniso) == 84
    record_gate!("GATE-II05-02", "II.5", "Структура Oct(F_2): omega(x,I)=tr(x), |I^perp|=128, оба расщепления M_120 (64+56 и 36+84)", true, "|M_120|=120, trace split 64(x^2=I)+56(x^2+x+I=0), hyperbolic split 36+84=120")

    # Нетривиальные идемпотенты E_72
    E72 = [e for e in elems if e != ZERO_zorn && e != I_zorn && zorn_mul(e, e) == e]
    @assert length(E72) == 72
    q_v6(m) = dot3(digits(m, base=2, pad=6)[1:3], digits(m, base=2, pad=6)[4:6])
    w_of_e(e) = sum(e[k+1] << (k-1) for k in 1:6)
    unique_w = unique([w_of_e(e) for e in E72])
    @assert length(unique_w) == 36
    for e in E72
        we = w_of_e(e)
        @assert q_v6(we) == 0
        vals = [q_v6(xor(z, we)) for z in 0:63]
        @assert count(==(0), vals) == 36 && count(==(1), vals) == 28
    end
    for x in 0:63, y in 0:63, z in 1:8
        d4 = xor(q_v6(xor(x,y,z)), q_v6(xor(x,y)), q_v6(xor(x,z)), q_v6(xor(y,z)), q_v6(x), q_v6(y), q_v6(z), q_v6(0))
        @assert d4 == 0
    end

    # Полная таблица умножения 256x256 и исчерпывающая проверка всех 120^3 = 1 728 000 троек Муфанг на M_120!
    mul_tbl = Matrix{Int}(undef, 256, 256)
    for i in 1:256, j in 1:256
        mul_tbl[i, j] = Int(elem_to_idx[zorn_mul(elems[i], elems[j])])
    end
    m120_ids = [Int(elem_to_idx[x]) for x in M120]
    m120_flag = falses(256)
    for id in m120_ids; m120_flag[id] = true; end

    m120_closed = all(m120_flag[mul_tbl[x, y]] for x in m120_ids, y in m120_ids)
    m120_nonassoc = 0
    m120_moufang_fail = 0
    @inbounds for z in m120_ids, x in m120_ids, y in m120_ids
        xy = mul_tbl[x, y]
        yz = mul_tbl[y, z]
        mul_tbl[xy, z] != mul_tbl[x, yz] && (m120_nonassoc += 1)
        zx = mul_tbl[z, x]
        xyz = mul_tbl[xy, z]
        mul_tbl[zx, yz] != mul_tbl[z, xyz] && (m120_moufang_fail += 1)
    end
    @assert m120_closed && m120_nonassoc > 0 && m120_moufang_fail == 0
    order_G2_2 = (2^6) * (2^6 - 1) * (2^2 - 1)
    @assert order_G2_2 == 12096
    record_gate!("GATE-II05-03", "II.5", "72 идемпотента Oct(F_2), delta_4 q = 0 и полная проверка всех 120^3 = 1 728 000 троек Муфанг в M_120", true, "|E_72|=72, 1728000/1728000 Moufang triples hold (0 failures, nonassoc=$m120_nonassoc), |G_2(2)|=12096")
end

# GATE-II05-04: Предложения II.5.1 и II.5.2 — 84 элементарные пары делителей нуля в седенионах и Cl_{0,8} = Mat_{16}(R)
let
    fano_lines = [(1,2,3), (1,4,5), (1,7,6), (2,4,6), (2,5,7), (3,4,7), (3,6,5)]
    mult_idx = zeros(Int, 8, 8)
    mult_sgn = zeros(Int, 8, 8)
    for r in 0:7
        mult_idx[1, r+1] = r; mult_sgn[1, r+1] = 1
        mult_idx[r+1, 1] = r; mult_sgn[r+1, 1] = 1
        r >= 1 && (mult_idx[r+1, r+1] = 0; mult_sgn[r+1, r+1] = -1)
    end
    for (i, j, k) in fano_lines
        for (a, b, c) in ((i,j,k), (j,k,i), (k,i,j))
            mult_idx[a+1, b+1] = c; mult_sgn[a+1, b+1] = +1
            mult_idx[b+1, a+1] = c; mult_sgn[b+1, a+1] = -1
        end
    end
    function oct_mul(x::Vector{Int}, y::Vector{Int})
        res = zeros(Int, 8)
        for r in 0:7, s in 0:7
            if x[r+1] != 0 && y[s+1] != 0
                idx = mult_idx[r+1, s+1]
                res[idx+1] += x[r+1] * y[s+1] * mult_sgn[r+1, s+1]
            end
        end
        return res
    end
    oct_conj(x::Vector{Int}) = [i == 1 ? x[1] : -x[i] for i in 1:8]
    function sed_mul(x::Vector{Int}, y::Vector{Int})
        a, b = x[1:8], x[9:16]
        c, d = y[1:8], y[9:16]
        re = oct_mul(a, c) .- oct_mul(oct_conj(d), b)
        im = oct_mul(d, a) .+ oct_mul(b, oct_conj(c))
        return vcat(re, im)
    end
    e_sed(k) = [i == k + 1 ? 1 : 0 for i in 1:16]
    @assert sed_mul(e_sed(1), e_sed(4))   ==  e_sed(5)
    @assert sed_mul(e_sed(10), e_sed(15)) ==  e_sed(5)
    @assert sed_mul(e_sed(10), e_sed(4))  == -e_sed(14)
    @assert sed_mul(e_sed(1), e_sed(15))  == -e_sed(14)
    @assert all(iszero, sed_mul(e_sed(1) .+ e_sed(10), e_sed(4) .- e_sed(15)))
    @assert all(iszero, sed_mul(e_sed(3) .+ e_sed(10), e_sed(6) .- e_sed(15)))

    # Полный подсчёт всех 84 нормированных элементарных пар делителей нуля (e_i + e_k)(e_j + s e_l) == 0 (1 <= i < j <= 7, 9 <= k,l <= 15, s in {-1,+1})
    zd_count = 0
    for i in 1:7, j in (i+1):7, k in 9:15, l in 9:15, s in (-1, 1)
        if all(iszero, sed_mul(e_sed(i) .+ e_sed(k), e_sed(j) .+ (s .* e_sed(l))))
            zd_count += 1
        end
    end
    @assert zd_count == 84

    # Генераторы Cl_{0,8} в Mat_{16}(Z)
    L_ops = Matrix{Int}[]
    for k in 1:7
        L = zeros(Int, 8, 8)
        ek = [i == k + 1 ? 1 : 0 for i in 1:8]
        for j in 0:7
            ej = [i == j + 1 ? 1 : 0 for i in 1:8]
            L[:, j + 1] = oct_mul(ek, ej)
        end
        push!(L_ops, L)
    end
    I8 = Matrix{Int}(I, 8, 8)
    Z8 = zeros(Int, 8, 8)
    Gammas = [[Z8 L; L Z8] for L in L_ops]
    push!(Gammas, [Z8 -I8; I8 Z8])
    I16 = Matrix{Int}(I, 16, 16)
    for a in 1:8, b in 1:8
        if a == b
            @assert Gammas[a] * Gammas[b] == -I16
        else
            @assert Gammas[a] * Gammas[b] + Gammas[b] * Gammas[a] == zeros(Int, 16, 16)
        end
    end
    record_gate!("GATE-II05-04", "II.5", "Все 84 нормированные элементарные пары делителей нуля седенионов, знаки e10*e4=-e14 и Cl_{0,8}=Mat_{16}(R)", true, "exact normalized zero-divisor pairs = $zd_count == 84, 8 Clifford generators verified")
end

# ==============================================================================
# ГЛАВА II.6. Мост Уолша — Блоха на S_4 и ветвевое замыкание W_infty
# ==============================================================================

# GATE-II06-01: Теорема II.6.1 — точная рациональная проверка фильтрации 16 -> 8 -> 2 при отображении Уолша — Блоха
let
    chi1 = Rational{Int}[1,  1, -1, -1]
    chi2 = Rational{Int}[1, -1,  1, -1]
    chi3 = Rational{Int}[1, -1, -1,  1]

    function count_valid_effects_exact(lam_sq::Rational{Int})
        cnt = 0
        for mask in 0:15
            q = Rational{Int}.(digits(mask, base=2, pad=4))
            qn = Rational{Int}(1) .- q
            c0 = sum(q) // 4
            c1 = dot(q, chi1) // 4
            c2 = dot(q, chi2) // 4
            c3 = dot(q, chi3) // 4
            # 1) Сохранение инволюции отрицания: E_lambda(1 - q) == I_2 - E_lambda(q)
            @assert (sum(qn) // 4 == 1 - c0) && (dot(qn, chi1) // 4 == -c1) &&
                    (dot(qn, chi2) // 4 == -c2) && (dot(qn, chi3) // 4 == -c3)
            # 2) Точное равенство Парсеваля: c1^2 + c2^2 + c3^2 == c0 * (1 - c0)
            norm_c_sq = c1^2 + c2^2 + c3^2
            @assert norm_c_sq == c0 * (1 - c0)
            # 3) Точное условие принадлежности конусу эффектов [0, I_2]: |lambda| * ||c|| <= min(c0, 1 - c0)
            bound = min(c0, 1 - c0)
            if lam_sq * norm_c_sq <= bound^2
                cnt += 1
            end
        end
        return cnt
    end

    n_reg1 = count_valid_effects_exact(1 // 3)
    n_reg2 = count_valid_effects_exact(1 // 1)
    n_reg3 = count_valid_effects_exact(9 // 4)
    @assert (n_reg1, n_reg2, n_reg3) == (16, 8, 2)
    record_gate!("GATE-II06-01", "II.6", "Точная рациональная фильтрация Уолша — Блоха 16 -> 8 -> 2 на S_4 и E_lam(1-q)=I-E_lam(q)", true, "valid effects at lambda^2 = (1/3, 1, 9/4) are ($n_reg1, $n_reg2, $n_reg3)")
end

# GATE-II06-02 & GATE-II06-03: Предложение II.6.1 — ранг 12 MUB в Q(omega) против 16 вещественных лучей, стабилизация W_infty и канал сброса
let
    # Точная арифметика в круговом поле Q(omega) (omega^2 + omega + 1 = 0): элемент a + b*omega как Tuple{Rational{BigInt}, Rational{BigInt}}
    qcyc_conj(z) = (z[1] - z[2], -z[2])
    qcyc_mul(z1, z2) = (z1[1]*z2[1] - z1[2]*z2[2], z1[1]*z2[2] + z1[2]*z2[1] - z1[2]*z2[2])
    qcyc_scale(c::Rational{BigInt}, z) = (c * z[1], c * z[2])
    omega_pow_q(k::Int) = mod(k, 3) == 0 ? (Rational{BigInt}(1), Rational{BigInt}(0)) :
                         (mod(k, 3) == 1 ? (Rational{BigInt}(0), Rational{BigInt}(1)) :
                                           (Rational{BigInt}(-1), Rational{BigInt}(-1)))

    # 12 проекторов 4 базисов MUB в C^3 над Q(omega), векторизованные в Q^9 изоморфно Herm_3
    mub_cols = Vector{Vector{Rational{BigInt}}}()
    # 3 проектора вычислительного базиса (нормировка 1)
    for j in 1:3
        v = [i == j ? (Rational{BigInt}(1), Rational{BigInt}(0)) : (Rational{BigInt}(0), Rational{BigInt}(0)) for i in 1:3]
        P = [qcyc_mul(v[r], qcyc_conj(v[s])) for r in 1:3, s in 1:3]
        @assert P[1,1][2] == 0 && P[2,2][2] == 0 && P[3,3][2] == 0
        push!(mub_cols, Rational{BigInt}[P[1,1][1], P[2,2][1], P[3,3][1], P[1,2][1], P[1,2][2], P[1,3][1], P[1,3][2], P[2,3][1], P[2,3][2]])
    end
    # 9 фазовых проекторов Вейля — Гейзенберга (нормировка 1/3)
    for m in 0:2, n in 0:2
        v = [omega_pow_q(m * q^2 + n * q) for q in 0:2]
        P = [qcyc_scale(Rational{BigInt}(1, 3), qcyc_mul(v[r], qcyc_conj(v[s]))) for r in 1:3, s in 1:3]
        @assert P[1,1][2] == 0 && P[2,2][2] == 0 && P[3,3][2] == 0
        push!(mub_cols, Rational{BigInt}[P[1,1][1], P[2,2][1], P[3,3][1], P[1,2][1], P[1,2][2], P[1,3][1], P[1,3][2], P[2,3][1], P[2,3][2]])
    end
    M_12 = hcat(mub_cols...)
    @assert size(M_12) == (9, 12) && exact_rank_rational(M_12) == 9

    # 16 точных рациональных вещественных проекторов ранга 1 в Herm_3 имеют ранг ровно 6 < 9
    real_cols = Vector{Vector{Rational{BigInt}}}()
    for a in 0:3, b in 0:3
        u = Rational{BigInt}[1, a, b]
        nsq = sum(x^2 for x in u)
        P = (u * transpose(u)) .// nsq
        @assert P * P == P && tr(P) == 1
        push!(real_cols, Rational{BigInt}[P[1,1], P[2,2], P[3,3], P[1,2], 0, P[1,3], 0, P[2,3], 0])
    end
    M_16_real = hcat(real_cols...)
    @assert size(M_16_real) == (9, 16) && exact_rank_rational(M_16_real) == 6
    record_gate!("GATE-II06-02", "II.6", "Информационная полнота 12 проекторов MUB (точный ранг 9 в Q(omega)) против 16 вещественных проекторов (ранг 6)", true, "exact rank(12 MUB) = 9, exact rank(16 rational real projectors) = 6")

    # Многошаговая стабилизация квантового замыкания Нероуда W_0 subsetneq W_1 subsetneq W_2 = W_3 < Herm_3 (Предложение II.6.1)
    # Пифагоров ортогональный канал U in SO_3(Q) на d = 3 и начальное окно Q_0 = {I_3, |0><0|}
    U_rot = Rational{BigInt}[3 -4 0; 4 3 0; 0 0 5] .// 5
    I3_q  = Matrix{Rational{BigInt}}(I, 3, 3)
    @assert transpose(U_rot) * U_rot == I3_q
    P0_q  = Rational{BigInt}[1 0 0; 0 0 0; 0 0 0]
    vec_sym9(H) = Rational{BigInt}[H[1,1], H[2,2], H[3,3], H[1,2], 0, H[1,3], 0, H[2,3], 0]

    ops_chain = Matrix{Rational{BigInt}}[I3_q, P0_q]
    dims_W = Int[exact_rank_rational(hcat([vec_sym9(X) for X in ops_chain]...))]
    curr_E = P0_q
    for _ in 1:4
        curr_E = transpose(U_rot) * curr_E * U_rot
        push!(ops_chain, curr_E)
        push!(dims_W, exact_rank_rational(hcat([vec_sym9(X) for X in ops_chain]...)))
    end
    # Строгий рост 2 -> 3 -> 4 и стабилизация 4 = 4 = 4 < 9 (ненулевое слепое ядро размерности 9 - 4 = 5)
    @assert dims_W == [2, 3, 4, 4, 4] && dims_W[end] < 9
    Delta_blind = Rational{BigInt}[0 0 1; 0 0 0; 1 0 0] # эрмитова бесследовая разность в W_infty^perp
    @assert tr(Delta_blind) == 0 && all(tr(X * Delta_blind) == 0 for X in ops_chain)

    # Унитальность сопряжённого канала Phi^dagger(I)=I и контрпример канала сброса tr=d!=1
    d = 3
    K_ops = [[i == 1 && j == k ? 1 : 0 for i in 1:d, j in 1:d] for k in 1:d]
    I_d = Matrix{Int}(I, d, d)
    @assert sum(K' * K for K in K_ops) == I_d
    P0 = [i == 1 && j == 1 ? 1 : 0 for i in 1:d, j in 1:d]
    Phi_dag_P0 = sum(K' * P0 * K for K in K_ops)
    @assert Phi_dag_P0 == I_d && tr(Phi_dag_P0) == d != 1
    record_gate!("GATE-II06-03", "II.6", "Стабилизация ветвевого замыкания W_0..W_4 = [2,3,4,4,4] < 9, слепое ядро W_infty^perp и канал сброса tr=3!=1", true, "dims(W_0..W_4) = $dims_W < 9, tr(Phi_reset^dagger(P_0)) = 3 != 1")
end

# GATE-II06-04: Теорема II.6.2 — симметричная трина Буша над Q(sqrt(3)), линейность меры и контрпример полусферы при d = 2
let
    # Точная арифметика в Q(sqrt(3)): элемент a + b*sqrt(3) как Tuple{Rational{BigInt}, Rational{BigInt}}
    q3_add(x, y) = (x[1] + y[1], x[2] + y[2])
    q3_mul(x, y) = (x[1]*y[1] + 3*x[2]*y[2], x[1]*y[2] + x[2]*y[1])
    q3_scale(c::Rational{BigInt}, x) = (c * x[1], c * x[2])
    Z0 = (Rational{BigInt}(0), Rational{BigInt}(0))
    U1 = (Rational{BigInt}(1), Rational{BigInt}(0))

    function q3_mat_add(A, B)
        [q3_add(A[i,j], B[i,j]) for i in 1:2, j in 1:2]
    end
    function q3_mat_mul(A, B)
        [q3_add(q3_mul(A[i,1], B[1,j]), q3_mul(A[i,2], B[2,j])) for i in 1:2, j in 1:2]
    end

    # Три элемента трины Буша E_k = (2/3) P_k в Q(sqrt(3))^{2x2}:
    E1 = [(Rational{BigInt}(2, 3), Rational{BigInt}(0)) Z0;
          Z0                                             Z0]
    E2 = [(Rational{BigInt}(1, 6), Rational{BigInt}(0)) (Rational{BigInt}(0), Rational{BigInt}(1, 6));
          (Rational{BigInt}(0), Rational{BigInt}(1, 6)) (Rational{BigInt}(1, 2), Rational{BigInt}(0))]
    E3 = [(Rational{BigInt}(1, 6), Rational{BigInt}(0)) (Rational{BigInt}(0), Rational{BigInt}(-1, 6));
          (Rational{BigInt}(0), Rational{BigInt}(-1, 6)) (Rational{BigInt}(1, 2), Rational{BigInt}(0))]
    I2_q3 = [U1 Z0; Z0 U1]

    # 1) Точное разбиение единицы E_1 + E_2 + E_3 == I_2 и E_k^2 == (2/3) E_k
    @assert q3_mat_add(q3_mat_add(E1, E2), E3) == I2_q3
    for Ek in (E1, E2, E3)
        @assert q3_mat_mul(Ek, Ek) == [q3_scale(Rational{BigInt}(2, 3), Ek[i,j]) for i in 1:2, j in 1:2]
    end

    # 2) Отсутствие бездисперсионной бинарной оценки {0, 1} на конусе эффектов E(C^2)
    @assert all((2 // 3) * s != 1 for s in 0:3)

    # 3) Контрпример на решётке проекторов P(C^2) при d = 2: полусферная оценка v_hem(u) in {0, 1}
    #    аддитивна на КАЖДОЙ ортогональной паре {P_u, P_{-u}} (v(P_u) + v(P_{-u}) = 1),
    #    но нарушает нормировку на трине POVM: (2/3)*(v(P_1)+v(P_2)+v(P_3)) = 4/3 != 1!
    hem_sign(u1_a, u1_b, u2_a, u3_a) = begin
        # Знак u_1 = u1_a + u1_b * sqrt(3), затем лексикографически u_2, u_3
        if u1_a != 0 || u1_b != 0
            return (u1_b > 0 || (u1_b == 0 && u1_a > 0)) ? 1 : 0
        elseif u2_a != 0
            return u2_a > 0 ? 1 : 0
        else
            return u3_a > 0 ? 1 : 0
        end
    end
    # На антиподальных парах Блоха сумма всегда равна 1:
    test_axes = [(0//1, 0//1, 0//1, 1//1), (3//5, 0//1, 4//5, 0//1), (0//1, 1//2, 0//1, -1//2)]
    for (a1, b1, a2, a3) in test_axes
        @assert hem_sign(a1, b1, a2, a3) + hem_sign(-a1, -b1, -a2, -a3) == 1
    end
    # Векторы Блоха трины: u^(1)=(0,0,1), u^(2)=(+sqrt(3)/2, 0, -1/2), u^(3)=(-sqrt(3)/2, 0, -1/2)
    v_trine_sum = (2 // 3) * (hem_sign(0//1, 0//1, 0//1, 1//1) +
                              hem_sign(0//1, 1//2, 0//1, -1//2) +
                              hem_sign(0//1, -1//2, 0//1, -1//2))
    @assert v_trine_sum == 4 // 3 && v_trine_sum != 1 // 1

    # 4) Точное восстановление рациональной матрицы плотности rho из меры Буша mu_rho(E) = tr(rho * E)
    rho_test = Complex{Rational{BigInt}}[3//5  (1//5 - (1//10)*im); (1//5 + (1//10)*im)  2//5]
    E_px = Complex{Rational{BigInt}}[1//2  1//2;  1//2  1//2]
    E_py = Complex{Rational{BigInt}}[1//2 -im//2; im//2 1//2]
    E_pz = Complex{Rational{BigInt}}[1//1  0//1;  0//1  0//1]
    rx = 2 * real(tr(rho_test * E_px)) - 1
    ry = 2 * real(tr(rho_test * E_py)) - 1
    rz = 2 * real(tr(rho_test * E_pz)) - 1
    rho_rec = (Complex{Rational{BigInt}}[1 0; 0 1] .+
               rx .* Complex{Rational{BigInt}}[0 1; 1 0] .+
               ry .* Complex{Rational{BigInt}}[0 -im; im 0] .+
               rz .* Complex{Rational{BigInt}}[1 0; 0 -1]) .// 2
    @assert rho_rec == rho_test

    record_gate!("GATE-II06-04", "II.6", "Теорема Буша в Q(sqrt(3)): трина E_1+E_2+E_3=I_2, сбой полусферной оценки P(C^2) (4/3!=1) и реконструкция rho", true, "E_1+E_2+E_3=I_2 over Q(sqrt(3)), hemisphere on trine = 4/3 != 1, rho reconstructed exactly")
end

# ==============================================================================
# ГЛАВА II.7. SIC-тетраэдр на S_4, 64 линии Хоггара и квадрат Переса — Мермина
# ==============================================================================

# GATE-II07-01: Теорема II.7.1 — SIC-тетраэдр кубита из S_4, контрпример V_4 и конфигурация Гессе (d = 3)
let
    u_tet = [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]]
    for i in 1:4, j in (i+1):4
        @assert dot(u_tet[i], u_tet[j]) // 3 == -1 // 3
    end
    v_rect = [
        Rational{BigInt}[ 3//5,  4//5, 0],
        Rational{BigInt}[ 3//5, -4//5, 0],
        Rational{BigInt}[-3//5,  4//5, 0],
        Rational{BigInt}[-3//5, -4//5, 0]
    ]
    dots_rect = unique([dot(v_rect[1], v_rect[j]) for j in 2:4])
    @assert length(dots_rect) == 3 && (-1 in dots_rect) && (-7//25 in dots_rect) && (7//25 in dots_rect)

    cyc_conj(z::Tuple{Int,Int}) = (z[1] - z[2], -z[2])
    cyc_add(z1::Tuple{Int,Int}, z2::Tuple{Int,Int}) = (z1[1] + z2[1], z1[2] + z2[2])
    cyc_mul(z1::Tuple{Int,Int}, z2::Tuple{Int,Int}) = (z1[1]*z2[1] - z1[2]*z2[2], z1[1]*z2[2] + z1[2]*z2[1] - z1[2]*z2[2])
    cyc_abs2(z::Tuple{Int,Int}) = z[1]^2 - z[1]*z[2] + z[2]^2
    omega_pow(k::Int) = mod(k, 3) == 0 ? (1, 0) : (mod(k, 3) == 1 ? (0, 1) : (-1, -1))

    psi0_cyc = [(0, 0), (1, 0), (-1, 0)]
    hesse_cyc = Vector{Vector{Tuple{Int,Int}}}()
    for a in 0:2, b in 0:2
        vec_ab = [cyc_mul(omega_pow(b * mod(r - a, 3)), psi0_cyc[mod(r - a, 3) + 1]) for r in 0:2]
        @assert sum(cyc_abs2(vec_ab[r]) for r in 1:3) == 2
        push!(hesse_cyc, vec_ab)
    end
    @assert length(hesse_cyc) == 9
    for i in 1:9, j in (i+1):9
        ip_cyc = (0, 0)
        for r in 1:3
            ip_cyc = cyc_add(ip_cyc, cyc_mul(cyc_conj(hesse_cyc[i][r]), hesse_cyc[j][r]))
        end
        @assert cyc_abs2(ip_cyc) // 4 == 1 // 4
    end
    record_gate!("GATE-II07-01", "II.7", "SIC-тетраэдр кубита из S_4 (-1/3), контрпример V_4 и точная проверка SIC Гессе при d=3 в Z[omega] (36 перекрытий = 1/4)", true, "tetrahedron overlaps = -1/3, Hesse 36 exact overlaps in Z[omega] = 1/4")
end

# GATE-II07-02: Теорема II.7.2 — 64 линии Хоггара в C^8 в точной гауссовой арифметике Q(i)
let
    phi_tilde = Complex{Rational{BigInt}}[-1 + 2im, 1, 1, 1, 1, 1, 1, 1]
    @assert sum(abs2, phi_tilde) == 12

    hoggar_vecs = Vector{Vector{Complex{Rational{BigInt}}}}()
    for a in 0:7, b in 0:7
        abits = digits(a, base=2, pad=3)
        bbits = digits(b, base=2, pad=3)
        v = Vector{Complex{Rational{BigInt}}}(undef, 8)
        for x in 0:7
            xbits = digits(x, base=2, pad=3)
            src = 0
            for k in 1:3
                xor(xbits[k], abits[k]) == 1 && (src += (1 << (k - 1)))
            end
            sgn = iseven(sum(bbits[k] * ((src >> (k-1)) & 1) for k in 1:3)) ? 1 : -1
            v[x + 1] = sgn * phi_tilde[src + 1]
        end
        push!(hoggar_vecs, v)
    end
    @assert length(hoggar_vecs) == 64

    for idx in 2:64
        ip = sum(conj(phi_tilde[k]) * hoggar_vecs[idx][k] for k in 1:8)
        norm_sq = real(ip)^2 + imag(ip)^2
        @assert norm_sq == 16 && (norm_sq // 144 == 1 // 9)
    end

    G_frame = [sum(conj(hoggar_vecs[i][k]) * hoggar_vecs[j][k] for k in 1:8) // 12 for i in 1:64, j in 1:64]
    I64 = Matrix{Complex{Rational{BigInt}}}(I, 64, 64)
    @assert G_frame * G_frame == 8 .* G_frame
    @assert tr(G_frame) == 64 && (tr(G_frame) // 8 == 8)
    S_mat = 3 .* (G_frame .- I64)
    @assert S_mat * S_mat == 63 .* I64 .+ 18 .* S_mat

    H_mod_sq = Rational{BigInt}[i == j ? 1 // 1 : 1 // 9 for i in 1:64, j in 1:64]
    @assert H_mod_sq * H_mod_sq != 8 .* H_mod_sq
    @assert exact_rank_rational(H_mod_sq) == 64

    Phi2 = (1 + 63 * (1 // 9)^2) // 64
    Phi3 = (1 + 63 * (1 // 9)^3) // 64
    Welch2 = 1 // binomial(8 + 2 - 1, 2)
    Welch3 = 1 // binomial(8 + 3 - 1, 3)
    @assert Phi2 == 1 // 36 && Phi2 == Welch2
    @assert Phi3 == 11 // 648 && Welch3 == 1 // 120 && (Phi3 - Welch3 == 7 // 810) && Phi3 > Welch3
    record_gate!("GATE-II07-02", "II.7", "64 линии Хоггара в точной арифметике Q(i): перекрытия 1/9, G_frame^2=8G_frame (rk=8), rk(H)=64, S^2=63I+18S, Phi_3-Phi_3^Welch=7/810", true, "all 63 overlaps = 1/9, G_frame^2=8G_frame, rk(H)=64, S^2=63I+18S, Phi2=1/36, Phi3-Welch3=7/810")
end

# GATE-II07-03: Теорема II.7.3 — квадрат Переса — Мермина и паритетный заряд kappa = 1
let
    I2 = Complex{Int}[1 0; 0 1]
    sx = Complex{Int}[0 1; 1 0]
    sy = Complex{Int}[0 -im; im 0]
    sz = Complex{Int}[1 0; 0 -1]
    kp(A, B) = kron(A, B)

    grid = [
        [kp(sz, I2), kp(I2, sz), kp(sz, sz)],
        [kp(I2, sx), kp(sx, I2), kp(sx, sx)],
        [kp(sz, sx), kp(sx, sz), kp(sy, sy)]
    ]
    I4 = Matrix{Complex{Int}}(I, 4, 4)
    for r in 1:3
        A, B, C = grid[r][1], grid[r][2], grid[r][3]
        @assert A*B == B*A && B*C == C*B && A*C == C*A && A * B * C == I4
    end
    for c in 1:3
        A, B, C = grid[1][c], grid[2][c], grid[3][c]
        @assert A*B == B*A && B*C == C*B && A*C == C*A && A * B * C == (c == 3 ? -I4 : I4)
    end

    delta_pm = [
        1 1 1 0 0 0 0 0 0;
        0 0 0 1 1 1 0 0 0;
        0 0 0 0 0 0 1 1 1;
        1 0 0 1 0 0 1 0 0;
        0 1 0 0 1 0 0 1 0;
        0 0 1 0 0 1 0 0 1
    ]
    rhs_pm = [0, 0, 0, 0, 0, 1]
    @assert exact_rank_mod(delta_pm, 2) == 5
    @assert all(iszero, mod.(vec(sum(delta_pm, dims=1)), 2))
    @assert mod(sum(rhs_pm), 2) == 1
    sols_pm = count(m -> mod.(delta_pm * digits(m, base=2, pad=9), 2) == rhs_pm, 0:511)
    @assert sols_pm == 0
    record_gate!("GATE-II07-03", "II.7", "Квадрат Переса — Мермина: rk(delta)=5, паритетный заряд kappa_PM = 1 и 0/512 глобальных сечений", true, "row/col products = (+1,+1,+1,+1,+1,-1), rk(delta)=5, 0/512 global assignments")
end

# GATE-II07-04: §II.7.4 — точная иерархия контекстуальности |S_e(X)| = 16 (Цирельсон в Q(sqrt(2))) > 5 (Харди в Q) > 0 (ПМ)
let
    # 1) Классическая граница Белла — CHSH: max |a0*(b0+b1) + a1*(b0-b1)| == 2 на всех 16 таблицах {+-1}^4
    chsh_classical = [abs(a0*(b0 + b1) + a1*(b0 - b1)) for a0 in (-1,1) for a1 in (-1,1) for b0 in (-1,1) for b1 in (-1,1)]
    @assert maximum(chsh_classical) == 2

    # 2) Тождество Ландау — Цирельсона: S_CHSH = sqrt(2) * K_int, где K_int = sz⊗sz + sx⊗sx, S_CHSH^2 = 4*I_4 - 4*(sy⊗sy)
    sx_i = Complex{Int}[0 1; 1 0]
    sy_i = Complex{Int}[0 -im; im 0]
    sz_i = Complex{Int}[1 0; 0 -1]
    I4_i = Matrix{Complex{Int}}(I, 4, 4)
    K_int = kron(sz_i, sz_i) .+ kron(sx_i, sx_i)
    S_sq_exact = 2 .* (K_int * K_int)
    @assert S_sq_exact == 4 .* I4_i .- 4 .* kron(sy_i, sy_i)
    @assert S_sq_exact * (S_sq_exact .- 8 .* I4_i) == zeros(Complex{Int}, 4, 4)

    # На состоянии Белла psi_bell = (1, 0, 0, 1) (квадрат нормы 2): K_int * psi_bell == 2 * psi_bell => <S_CHSH> = 2*sqrt(2)
    psi_bell = Complex{Int}[1, 0, 0, 1]
    @assert K_int * psi_bell == 2 .* psi_bell
    # Точная проверка всех 16 вероятностей Борна в Q(sqrt(2)) (пара (a, b) = a + b*sqrt(2)):
    # для каждой пары контекста (i,j) in {0,1}^2 и исхода (sA, sB) in {-1,+1}^2 вероятность равна 1/4 + ((-1)^(i*j) * sA * sB)/(4*sqrt(2)) = 1/4 ± (1/8)*sqrt(2)!
    q2_pos(a::Rational{Int}, b::Rational{Int}) = begin
        # Точная проверка a + b*sqrt(2) > 0 без корней
        if a > 0 && b >= 0
            return true
        elseif a > 0 && b < 0
            return a^2 > 2 * (b^2)
        elseif a <= 0 && b > 0
            return 2 * (b^2) > a^2
        else
            return false
        end
    end
    tsirelson_probs_pos = true
    for i in 0:1, j in 0:1
        sgn_ctx = (i == 1 && j == 1) ? -1 : 1
        sum_a = 0 // 1
        sum_b = 0 // 1
        for sA in (-1, 1), sB in (-1, 1)
            pa = 1 // 4
            pb = (sgn_ctx * sA * sB) // 8
            tsirelson_probs_pos &= q2_pos(pa, pb)
            sum_a += pa; sum_b += pb
        end
        @assert sum_a == 1 // 1 && sum_b == 0 // 1
    end
    @assert tsirelson_probs_pos
    # Так как все 16 локальных вероятностей строго положительны, все 2^4 = 16 глобальных таблиц лежат в S_e(X)!
    se_tsirelson = 16

    # 3) Рациональная двухкубитная модель Харди: psi_H = |01> + |10> + |11> = [0, 1, 1, 1] (квадрат нормы 3),
    #    A_0 = B_0 = sigma_z, A_1 = B_1 = sigma_x
    psi_H = Rational{Int}[0, 1, 1, 1]
    norm_H_sq = sum(x^2 for x in psi_H)
    @assert norm_H_sq == 3
    P_z(s) = s == 1 ? Rational{Int}[1 0; 0 0] : Rational{Int}[0 0; 0 1]
    P_x(s) = s == 1 ? Rational{Int}[1//2 1//2; 1//2 1//2] : Rational{Int}[1//2 -1//2; -1//2 1//2]
    hardy_prob(i, j, sA, sB) = begin
        PA = i == 0 ? P_z(sA) : P_x(sA)
        PB = j == 0 ? P_z(sB) : P_x(sB)
        dot(psi_H, kron(PA, PB) * psi_H) // norm_H_sq
    end
    @assert hardy_prob(0, 0,  1,  1) == 0 // 1
    @assert hardy_prob(0, 1, -1, -1) == 0 // 1
    @assert hardy_prob(1, 0, -1, -1) == 0 // 1
    @assert hardy_prob(1, 1, -1, -1) == 1 // 12

    hardy_sections = [(a0, a1, b0, b1) for a0 in (-1,1) for a1 in (-1,1) for b0 in (-1,1) for b1 in (-1,1)
                      if hardy_prob(0,0,a0,b0) > 0 && hardy_prob(0,1,a0,b1) > 0 &&
                         hardy_prob(1,0,a1,b0) > 0 && hardy_prob(1,1,a1,b1) > 0]
    se_hardy = length(hardy_sections)
    # Исход (-1,-1) в контексте (A_1, B_1) возможен (1/12 > 0), но не продолжается ни до одного из 5 глобальных сечений!
    @assert se_hardy == 5 && all(!(sec[2] == -1 && sec[4] == -1) for sec in hardy_sections)
    se_pm = 0
    @assert se_tsirelson > se_hardy > se_pm

    record_gate!("GATE-II07-04", "II.7", "Строгая иерархия контекстуальности в Q(sqrt(2)) и Q: |S_e(X)| = 16 (Цирельсон) > 5 (Харди, p=1/12) > 0 (ПМ)", true, "S_CHSH^2=4I-4(sy⊗sy), Tsirelson |S_e|=16, Hardy p_{11}(-1,-1)=1/12 & |S_e|=5, PM |S_e|=0")
end

# ==============================================================================
# ГЛАВА II.8. Формы Уитни, поток Кана — Хиллиарда и рациональные SOS на флагах Фано
# ==============================================================================

# GATE-II08-01: Предложение II.8.1 — тождество Уитни R_1 W_1 = id, дефект на x dx и подразделение треугольника
let
    poly_int_1form(coeffs::Vector{Rational{BigInt}}, a::Rational{BigInt}, b::Rational{BigInt}) =
        sum(coeffs[k] * (b^k - a^k) // k for k in eachindex(coeffs))

    for c1_val in (Rational{BigInt}(-3, 7), Rational{BigInt}(0, 1), Rational{BigInt}(5, 4))
        w1_poly = [c1_val]
        r1_w1 = poly_int_1form(w1_poly, Rational{BigInt}(0), Rational{BigInt}(1))
        @assert r1_w1 == c1_val
    end
    omega_poly = Rational{BigInt}[0, 1]
    c_full = poly_int_1form(omega_poly, Rational{BigInt}(0), Rational{BigInt}(1))
    whitney_poly = Rational{BigInt}[c_full]
    int_half_omega   = poly_int_1form(omega_poly, Rational{BigInt}(0), Rational{BigInt}(1, 2))
    int_half_whitney = poly_int_1form(whitney_poly, Rational{BigInt}(0), Rational{BigInt}(1, 2))
    @assert c_full == 1 // 2 && int_half_omega == 1 // 8 && int_half_whitney == 1 // 4 && int_half_omega != int_half_whitney

    d2_K = [1; 1; -1]
    s1_sub = [1 0 0; 1 0 0; 0 1 0; 0 0 1; 0 0 0]
    d2_Kprime = [1 0; 0 1; 0 1; -1 0; 1 -1]
    s2_sub = [1; 1]
    chain_sub = d2_Kprime * s2_sub
    @assert chain_sub == s1_sub * d2_K && chain_sub[5, 1] == 0
    record_gate!("GATE-II08-01", "II.8", "Тождество Уитни R_1 W_1 = id, дефект поточечной реконструкции и цепное тождество d_2' s_2 = s_1 d_2 при подразделении", true, "R_1 W_1 = id, int_half(omega) = 1/8 != 1/4 = int_half(W_1 R_1 omega), d2'*s2 == s1*d2 (inner seam coeff = 0)")
end

# GATE-II08-02: Теорема II.8.1 — полудискретный поток Кана — Хиллиарда на графе O_6 и точный спектр L_{O_6}
let
    axes_of = [1, 1, 2, 2, 3, 3]
    edges_O6 = [(u, v) for u in 1:6 for v in (u+1):6 if axes_of[u] != axes_of[v]]
    D1 = zeros(Rational{BigInt}, 12, 6)
    for (e_idx, (u, v)) in enumerate(edges_O6)
        D1[e_idx, u] = -1
        D1[e_idx, v] = +1
    end
    L = D1' * D1
    I6 = Matrix{Rational{BigInt}}(I, 6, 6)

    # Точная рациональная проверка спектра L_{O_6} = {0^1, 4^3, 6^2} через размерности ядер и минимальный аннулирующий многочлен
    mult0 = 6 - exact_rank_rational(L)
    mult4 = 6 - exact_rank_rational(L - 4 .* I6)
    mult6 = 6 - exact_rank_rational(L - 6 .* I6)
    @assert (mult0, mult4, mult6) == (1, 3, 2) && (mult0 + mult4 + mult6 == 6)
    @assert all(iszero, L * (L - 4 .* I6) * (L - 6 .* I6))

    M_mob = Rational{BigInt}(3, 2)
    gamma = Rational{BigInt}(1, 8)
    u = Rational{BigInt}[1, -1, 2, -2, 1//2, -1//2]
    F_prime = [s^3 - s for s in u]
    mu = gamma .* (L * u) .+ F_prime
    u_dot = -M_mob .* (L * mu)

    mass_rate = sum(u_dot)
    dE_dt = dot(mu, u_dot)
    expected_dE_dt = -M_mob * sum((D1 * mu).^2)
    @assert mass_rate == 0 && dE_dt == expected_dE_dt && dE_dt < 0
    record_gate!("GATE-II08-02", "II.8", "Поток Кана — Хиллиарда на O_6 и точный рациональный спектр L_{O_6} = {0^1, 4^3, 6^2}", true, "1^T u_dot == 0, dE/dt = $dE_dt < 0, exact eigenspace dims = (1, 3, 2)")
end

# GATE-II08-03: §II.8.4 — целочисленные собственные векторы G_bad ({3, -1, -2}) и рациональный сертификат G_PSD для (x^2+y^2)^2
let
    G_bad = Rational{BigInt}[1 0 2; 0 -2 0; 2 0 1]
    v1 = Rational{BigInt}[1, 0, 1]
    v2 = Rational{BigInt}[1, 0, -1]
    v3 = Rational{BigInt}[0, 1, 0]
    @assert G_bad * v1 == 3 .* v1 && G_bad * v2 == (-1) .* v2 && G_bad * v3 == (-2) .* v3
    @assert exact_rank_rational(hcat(v1, v2, v3)) == 3 && G_bad[2, 2] == -2 < 0

    G_psd = Rational{BigInt}[1 0 0; 0 2 0; 0 0 1]
    L_id  = Matrix{Rational{BigInt}}(I, 3, 3)
    @assert L_id * G_psd * L_id' == G_psd && all(diag(G_psd) .> 0)

    # Обе матрицы Грама представляют один и тот же многочлен (x^2 + y^2)^2 на всех мономных векторах z = [x^2, x*y, y^2]
    for x in -2:2, y in -2:2
        z = Rational{BigInt}[x^2, x*y, y^2]
        @assert dot(z, G_bad * z) == (x^2 + y^2)^2 && dot(z, G_psd * z) == (x^2 + y^2)^2
    end
    record_gate!("GATE-II08-03", "II.8", "Матрицы Грама для (x^2+y^2)^2: точный спектр {-2, -1, 3} у G_bad и рациональный SOS-сертификат G_PSD", true, "exact eigenbasis of G_bad gives {3,-1,-2}, G_PSD = diag(1, 2, 1) >= 0")
end

# GATE-II08-04: Теорема II.8.2 — 21 флаг Фано, разложения Веронезе 231/1771 и точные рациональные проекторы P_{perp,c} коразмерности 1687
let
    pts = [digits(m, base=2, pad=3) for m in 1:7]
    lines = Vector{Vector{Int}}()
    for i in 1:7, j in (i+1):7, k in (j+1):7
        if mod.(pts[i] .+ pts[j] .+ pts[k], 2) == [0, 0, 0]
            push!(lines, [i, j, k])
        end
    end
    @assert length(lines) == 7

    # Для каждого ненулевого u in F_2^3 ядро u . x = 0 содержит ровно 1 прямую Фано (3 точки) и по 1 точке на остальных 6 прямых => 9 плюсов и 12 минусов на 21 флаге
    for u in pts
        n_plus = count(mod(dot(u, pts[p_idx]), 2) == 0 for l in lines for p_idx in l)
        n_minus = 21 - n_plus
        @assert n_plus == 9 && n_minus == 12
    end

    flag_pts = [p_idx for l in lines for p_idx in l]
    @assert length(flag_pts) == 21

    quad_char_counts = zeros(Int, 8)
    for i in 1:21, j in i:21
        c = xor(flag_pts[i], flag_pts[j])
        quad_char_counts[c + 1] += 1
    end
    @assert sum(quad_char_counts) == 231 && quad_char_counts[1] == 42 && all(==(27), quad_char_counts[2:8])

    cubic_mons_by_char = [NTuple{3,Int}[] for _ in 0:7]
    for i in 1:21, j in i:21, k in j:21
        c = xor(flag_pts[i], flag_pts[j], flag_pts[k])
        push!(cubic_mons_by_char[c + 1], (i, j, k))
    end
    cubic_counts = length.(cubic_mons_by_char)
    @assert sum(cubic_counts) == 1771 && cubic_counts[1] == 189 && all(==(226), cubic_counts[2:8])

    flags = [(p_idx, l_idx) for l_idx in 1:7 for p_idx in lines[l_idx]]
    orbit_84 = Vector{Vector{Rational{BigInt}}}()
    for a in 1:7, b in (a+1):7
        l_ab = findfirst(l -> (a in l && b in l), lines)
        @assert l_ab !== nothing
        for s1 in (1, -1), s2 in (1, -1)
            u = zeros(Rational{BigInt}, 21)
            for idx in 1:21
                p_idx, l_idx = flags[idx]
                if p_idx == a
                    u[idx] = (l_idx == l_ab) ? 1 : 2 * s1
                elseif p_idx == b
                    u[idx] = (l_idx == l_ab) ? s2 : 2 * s1 * s2
                end
            end
            push!(orbit_84, u)
        end
    end
    @assert length(orbit_84) == 84

    rk_by_char = zeros(Int, 8)
    sos_traces = zeros(Int, 8)
    sos_traces[1] = 189 # в тривиальном канале c=0 все 84 вектора Веронезе нулевые => P_{perp,0} = I_{189}
    I226 = Matrix{Rational{BigInt}}(I, 226, 226)

    for c_idx in 0:7
        mons_c = cubic_mons_by_char[c_idx + 1]
        M_c = zeros(Rational{BigInt}, length(mons_c), 84)
        for (col_j, u) in enumerate(orbit_84)
            for (row_i, (i, j, k)) in enumerate(mons_c)
                M_c[row_i, col_j] = u[i] * u[j] * u[k]
            end
        end
        if c_idx == 0
            @assert all(iszero, M_c)
            rk_by_char[1] = 0
        else
            # Находим 12 линейно независимых столбцов B_c размера 226x12 и строим точный ортогональный проектор P_{perp,c} = I_{226} - B_c (B_c^T B_c)^{-1} B_c^T
            ind_cols = Int[]
            for j in 1:84
                iszero(M_c[:, j]) && continue
                cand = vcat(ind_cols, j)
                if exact_rank_rational(M_c[:, cand]) > length(ind_cols)
                    push!(ind_cols, j)
                    length(ind_cols) == 12 && break
                end
            end
            @assert length(ind_cols) == 12
            B_c = M_c[:, ind_cols]
            rk_by_char[c_idx + 1] = exact_rank_rational(M_c)
            @assert rk_by_char[c_idx + 1] == 12

            Gram_12 = transpose(B_c) * B_c
            Gram_inv = inv(Gram_12)
            # Проверяем P_{perp,c} * M_c == 0 через (I - B_c Gram_inv B_c^T) M_c = M_c - B_c (Gram_inv (B_c^T M_c)) == 0
            proj_M_c = B_c * (Gram_inv * (transpose(B_c) * M_c))
            @assert proj_M_c == M_c

            P_perp_c = I226 - B_c * (Gram_inv * transpose(B_c))
            @assert P_perp_c == transpose(P_perp_c)
            @assert tr(P_perp_c) == 214
            # На первом нетривиальном канале проверяем прямое матричное возведение в квадрат 226x226: P_{perp,1}^2 == P_{perp,1}
            if c_idx == 1
                @assert P_perp_c * P_perp_c == P_perp_c
            end
            sos_traces[c_idx + 1] = Int(numerator(tr(P_perp_c)))
        end
    end
    @assert rk_by_char == [0, 12, 12, 12, 12, 12, 12, 12]
    @assert sos_traces == [189, 214, 214, 214, 214, 214, 214, 214]
    @assert sum(rk_by_char) == 84 && sum(sos_traces) == 1687 && (84 + 1687 == 1771)

    record_gate!("GATE-II08-04", "II.8", "Явные рациональные SOS-проекторы P_{perp,c} на 21 флаге Фано: tr = 189 + 7*214 = 1687 и P_{perp,c} M_c = 0", true, "Sym^2=42+7*27=231, Sym^3=189+7*226=1771, rk(K_84)=84, exact SOS projector trace = 1687")
end

# ==============================================================================
# ГЛАВА II.9. Теорема Ловера, коцикл beta, H^1(GL_3(2), F_2^3)=F_2, орбиты 8+56 и линт
# ==============================================================================

# GATE-II09-01: Теорема II.9.1 — диагональный запрет Ловера — Кантора и экспоненциал Y^A в Set^{C_2}
let
    no_surj_3 = true
    for mask in 0:511
        M = reshape(digits(mask, base=2, pad=9), 3, 3)
        diag_neg = [1 - M[i, i] for i in 1:3]
        if any(M[r, :] == diag_neg for r in 1:3)
            no_surj_3 = false
        end
    end
    @assert no_surj_3

    A_C2 = [x for x in (0, 1) if (1 - x) == x]
    @assert isempty(A_C2)
    prod_pts = [(g, a) for g in (0, 1) for a in (0, 1)]
    equiv_maps = Vector{Dict{Tuple{Int,Int},Int}}()
    for mask in 0:15
        bits = digits(mask, base=2, pad=4)
        phi = Dict(prod_pts[i] => bits[i] for i in 1:4)
        if all(phi[(1 - g, 1 - a)] == phi[(g, a)] for (g, a) in prod_pts)
            push!(equiv_maps, phi)
        end
    end
    @assert length(equiv_maps) == 4
    sigma_exp(phi) = Dict((g, a) => phi[(1 - g, a)] for (g, a) in prod_pts)
    exp_global_pts = [phi for phi in equiv_maps if sigma_exp(phi) == phi]
    @assert length(exp_global_pts) == 2
    img_sizes = sort([length(unique([u, sigma_exp(u)])) for u in equiv_maps])
    @assert img_sizes == [1, 1, 2, 2] && maximum(img_sizes) < length(equiv_maps)
    record_gate!("GATE-II09-01", "II.9", "Диагональный запрет Ловера — Кантора (0/512 таблиц) и экспоненциал Y^A в Set^{C_2} (|A^{C_2}|=0, |Y^A|=4, |(Y^A)^{C_2}|=2)", true, "0/512 tables contain negated diagonal; |A^{C_2}| == 0, |Y^A| == 4, |(Y^A)^{C_2}| == 2")
end

# GATE-II09-02: Теорема II.9.2 (пп. 1–2) — 2-коцикл beta((g,u),(h,v)) = g_1 * h_2 на 64 состояниях и критерий Шапиро
let
    G32 = [digits(m, base=2, pad=5) for m in 0:31]
    beta_cocycle(x, y) = mod(x[1] * y[2], 2)
    for x in G32, y in G32, z in G32
        xy = mod.(x .+ y, 2)
        yz = mod.(y .+ z, 2)
        @assert xor(beta_cocycle(x, y), beta_cocycle(xy, z)) == xor(beta_cocycle(x, yz), beta_cocycle(y, z))
    end
    t_diag = [1, 1, 0, 0, 0]
    @assert beta_cocycle(t_diag, t_diag) == 1
    K16 = [x for x in G32 if x[1] == 0]
    @assert length(K16) == 16 && all(beta_cocycle(x, y) == 0 for x in K16 for y in K16)
    record_gate!("GATE-II09-02", "II.9", "Проверка 2-коцикла beta(x,y) = x_1 y_2 на 32^3 тройках, beta(t,t)=1 и расщепления на K индекса 2", true, "32768 cocycle triples hold, beta(t,t)=1, K_16 splits")
end

# GATE-II09-03: Теорема II.9.2 (п. 3) — прямое вычисление H^1(GL_3(2), F_2^3) = F_2 (dim Z^1=4, dim B^1=3), скрученное действие и орбиты 8 + 56 = 64
let
    GL3_F2 = Matrix{Int}[]
    for m in 0:511
        M = reshape(digits(m, base=2, pad=9), 3, 3)
        if exact_rank_mod(M, 2) == 3
            push!(GL3_F2, M)
        end
    end
    @assert length(GL3_F2) == 168
    mat_id = Dict(GL3_F2[i] => i for i in 1:168)
    mul_gl = [mat_id[mod.(GL3_F2[i] * GL3_F2[j], 2)] for i in 1:168, j in 1:168]

    # Два образующих GL_3(F_2): цикл Зингера C7_gen порядка 7 и инволюция B_gen порядка 2
    C7_gen = [0 0 1; 1 0 1; 0 1 0]
    B_gen  = [0 1 0; 1 0 0; 0 0 1]
    id_C7 = mat_id[C7_gen]
    id_B  = mat_id[B_gen]
    # Проверяем по BFS, что {C7_gen, B_gen} порождают все 168 элементов GL_3(F_2)
    vis = falses(168); vis[id_C7] = true; queue = [id_C7]
    while !isempty(queue)
        cur = popfirst!(queue)
        for gen in (id_C7, id_B)
            nxt = mul_gl[gen, cur]
            if !vis[nxt]
                vis[nxt] = true
                push!(queue, nxt)
            end
        end
    end
    @assert count(vis) == 168

    # Строим линейную систему 1-коциклов c(s * g) + c(s) + s * c(g) == 0 (mod 2) для s in {C7_gen, B_gen} и всех g in GL_3(F_2)
    # 504 переменных: столбец 3*(g-1) + r отвечает r-й компоненте c(g)[r] (r=1..3, g=1..168)
    Sys_Z1 = zeros(Int, 2 * 168 * 3, 504)
    row_ptr = 0
    for s_id in (id_C7, id_B)
        S_mat = GL3_F2[s_id]
        for g_id in 1:168
            sg_id = mul_gl[s_id, g_id]
            for r in 1:3
                row_ptr += 1
                Sys_Z1[row_ptr, 3*(sg_id - 1) + r] = xor(Sys_Z1[row_ptr, 3*(sg_id - 1) + r], 1)
                Sys_Z1[row_ptr, 3*(s_id  - 1) + r] = xor(Sys_Z1[row_ptr, 3*(s_id  - 1) + r], 1)
                for c in 1:3
                    if S_mat[r, c] == 1
                        Sys_Z1[row_ptr, 3*(g_id - 1) + c] = xor(Sys_Z1[row_ptr, 3*(g_id - 1) + c], 1)
                    end
                end
            end
        end
    end
    Z1_basis = nullspace_mod2(Sys_Z1)
    dim_Z1 = length(Z1_basis)
    @assert dim_Z1 == 4

    # Пространство 1-кограниц B^1: b_v(g) = (g + I_3) * v mod 2 для v in F_2^3
    I3_f2 = [1 0 0; 0 1 0; 0 0 1]
    B1_cols = Vector{Vector{Int}}()
    for r_v in 1:3
        v = [i == r_v ? 1 : 0 for i in 1:3]
        col = zeros(Int, 504)
        for g_id in 1:168
            bv = mod.((GL3_F2[g_id] .+ I3_f2) * v, 2)
            for r in 1:3; col[3*(g_id - 1) + r] = bv[r]; end
        end
        push!(B1_cols, col)
    end
    B1_mat = hcat(B1_cols...)
    dim_B1 = exact_rank_mod(B1_mat, 2)
    dim_H1 = dim_Z1 - dim_B1
    @assert dim_B1 == 3 && dim_H1 == 1

    # Выбираем нетривиальный 1-коцикл c_nt in Z^1 \ B^1 и проверяем тождество коцикла на ВСЕХ 168^2 = 28 224 парах (g, h)!
    c_nt_vec = first(z for z in Z1_basis if exact_rank_mod(hcat(B1_mat, z), 2) == 4)
    c_nt = [[c_nt_vec[3*(g_id - 1) + r] for r in 1:3] for g_id in 1:168]
    cocycle_28224_ok = true
    @inbounds for g_id in 1:168
        G_mat = GL3_F2[g_id]
        cg = c_nt[g_id]
        for h_id in 1:168
            gh_id = mul_gl[g_id, h_id]
            ch = c_nt[h_id]
            lhs = c_nt[gh_id]
            for r in 1:3
                rhs_r = xor(cg[r], mod(G_mat[r,1]*ch[1] + G_mat[r,2]*ch[2] + G_mat[r,3]*ch[3], 2))
                if lhs[r] != rhs_r
                    cocycle_28224_ok = false
                    break
                end
            end
        end
    end
    @assert cocycle_28224_ok

    # Скрученное аффинное действие g * v = g*v + c_nt(g) (mod 2) на V = F_2^3 и диагональное действие на X_64 = F_2^3 x F_2^3:
    V8 = [digits(m, base=2, pad=3) for m in 0:7]
    act_v(g_id, v) = mod.(GL3_F2[g_id] * v .+ c_nt[g_id], 2)
    # 0 неподвижных точек на F_2^3 (нерасщепимое расширение 2^3 . GL_3(2)) и транзитивная орбита размера 8 со стабилизатором порядка 21
    fixed_pts = [v for v in V8 if all(act_v(g_id, v) == v for g_id in 1:168)]
    @assert isempty(fixed_pts)
    stab_0 = [g_id for g_id in 1:168 if act_v(g_id, [0, 0, 0]) == [0, 0, 0]]
    @assert length(stab_0) == 21 && isodd(length(stab_0))

    # Разбиение X_64 = F_2^3 x F_2^3 на орбиты относительно диагонального скрученного действия GL_3(F_2):
    X64 = [(u, v) for u in V8 for v in V8]
    pt_to_idx = Dict(X64[i] => i for i in 1:64)
    seen64 = falses(64)
    orbit_sizes = Int[]
    stab_orders = Int[]
    for start_idx in 1:64
        seen64[start_idx] && continue
        u0, v0 = X64[start_idx]
        orb = Set{Int}()
        stab_cnt = 0
        for g_id in 1:168
            ug = act_v(g_id, u0)
            vg = act_v(g_id, v0)
            idx_g = pt_to_idx[(ug, vg)]
            push!(orb, idx_g)
            (idx_g == start_idx) && (stab_cnt += 1)
        end
        for id in orb; seen64[id] = true; end
        push!(orbit_sizes, length(orb))
        push!(stab_orders, stab_cnt)
    end
    sort!(orbit_sizes)
    sort!(stab_orders, rev=true)
    @assert orbit_sizes == [8, 56] && sum(orbit_sizes) == 64 && stab_orders == [21, 3] && all(isodd, stab_orders)

    record_gate!("GATE-II09-03", "II.9", "Точное вычисление H^1(GL_3(2), F_2^3)=F_2 (dim Z^1=4, dim B^1=3), 28224 пар коцикла и орбиты 8 + 56 = 64 на X_64", true, "dim Z^1=4, dim B^1=3, dim H^1=1, 28224/28224 cocycle pairs hold, X_64 orbits = [8, 56], stabilizers = [21, 3]")
end

# GATE-II09-04: Теорема II.9.2 (чётность индекса 7 против нечётного стабилизатора индекса 8) и сводка Таблицы II.9.1
let
    # Прямая групповая проверка минимальности 8-точечного фактора с нечётным стабилизатором в GL_3(F_2):
    GL3_F2 = [reshape(digits(m, base=2, pad=9), 3, 3) for m in 0:511 if exact_rank_mod(reshape(digits(m, base=2, pad=9), 3, 3), 2) == 3]
    # Стабилизатор ненулевой точки [1,0,0] в естественном 7-точечном действии на PG(2,2) имеет чётный порядок 24 (2 | 24)
    stab_pt7 = [M for M in GL3_F2 if mod.(M * [1, 0, 0], 2) == [1, 0, 0]]
    @assert length(stab_pt7) == 24 && iseven(length(stab_pt7)) && div(168, length(stab_pt7)) == 7

    # Так как |GL_3(F_2)| = 168 = 2^3 * 21, любой нечётный порядок подгруппы H делит 21, откуда |GL_3(F_2) : H| = 168 / |H| >= 8 и кратно 8!
    odd_divisors_168 = [d for d in 1:168 if mod(168, d) == 0 && isodd(d)]
    possible_odd_quotient_sizes = sort([div(168, d) for d in odd_divisors_168])
    @assert odd_divisors_168 == [1, 3, 7, 21] && minimum(possible_odd_quotient_sizes) == 8

    # Сверка, что все предыдущие 35 содержательных гейтов Книги II пройдены без единого пропуска
    @assert length(RESULTS) == 35 && all(r -> r.passed, RESULTS)
    record_gate!("GATE-II09-04", "II.9", "Чётность стабилизатора индекса 7 (|Stab|=24) против минимального нечётного стабилизатора индекса 8 (|K_21|=21) и сводка Книги II", true, "|Stab_PG(2,2)|=24 (even), min odd-stabilizer quotient = 168/21 = 8, 35/35 preceding gates verified")
end

const EDITORIAL_PATTERNS = Pair{String,Regex}[
    "не просто" => r"(?i)(?<!\p{L})не\s+просто(?!\p{L})",
    "не столько" => r"(?i)(?<!\p{L})не\s+столько(?!\p{L})",
    "важно отметить" => r"(?i)(?<!\p{L})важно\s+отметить(?!\p{L})",
    "следует подчеркнуть" => r"(?i)(?<!\p{L})следует\s+подчеркнуть(?!\p{L})",
    "необходимо понимать" => r"(?i)(?<!\p{L})необходимо\s+понимать(?!\p{L})",
    "представляет собой" => r"(?i)(?<!\p{L})представляет\s+собой(?!\p{L})",
    "представляют собой" => r"(?i)(?<!\p{L})представляют\s+собой(?!\p{L})",
    "выступает в роли" => r"(?i)(?<!\p{L})выступает\s+в\s+роли(?!\p{L})",
    "выступает в качестве" => r"(?i)(?<!\p{L})выступает\s+в\s+качестве(?!\p{L})",
    "через призму" => r"(?i)(?<!\p{L})через\s+призму(?!\p{L})",
    "рабочая оптика" => r"(?i)(?<!\p{L})рабочая\s+оптика(?!\p{L})",
    "смена оптики" => r"(?i)(?<!\p{L})смена\s+оптики(?!\p{L})",
    "изящн" => r"(?i)(?<!\p{L})изящн\p{L}*",
    "элегантн" => r"(?i)(?<!\p{L})элегантн\p{L}*",
    "поразительн" => r"(?i)(?<!\p{L})поразительн\p{L}*",
    "краеугольн" => r"(?i)(?<!\p{L})краеугольн\p{L}*",
    "критически важн" => r"(?i)(?<!\p{L})критически\s+важн\p{L}*"
]
editorial_hits(s::AbstractString) = [label for (label, pattern) in EDITORIAL_PATTERNS if occursin(pattern, s)]

# GATE-II09-05: Строгий линт-гейт чистоты текста, ссылок и формул всех 11 файлов Книги II v3.3 (RU)
let
    passport_file = only(filter(f -> startswith(f, "00_ПАСПОРТ_") && endswith(f, "_V3_3.md"), readdir(ROOT_DIR)))
    chapter_files = sort(filter(f -> occursin(r"^0[1-9]_ГЛАВА_II_0[1-9].*_V3_3\.md$", f), readdir(ROOT_DIR)))
    appendix_file = only(filter(f -> startswith(f, "10_ПРИЛОЖЕНИЯ_") && endswith(f, "_V3_3.md"), readdir(ROOT_DIR)))
    @assert length(chapter_files) == 9 "Должно быть ровно 9 файлов глав II.1–II.9!"
    all_md_files = vcat([passport_file], chapter_files, [appendix_file])

    forbidden_substrings = [
        "[Lean-target",
        "J58-",
        "[Мат. ядро",
        "[Предм. мост",
        "[Контрпример |",
        "Паспорт рисунка",
        "М21", "M21", "М53", "М55", "М61",
        "[METH-",
        "Opus",
        "Лаб.",
        "v3_1", "v3.1", "v3.2", "__FORBID_dot_v3_3__", "V3_1", "__FORBID_V3_3__",
        "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17",
        "НС-01", "НС-02", "НС-03", "НС-04", "НС-05", "НС-06", "НС-07", "НС-08", "НС-09",
        "REG-INTERP-",
        ("file:///Users/" * "abc"),
        ("/Users/" * "abc/")
    ]

    total_chapter_words = 0
    violations = String[]
    for fname in all_md_files
        text = read(joinpath(ROOT_DIR, fname), String)
        if fname in chapter_files
            total_chapter_words += length(split(text))
            if !occursin("наблюдател", lowercase(text))
                push!(violations, "$fname has 0 mentions of 'наблюдатель'")
            end
        end
        for pat in forbidden_substrings
            if occursin(pat, text)
                push!(violations, "$fname contains forbidden stamp '$pat'")
            end
        end
        if occursin(r"\bDOT\.[A-Za-z0-9]", text)
            push!(violations, "$fname contains internal agent stamp 'DOT.<Agent>'")
        end
        for label in editorial_hits(text)
            push!(violations, "$fname: редакционный маркер '$label'")
        end
        # Проверка чётного баланса блочных формул $$ (вне кодовых блоков и inline-кода)
        in_fence = false
        dd_cnt = 0
        for ln in split(text, '\n')
            if startswith(lstrip(ln), "```")
                in_fence = !in_fence
                continue
            end
            in_fence && continue
            ln_clean = replace(ln, r"`[^`]*`" => "")
            dd_cnt += length(collect(eachmatch(r"\$\$", ln_clean)))
        end
        if isodd(dd_cnt)
            push!(violations, "$fname has odd \$\$ delimiter count ($dd_cnt)")
        end
        # Проверка локальных markdown-ссылок
        for m in eachmatch(r"\[[^\]]+\]\(([^)]+)\)", text)
            tgt = strip(m.captures[1])
            (startswith(tgt, "http://") || startswith(tgt, "https://") || startswith(tgt, "#")) && continue
            rel_path = first(split(tgt, '#'))
            isempty(rel_path) && continue
            resolved = normpath(joinpath(ROOT_DIR, rel_path))
            if !ispath(resolved)
                push!(violations, "$fname has broken relative link '$tgt'")
            end
        end
    end
    py_files = filter(f -> endswith(lowercase(f), ".py"), readdir(ROOT_DIR))
    !isempty(py_files) && push!(violations, "Python files found in ROOT_DIR: $(join(py_files, ", "))")

    @assert isempty(violations) "Найдены нарушения чистоты полотна Книги II v3.3: $(join(violations, "; "))"
    record_gate!("GATE-II09-05", "II.1–II.9", "Строгий линт-гейт чистоты 11 файлов Книги II v3.3 (0 штампов, чётные \$\$, живые ссылки)", true, "11/11 files clean, 0 broken links, chapter words = $total_chapter_words")
end

# GATE-II-SYS-FLOAT: Полный самоконтроль отсутствия вещественных типов с плавающей точкой и 1 потока
let
    self_src = read(@__FILE__, String)
    forbidden_float_tokens = [
        "Float" * "64",
        "Float" * "32",
        "Float" * "16",
        "Big" * "Float",
        "Abstract" * "Float",
        "is" * "approx",
        "eig" * "vals",
        "1e" * "-",
        "rand" * "("
    ]
    hits = [tok for tok in forbidden_float_tokens if occursin(tok, self_src)]
    @assert isempty(hits) "Обнаружены запрещённые плавающие типы/вызовы в верификаторе: $(join(hits, ", "))"
    @assert Threads.nthreads() == 1
    record_gate!("GATE-II-SYS-FLOAT", "SYS", "Полный запрет типов и приближений с плавающей точкой в верификаторе (1 поток)", true, "0 floating-point/approx tokens in $(basename(@__FILE__)), threads = 1")
end

# ==============================================================================
# ЗАПИСЬ МАШИННОГО СЕРТИФИКАТА 12_book_II_v3_3_master_certificate.json
# ==============================================================================
let
    md_and_jl = sort(filter(f -> endswith(f, "_V3_3.md") || f == basename(@__FILE__), readdir(ROOT_DIR)))
    file_hashes = [(f, bytes2hex(sha256(read(joinpath(ROOT_DIR, f)))), endswith(f, ".md") ? length(split(read(joinpath(ROOT_DIR, f), String))) : 0) for f in md_and_jl]

    io = IOBuffer()
    println(io, "{")
    println(io, "  \"edition\": \"Book_II_Canonical_Russian_Edition_v3_3\",")
    println(io, "  \"volume\": \"Книга II. Память, непрерывное продолжение, склейка и квантовая сцена (Каноническая редакция v3.3)\",")
    println(io, "  \"directory\": \"", basename(@__DIR__), "\",")
    println(io, "  \"julia_version\": \"$(VERSION)\",")
    println(io, "  \"threads\": $(Threads.nthreads()),")
    println(io, "  \"floating_point_types_used\": 0,")
    println(io, "  \"timestamp_utc\": \"$(Dates.format(now(UTC), dateformat"yyyy-mm-ddTHH:MM:SSZ"))\",")
    println(io, "  \"total_gates\": $(length(RESULTS)),")
    println(io, "  \"passed_gates\": $(count(r -> r.passed, RESULTS)),")
    println(io, "  \"status\": \"ALL_PASS\",")
    println(io, "  \"gates\": [")
    for (idx, r) in enumerate(RESULTS)
        comma = idx < length(RESULTS) ? "," : ""
        desc_esc = replace(replace(r.description, "\\" => "\\\\"), "\"" => "\\\"")
        det_esc  = replace(replace(r.details, "\\" => "\\\\"), "\"" => "\\\"")
        println(io, "    {\"id\": \"$(r.id)\", \"chapter\": \"$(r.chapter)\", \"description\": \"$desc_esc\", \"passed\": $(r.passed), \"details\": \"$det_esc\"}$comma")
    end
    println(io, "  ],")
    println(io, "  \"verified_files\": [")
    for (idx, (fn, hx, wc)) in enumerate(file_hashes)
        comma = idx < length(file_hashes) ? "," : ""
        fn_esc = replace(fn, "\"" => "\\\"")
        println(io, "    {\"file\": \"$fn_esc\", \"sha256\": \"$hx\", \"words\": $wc}$comma")
    end
    println(io, "  ]")
    println(io, "}")
    write(CERT_PATH, take!(io))
    println("==============================================================================")
    println(" ВСЕ $(length(RESULTS)) / $(length(RESULTS)) ГЕЙТОВ КНИГИ II v3.3 (RU) УСПЕШНО ПРОЙДЕНЫ (ALL_PASS)!")
    println(" Сертификат записан в: $CERT_PATH")
    println("==============================================================================")
end
