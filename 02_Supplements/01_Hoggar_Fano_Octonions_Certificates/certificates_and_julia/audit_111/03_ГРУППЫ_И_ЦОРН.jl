include("02_ОБЩЕЕ.jl")
function main()
 t0=time();MT=[zmul111(x,y) for x=0:255,y=0:255]
 @assert all(MT[130,x+1]==x&&MT[x+1,130]==x for x=0:255)
 @assert all(znorm111(MT[x+1,y+1])==(znorm111(x)&znorm111(y)) for x=0:255,y=0:255)
 @assert all(MT[MT[x+1,x+1]+1,y+1]==MT[x+1,MT[x+1,y+1]+1]&&MT[MT[y+1,x+1]+1,x+1]==MT[y+1,MT[x+1,x+1]+1] for x=0:255,y=0:255)
 nonassoc=count(MT[MT[x+1,y+1]+1,z+1]!=MT[x+1,MT[y+1,z+1]+1] for x=0:255,y=0:255,z=0:255)
 idem=[e for e=0:255 if ztrace111(e)==1&&MT[e+1,e+1]==e]
 autos=Vector{Vector{UInt8}}();keys=UInt64[];frames=Int[]
 for e in idem
  U=[x for x=0:255 if MT[e+1,x+1]==x&&MT[x+1,e+1]==0]
  @assert length(U)==8
  cnt=0
  for u1 in U,u2 in U,u3 in U
   u1==0&&continue
   u2 in (0,u1)&&continue
   u3 in (0,u1,u2,u1⊻u2)&&continue
   v1=MT[u2+1,u3+1];v2=MT[u3+1,u1+1];v3=MT[u1+1,u2+1]
   cols=UInt8[e,u1,u2,u3,v1,v2,v3,e⊻129];fm=linmap111(cols,8)
   @assert length(unique(fm))==256
   @assert all(fm[MT[(1<<i)+1,(1<<j)+1]+1]==MT[cols[i+1]+1,cols[j+1]+1] for i=0:7,j=0:7)
   @assert all(ztrace111(fm[x+1])==ztrace111(x)&&znorm111(fm[x+1])==znorm111(x) for x=0:255)
   push!(autos,cols);push!(keys,pack111(cols,8));cnt+=1
  end
  push!(frames,cnt)
 end
 @assert length(unique(keys))==length(keys)
 N=length(autos);A=reduce(hcat,autos);FM=reduce(hcat,[linmap111(c,8) for c in autos])
 S=zeros(UInt8,6,N)
 for j=1:N,i=1:6
  v=A[i+1,j];@assert ztrace111(v)==0
  S[i,j]=(v>>1)&63
 end
 SM=reduce(hcat,[linmap111(view(S,:,j),6) for j=1:N])
 skeys=[pack111(view(S,:,j),6) for j=1:N];@assert length(unique(skeys))==N
 idx=Dict(k=>i for (i,k) in enumerate(skeys))
 @assert all(sym111(Int(S[i,j]),Int(S[k,j]))==sym111(1<<(i-1),1<<(k-1)) for i=1:6,k=1:6,j=1:N)
 println("Цорн: идемпотентов ",length(idem),"; базисов на идемпотент ",unique(frames),"; автоморфизмов ",N);flush(stdout)
 # Все симплектические базисы, а не только найденные автоморфизмы.
 cols=zeros(UInt8,6);img=zeros(UInt8,64);hh=zeros(UInt8,64);ll=zeros(UInt8,64)
 spcount=Ref(0);hogkeys=UInt64[];hogtype=UInt8[]
 function visit(level,allowed)
  if level==4
   spcount[]+=1;ty=symmetry111(cols,img,hh,ll)
   if ty!=0;push!(hogkeys,pack111(cols,6));push!(hogtype,ty);end
   return
  end
  for x in allowed,z in allowed
   sym111(x,z)==1||continue
   cols[level]=x;cols[level+3]=z
   nxt=[v for v in allowed if sym111(v,x)==0&&sym111(v,z)==0]
   visit(level+1,nxt)
  end
 end
 visit(1,collect(1:63))
 @assert Set(hogkeys)==Set(skeys)
 typ=zeros(UInt8,N)
 for (k,v) in zip(hogkeys,hogtype);typ[idx[k]]=v;end
 uni=findall(==(1),typ);anti=findall(==(2),typ)
 println("Sp: ",spcount[],"; Хоггар: ",length(uni),"+",length(anti),"; множества совпали");flush(stdout)
 idkey=pack111(UInt8[1,2,4,8,16,32],6);id=idx[idkey]
 @inline function comp(i,j)
  k=UInt64(0)
  @inbounds for a=1:6;k|=UInt64(SM[S[a,j]+1,i])<<(6(a-1));end
  get(idx,k,0)
 end
 # 146 313 216 пар; также восемь координат подъёма и гомоморфизм индекса 2.
 for j=1:N,i=1:N
  k=comp(i,j);@assert k!=0
  @assert (typ[k]-1)==((typ[i]-1)⊻(typ[j]-1))
  @inbounds for a=1:8;@assert FM[A[a,j]+1,i]==A[a,k];end
 end
 ord=zeros(Int,N);inv=zeros(Int,N)
 for i=1:N
  k=id;pr=id;o=0
  while true
   pr=k;k=comp(k,i);o+=1
   k==id&&break
   @assert o<=N
  end
  ord[i]=o;inv[i]=pr
 end
 function generated(gs;limit=N)
  seen=falses(N);seen[id]=true;queue=[id];head=1
  while head<=length(queue)
   i=queue[head];head+=1
   for g in gs
    j=comp(g,i);@assert j>0
    if !seen[j];seen[j]=true;push!(queue,j);end
   end
  end
  findall(seen)
 end
 function generators(target)
  gs=Int[];seen=Set([id])
  for i in target
   i in seen&&continue
   push!(gs,i);seen=Set(generated(gs))
   length(seen)==length(target)&&break
  end
  @assert seen==Set(target)
  gs
 end
 gu=generators(uni);gf=generators(collect(1:N))
 center=[i for i=1:N if all(comp(i,g)==comp(g,i) for g in gf)]
 centralU=[i for i=1:N if all(comp(i,g)==comp(g,i) for g in gu)]
 invol=findfirst(i->typ[i]==2&&ord[i]==2,1:N);@assert invol!==nothing
 # Нормальные замыкания представителей классов внутри унитарной части.
 assigned=falses(N);classes=Vector{Vector{Int}}()
 for i in uni
  assigned[i]&&continue
  c=Set([i]);queue=[i];head=1
  while head<=length(queue)
   a=queue[head];head+=1
   for g in gu
    z=comp(comp(g,a),inv[g])
    if !(z in c);push!(c,z);push!(queue,z);end
   end
  end
  for a in c;assigned[a]=true;end
  push!(classes,sort(collect(c)))
 end
 normals=Int[]
 for c in classes
  id in c&&continue
  gs=Int[];seen=Set([id])
  for a in c
   a in seen&&continue
   push!(gs,a);seen=Set(generated(gs))
   length(seen)==length(uni)&&break
  end
  push!(normals,length(seen))
 end
 @assert all(==(length(uni)),normals)
 comms=unique([comp(comp(comp(inv[g],inv[h]),g),h) for g in gf for h in gf])
 normal=Set(comms);queue=copy(comms);head=1
 while head<=length(queue)
  a=queue[head];head+=1
  for g in gf
   z=comp(comp(g,a),inv[g])
   if !(z in normal);push!(normal,z);push!(queue,z);end
  end
 end
 derived=generated(collect(normal));@assert Set(derived)==Set(uni)
 println("Все пары, подъёмы, расширение и простота проверены");flush(stdout)
 # Все 135 лагранжевых, все дополнительные пары, все формы.
 masks=Set{UInt64}()
 for a=1:63,b=a+1:63,c=b+1:63
  sym111(a,b)==0&&sym111(a,c)==0&&sym111(b,c)==0||continue
  span=unique([0,a,b,c,a⊻b,a⊻c,b⊻c,a⊻b⊻c]);length(span)==8||continue
  push!(masks,foldl((m,v)->m|(UInt64(1)<<v),span;init=UInt64(0)))
 end
 lag=sort(collect(masks));members=[findall(v->(m>>v)&1==1,0:63).-1 for m in lag]
 keeps=falses(length(lag),length(uni))
 for l in eachindex(lag),j in eachindex(uni)
  i=uni[j];keeps[l,j]=all(((lag[l]>>SM[a+1,i])&1)==1 for a in members[l])
 end
 ps=Any[];qsets=UInt64[];subs=Vector{Vector{Int}}();complementary=0
 for i=1:length(lag),j=i+1:length(lag)
  lag[i]&lag[j]==1||continue;complementary+=1
  sub=[uni[k] for k in eachindex(uni) if keeps[i,k]&&keeps[j,k]]
  length(sub)==168||continue
  restr=Set(Tuple(SM[a+1,k] for a in members[i]) for k in sub);@assert length(restr)==168
  q=zeros(UInt8,64)
  for a in members[i],b in members[j];q[(a⊻b)+1]=sym111(a,b);end
  @assert count(==(0),q)==36
  qm=foldl((m,a)->m|(UInt64(q[a+1])<<a),0:63;init=UInt64(0))
  push!(qsets,qm);push!(subs,sub)
  push!(ps,Dict("lagrangian_1"=>string(lag[i]),"lagrangian_2"=>string(lag[j]),"form"=>string(qm),"stabilizer_order"=>length(sub)))
 end
 allforms=[UInt8[Q111[a+1]⊻sym111(c,a) for a=0:63] for c=0:63]
 plus=[q for q in allforms if count(==(0),q)==36]
 plusm=[foldl((m,a)->m|(UInt64(q[a+1])<<a),0:63;init=UInt64(0)) for q in plus]
 @assert Set(qsets)==Set(plusm)&&length(unique(qsets))==length(ps)
 @assert length(Set(Tuple(s) for s in subs))==length(ps)
 q0stab=[i for i in uni if all(Q111[SM[a+1,i]+1]==Q111[a+1] for a=0:63)]
 lx=Set(0:7);lz=Set(0:8:56)
 stdlevi=[i for i in uni if all(Int(SM[a+1,i]) in lx for a in lx)&&all(Int(SM[a+1,i]) in lz for a in lz)]
 @assert Set(q0stab)==Set(stdlevi)&&length(q0stab)==168
 for (qm,sub) in zip(qsets,subs)
  st=[i for i in uni if all(((qm>>SM[a+1,i])&1)==((qm>>a)&1) for a=0:63)]
  @assert st==sub
 end
 orbits=Int[];stabs=Int[]
 for q in allforms
  orb=Set(Tuple(q[SM[a+1,i]+1] for a=0:63) for i in uni)
  push!(orbits,length(orb));push!(stabs,count(i->all(q[SM[a+1,i]+1]==q[a+1] for a=0:63),uni))
 end
 # Норма не спускается как квадратичная форма на фактор T0/<1>.
 normcounter=[0,129,znorm111(0),znorm111(129)]
 cert=Dict("environment"=>env111(),"elapsed_s"=>time()-t0,"idempotents"=>length(idem),"bases_per_idempotent"=>unique(frames),
 "aut_order"=>N,"all_basis_products_checked"=>N*64,"norm_and_trace_preserved"=>true,"nonassociative_triples"=>nonassoc,
 "Sp_order"=>spcount[],"unitary_order"=>length(uni),"antiunitary_order"=>length(anti),"aut_equals_hoggar_image"=>true,
 "all_group_pairs_checked"=>N*N,"all_lift_compositions_checked"=>N*N,"lift_unique"=>true,"index2_homomorphism"=>true,
 "antiunitary_involution_index"=>invol,"center_order"=>length(center),"centralizer_unitary_order"=>length(centralU),
 "commutator_order"=>length(derived),"conjugacy_order_size"=>[collect(p) for p in sort([(ord[c[1]],length(c)) for c in classes])],
 "normal_closure_orders"=>normals,"unitary_simple"=>true,"generators_unitary"=>gu,"generators_full"=>gf,
 "lagrangians"=>length(lag),"complementary_unordered_pairs"=>complementary,"levi_pairs"=>ps,
 "levi_subgroups"=>length(subs),"plus_forms"=>length(plus),"bijection"=>true,"Q0_stabilizer_order"=>length(q0stab),
 "Q0_stabilizer_equals_standard_Levi"=>true,"form_orbit_sizes"=>sort(unique(orbits)),"form_stabilizer_orders"=>sort(unique(stabs)),
 "norm_does_not_descend_counterexample"=>normcounter,
 "completeness"=>"Любой автоморфизм переводит e в идемпотент следа 1 и базис U_e в базис U_f. Образы V вынуждены попарными произведениями U. Перебраны все идемпотенты и все упорядоченные базисы U; каждый линейный кандидат проверен на 64 произведениях базиса.")
 save111("03_СЕРТИФИКАТ_ГРУПП_И_ЦОРНА.json",cert)
 serialize(joinpath(D111,"data","03_ГРУППЫ.bin"),(;A,S,FM,SM,skeys,typ,uni,anti,ord,inv,gu,gf,subs,plusm))
 println("Готово: ",time()-t0," с");flush(stdout)
end
abspath(PROGRAM_FILE)==(@__FILE__)&&main()

