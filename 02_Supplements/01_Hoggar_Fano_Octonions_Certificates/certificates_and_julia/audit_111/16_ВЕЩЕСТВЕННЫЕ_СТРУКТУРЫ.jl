include("04_ФАЗЫ_И_ФОРМУЛЫ.jl")
function main16()
 P=[pauli_int111(a,3) for a=0:63];I8=Matrix{Complex{Int}}(I,8,8)
 realc=Int[];quaternionicc=Int[]
 for c=0:63
  sq=P[c+1]*conj(P[c+1]);@assert sq==(-1)^Q111[c+1]*I8
  push!(Q111[c+1]==0 ? realc : quaternionicc,c)
  for a=0:63
   qc=Q111[a+1]⊻sym111(c,a)
   @assert P[c+1]*conj(P[a+1])*P[c+1]==(-1)^qc*P[a+1]
  end
 end
 for a=0:63
  R=Q111[a+1]==0 ? P[a+1] : -im*P[a+1]
  @assert all(iszero,imag.(R))
  @assert transpose(R)==(-1)^Q111[a+1]*R
 end
 @assert length(realc)==36&&length(quaternionicc)==28
 save111("16_СЕРТИФИКАТ_ВЕЩЕСТВЕННЫХ_СТРУКТУР.json",Dict("environment"=>env111(),
 "real_structures"=>realc,"quaternionic_structures"=>quaternionicc,
 "conjugations_checked"=>4096,"transpose_checks"=>64,"all_exact"=>true,
 "scope"=>"Семейство J_c=P_c K, c∈F₂⁶, с точностью до общей фазы; не все возможные антиунитарные структуры на C⁸.",
 "formula"=>"J_c²=(-1)^Q0(c)I; J_c P_a J_c^(-1)=(-1)^(Q0(a)+ω(c,a))P_a.",
 "real_so8_note"=>"При Q0(a)=1 эрмитов P_a чисто мнимый. Вещественный кососимметричный представитель — -i P_a."))
 println("Точные антиунитарные структуры: 36 вещественных и 28 кватернионных")
end
abspath(PROGRAM_FILE)==(@__FILE__)&&main16()

