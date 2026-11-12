include("02_ОБЩЕЕ.jl")
function anf111(v)
 a=copy(v);n=trailing_zeros(length(a))
 for b=0:n-1,m=0:length(a)-1
  (m>>b)&1==1&&(a[m+1]⊻=a[(m⊻(1<<b))+1])
 end
 mons=[m for m=0:length(a)-1 if a[m+1]!=0]
 Dict("monomials"=>mons,"degree"=>isempty(mons) ? -1 : maximum(count_ones.(mons)),"top_coefficient"=>Int(a[end]))
end
function pauli_int111(a,n)
 d=1<<n;x=a&(d-1);z=a>>n
 M=zeros(Complex{Int},d,d)
 for b=0:d-1;M[(b⊻x)+1,b+1]=im^count_ones(x&z)*(-1)^par111(z&b);end
 M
end
function K111(n;gauge=nothing)
 d=1<<n;N=d*d;K=0
 ff(a)=count_ones((a&(d-1))&(a>>n))
 for a=1:N-1,b=a+1:N-1
  x=a&(d-1);z=a>>n;X=b&(d-1);Z=b>>n
  isodd(count_ones(x&Z)+count_ones(z&X))&&continue
  phase=mod(ff(a)+ff(b)-ff(a⊻b)+2count_ones(z&X),4)
  if gauge!==nothing;phase=mod(phase+2*(gauge[a+1]⊻gauge[b+1]⊻gauge[(a⊻b)+1]),4);end
  K+=(phase==2)
 end
 K
end
function main()
 checks=Any[];put(n,ok,details=Dict())=(push!(checks,Dict("name"=>n,"passed"=>Bool(ok),"details"=>details));@assert ok)
 P=[pauli_int111(a,3) for a=0:63]
 put("Фаза — целочисленное число общих единиц",all(P[a+1]*P[b+1]==im^PH111[a+1,b+1]*P[(a⊻b)+1] for a=0:63,b=0:63))
 km=[]
 for n=1:6
  k=K111(n);f=((big(16)^n+big(4)^n)÷2-big(10)^n)÷4
  push!(km,Dict("n"=>n,"enumerated"=>k,"formula"=>Int(f)))
  put("K, n="*string(n),k==f)
 end
 e=sum(SIG111)%2;put("Чётность канонического фидуциала",e==1&&K111(3)==270)
 mc=Int[]
 for c=1:63
  neg=0;tot=0;nn=0
  for a=1:63
   a==c&&continue;b=a⊻c
   a<b&&sym111(a,c)==0||continue
   t=(-1)^(Int(SIG111[a+1]⊻SIG111[b+1])+PH111[a+1,b+1]÷2)
   tot+=t;neg+=t==-1;nn+=1
  end
  put("Тождество чистоты c="*string(c),nn==15&&tot==9*(-1)^SIG111[c+1])
  push!(mc,neg)
 end
 # Произвольное разрешённое эрмитово изменение знаков, затем тензорное.
 rg=zeros(UInt8,64);rg[2]=1
 kg=K111(3;gauge=rg);eg=sum(SIG111.⊻rg)%2
 put("Инвариантность равенства при смене сечения",eg==(1+kg)%2,Dict("K"=>kg,"negative_parity"=>eg))
 put("Буквальная нечётность не инвариантна при произвольном сечении",eg==0)
 rt=UInt8[(ax111(a)&1)!=0&&(az111(a)&1)!=0 for a=0:63]
 put("Локальная смена знака Y оставляет нечётность",sum(SIG111.⊻rt)%2==1)
 rf=UInt8[fld(F111[a+1],2)%2 for a=0:63]
 put("Соглашение с бинарным скалярным произведением",sum(SIG111.⊻rf)%2==(1+K111(3;gauge=rf))%2,
  Dict("K_mod2_dot"=>K111(3;gauge=rf),"changed_signs"=>sum(rf)))
 # CNOT: x_t←x_t+x_c, z_c←z_c+z_t.
 cols=UInt8[3,2,4,8,24,32];imS=linmap111(cols,6)
 C=zeros(Complex{Int},8,8)
 for x=0:7;y=x⊻((x&1)<<1);C[y+1,x+1]=1;end
 h=zeros(UInt8,64)
 for a=0:63
  B=C*P[a+1]*C'
  @assert B==P[imS[a+1]+1]||B==-P[imS[a+1]+1]
  h[a+1]=B==-P[imS[a+1]+1]
 end
 an=anf111(h)
 put("Фаза CNOT имеет кубический член",an["degree"]==3,an)
 put("Фаза CNOT не меняет старший коэффициент степени 6",sum(h)%2==0)
 gens_even=true
 for j=0:2
  hg=UInt8[((ax111(a)>>j)&1)&((az111(a)>>j)&1) for a=0:63]
  gens_even&=iseven(sum(hg))
 end
 put("Чётность фаз генераторов H/S/CNOT в трёх кубитах",gens_even&&iseven(sum(h)))
 fids=[]
 for sign in (-1,1)
  p=Complex{Int}[-1+sign*2im,1,1,1,1,1,1,1]
  vals=[real(dot(p,P[a+1]*p)) for a=1:63]
  put("Канонический фидуциал "*string(sign),all(abs.(vals).==4)&&dot(p,p)==12)
  fixed=0;allgl=0
  for a=1:7,b=1:7,c=1:7
   b==a&&continue;c in (a,b,a⊻b)&&continue
   imG=linmap111(UInt8[a,b,c],3);length(unique(imG))==8||continue
   allgl+=1;fixed+=all(p[imG[x+1]+1]==p[x+1] for x=0:7)
  end
  put("Вся GL3(2) фиксирует вектор "*string(sign),fixed==168&&allgl==168)
  push!(fids,Dict("sign"=>sign,"fixed_group_order"=>fixed))
 end
 # На плоскости CNOT-инвариантности B=0 даёт |000>, не SIC.
 put("Пропущенный проективный случай B=0 не даёт SIC",abs(dot(Complex{Int}[1,0,0,0,0,0,0,0],P[2]*Complex{Int}[1,0,0,0,0,0,0,0]))==0)
 # Контрпример к безусловной оценке остатка Ричардсона.
 L2=[1.,0.];L3=[1.01,0.];Ltrue=[0.,1.]
 put("Малый межразрядный прирост не ограничивает истинный остаток",L3[1]-2abs(L3[1]-L2[1])>L3[2]+2abs(L3[2]-L2[2])&&argmax(L3)!=argmax(Ltrue))
 save111("04_СЕРТИФИКАТ_ФАЗ_И_ФОРМУЛ.json",Dict("environment"=>env111(),"passed"=>count(c->c["passed"],checks),"checks"=>checks,"K"=>km,
 "minus_counts"=>sort(unique(mc)),"canonical_fiducials"=>fids,"parity_phase_note"=>"Инвариантно e≡1+K, но не e=1 при произвольной смене знаков эрмитовых представителей. Фаза CNOT кубическая, не только квадратичная."))
 println("Математические проверки: ",length(checks))
end
abspath(PROGRAM_FILE)==(@__FILE__)&&main()

