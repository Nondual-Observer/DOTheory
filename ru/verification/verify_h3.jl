# Самостоятельная точная проверка корневой редукции H3 и её связи с вопросами ТНР.
# Запуск: julia --startup-file=no verify_h3.jl
# Требуется только стандартная библиотека Julia; внешние пакеты и временные файлы не нужны.
# Поля: R=Z[φ], φ²=φ+1; k=F4=F2[t]/(t²+t+1).
# V=k³, радикал U=k(1,0,t); V/U=k², после ограничения скаляров — F2⁴.
# «Паули» означает только классы операторов по фазе; квантовые состояния здесь не задаются.
# Первичные источники:
# https://link.springer.com/article/10.1007/s00006-021-01139-2
# https://webbox.lafayette.edu/~gordong/pubs/Ico.pdf
# https://backoffice.biblio.ugent.be/download/3217947/3226884 (лемма 3.16)
# https://sigma-journal.com/2007/075/sigma07-075.pdf
# https://webspace.maths.qmul.ac.uk/l.h.soicher/partialspreads/PG42new.pdf
#
# Gold(a,b) означает a+bφ; F4-коды 0,1,2,3 означают 0,1,t,t².
# Код F4(2) — элемент t, а не вложение целого числа 2.

using LinearAlgebra

struct Gold <: Number
    a::Int
    b::Int
end
Gold(a::Integer)=Gold(Int(a),0)
Base.:+(x::Gold,y::Gold)=Gold(x.a+y.a,x.b+y.b)
Base.:-(x::Gold,y::Gold)=Gold(x.a-y.a,x.b-y.b)
Base.:-(x::Gold)=Gold(-x.a,-x.b)
Base.:*(x::Gold,y::Gold)=Gold(x.a*y.a+x.b*y.b,x.a*y.b+x.b*y.a+x.b*y.b)
Base.zero(::Type{Gold})=Gold(0)
Base.one(::Type{Gold})=Gold(1)
Base.iszero(x::Gold)=iszero(x.a)&&iszero(x.b)
Base.conj(x::Gold)=x
Base.convert(::Type{Gold},x::Integer)=Gold(x)
Base.promote_rule(::Type{Gold},::Type{T}) where {T<:Integer}=Gold
Base.show(io::IO,x::Gold)=print(io,"(",x.a,",",x.b,")")
Base.:(==)(x::Gold,y::Gold)=x.a==y.a&&x.b==y.b
Base.hash(x::Gold,h::UInt)=hash((x.a,x.b),h)

struct F4 <: Number
    a::UInt8
end
F4(a::Integer)=F4(UInt8(mod(a,4)))
Base.:+(x::F4,y::F4)=F4(xor(x.a,y.a))
Base.:-(x::F4,y::F4)=x+y
Base.:-(x::F4)=x
function Base.:*(x::F4,y::F4)
    a=x.a&1; b=(x.a>>1)&1; c=y.a&1; d=(y.a>>1)&1
    F4(xor(a*c,b*d) | (xor(xor(a*d,b*c),b*d)<<1))
end
Base.zero(::Type{F4})=F4(0)
Base.one(::Type{F4})=F4(1)
Base.iszero(x::F4)=x.a==0
Base.convert(::Type{F4},x::Integer)=F4(x)
Base.promote_rule(::Type{F4},::Type{T}) where {T<:Integer}=F4
Base.:(==)(x::F4,y::F4)=x.a==y.a
Base.hash(x::F4,h::UInt)=hash(x.a,h)
Base.show(io::IO,x::F4)=print(io,Int(x.a))
Base.inv(x::F4)=iszero(x) ? error("zero inverse") : x*x
Base.:/(x::F4,y::F4)=x*inv(y)
red(x::Gold)=F4(mod(x.a,2)+2mod(x.b,2))
key(x)=Tuple(vec(x))

function group(gens)
    n=size(first(gens),1)
    unit=Matrix{eltype(first(gens))}(I,n,n)
    result=[unit]; seen=Set([key(unit)]); i=1
    while i<=length(result)
        for g in gens
            h=g*result[i]; k=key(h)
            if !(k in seen)
                push!(seen,k); push!(result,h)
            end
        end
        i+=1
        length(result)>1000&&error("unexpected group size")
    end
    result
end
function reflections(G)
    n=size(G,1)
    gens=Matrix{eltype(G)}[]
    for i=1:n
        s=Matrix{eltype(G)}(I,n,n)
        for j=1:n
            s[i,j]-=G[i,j]
        end
        push!(gens,s)
    end
    gens
end
function proj(v)
    j=findfirst(!iszero,v)
    j===nothing&&error("zero projectivization")
    Tuple(v/v[j])
end
φ=Gold(0,1)
G=Gold[2 -φ 0; -φ 2 -1; 0 -1 2]
W=group(reflections(G))
Wr=group([red.(s) for s in reflections(G)])
roots=collect(Set(Tuple(g[:,i]) for g in W for i=1:3))
rootred=Set(Tuple(red.(collect(r))) for r in roots)
rp=Set(proj(collect(r)) for r in rootred)
P=Set(proj(F4[a,b,c]) for a=0:3 for b=0:3 for c=0:3 if a+b+c>0)
function q(v)
    x,y,z=v
    x*x+y*y+z*z+F4(2)*x*y+y*z
end
B=red.(G)
rad=Set(Tuple(F4[a,b,c]) for a=0:3 for b=0:3 for c=0:3 if all(iszero,B*F4[a,b,c]))
radp=Set(proj(collect(r)) for r in rad if any(!iszero,r))
conic=Set(p for p in P if iszero(q(p)))
u=F4[1,0,2]
lines=Set{Tuple}()
for p in P
    proj(collect(p))==proj(u)&&continue
    pts=Set([proj(u),p])
    for a=0:3
        push!(pts,proj(collect(p)+F4(a)*u))
    end
    push!(lines,Tuple(sort!(collect(pts),by=string)))
end
println("H3: матрица Грама = ",G)
println("H3: порядок полной группы = ",length(W),"; порядок образа = ",length(Wr))
println("H3: центральная инверсия входит в группу = ",-Matrix{Gold}(I,3,3) in W)
println("H3: размер ядра редукции = ",count(g->red.(g)==Matrix{F4}(I,3,3),W))
println("H3: корней = ",length(roots),"; различных редуцированных векторов = ",length(rootred),"; корневых проективных точек = ",length(rp))
println("H3: проективных точек = ",length(P),"; радикал = ",rad,"; q(u) = ",q(u))
println("H3: части не пересекаются = ",isempty(intersect(rp,conic))&&isempty(intersect(rp,radp))&&isempty(intersect(conic,radp)),"; покрывают плоскость = ",union(rp,conic,radp)==P)
println("H3: точек коники = ",length(conic),"; прямых через ядро = ",length(lines))
println("H3: состав прямых через ядро (корни, коника, ядро) = ",[(length(intersect(Set(l),rp)),length(intersect(Set(l),conic)),length(intersect(Set(l),radp))) for l in lines])

realroots=Dict{Tuple,Vector{Gold}}()
for r in roots
    realroots[proj(red.(collect(r)))]=collect(r)
end
orthchecks=Bool[]
for l in lines
    rr=collect(intersect(Set(l),rp))
    push!(orthchecks,all(iszero(dot(realroots[rr[i]],G*realroots[rr[j]])) for i=1:3 for j=i+1:3))
end
println("H3: тройки ортогональны над Z[φ] = ",all(orthchecks))
det3(M)=M[1,1]*(M[2,2]*M[3,3]-M[2,3]*M[3,2])-M[1,2]*(M[2,1]*M[3,3]-M[2,3]*M[3,1])+M[1,3]*(M[2,1]*M[3,2]-M[2,2]*M[3,1])
println("H3: определители ортогональных троек = ",[det3(hcat([realroots[r] for r in intersect(Set(l),rp)]...)) for l in lines])
orbits=Set{Tuple}()
for p in P
    push!(orbits,Tuple(sort!(collect(Set(proj(g*collect(p)) for g in Wr)),by=string)))
end
println("H3: размеры орбит = ",sort(length.(collect(orbits))))
println("H3: нормы редуцированных корней = ",Set(q(r) for r in rootred))
println("H3: точные скалярные произведения корней = ",sort!(collect(Set(dot(collect(r),G*collect(s)) for r in roots for s in roots)),by=x->(x.a,x.b)))

GA=[2 -1 0; -1 2 -1; 0 -1 2]
WA=group(reflections(GA))
WAr=Set(Tuple(mod.(vec(g),2)) for g in WA)
aroots=Set(Tuple(g[:,i]) for g in WA for i=1:3)
arootred=Set(Tuple(mod.(collect(r),2)) for r in aroots)
qA(x)=mod(sum(t*t for t in x)-x[1]*x[2]-x[2]*x[3],2)
Arad=[(a,b,c) for a=0:1 for b=0:1 for c=0:1 if all(iszero,mod.(GA*[a,b,c],2))]
println("A3: порядок группы = ",length(WA),"; порядок образа = ",length(WAr))
println("A3: корней = ",length(aroots),"; различных редуцированных векторов = ",length(arootred))
println("A3: радикал = ",Arad,"; q(1,0,1) = ",qA((1,0,1)))
println("A3: нормы редуцированных корней = ",Set(qA(r) for r in arootred))
println("A3: образ фиксирует ядро = ",all(mod.(g*[1,0,1],2)==[1,0,1] for g in WA))


f4str(a::F4)=a.a==0 ? "0" : a.a==1 ? "1" : a.a==2 ? "t" : "t²"
ptstr(p)="("*join(f4str.(p),",")*")"
lfun(l,p)=sum(l[i]*p[i] for i=1:3)
PL=sort!(collect(P),by=ptstr)
linepts=Dict(l=>Set(p for p in P if iszero(lfun(l,p))) for l in P)
H=union(conic,radp)
external=sort!([l for l in P if isempty(intersect(linepts[l],H))],by=ptstr)
secant=sort!([l for l in P if length(intersect(linepts[l],H))==2],by=ptstr)
dlines=[intersect(linepts[l],rp) for l in secant]
spread=[i for i=1:length(secant) if proj(u) in linepts[secant[i]]]
edges=Dict(p=>Tuple(i for i=1:6 if p in linepts[external[i]]) for p in rp)
println("ГЕОМЕТРИЯ: внешних прямых = ",length(external),"; секущих = ",length(secant),"; размеры троек обобщённого четырёхугольника = ",sort!(length.(dlines)))
println("ГЕОМЕТРИЯ: число внешних прямых через корневую точку = ",sort!(length.(collect(values(edges)))))
println("ГЕОМЕТРИЯ: 15 различных рёбер K6 = ",length(Set(values(edges)))==15)
println("ГЕОМЕТРИЯ: все тройки — совершенные паросочетания = ",all(sort!(collect(Iterators.flatten(edges[p] for p in L)))==collect(1:6) for L in dlines))
println("ГЕОМЕТРИЯ: аксиома обобщённого четырёхугольника = ",all(count(r->any(p in M && r in M for M in dlines),L)==1 for p in rp for L in dlines if !(p in L)))
println("ГЕОМЕТРИЯ: число троек через точку = ",sort!([count(L->p in L,dlines) for p in rp]))
println("ГЕОМЕТРИЯ: размер выделенного разбиения = ",length(spread),"; разбиение верно = ",union(dlines[spread]...)==rp && sum(length.(dlines[spread]))==15)

trace4(a)=a+a*a
normal(p)=q(p).*collect(p)
quot(p)=begin v=normal(p); (v[2],v[3]+F4(2)*v[1]) end
pair4(v,w)=v[1]*w[2]+v[2]*w[1]
pair2(p,r)=trace4(pair4(quot(p),quot(r)))
function paulibits(p)
    a,b=quot(p)
    a0=Int(a.a&1); a1=Int((a.a>>1)&1)
    b0=Int(b.a&1); b1=Int((b.a>>1)&1)
    (b1,a0,xor(b0,b1),a1)
end
function paulilabel(p)
    x1,z1,x2,z2=paulibits(p)
    symbols=Dict((0,0)=>"I",(1,0)=>"X",(0,1)=>"Z",(1,1)=>"Y")
    symbols[(x1,z1)]*symbols[(x2,z2)]
end
commbits(v,w)=mod(v[1]*w[2]+v[2]*w[1]+v[3]*w[4]+v[4]*w[3],2)
bitsxor(v,w)=Tuple(xor.(collect(v),collect(w)))
println("ПАУЛИ: биекция с ненулевыми векторами F4² = ",length(Set(quot(p) for p in rp))==15 && all(quot(p)!=(F4(0),F4(0)) for p in rp))
println("ПАУЛИ: биекция с ненулевыми векторами F2⁴ = ",length(Set(paulibits(p) for p in rp))==15)
println("ПАУЛИ: след формы совпадает с бинарной симплектической формой = ",all(Int(pair2(p,r).a)==commbits(paulibits(p),paulibits(r)) for p in rp for r in rp))
println("ПАУЛИ: коммутация равносильна принадлежности одной тройке = ",all((iszero(pair2(p,r))==any(p in L&&r in L for L in dlines)) for p in rp for r in rp if p!=r))
println("ПАУЛИ: сумма каждой тройки равна нулю = ",all(iszero(sum(normal(p)[2] for p in L))&&iszero(sum(normal(p)[3]+F4(2)*normal(p)[1] for p in L)) for L in dlines))

function combinations5(n)
    [(a,b,c,d,e) for a=1:n for b=a+1:n for c=b+1:n for d=c+1:n for e=d+1:n]
end
spreads=[s for s in combinations5(15) if union(dlines[collect(s)]...)==rp && sum(length.(dlines[collect(s)]))==15]
println("ГЕОМЕТРИЯ: всего разбиений на пять троек = ",length(spreads))

println("НОМЕРА ВНЕШНИХ ПРЯМЫХ")
for i=1:6
    println(i,": ",ptstr(external[i])," · x = 0")
end
println("КАРТА: корневая точка | нормированный образ (a,b) | ребро K6 | Паули")
for p in sort!(collect(rp),by=p->edges[p])
    println(ptstr(p)," | ",ptstr(quot(p))," | ",edges[p]," | ",paulilabel(p))
end
println("ТРОЙКИ: паросочетание | Паули | вещественный определитель | выделенное разбиение")
for i=1:15
    L=dlines[i]
    matching=sort!([edges[p] for p in L])
    labels=sort!([paulilabel(p) for p in L])
    detreal=det3(hcat([realroots[p] for p in L]...))
    println(matching," | ",labels," | ",detreal," | ",i in spread)
end

real_line5_checks=Bool[]
for l in external
    rr=collect(linepts[l])
    push!(real_line5_checks,all(iszero(det3(hcat(realroots[rr[i]],realroots[rr[j]],realroots[rr[k]]))) for i=1:5 for j=i+1:5 for k=j+1:5))
end
println("НАД R: все шесть внешних пятёрок копланарны = ",all(real_line5_checks))
println("НАД R: зависимых/независимых троек = ",count(L->iszero(det3(hcat([realroots[p] for p in L]...))),dlines)," / ",count(L->!iszero(det3(hcat([realroots[p] for p in L]...))),dlines))

edge_order=sort!(collect(values(edges)))
root_order=sort!(collect(rp),by=p->edges[p])
perms=Set(Tuple(findfirst(==(proj(g*collect(p))),root_order) for p in root_order) for g in Wr)
extperms=Set{Tuple}()
spreadperms=Set{Tuple}()
for g in Wr
    pmap=Dict(p=>proj(g*collect(p)) for p in rp)
    ep=Tuple(findfirst(j->Set(pmap[p] for p in linepts[external[i]])==linepts[external[j]],1:6) for i=1:6)
    push!(extperms,ep)
    sp=Tuple(findfirst(j->Set(pmap[p] for p in dlines[spread[i]])==dlines[spread[j]],1:5) for i=1:5)
    push!(spreadperms,sp)
end
println("ГРУППА: размеры образов на корнях / внешних прямых / выделенных тройках = ",length(perms)," / ",length(extperms)," / ",length(spreadperms))
println("ГРУППА: действие на шести внешних прямых транзитивно = ",length(Set(p[1] for p in extperms))==6)

function permutations(v)
    isempty(v)&&return [Int[]]
    [vcat(i,p) for i in v for p in permutations([j for j in v if j!=i])]
end
function edgeperm(e,p)
    Tuple(sort!([p[e[1]],p[e[2]]]))
end
matchings=[Set(edges[r] for r in L) for L in dlines]
spreadmatch=Set(Tuple(sort!(collect(matchings[i]))) for i in spread)
allspreadmatch=[Set(Tuple(sort!(collect(matchings[i]))) for i in s) for s in spreads]
all6perms=permutations(collect(1:6))
function matchingperm(M,p)
    Tuple(sort!([edgeperm(e,p) for e in M]))
end
function spreadperm(S,p)
    Set(matchingperm(M,p) for M in S)
end
spreadstab=[p for p in all6perms if spreadperm(spreadmatch,p)==spreadmatch]
ovoidstab=[p for p in all6perms if p[1]==1]
println("ГРУППА: порядки стабилизаторов разбиения/овоида в S6 = ",length(spreadstab)," / ",length(ovoidstab))
println("ГРУППА: стабилизатор разбиения транзитивен на шести номерах = ",length(Set(p[1] for p in spreadstab))==6)
println("ГРУППА: порядки пересечений стабилизаторов (два S5 / H3-A5 и S5 овоида) = ",count(p->p[1]==1,spreadstab)," / ",count(p->p[1]==1,extperms))
τ=[2,1,3,4,5,6]
spaction=Tuple(findfirst(==(spreadperm(S,τ)),allspreadmatch) for S in allspreadmatch)
println("ГРУППА: транспозиция вершин действует на шести разбиениях как = ",spaction,"; неподвижных разбиений = ",count(i->spaction[i]==i,1:6))

chosenovoid=linepts[external[1]]
ten=setdiff(rp,chosenovoid)
petersenedges=[setdiff(L,chosenovoid) for L in dlines]
println("ПЕТЕРСЕН: точек = ",length(ten),"; рёбер = ",length(petersenedges),"; все рёбра двухточечные = ",all(length.(petersenedges).==2))
println("ПЕТЕРСЕН: степени вершин = ",sort!([count(L->p in L,petersenedges) for p in ten]))
println("ПЕТЕРСЕН: соседство равно непересечению рёбер K5 = ",all((isempty(intersect(Set(edges[p]),Set(edges[r])))==any(p in L&&r in L for L in petersenedges)) for p in ten for r in ten if p!=r))
matching5=[setdiff(dlines[i],chosenovoid) for i in spread]
remainingpairs=[L for L in petersenedges if !(L in matching5)]
components=Set{Tuple}()
for p in ten
    reached=Set([p]); changed=true
    while changed
        old=length(reached)
        for e in remainingpairs
            !isempty(intersect(e,reached))&&union!(reached,e)
        end
        changed=length(reached)>old
    end
    push!(components,Tuple(sort!(collect(reached),by=ptstr)))
end
println("ПЕТЕРСЕН: выделенное разбиение даёт совершенное паросочетание = ",union(matching5...)==ten&&sum(length.(matching5))==10)
println("ПЕТЕРСЕН: удаление паросочетания оставляет компоненты размеров = ",sort!(length.(collect(components))))

u1=F4(2).*u
states=sort!([Tuple(F4[a,b,c]) for a=0:3 for b=0:3 for c=0:3 if lfun(F4[a,b,c],u1)==F4(1)],by=ptstr)
dualaction(l,g)=Tuple(sum(l[k]*g[k,j] for k=1:3) for j=1:3)
stateorbits=Set(Tuple(sort!(collect(Set(dualaction(l,g) for g in Wr)),by=ptstr)) for l in states)
U2=[(F4(a),F4(b)) for a=0:3 for b=0:3]
qref(l,w)=begin
    v=F4[0,w[1],w[2]]
    e=lfun(l,v)
    trace4(q(v)+e*e)
end
refinements=Set(Tuple(qref(l,w) for w in U2) for l in states)
zerocount(l)=count(w->iszero(qref(l,w)),U2)
zerosets=Dict(l=>Set(p for p in rp if iszero(qref(l,quot(p)))) for l in states)
onecount(l)=count(p->lfun(l,normal(p))==F4(1),rp)
println("СОСТОЯНИЯ: Q(u₁)=",q(u1),"; число состояний=",length(states),"; размеры орбит=",sort!(length.(collect(stateorbits))))
println("СОСТОЯНИЯ: различных бинарных квадратичных уточнений=",length(refinements),"; число нулей, включая 0=",sort!(zerocount.(states)))
println("СОСТОЯНИЯ: орбиты (размер, число нулей, ответы 1 на корневые вопросы, всего флагов)=",[(length(O),Set(zerocount(l) for l in O),Set(onecount(l) for l in O),sum(onecount(l) for l in O)) for O in stateorbits])
println("СОСТОЯНИЯ: нечётные уточнения дают шесть внешних овоидов=",Set(Tuple(sort!(collect(zerosets[l]),by=ptstr)) for l in states if zerocount(l)==6)==Set(Tuple(sort!(collect(linepts[l]),by=ptstr)) for l in external))
println("СОСТОЯНИЯ: число троек в каждой сетке чётного уточнения=",[count(L->issubset(L,zerosets[l]),dlines) for l in states if zerocount(l)==10])
questions=[Tuple(F4[a,b,c]) for a=0:3 for b=0:3 for c=0:3]
tables=Set(Tuple(lfun(l,v) for l in states) for v in questions)
println("ВОПРОСЫ: различных четырёхзначных аффинных таблиц=",length(tables),"; константных таблиц=",count(T->length(Set(T))==1,tables))
println("ВОПРОСЫ: каждый ответ неконстантного вопроса имеет четыре состояния=",all(all(count(==(F4(a)),T)==4 for a=0:3) for T in tables if length(Set(T))>1))
println("СОСТОЯНИЯ: неподвижного состояния нет=",all(length(Set(dualaction(l,g) for g in Wr))>1 for l in states))
println("СОСТОЯНИЯ: квадратичное уточнение корректно на факторе=",all(begin
    v=F4[a,b,c]; e=lfun(l,v); w=v+F4(d).*u1; f=lfun(l,w)
    trace4(q(v)+e*e)==trace4(q(w)+f*f)
end for l in states for a=0:3 for b=0:3 for c=0:3 for d=0:3))
println("СОСТОЯНИЯ: полярная форма уточнений равна следу формы=",all(qref(l,(w[1]+z[1],w[2]+z[2]))+qref(l,w)+qref(l,z)==trace4(pair4(w,z)) for l in states for w in U2 for z in U2))

ginverses=[first(h for h in Wr if g*h==Matrix{F4}(I,3,3)) for g in Wr]
flags=Set((p,l) for p in rp for l in states if lfun(l,normal(p))==F4(1))
flagorbits=Set{Tuple}()
for (p,l) in flags
    O=Set((proj(ginverses[i]*normal(p)),dualaction(l,Wr[i])) for i=1:length(Wr))
    push!(flagorbits,Tuple(sort!(collect(O),by=string)))
end
println("ФЛАГИ: число пар с ответом 1=",length(flags),"; размеры орбит=",sort!(length.(collect(flagorbits))),"; действие регулярно=",length(flagorbits)==1&&length(first(flagorbits))==length(Wr))
println("ЧУ: точный перенос оценки=",all(lfun(dualaction(l,g),v)==lfun(l,g*collect(v)) for l in states for v in questions for g in Wr))

# Фактор 60 флагов по корневой трансвекции: две пары над каждой из 15 осей.
# Вещественный оператор -s_α — поворот, фиксирующий α, а не отражение s_α.
transvections=Dict{Tuple,Matrix{F4}}()
for p in rp
    v=normal(p); bv=B*v
    transvections[p]=Matrix{F4}(I,3,3)+[v[i]*bv[j] for i=1:3,j=1:3]
end
foldflag(p,l)=(p,Tuple(sort!([l,dualaction(l,transvections[p])],by=string)))
folded=Set(foldflag(p,l) for (p,l) in flags)
foldaction(C,g,gi)=(proj(g*normal(C[1])),Tuple(sort!([dualaction(l,gi) for l in C[2]],by=string)))
foldedorbits=Set(Tuple(sort!(collect(Set(foldaction(C,Wr[i],ginverses[i]) for i=1:length(Wr))),by=string)) for C in folded)
rotations=[g for g in W if det3(g)==Gold(1)]
realbyred=Dict(key(red.(g))=>g for g in rotations)
realaxisrotations=Dict{Tuple,Matrix{Gold}}()
for p in rp
    α=realroots[p]; gα=G*α
    realaxisrotations[p]=-Matrix{Gold}(I,3,3)+[α[i]*gα[j] for i=1:3,j=1:3]
end

# Это свидетель существования, с явно выбранными начальным классом и знаком.
# Такой выбор не объявляется канонической геометрической биекцией.
basefold=first(sort!(collect(folded),by=string))
baseroot=realroots[basefold[1]]
fold_to_real=Dict{Tuple,Tuple}()
for i=1:length(Wr)
    C=foldaction(basefold,Wr[i],ginverses[i])
    α=Tuple(realbyred[key(Wr[i])]*baseroot)
    @assert !haskey(fold_to_real,C)||fold_to_real[C]==α
    fold_to_real[C]=α
end
@assert length(Set(key(T) for T in values(transvections)))==15
@assert all(T in Wr && T*T==Matrix{F4}(I,3,3) && T!=Matrix{F4}(I,3,3) for T in values(transvections))
@assert all(transvections[p]*normal(p)==normal(p) for p in rp)
@assert all(dualaction(l,transvections[p])!=l && lfun(dualaction(l,transvections[p]),normal(p))==F4(1) for (p,l) in flags)
@assert all(length(C[2])==2 for C in folded)
@assert length(folded)==30 && sort(length.(collect(foldedorbits)))==[30]
@assert all(transvections[proj(Wr[i]*normal(p))]==Wr[i]*transvections[p]*ginverses[i] for i=1:length(Wr) for p in rp)
@assert length(rotations)==60 && length(realbyred)==60
@assert all(realaxisrotations[p] in rotations && realaxisrotations[p]*realroots[p]==realroots[p] && red.(realaxisrotations[p])==transvections[p] for p in rp)
@assert all(count(g->g*realroots[p]==realroots[p],rotations)==2 for p in rp)
@assert length(fold_to_real)==30 && Set(values(fold_to_real))==Set(roots)
@assert all(proj(red.(collect(α)))==C[1] for (C,α) in fold_to_real)
@assert all(fold_to_real[foldaction(C,Wr[i],ginverses[i])]==Tuple(realbyred[key(Wr[i])]*collect(fold_to_real[C])) for C in folded for i=1:length(Wr))
println("ФАКТОР 60 → 30: 15 корневых трансвекций; 30 двухэлементных классов; одна орбита размера 30.")
println("Свидетель биекции с 30 вещественными корнями проверен; начальный класс и знак выбраны явно.")

# Обязательные проверки объявленных связей; любой сбой завершает запуск ошибкой.
@assert length(W)==120 && length(Wr)==60
@assert -Matrix{Gold}(I,3,3) in W
@assert count(g->red.(g)==Matrix{F4}(I,3,3),W)==2
@assert length(roots)==30 && length(rootred)==15 && length(rp)==15
@assert length(P)==21 && length(rad)==4 && length(radp)==1
@assert q(u)==F4(2) && q(u1)==F4(1)
@assert union(rp,conic,radp)==P
@assert isempty(intersect(rp,conic)) && isempty(intersect(rp,radp))
@assert length(conic)==5 && length(H)==6
@assert sort(length.(collect(orbits)))==[1,5,15]
@assert all(q(r)==F4(1) for r in rootred)
@assert all(g*u1==u1 for g in Wr)
@assert length(external)==6 && length(secant)==15
@assert all(length.(dlines).==3)
@assert all(length(e)==2 for e in values(edges))
@assert length(Set(values(edges)))==15
@assert all(sort!(collect(Iterators.flatten(edges[p] for p in L)))==collect(1:6) for L in dlines)
@assert all(count(L->p in L,dlines)==3 for p in rp)
@assert all(count(r->any(p in M && r in M for M in dlines),L)==1 for p in rp for L in dlines if !(p in L))
@assert length(spread)==5 && union(dlines[spread]...)==rp
@assert sum(length.(dlines[spread]))==15 && length(spreads)==6
@assert all(orthchecks) && all(real_line5_checks)
@assert count(L->iszero(det3(hcat([realroots[p] for p in L]...))),dlines)==10
@assert count(L->!iszero(det3(hcat([realroots[p] for p in L]...))),dlines)==5
@assert length(Set(quot(p) for p in rp))==15
@assert all(quot(p)!=(F4(0),F4(0)) for p in rp)
@assert length(Set(paulibits(p) for p in rp))==15
@assert all(Int(pair2(p,r).a)==commbits(paulibits(p),paulibits(r)) for p in rp for r in rp)
@assert all((iszero(pair2(p,r))==any(p in L && r in L for L in dlines)) for p in rp for r in rp if p!=r)
@assert all(iszero(sum(normal(p)[2] for p in L)) && iszero(sum(normal(p)[3]+F4(2)*normal(p)[1] for p in L)) for L in dlines)
@assert length(extperms)==60 && length(spreadperms)==60
@assert length(Set(p[1] for p in extperms))==6
@assert length(spreadstab)==120 && length(ovoidstab)==120
@assert length(Set(p[1] for p in spreadstab))==6
@assert count(p->p[1]==1,spreadstab)==20
@assert count(p->p[1]==1,extperms)==10
@assert count(i->spaction[i]==i,1:6)==0
@assert length(ten)==10 && length(petersenedges)==15
@assert all(length.(petersenedges).==2)
@assert all(count(L->p in L,petersenedges)==3 for p in ten)
@assert all((isempty(intersect(Set(edges[p]),Set(edges[r])))==any(p in L && r in L for L in petersenedges)) for p in ten for r in ten if p!=r)
@assert union(matching5...)==ten && sum(length.(matching5))==10
@assert sort(length.(collect(components)))==[5,5]
@assert length(states)==16 && sort(length.(collect(stateorbits)))==[6,10]
@assert length(refinements)==16
@assert sort(zerocount.(states))==vcat(fill(6,6),fill(10,10))
@assert all(length(Set(dualaction(l,g) for g in Wr))>1 for l in states)
@assert Set(Tuple(sort!(collect(zerosets[l]),by=ptstr)) for l in states if zerocount(l)==6)==Set(Tuple(sort!(collect(linepts[l]),by=ptstr)) for l in external)
@assert all(count(L->issubset(L,zerosets[l]),dlines)==6 for l in states if zerocount(l)==10)
@assert all(onecount(l)==(zerocount(l)==6 ? 0 : 6) for l in states)
@assert all(begin
    v=F4[a,b,c]; e=lfun(l,v); w=v+F4(d).*u1; f=lfun(l,w)
    trace4(q(v)+e*e)==trace4(q(w)+f*f)
end for l in states for a=0:3 for b=0:3 for c=0:3 for d=0:3)
@assert all(qref(l,(w[1]+z[1],w[2]+z[2]))+qref(l,w)+qref(l,z)==trace4(pair4(w,z)) for l in states for w in U2 for z in U2)
@assert length(tables)==64 && count(T->length(Set(T))==1,tables)==4
@assert all(all(count(==(F4(a)),T)==4 for a=0:3) for T in tables if length(Set(T))>1)
@assert length(flags)==60 && length(flagorbits)==1 && length(first(flagorbits))==60
@assert all(lfun(dualaction(l,g),v)==lfun(l,g*collect(v)) for l in states for v in questions for g in Wr)
@assert length(WA)==24 && length(WAr)==24 && length(aroots)==12 && length(arootred)==6
@assert Arad==[(0,0,0),(1,0,1)] && qA((1,0,1))==0
println("ИТОГ: все обязательные проверки пройдены.")
println("H3: 120 → 60; PG(2,4)=1+5+15; GQ(2,2): 15 точек и 15 троек.")
println("V/U: F4² → F2⁴; 15 классов Паули; выделенное разбиение на пять троек.")
println("ТНР: 16 аффинных состояний, орбиты 6+10; 64 четырёхзначных вопроса.")
println("16 квадратичных уточнений: 6 овоидов и 10 сеток; 60 флагов ответа 1 — регулярная орбита.")
println("Фактор по соответствующей корневой трансвекции даёт 30 классов; их связь с вещественными корнями требует выбора знака.")
println("Предупреждение: пять ортогональных вещественных троек становятся зависимыми после редукции.")
