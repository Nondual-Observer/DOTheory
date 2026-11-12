# =============================================================================
# Исследование 41, Этап 4. Скрипт 10b: канонический фидуциал Хоггара
# ψ± = (−1 ± 2i, 1, 1, 1, 1, 1, 1, 1)/√12 — функция на F2^3: особое значение
# в точке 0 и 1 на семи точках Фано. Проверки: SIC; буквальная инвариантность
# относительно всех CNOT; совпадение с явным фидуциалом ψ′ Этапа 3 (T4) с точностью
# до сдвига Паули и фазы (или комплексного сопряжения).
# =============================================================================
using LinearAlgebra, Printf, JSON
const X1 = ComplexF64[0 1; 1 0]; const Z1 = ComplexF64[1 0; 0 -1]; const I1 = Matrix{ComplexF64}(I, 2, 2)
ax(a) = a & 7; az(a) = (a >> 3) & 7
pauli(a) = im^(count_ones(ax(a) & az(a)) % 4) * reduce(kron, [X1^((ax(a) >> (j - 1)) & 1) * Z1^((az(a) >> (j - 1)) & 1) for j in 1:3])
P = [pauli(a) for a in 0:63]
on(j, U) = reduce(kron, [k == j ? U : I1 for k in 1:3])
cnot(c, t) = (on(c, I1) + on(c, Z1)) / 2 + (on(c, I1) - on(c, Z1)) / 2 * on(t, X1)
c06 = JSON.parsefile(joinpath(@__DIR__, "06_СЕРТИФИКАТ_ХОГГАР_ФАНО_ЧЁТНОСТЬ.json"))["results"]["T4_levi_GL32"]["explicit_fiducial"]
ψp = ComplexF64.(c06["fiducial_real"]) .+ im .* ComplexF64.(c06["fiducial_imag"])
res = Pair{String,Any}[]
for (nm, z) in (("−1+2i", -1 + 2im), ("−1−2i", -1 - 2im), ("+1+2i (контроль)", 1 + 2im))
    ψ = ComplexF64[z, 1, 1, 1, 1, 1, 1, 1] / sqrt(12)
    E = [abs2(dot(ψ, P[a+1] * ψ)) for a in 1:63]
    sic = maximum(abs.(E .- 1 / 9)) < 1e-12
    cn = all(norm(cnot(c, t) * ψ - ψ) < 1e-12 for c in 1:3 for t in 1:3 if c != t)
    eq = maximum(abs(dot(P[b+1] * ψp, ψ)) for b in 0:63)
    eqc = maximum(abs(dot(P[b+1] * conj.(ψp), ψ)) for b in 0:63)
    @printf("  %-18s SIC: %s ; CNOT-инвариантен буквально: %s ; совпадение с ψ′ (Паули·фаза): %.12f ; с conj(ψ′): %.12f\n", nm, sic, cn, eq, eqc)
    push!(res, nm => Pair{String,Any}["sic"=>sic, "cnot_fixed"=>cn, "overlap_with_psi_prime"=>eq, "overlap_with_conj_psi_prime"=>eqc])
end
open(joinpath(@__DIR__, "10b_СЕРТИФИКАТ_КАНОНИЧЕСКОГО_ФИДУЦИАЛА.json"), "w") do f
    JSON.print(f, Dict("script" => basename(@__FILE__), "results" => Dict(res),
        "note" => "Канонический вид фидуциала Хоггара: ψ(0) = −1±2i, ψ(x) = 1 при x ≠ 0 (нормировка √12). По-видимому, известен в литературе (вероятный источник — Jedwab–Wiebe 2015, требуется сверка); поисковая сводка давала опечатку −1±i (не SIC, см. 10, F5)."), 2)
end
println("Сертификат: 10b_СЕРТИФИКАТ_КАНОНИЧЕСКОГО_ФИДУЦИАЛА.json")
