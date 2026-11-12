include("02_ОБЩЕЕ.jl")
function main()
 z=deserialize(joinpath(D111,"data","03_ГРУППЫ.bin"));N=length(z.skeys)
 idx=Dict(k=>i for (i,k) in enumerate(z.skeys));id=idx[pack111(UInt8[1,2,4,8,16,32],6)]
 function mul(i,j)
  k=UInt64(0)
  for a=1:6;k|=UInt64(z.SM[z.S[a,j]+1,i])<<(6(a-1));end
  idx[k]
 end
 pow(a,n)=foldl((x,_)->mul(x,a),1:n;init=id)
 com(a,b)=mul(mul(mul(z.inv[a],z.inv[b]),a),b)
 function gen(a,b)
  seen=falses(N);seen[id]=true;queue=[id];h=1
  while h<=length(queue)
   x=queue[h];h+=1
   for g in (a,b)
    y=mul(x,g)
    if !seen[y];seen[y]=true;push!(queue,y);end
   end
  end
  sum(seen)
 end
 a=first(i for i in z.uni if z.ord[i]==2);abfound=nothing
 for b in z.uni
  z.ord[b]==6&&z.ord[mul(a,b)]==7||continue
  com(a,pow(mul(a,pow(b,2)),3))==id||continue
  mul(pow(b,3),pow(com(pow(b,2),mul(mul(a,pow(b,3)),a)),2))==id||continue
  gen(a,b)==6048||continue;abfound=(a,b);break
 end
 @assert abfound!==nothing
 c=first(i for i in z.anti if z.ord[i]==2);cdfound=nothing
 for dd=1:N
  z.ord[dd]==4&&z.ord[mul(c,dd)]==7||continue
  pow(com(c,dd),6)==id||continue
  pow(mul(mul(c,dd),pow(mul(c,pow(dd,2)),3)),2)==id||continue
  pow(com(pow(dd,2),mul(mul(c,dd),c)),3)==id||continue
  gen(c,dd)==12096||continue;cdfound=(c,dd);break
 end
 @assert cdfound!==nothing
 save111("15_СЕРТИФИКАТ_ПРЕДСТАВЛЕНИЙ_ATLAS.json",Dict("environment"=>env111(),
 "unitary_generators"=>collect(abfound),"full_generators"=>collect(cdfound),
 "unitary_matrices"=>[Int.(z.S[:,i]) for i in abfound],
 "full_matrices"=>[Int.(z.S[:,i]) for i in cdfound],
 "unitary_generated_order"=>gen(abfound...),"full_generated_order"=>gen(cdfound...),
 "all_relators_identity"=>true,"source"=>"https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/U33/",
 "meaning"=>"Пары порождают независимо перечисленные группы и удовлетворяют полным определяющим соотношениям ATLAS. Название группы сверено с ATLAS; порядок алгебры Цорна получен независимо от него."))
 println("Определяющие соотношения и порождение: 6048 и 12096 подтверждены")
end
abspath(PROGRAM_FILE)==(@__FILE__)&&main()

