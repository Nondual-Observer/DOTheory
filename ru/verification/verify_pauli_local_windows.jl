using LinearAlgebra

# Четыре двоичных разряда адресуют операторы, не квантовые состояния.
# Мнимая единица ниже — комплексная в указанном матричном осуществлении.
checks = Ref(0)
function require(value, description)
    checks[] += 1
    value || error(description)
end
parity(x) = count_ones(x) % 2
symp(v,w) = parity(((v & 3) & ((w >> 2) & 3)) ⊻ (((v >> 2) & 3) & (w & 3)))
II = Complex{Int}[1 0; 0 1]
X = Complex{Int}[0 1; 1 0]
Z = Complex{Int}[1 0; 0 -1]
Y = Complex{Int}[0 -im; im 0]
single(x,z) = x == 0 ? (z == 0 ? II : Z) : (z == 0 ? X : Y)
pauli(v) = kron(single(v & 1,(v >> 2) & 1), single((v >> 1) & 1,(v >> 3) & 1))
P = Dict(v => pauli(v) for v in 0:15)
I4 = Matrix{Complex{Int}}(I,4,4)

for v in 0:15
    require(P[v] * P[v] == I4, "Операторы Паули инволютивны")
    for w in 0:15
        require(P[v]*P[w] == (-1)^symp(v,w)*P[w]*P[v], "Симплектический признак коммутатора")
        require(any(P[v]*P[w] == phase*P[xor(v,w)] for phase in (1,-1,im,-im)), "Нужна центральная фаза произведения")
    end
end

lines = Set{Tuple{Int,Int,Int}}()
for v in 1:15, w in (v+1):15
    push!(lines,Tuple(sort([v,w,xor(v,w)])))
end
require(length(lines) == 35, "PG(3,2) имеет35линий")
commuting = Set(l for l in lines if symp(l[1],l[2]) == 0)
require(length(commuting) == 15, "W(3,2) имеет15коммутирующихлиний")
for l in commuting
    product = P[l[1]]*P[l[2]]*P[l[3]]
    require(product == I4 || product == -I4, "Фаза контекста равна плюс или минус единице")
end

for p in 1:15
    V = [v for v in 0:15 if symp(v,p) == 0]
    A = [v for v in V if v != 0 && v != p]
    require(length(V) == 8 && length(A) == 6, "Местная восьмерка и шестёрка")
    rad = [v for v in V if all(symp(v,w) == 0 for w in V)]
    require(Set(rad) == Set([0,p]), "Отмеченный оператор —радикалместногоокна")
    local_lines = [l for l in lines if all(v in V for v in l)]
    require(length(local_lines) == 7, "Местное Фано")
    require(count(l -> p in l,local_lines) == 3, "Три линии через радикал")
    require(count(l -> symp(l[1],l[2]) == 0,local_lines) == 3, "Только три линии коммутируют")
    for v in A
        require(xor(v,p) in A, "Дополняющая пара")
        require(symp(v,xor(v,p)) == 0, "В паре операторы коммутируют")
        for w in A
            v == w && continue
            require((symp(v,w) == 0) == (w == xor(v,p)), "Шестёрка:коммутация3ребра,антикоммутацияоктаэдр")
        end
    end
end
println("Проверки завершены: ",checks[],"; 15 местных Q3/O6/F7, 35 XOR-линий, 15 коммутирующих контекстов.")
