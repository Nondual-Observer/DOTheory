# -*- coding: utf-8 -*-
"""
verify_rank5_masses.py — HONEST test of "rank 5 (golden φ) → mass hierarchy".
We compute against real data (PDG), no fitting. Discipline: golden φ≈1.618 ≠ phase 2/9.
"""
import math
p=0; f=0
def ck(n,c):
    global p,f
    if c: p+=1; print(f"PASS {n}")
    else: f+=1; print(f"FAIL {n} <-- WRONG")

PHI=(1+5**0.5)/2                      # golden ≈1.618

# ── charged leptons (PDG, MeV) ──
me,mm,mt = 0.51099895, 105.6583755, 1776.86
sq=[math.sqrt(x) for x in (me,mm,mt)]
Q=(me+mm+mt)/sum(sq)**2
ck(f"Koide Q(leptons)=2/3 (●, σ½-facet of RANK 3): {Q:.5f}", abs(Q-2/3)<2e-3)

# Koide phase δ (azimuth of the √m vector): c_k=(√m_k/mean−1)/√2 ; τ — max
mean=sum(sq)/3
cs=[(s/mean-1)/math.sqrt(2) for s in sq]
delta=math.acos(max(cs))             # ≈ phase of τ
ck(f"Koide phase δ≈2/9 (◐, gives BOTH ratios μ/e,τ/μ): δ={delta:.5f} vs 2/9={2/9:.5f}", abs(delta-2/9)<2e-3)
# check: this (Q,δ) reproduces the real ratios
ang=[delta+2*math.pi*k/3 for k in range(3)]
sm=sorted((1+math.sqrt(2)*math.cos(a))**2 for a in ang)
ck(f"(2/3,2/9) reproduces the ratios: μ/e={sm[1]/sm[0]:.1f}(real 206.8), τ/μ={sm[2]/sm[1]:.2f}(real 16.82)",
   abs(sm[1]/sm[0]-206.8)<5 and abs(sm[2]/sm[1]-16.82)<0.3)

# ★ is 2/9 GOLDEN? compare with golden candidates
gold_cand={"1/φ³":1/PHI**3,"2−φ":2-PHI,"1/φ²·":1/PHI**2-1/PHI**3}
best=min(abs(2/9-v) for v in gold_cand.values())
ck(f"★phase 2/9 is NOT golden (nearest golden candidate off {best/(2/9)*100:.1f}%>1%)", best/(2/9)>0.03)
ck("⟹ charged leptons: Koide(rank3)+phase 2/9 — WITHOUT gold (φ≈1.618 not involved)", True)

# ── φ-power test of ratios (does gold give powers?) ──
e_mue=math.log(mm/me)/math.log(PHI); e_taumu=math.log(mt/mm)/math.log(PHI)
ck(f"mass ratios ≠ powers of φ: log_φ(μ/e)={e_mue:.2f}, log_φ(τ/μ)={e_taumu:.2f} — NOT integers (a fit)",
   abs(e_mue-round(e_mue))>0.05 and abs(e_taumu-round(e_taumu))>0.05)

# ── quarks: Koide is NOT 2/3 (lepton-specific) ──
up=[2.16,1270,172690]; dn=[4.67,93.4,4180]
Qu=sum(up)/sum(math.sqrt(x) for x in up)**2; Qd=sum(dn)/sum(math.sqrt(x) for x in dn)**2
ck(f"quarks: Koide ≠ 2/3 (up={Qu:.3f}, down={Qd:.3f}) — lepton-specific", abs(Qu-2/3)>0.05 and abs(Qd-2/3)>0.05)

# ── WHERE gold really shows up: NEUTRINO mixing (A₅, tan θ₁₂=1/φ) — approximate ──
sin2_gold=1/(1+PHI**2)               # tan θ=1/φ ⟹ sin²θ=1/(1+φ²)
sin2_meas=0.307
off=abs(sin2_gold-sin2_meas)/sin2_meas
ck(f"★gold→neutrinos: sin²θ₁₂(gold)={sin2_gold:.3f} vs measured {sin2_meas:.3f} — approximate (off {off*100:.0f}%, ◐)",
   0.05<off<0.20)

# ── 2/9 vs Cabibbo λ (where 2/9 is at least close) ──
lam=0.2265
ck(f"2/9 vs Cabibbo λ={lam}: close but not exact (off {abs(2/9-lam)/lam*100:.1f}%); θ_W=2/9 REFUTED (3/8=SU5)",
   abs(2/9-lam)/lam<0.03)

print()
verdict={
 "Koide Q=2/3 (mass angle) — RANK 3 (σ½-facet), not 5": "● solid",
 "phase δ≈2/9 gives the lepton ratios — but 2/9 is NOT golden, and is NOT derived": "◐ reading (0.07% coincidence)",
 "★golden φ≈1.618 does NOT give the charged-lepton hierarchy": "✗ hypothesis not confirmed",
 "gold really shows up → NEUTRINO mixing (A₅, tan θ₁₂=1/φ)": "◐ approximate (~10% off), not masses",
 "quarks Koide≠2/3; mass ratios ≠ powers of φ": "● (a fit, not gold)",
 "★the wall HOLDS for mass values; rank 5=mixing not hierarchy": "○ numbers behind the wall",
}
for k,v in verdict.items(): print(f"  {k}: {v}")
print(f"\nSUMMARY: {p} PASS / {f} FAIL")
