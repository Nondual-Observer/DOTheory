include("02_ОБЩЕЕ.jl")
function main()
 g=deserialize(joinpath(D111,"data","03_ГРУППЫ.bin"));N=length(g.skeys)
 q0=foldl((m,a)->m|(UInt64(Q111[a+1])<<a),0:63;init=UInt64(0))
 qfrommap(i)=begin
  q=UInt64(0)
  for a=0:63;q|=UInt64(Q111[a+1])<<g.SM[a+1,i];end
  q
 end
 bypair=Dict{Int,UInt64}()
 for i=1:N
  e=Int(g.A[1,i]);p=min(e,e⊻129);q=qfrommap(i)
  haskey(bypair,p)&&@assert bypair[p]==q
  bypair[p]=q
 end
 @assert length(bypair)==36&&Set(values(bypair))==Set(g.plusm)
 uorbit=Set(Int(g.A[1,i]) for i in g.uni);aorbit=Set(Int(g.A[1,i]) for i in g.anti)
 @assert length(uorbit)==36&&length(aorbit)==36&&isempty(intersect(uorbit,aorbit))
 stU=[i for i in g.uni if qfrommap(i)==q0]
 stF=[i for i=1:N if qfrommap(i)==q0]
 @assert length(stU)==168&&length(stF)==336
 formact(q,i)=foldl((m,a)->m|(UInt64((q>>a)&1)<<g.SM[a+1,i]),0:63;init=UInt64(0))
 seen=Set{UInt64}();orbs=Int[]
 for q in g.plusm
  q in seen&&continue
  o=Set(formact(q,i) for i in stU);push!(orbs,length(o));union!(seen,o)
 end
 @assert sort(orbs)==[1,7,7,21]
 save111("09_СЕРТИФИКАТ_ФОРМ_И_ИДЕМПОТЕНТОВ.json",Dict("environment"=>env111(),"idempotent_pairs"=>length(bypair),
 "pairs_bijective_plus_forms"=>true,"unitary_orbits_on_idempotents"=>[length(uorbit),length(aorbit)],
 "Q0_unitary_stabilizer"=>length(stU),"Q0_full_stabilizer"=>length(stF),"suborbits_on_plus_forms"=>sort(orbs),
 "pairs"=>[Dict("e"=>p,"one_minus_e"=>p⊻129,"form"=>string(q)) for (p,q) in sort(collect(bypair))],
 "meaning"=>"Квадратичная норма на T0 не спускается на T0/<1>. Формы получаются выбором сечения U_e⊕V_e. Неупорядоченные пары {e,1+e} взаимно однозначно соответствуют 36 формам плюс-типа."))
 println("Пары идемпотентов и 36 форм проверены")
end
abspath(PROGRAM_FILE)==(@__FILE__)&&main()

