using LinearAlgebra,Statistics,Random,JSON,SHA,Dates,Serialization,Printf
BLAS.set_num_threads(1)
const D111=@__DIR__
env111()=Dict("utc"=>string(now(UTC))*"Z","julia"=>string(VERSION),"cpu_threads"=>Threads.nthreads(),"blas_threads"=>BLAS.get_num_threads(),"gpu_bytes"=>0)
save111(f,x)=open(io->JSON.print(io,x,2),joinpath(D111,f),"w")
sha111(p)=open(io->bytes2hex(sha256(io)),p)
par111(x)=count_ones(x)&1
ax111(a)=a&7;az111(a)=(a>>3)&7
sym111(a,b)=par111((ax111(a)&az111(b))⊻(az111(a)&ax111(b)))
f111(a)=count_ones(ax111(a)&az111(a))
phase111(a,b)=mod(f111(a)+f111(b)-f111(a⊻b)+2count_ones(az111(a)&ax111(b)),4)
function linmap111(cols,n)
 out=zeros(UInt8,1<<n)
 for a=1:(1<<n)-1
  k=trailing_zeros(a);out[a+1]=out[(a⊻(1<<k))+1]⊻cols[k+1]
 end
 out
end
pack111(cols,shift)=foldl((k,p)->k|(UInt64(p[2])<<(shift*(p[1]-1))),enumerate(cols);init=UInt64(0))
unpack111(k,n,shift)=UInt8[(k>>(shift*i))&((1<<shift)-1) for i=0:n-1]
dot3111(x,y)=par111(x&y)
function cross3111(x,y)
 a=((x>>1)&1)*((y>>2)&1)⊻((x>>2)&1)*((y>>1)&1)
 b=((x>>2)&1)*(y&1)⊻(x&1)*((y>>2)&1)
 c=(x&1)*((y>>1)&1)⊻((x>>1)&1)*(y&1)
 a|(b<<1)|(c<<2)
end
function zmul111(x,y)
 a=x&1;b=(x>>7)&1;v=(x>>1)&7;w=(x>>4)&7
 A=y&1;B=(y>>7)&1;V=(y>>1)&7;W=(y>>4)&7
 aa=(a&A)⊻dot3111(v,W)
 vv=(a==1 ? V : 0)⊻(B==1 ? v : 0)⊻cross3111(w,W)
 ww=(A==1 ? w : 0)⊻(b==1 ? W : 0)⊻cross3111(v,V)
 bb=(b&B)⊻dot3111(w,V)
 UInt8(aa|(vv<<1)|(ww<<4)|(bb<<7))
end
znorm111(x)=((x&1)&((x>>7)&1))⊻dot3111((x>>1)&7,(x>>4)&7)
ztrace111(x)=(x&1)⊻((x>>7)&1)
const ONE111=UInt8(129)
function canonical_sign111()
 p=Complex{Int}[-1+2im,1,1,1,1,1,1,1]
 out=zeros(UInt8,64);ev=zeros(Int,64)
 for a=0:63
  z=sum(conj(p[(x⊻ax111(a))+1])*(im^f111(a))*((-1)^par111(az111(a)&x))*p[x+1] for x=0:7)
  @assert imag(z)==0
  ev[a+1]=Int(real(z));out[a+1]=real(z)<0
 end
 @assert ev[1]==12&&all(abs.(ev[2:end]).==4)
 out,ev
end
const SIG111,EV111=canonical_sign111()
const PH111=[phase111(a,b) for a=0:63,b=0:63]
const F111=[f111(a) for a=0:63]
const Q111=UInt8[par111(ax111(a)&az111(a)) for a=0:63]
function symmetry111(cols,img=zeros(UInt8,64),hh=zeros(UInt8,64),ll=zeros(UInt8,64))
 u=true;k=true
 for a=1:63
  b=63-leading_zeros(UInt64(a));bit=1<<b;lo=a⊻bit
  imlo=Int(img[lo+1]);imbit=Int(cols[b+1]);imall=imlo⊻imbit
  img[a+1]=imall
  hv=mod(Int(hh[lo+1])+PH111[imlo+1,imbit+1]+F111[a+1]-F111[lo+1],4)
  @assert iseven(hv)
  hh[a+1]=hv
  dv=SIG111[imall+1]⊻SIG111[a+1]⊻UInt8(hv÷2)
  ll[a+1]=lo==0 ? dv : ll[lo+1]⊻ll[bit+1]
  u&=(dv==ll[a+1]);k&=((dv⊻Q111[a+1])==ll[a+1])
  !u&&!k&&return UInt8(0)
 end
 UInt8(u ? 1 : k ? 2 : 0)
end

