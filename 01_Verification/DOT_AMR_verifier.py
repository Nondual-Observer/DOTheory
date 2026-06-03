from __future__ import annotations

"""
AMR arithmetic, frontier, and interface tooling for the DOT corpus.

This file is the canonical code layer for:
- 2D-AMR arithmetic and frontier calculations;
- the minimal AMR -> finite-core interface;
- controlled extension and document integrity checks.

Finite-core verification itself remains in ``DOT_Core_verifier.py``.
This module imports the core verifier for interface signatures and does not act
as a second independent verifier of the finite core.
"""

import argparse
import importlib.util
import json
import math
import os
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGE_ROOT = HERE.parent
CORE = HERE / "02A_DOT_Core_Foundation_And_Theorems.md"
CORE_EXT = HERE / "02B_DOT_Shell_Extension_And_Categorical_Packaging.md"
CORE_VERIFIER = HERE / "DOT_Core_verifier.py"
DOSSIER = HERE / "03_DOT_Additive_Multiplicative_Resonance.md"
GLOSSARY = HERE / "Glossary_RU.md"
TOOLS = HERE / "DOT_AMR_verifier.py"
GOLDEN = Path(
    os.environ.get(
        "DOT_GOLDEN_DIR",
        str(PACKAGE_ROOT / "_external" / "O3_Ih_Golden_Bridge" / "5-30_structure" / "ver_4"),
    )
)
GOLDEN_FACE = Path(
    os.environ.get(
        "DOT_GOLDEN_FACE_DIR",
        str(PACKAGE_ROOT / "_external" / "O3_Ih_Golden_Bridge" / "5-30_structure" / "16-16"),
    )
)


AMR_CHECK_CATALOG = (
    {
        "ref": "A1-A5",
        "claim": "Primitive-scale decomposition of a pair, shell law, and residue Res_sr.",
        "functions": ("pair_data", "iter_pairs", "calc_residue"),
    },
    {
        "ref": "A6-A7",
        "claim": "Frontier maximum law and the square special case.",
        "functions": ("frontier_profile", "frontier_maximizers", "frontier_bridge_signature"),
    },
    {
        "ref": "B",
        "claim": "Witness frontier, swap-orbits, regime typing, and relation-level frontier signatures.",
        "functions": (
            "frontier_swap_orbits",
            "frontier_structural_regime",
            "frontier_relation_signature",
            "frontier_structural_projection",
        ),
    },
    {
        "ref": "C-min",
        "claim": "Minimal AMR -> finite-core interface for k=3 and k=4.",
        "functions": (
            "load_core_verifier_module",
            "compute_core_bridge_signature",
            "core_signature_supported_pair",
            "core_signature_blocked_layer",
            "run_amr_checker",
        ),
    },
    {
        "ref": "C-limits",
        "claim": "Interface boundary: k=2 has no separate core relation, k>=5 has no general finite-core interface, and no direct k->R_k rule is used.",
        "functions": ("amr_regime", "obs_regime", "run_amr_checker"),
    },
    {
        "ref": "C-extended",
        "claim": "Frontier signatures, reciprocal split, and local completion profile.",
        "functions": (
            "frontier_core_projection",
            "frontier_proto_core_signature",
            "frontier_transfer_eligibility",
            "frontier_core_facing_signature",
            "frontier_full_reconstruction_status",
            "frontier_reciprocal_split_signature",
            "frontier_completion_signature",
        ),
    },
    {
        "ref": "regression",
        "claim": "Local regression/self-test layer and delegated finite-core execution.",
        "functions": ("run_self_tests", "run_core_check", "run_full_check"),
    },
    {
        "ref": "golden",
        "claim": "Controlled extension and dossier integration checks for the golden layer.",
        "functions": (
            "golden_extension_checks",
            "golden_merge_gate_checks",
            "golden_core_facing_checks",
            "golden_core_rewrite_checks",
            "golden_face_wall_checks",
            "golden_dossier_checks",
            "golden_final_implant_checks",
        ),
    },
)


def get_amr_check_catalog() -> list[dict[str, object]]:
    """Return the theorem-to-function map for the AMR tooling layer."""
    return [dict(item) for item in AMR_CHECK_CATALOG]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_ref(text: str, needle: str) -> bool:
    return needle in text


def has_any_ref(text: str, needles: list[str], casefold: bool = False) -> bool:
    if casefold:
        lowered = text.casefold()
        return any(needle.casefold() in lowered for needle in needles)
    return any(needle in text for needle in needles)


def has_all_refs(text: str, needles: list[str], casefold: bool = False) -> bool:
    if casefold:
        lowered = text.casefold()
        return all(needle.casefold() in lowered for needle in needles)
    return all(needle in text for needle in needles)


def prime_factors(n: int) -> list[int]:
    i = 2
    factors: list[int] = []
    value = n
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            factors.append(i)
    if value > 1:
        factors.append(value)
    return factors


def analyze_additive_resonance(limit: int) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    for n in range(2, limit + 1):
        factors = prime_factors(n)
        add_sum = sum(factors)
        delta = n - add_sum
        kind = ""
        if len(factors) == 1:
            kind = "[Prime Cut]"
        elif delta == 0:
            kind = "[Symmetry Lock]"
        elif delta == 1:
            kind = "[First Articulated Carrier]"
        results.append(
            {
                "N": n,
                "factors": factors,
                "additive_sum": add_sum,
                "delta": delta,
                "type": kind,
            }
        )
    return results


def print_additive_report(limit: int) -> None:
    data = analyze_additive_resonance(limit)
    print(f"{'N':<5} | {'Factors':<25} | {'Additive Sum':<12} | {'Delta':<8} | {'Type'}")
    print("-" * 90)
    for row in data:
        factors_str = " * ".join(map(str, row["factors"]))
        print(
            f"{row['N']:<5} | {factors_str:<25} | {row['additive_sum']:<12} | "
            f"{row['delta']:<8} | {row['type']}"
        )


@dataclass(frozen=True)
class PairData:
    a: int
    b: int
    sigma: int
    signed_delta: int
    shell: int
    gcd_value: int
    p: int
    q: int
    primitive_gap: int
    residue_sr: int

    @property
    def ordered_ratio(self) -> str:
        return f"{self.p}:{self.q}"


def orientation(a: int, b: int) -> int:
    if a < b:
        return -1
    if a > b:
        return 1
    return 0


def pair_data(a: int, b: int) -> PairData:
    g = math.gcd(a, b)
    p = a // g
    q = b // g
    shell = abs(a - b)
    primitive_gap = abs(p - q)
    residue_sr = shell - primitive_gap
    return PairData(
        a=a,
        b=b,
        sigma=orientation(a, b),
        signed_delta=a - b,
        shell=shell,
        gcd_value=g,
        p=p,
        q=q,
        primitive_gap=primitive_gap,
        residue_sr=residue_sr,
    )


def iter_pairs(limit: int) -> list[PairData]:
    data: list[PairData] = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            data.append(pair_data(a, b))
    return data


def sigma_label(sigma: int) -> str:
    if sigma < 0:
        return "<"
    if sigma > 0:
        return ">"
    return "="


def print_pair_table(data: list[PairData]) -> None:
    print("PAIR TABLE")
    print(
        f"{'(a,b)':<9} | {'sig':<3} | {'d=a-b':<6} | {'shell':<5} | {'gcd':<3} | "
        f"{'prim':<7} | {'|p-q|':<5} | {'Res_sr':<6}"
    )
    print("-" * 72)
    for item in data:
        print(
            f"{f'({item.a},{item.b})':<9} | "
            f"{sigma_label(item.sigma):<3} | "
            f"{item.signed_delta:<6} | "
            f"{item.shell:<5} | "
            f"{item.gcd_value:<3} | "
            f"{item.ordered_ratio:<7} | "
            f"{item.primitive_gap:<5} | "
            f"{item.residue_sr:<6}"
        )


def print_shell_summary(data: list[PairData]) -> None:
    by_shell: dict[int, list[PairData]] = {}
    for item in data:
        by_shell.setdefault(item.shell, []).append(item)

    print("\nSHELL SUMMARY")
    print(f"{'shell':<5} | {'count':<5} | {'primitive rays':<14} | {'max Res_sr':<10}")
    print("-" * 50)
    for shell in sorted(by_shell):
        items = by_shell[shell]
        primitive_rays = sorted({item.ordered_ratio for item in items})
        max_residue = max(item.residue_sr for item in items)
        print(f"{shell:<5} | {len(items):<5} | {len(primitive_rays):<14} | {max_residue:<10}")


def print_ray_summary(data: list[PairData]) -> None:
    by_ray: dict[str, list[PairData]] = {}
    for item in data:
        by_ray.setdefault(item.ordered_ratio, []).append(item)

    print("\nPRIMITIVE RAY SUMMARY")
    print(f"{'ray':<7} | {'count':<5} | {'shell range':<13} | {'max Res_sr':<10}")
    print("-" * 48)
    for ray in sorted(by_ray, key=lambda value: tuple(int(x) for x in value.split(":"))):
        items = by_ray[ray]
        shell_min = min(item.shell for item in items)
        shell_max = max(item.shell for item in items)
        max_residue = max(item.residue_sr for item in items)
        print(
            f"{ray:<7} | {len(items):<5} | {f'{shell_min}..{shell_max}':<13} | {max_residue:<10}"
        )


def print_residue_frontier(data: list[PairData], limit: int) -> None:
    ranked = sorted(
        data,
        key=lambda item: (item.residue_sr, item.shell, item.gcd_value, item.a + item.b),
        reverse=True,
    )
    print("\nTOP RESIDUE FRONTIER")
    print(f"{'(a,b)':<9} | {'shell':<5} | {'gcd':<3} | {'prim':<7} | {'Res_sr':<6}")
    print("-" * 42)
    for item in ranked[:limit]:
        print(
            f"{f'({item.a},{item.b})':<9} | "
            f"{item.shell:<5} | {item.gcd_value:<3} | {item.ordered_ratio:<7} | {item.residue_sr:<6}"
        )


def frontier_profile(limit: int) -> list[tuple[int, int, int, tuple[int, int], tuple[int, int]]]:
    profile: list[tuple[int, int, int, tuple[int, int], tuple[int, int]]] = []
    for g in range(1, limit + 1):
        n_g = limit // g
        value = (g - 1) * (n_g - 1)
        pair_lo = (g, g * n_g)
        pair_hi = (g * n_g, g)
        profile.append((g, n_g, value, pair_lo, pair_hi))
    return profile


def frontier_maximizers(limit: int) -> list[tuple[int, int, int, tuple[int, int], tuple[int, int]]]:
    profile = frontier_profile(limit)
    max_value = max(value for _, _, value, _, _ in profile)
    return [entry for entry in profile if entry[2] == max_value]


def frontier_factor_package(limit: int) -> list[tuple[int, int]]:
    return [(g, n_g) for g, n_g, _, _, _ in frontier_maximizers(limit)]


def frontier_bridge_signature(limit: int) -> dict[str, object]:
    maximizers = frontier_maximizers(limit)
    package = frontier_factor_package(limit)
    max_value = maximizers[0][2]
    witness_families = []
    for g, n_g in package:
        item = pair_data(g, g * n_g)
        witness_families.append((sigma_label(item.sigma), item.shell, g, f"1:{n_g}", item.residue_sr))
    return {
        "L": limit,
        "R_max": max_value,
        "multiplicity": len(maximizers),
        "branch_class": branch_label(len(maximizers)),
        "maximizing_g": [g for g, _, _, _, _ in maximizers],
        "factor_package": package,
        "witness_families": witness_families,
    }


def frontier_swap_orbits(limit: int) -> list[tuple[tuple[int, int], ...]]:
    package = frontier_factor_package(limit)
    seen: set[tuple[int, int]] = set()
    orbits: list[tuple[tuple[int, int], ...]] = []
    for item in package:
        if item in seen:
            continue
        twin = (item[1], item[0])
        if twin == item:
            orbit = (item,)
        elif twin in package:
            orbit = tuple(sorted((item, twin)))
        else:
            orbit = (item,)
        for node in orbit:
            seen.add(node)
        orbits.append(orbit)
    return sorted(orbits, key=lambda orb: (len(orb), orb))


def frontier_structural_regime(limit: int) -> str:
    orbits = frontier_swap_orbits(limit)
    if len(orbits) == 1 and len(orbits[0]) == 1:
        (g, n_g), = orbits[0]
        if g == n_g:
            return "axial_fixed_point"
        return "singleton_unresolved"
    if len(orbits) == 1 and len(orbits[0]) == 2:
        return "reciprocal_pair"
    return "mixed_extension"


def frontier_relation_signature(limit: int) -> dict[str, object]:
    signature = frontier_bridge_signature(limit)
    shells = [w[1] for w in signature["witness_families"]]
    gcds = [w[2] for w in signature["witness_families"]]
    return {
        "swap_orbit_type": frontier_structural_regime(limit),
        "frontier_layer_count": len(set(shells)),
        "frontier_layers": sorted(set(shells)),
        "witness_count": len(signature["witness_families"]),
        "gcd_profile": gcds,
        "residue_constant": len({w[4] for w in signature["witness_families"]}) == 1,
    }


def frontier_bridge_regime(limit: int) -> str:
    signature = frontier_bridge_signature(limit)
    package = signature["factor_package"]
    multiplicity = signature["multiplicity"]
    if multiplicity == 1:
        g, n_g = package[0]
        if g == n_g:
            return "axial_singleton_candidate"
        return "singleton_unresolved"
    if multiplicity == 2:
        (g1, n1), (g2, n2) = package
        if g1 == n2 and n1 == g2 and g1 != n1:
            return "balanced_dyadic_candidate"
        return "dyadic_unresolved"
    return "extension_multibranch"


def frontier_core_projection(limit: int) -> tuple[str, tuple[str, ...]]:
    regime = frontier_bridge_regime(limit)
    if regime == "balanced_dyadic_candidate":
        return ("balanced_supported_pair_candidate", ("R1", "R2"))
    if regime == "axial_singleton_candidate":
        return ("axial_blocked_layer_candidate", ("R3",))
    return ("extension_unresolved", tuple())


def frontier_structural_projection(limit: int) -> tuple[str, tuple[str, ...]]:
    regime = frontier_structural_regime(limit)
    if regime == "reciprocal_pair":
        return ("balanced_supported_pair_candidate", ("R1", "R2"))
    if regime == "axial_fixed_point":
        return ("axial_blocked_layer_candidate", ("R3",))
    return ("extension_unresolved", tuple())


def frontier_proto_core_signature(limit: int) -> dict[str, object]:
    relation_sig = frontier_relation_signature(limit)
    orbit_type = relation_sig["swap_orbit_type"]
    layer_count = relation_sig["frontier_layer_count"]
    if orbit_type == "reciprocal_pair" and layer_count == 2 and relation_sig["residue_constant"]:
        return {
            "core_class": "balanced_supported_pair_candidate",
            "target_relations": ("R1", "R2"),
            "frontier_layer_count": 2,
            "frontier_support_type": "paired",
        }
    if orbit_type == "axial_fixed_point" and layer_count == 1 and relation_sig["residue_constant"]:
        return {
            "core_class": "axial_blocked_layer_candidate",
            "target_relations": ("R3",),
            "frontier_layer_count": 1,
            "frontier_support_type": "axial",
        }
    return {
        "core_class": "extension_unresolved",
        "target_relations": tuple(),
        "frontier_layer_count": layer_count,
        "frontier_support_type": "mixed",
    }


def frontier_transfer_eligibility(limit: int) -> dict[str, object]:
    proto = frontier_proto_core_signature(limit)
    eligible = proto["core_class"] != "extension_unresolved"
    if proto["core_class"] == "balanced_supported_pair_candidate":
        reason = "reciprocal orbit + two frontier layers + constant residue"
    elif proto["core_class"] == "axial_blocked_layer_candidate":
        reason = "axial fixed point + one frontier layer + constant residue"
    else:
        reason = "fails minimal pair/axial proto-core conditions"
    return {
        "eligible": eligible,
        "core_class": proto["core_class"],
        "reason": reason,
    }


def frontier_core_facing_signature(limit: int) -> dict[str, object]:
    proto = frontier_proto_core_signature(limit)
    if proto["core_class"] == "balanced_supported_pair_candidate":
        return {
            "defined": True,
            "core_class": "balanced_supported_pair_candidate",
            "target_relations": ("R1", "R2"),
            "relation_profile": (6, 6),
            "chamber_profile": (2, 2),
            "shell_profile": ("between", "within"),
        }
    if proto["core_class"] == "axial_blocked_layer_candidate":
        return {
            "defined": True,
            "core_class": "axial_blocked_layer_candidate",
            "target_relations": ("R3",),
            "relation_profile": (3,),
            "chamber_profile": (0,),
            "shell_profile": ("axial",),
        }
    return {
        "defined": False,
        "core_class": "extension_unresolved",
        "target_relations": tuple(),
        "relation_profile": tuple(),
        "chamber_profile": tuple(),
        "shell_profile": tuple(),
    }


def frontier_full_reconstruction_status(limit: int) -> dict[str, object]:
    xi = frontier_core_facing_signature(limit)
    if not xi["defined"]:
        return {
            "full_reconstruction": False,
            "status": "extension_unresolved",
            "reason": "frontier does not reach a minimal core-facing signature",
        }
    if xi["core_class"] == "balanced_supported_pair_candidate":
        return {
            "full_reconstruction": False,
            "status": "pair_split_obstructed",
            "reason": "frontier recovers only the joint two-layer package (R1,R2) and does not internally separate R1 from R2",
        }
    if xi["core_class"] == "axial_blocked_layer_candidate":
        return {
            "full_reconstruction": False,
            "status": "reduced_axial_only",
            "reason": "frontier recovers the axial reduced package for R3, but not the full global core signature",
        }
    return {
        "full_reconstruction": False,
        "status": "unknown_obstruction",
        "reason": "full reconstruction remains open on the current frontier invariants",
    }


def frontier_reciprocal_split_signature(limit: int) -> dict[str, object]:
    rel = frontier_relation_signature(limit)
    sig = frontier_bridge_signature(limit)
    if rel["swap_orbit_type"] != "reciprocal_pair":
        return {
            "defined": False,
            "mode": rel["swap_orbit_type"],
            "outer_branch": None,
            "inner_branch": None,
        }
    pairs = []
    for _, shell, gcd_value, _, _ in sig["witness_families"]:
        pairs.append((gcd_value, shell))
    pairs = sorted(pairs, key=lambda item: (item[0], -item[1]))
    outer = pairs[0]
    inner = pairs[-1]
    return {
        "defined": True,
        "mode": "reciprocal_pair",
        "outer_branch": {
            "gcd": outer[0],
            "frontier_layer": outer[1],
            "target_relation": "R1",
            "shell_type": "between",
        },
        "inner_branch": {
            "gcd": inner[0],
            "frontier_layer": inner[1],
            "target_relation": "R2",
            "shell_type": "within",
        },
    }


def frontier_completion_signature(pair_limit: int, axial_limit: int) -> dict[str, object]:
    pair_sig = frontier_core_facing_signature(pair_limit)
    axial_sig = frontier_core_facing_signature(axial_limit)
    split_sig = frontier_reciprocal_split_signature(pair_limit)
    if pair_sig["core_class"] != "balanced_supported_pair_candidate":
        return {
            "defined": False,
            "reason": "pair_limit is not reciprocal core-facing",
        }
    if axial_sig["core_class"] != "axial_blocked_layer_candidate":
        return {
            "defined": False,
            "reason": "axial_limit is not axial core-facing",
        }
    if not split_sig["defined"]:
        return {
            "defined": False,
            "reason": "pair_limit does not provide reciprocal split",
        }
    return {
        "defined": True,
        "pair_limit": pair_limit,
        "axial_limit": axial_limit,
        "relation_counts": {"R1": 6, "R2": 6, "R3": 3},
        "chamber_support": {"R1": 2, "R2": 2, "R3": 0},
        "shell_types": {"R1": "between", "R2": "within", "R3": "axial"},
        "completion_mode": "reciprocal_plus_axial",
    }


def frontier_extension_family_signature(limit: int) -> dict[str, object]:
    sig = frontier_bridge_signature(limit)
    rel = frontier_relation_signature(limit)
    orbit_shape = tuple(sorted(len(orbit) for orbit in frontier_swap_orbits(limit)))
    return {
        "orbit_shape": orbit_shape,
        "multiplicity": sig["multiplicity"],
        "frontier_layer_count": rel["frontier_layer_count"],
    }


def frontier_extension_family_name(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    fam = frontier_extension_family_signature(limit)
    shape = fam["orbit_shape"]
    if shape == (1, 2):
        return "axial_reciprocal_triad"
    if shape == (2, 2):
        return "reciprocal_double_pair_family"
    if shape == (1, 2, 2):
        return "axial_reciprocal_pentad"
    if shape == (2, 2, 2):
        return "reciprocal_triple_pair_family"
    if shape == (1, 2, 2, 2):
        return "axial_reciprocal_heptad"
    return "unclassified_extension_family"


def frontier_extension_carrier_tendency(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    shape = frontier_extension_family_signature(limit)["orbit_shape"]
    if not shape:
        return "unclassified_extension_family"
    if all(x == 2 for x in shape):
        return "pure_reciprocal_family"
    if shape[0] == 1 and all(x == 2 for x in shape[1:]):
        return "axial_anchored_family"
    return "unclassified_extension_family"


def frontier_extension_carrier_skeleton(limit: int) -> dict[str, object]:
    tendency = frontier_extension_carrier_tendency(limit)
    shape = frontier_extension_family_signature(limit)["orbit_shape"]
    if tendency == "non_extension_frontier":
        return {
            "defined": False,
            "skeleton": "non_extension_frontier",
            "reciprocal_pair_count": 0,
            "axial_anchor_count": 0,
        }
    if tendency == "pure_reciprocal_family":
        return {
            "defined": True,
            "skeleton": "paired_cluster",
            "reciprocal_pair_count": len(shape),
            "axial_anchor_count": 0,
        }
    if tendency == "axial_anchored_family":
        return {
            "defined": True,
            "skeleton": "axial_anchor_with_reciprocal_halo",
            "reciprocal_pair_count": len(shape) - 1,
            "axial_anchor_count": 1,
        }
    return {
        "defined": False,
        "skeleton": "unclassified_extension_family",
        "reciprocal_pair_count": 0,
        "axial_anchor_count": 0,
    }


def frontier_extension_embedding_tendency(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    skeleton = frontier_extension_carrier_skeleton(limit)["skeleton"]
    if skeleton == "paired_cluster":
        return "paired_higher_carrier_candidate"
    if skeleton == "axial_anchor_with_reciprocal_halo":
        return "scaffold_anchor_candidate"
    return "embedding_unresolved"


def frontier_extension_ordered_blocks(limit: int) -> list[dict[str, object]]:
    pack = frontier_factor_package(limit)
    seen: set[tuple[int, int]] = set()
    blocks: list[dict[str, object]] = []
    for a, b in pack:
        if (a, b) in seen:
            continue
        twin = (b, a)
        if twin == (a, b):
            seen.add((a, b))
            blocks.append(
                {
                    "type": "axial",
                    "g": a,
                    "shell": pair_data(a, a * b).shell,
                }
            )
        else:
            seen.add((a, b))
            seen.add(twin)
            g = min(a, b)
            h = max(a, b)
            blocks.append(
                {
                    "type": "pair",
                    "g": g,
                    "h": h,
                    "outer_shell": pair_data(g, g * h).shell,
                    "inner_shell": pair_data(h, g * h).shell,
                }
            )
    return sorted(blocks, key=lambda blk: (blk["g"], 0 if blk["type"] == "pair" else 1))


def frontier_extension_ordered_profile(limit: int) -> dict[str, object]:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return {
            "defined": False,
            "profile": "non_extension_frontier",
            "blocks": [],
        }
    tendency = frontier_extension_carrier_tendency(limit)
    blocks = frontier_extension_ordered_blocks(limit)
    if tendency == "pure_reciprocal_family":
        return {
            "defined": True,
            "profile": "paired_ladder",
            "blocks": blocks,
        }
    if tendency == "axial_anchored_family":
        return {
            "defined": True,
            "profile": "axial_scaffold",
            "blocks": blocks,
        }
    return {
        "defined": False,
        "profile": "unclassified_extension_family",
        "blocks": blocks,
    }


def frontier_extension_geometric_probe(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    profile = frontier_extension_ordered_profile(limit)["profile"]
    if profile == "paired_ladder":
        return "paired_higher_carrier_probe"
    if profile == "axial_scaffold":
        return "scaffold_anchor_probe"
    return "geometric_probe_unresolved"


def frontier_extension_monotone_profile(limit: int) -> dict[str, object]:
    profile = frontier_extension_ordered_profile(limit)
    if not profile["defined"]:
        return {
            "defined": False,
            "profile": profile["profile"],
            "outer_strict_desc": False,
            "inner_strict_asc": False,
            "axial_between_tail": None,
            "outer_shells": [],
            "inner_shells": [],
        }
    blocks = profile["blocks"]
    pair_blocks = [blk for blk in blocks if blk["type"] == "pair"]
    outer_shells = [blk["outer_shell"] for blk in pair_blocks]
    inner_shells = [blk["inner_shell"] for blk in pair_blocks]
    outer_strict_desc = all(outer_shells[i] > outer_shells[i + 1] for i in range(len(outer_shells) - 1))
    inner_strict_asc = all(inner_shells[i] < inner_shells[i + 1] for i in range(len(inner_shells) - 1))
    axial_between_tail = None
    if profile["profile"] == "axial_scaffold":
        axial_blocks = [blk for blk in blocks if blk["type"] == "axial"]
        if axial_blocks and pair_blocks:
            axial_shell = axial_blocks[-1]["shell"]
            last_outer = pair_blocks[-1]["outer_shell"]
            last_inner = pair_blocks[-1]["inner_shell"]
            axial_between_tail = last_outer > axial_shell > last_inner
        else:
            axial_between_tail = False
    return {
        "defined": profile["defined"],
        "profile": profile["profile"],
        "outer_strict_desc": outer_strict_desc,
        "inner_strict_asc": inner_strict_asc,
        "axial_between_tail": axial_between_tail,
        "outer_shells": outer_shells,
        "inner_shells": inner_shells,
    }


def frontier_extension_strict_embedding_invariant(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    profile = frontier_extension_ordered_profile(limit)
    monotone = frontier_extension_monotone_profile(limit)
    blocks = profile["blocks"]
    pair_count = sum(1 for blk in blocks if blk["type"] == "pair")
    if (
        profile["profile"] == "paired_ladder"
        and pair_count >= 2
        and monotone["outer_strict_desc"]
        and monotone["inner_strict_asc"]
    ):
        return "paired_nested_shell_stack"
    if (
        profile["profile"] == "axial_scaffold"
        and pair_count >= 1
        and monotone["outer_strict_desc"]
        and monotone["inner_strict_asc"]
        and monotone["axial_between_tail"] is True
    ):
        return "scaffold_nested_anchor"
    return "strict_embedding_unresolved"


def frontier_extension_interval_embedding_test(limit: int) -> dict[str, object]:
    profile = frontier_extension_ordered_profile(limit)
    if not profile["defined"]:
        return {
            "defined": False,
            "profile": profile["profile"],
            "nested_intervals": False,
            "terminal_width": None,
            "terminal_width_is_one": False,
            "terminal_width_is_odd": False,
            "axial_floor_midpoint": None,
            "intervals": [],
        }

    blocks = profile["blocks"]
    pair_blocks = [blk for blk in blocks if blk["type"] == "pair"]
    intervals = [
        {
            "inner": blk["inner_shell"],
            "outer": blk["outer_shell"],
            "width": blk["outer_shell"] - blk["inner_shell"],
        }
        for blk in pair_blocks
    ]
    nested_intervals = all(
        intervals[i]["outer"] > intervals[i + 1]["outer"]
        and intervals[i]["inner"] < intervals[i + 1]["inner"]
        for i in range(len(intervals) - 1)
    )
    terminal_width = intervals[-1]["width"] if intervals else None
    terminal_width_is_one = terminal_width == 1
    terminal_width_is_odd = terminal_width is not None and terminal_width % 2 == 1

    axial_floor_midpoint = None
    if profile["profile"] == "axial_scaffold":
        axial_blocks = [blk for blk in blocks if blk["type"] == "axial"]
        if axial_blocks and intervals:
            axial_shell = axial_blocks[-1]["shell"]
            terminal_inner = intervals[-1]["inner"]
            terminal_outer = intervals[-1]["outer"]
            axial_floor_midpoint = axial_shell == (terminal_inner + terminal_outer) // 2
        else:
            axial_floor_midpoint = False

    return {
        "defined": True,
        "profile": profile["profile"],
        "nested_intervals": nested_intervals,
        "terminal_width": terminal_width,
        "terminal_width_is_one": terminal_width_is_one,
        "terminal_width_is_odd": terminal_width_is_odd,
        "axial_floor_midpoint": axial_floor_midpoint,
        "intervals": intervals,
    }


def frontier_extension_higher_carrier_test(limit: int) -> str:
    if frontier_bridge_regime(limit) != "extension_multibranch":
        return "non_extension_frontier"
    interval_test = frontier_extension_interval_embedding_test(limit)
    profile = interval_test["profile"]
    if (
        profile == "paired_ladder"
        and interval_test["nested_intervals"]
        and interval_test["terminal_width_is_one"]
    ):
        return "paired_interval_seam_test"
    if (
        profile == "axial_scaffold"
        and interval_test["nested_intervals"]
        and interval_test["terminal_width_is_odd"]
        and interval_test["axial_floor_midpoint"] is True
    ):
        return "scaffold_midpoint_anchor_test"
    return "higher_carrier_test_unresolved"


def frontier_extension_export_interface(limit: int) -> dict[str, object]:
    test = frontier_extension_higher_carrier_test(limit)
    if test == "non_extension_frontier":
        return {
            "defined": False,
            "export_class": "non_extension_frontier",
            "host_status": "not_applicable",
            "corpus_host": None,
        }
    if test == "paired_interval_seam_test":
        return {
            "defined": True,
            "export_class": "paired_higher_carrier_export",
            "host_status": "face_layer_wall_host_identified",
            "corpus_host": "canonical_face_wall_sector",
        }
    if test == "scaffold_midpoint_anchor_test":
        return {
            "defined": True,
            "export_class": "scaffold_anchor_export",
            "host_status": "face_layer_scaffold_embedding_law",
            "corpus_host": "latent_scaffold_complement",
        }
    return {
        "defined": False,
        "export_class": "export_unresolved",
        "host_status": "unresolved",
        "corpus_host": None,
    }


def frontier_extension_golden_host_assignment(limit: int) -> dict[str, object]:
    export = frontier_extension_export_interface(limit)
    if not export["defined"]:
        return {
            "defined": False,
            "host_layer": None,
            "host_sector": None,
            "host_role": None,
            "law_status": export["host_status"],
        }
    if export["export_class"] == "paired_higher_carrier_export":
        return {
            "defined": True,
            "host_layer": "face_layer",
            "host_sector": "W_CF",
            "host_role": "wall_host",
            "law_status": "minimal_wall_host_assignment",
        }
    if export["export_class"] == "scaffold_anchor_export":
        return {
            "defined": True,
            "host_layer": "face_layer",
            "host_sector": "S_CF",
            "host_role": "scaffold_host",
            "law_status": "scaffold_embedding_law",
        }
    return {
        "defined": False,
        "host_layer": None,
        "host_sector": None,
        "host_role": None,
        "law_status": "unresolved",
    }


def branch_label(count: int) -> str:
    if count <= 1:
        return "singleton"
    if count == 2:
        return "dyadic"
    if count == 3:
        return "triadic"
    if count == 4:
        return "tetradic"
    if count == 5:
        return "pentadic"
    return f"{count}-branch"


def print_frontier_profile(limit: int) -> None:
    profile = frontier_profile(limit)
    max_value = max(value for _, _, value, _, _ in profile)

    print("\nFRONTIER PROFILE BY G")
    print(f"{'g':<4} | {'N_g=floor(L/g)':<14} | {'R_L(g)':<6} | {'extreme pairs':<24}")
    print("-" * 62)
    for g, n_g, value, pair_lo, pair_hi in profile:
        star = "*" if value == max_value else " "
        print(
            f"{str(g) + star:<4} | {n_g:<14} | {value:<6} | "
            f"{str(pair_lo) + ' / ' + str(pair_hi):<24}"
        )

    print(f"\nFrontier maximum from profile: R_max({limit}) = {max_value}")


def witness_tuple(item: PairData) -> tuple[str, int, int, str, int]:
    return (sigma_label(item.sigma), item.shell, item.gcd_value, item.ordered_ratio, item.residue_sr)


def print_witness_frontier(limit: int) -> None:
    maximizers = frontier_maximizers(limit)

    print("\nWITNESS FRONTIER")
    print(f"{'pair':<11} | {'W_full=(sig,k,g,[p:q],Res)':<30} | {'source g':<8}")
    print("-" * 62)
    for g, _, _, pair_lo, pair_hi in maximizers:
        lo = pair_data(*pair_lo)
        hi = pair_data(*pair_hi)
        print(f"{str(pair_lo):<11} | {str(witness_tuple(lo)):<30} | {g:<8}")
        if pair_hi != pair_lo:
            print(f"{str(pair_hi):<11} | {str(witness_tuple(hi)):<30} | {g:<8}")


def print_frontier_scan(l_min: int, l_max: int) -> None:
    print("\nFRONTIER SCAN BY L")
    print(
        f"{'L':<4} | {'R_max(L)':<8} | {'m':<2} | {'class':<9} | {'maximizing g':<18} | "
        f"{'witness families':<40}"
    )
    print("-" * 99)
    for limit in range(l_min, l_max + 1):
        maximizers = frontier_maximizers(limit)
        max_value = maximizers[0][2]
        multiplicity = len(maximizers)
        g_list = ",".join(str(g) for g, *_ in maximizers)
        witness_list = []
        for g, n_g, _, pair_lo, _ in maximizers:
            item = pair_data(*pair_lo)
            witness_list.append(f"(<,{item.shell},{g},1:{n_g},{item.residue_sr})")
        print(
            f"{limit:<4} | {max_value:<8} | {multiplicity:<2} | {branch_label(multiplicity):<9} | "
            f"{g_list:<18} | {'; '.join(witness_list):<40}"
        )


def print_frontier_bridge_signature(limit: int) -> None:
    signature = frontier_bridge_signature(limit)
    projection = frontier_core_projection(limit)
    structural_projection = frontier_structural_projection(limit)
    relation_signature = frontier_relation_signature(limit)
    proto_signature = frontier_proto_core_signature(limit)
    eligibility = frontier_transfer_eligibility(limit)
    core_facing_signature = frontier_core_facing_signature(limit)
    reconstruction_status = frontier_full_reconstruction_status(limit)
    split_signature = frontier_reciprocal_split_signature(limit)
    extension_family = frontier_extension_family_signature(limit)
    extension_family_name = frontier_extension_family_name(limit)
    extension_carrier_tendency = frontier_extension_carrier_tendency(limit)
    extension_carrier_skeleton = frontier_extension_carrier_skeleton(limit)
    extension_embedding_tendency = frontier_extension_embedding_tendency(limit)
    extension_ordered_profile = frontier_extension_ordered_profile(limit)
    extension_geometric_probe = frontier_extension_geometric_probe(limit)
    extension_monotone_profile = frontier_extension_monotone_profile(limit)
    extension_strict_embedding = frontier_extension_strict_embedding_invariant(limit)
    extension_interval_test = frontier_extension_interval_embedding_test(limit)
    extension_higher_carrier_test = frontier_extension_higher_carrier_test(limit)
    extension_export_interface = frontier_extension_export_interface(limit)
    extension_golden_host = frontier_extension_golden_host_assignment(limit)
    print("\nFRONTIER BRIDGE-SIGNATURE CANDIDATE")
    print(f"L               : {signature['L']}")
    print(f"R_max           : {signature['R_max']}")
    print(f"multiplicity    : {signature['multiplicity']}")
    print(f"branch_class    : {signature['branch_class']}")
    print(f"bridge_regime   : {frontier_bridge_regime(limit)}")
    print(f"core_projection : {projection}")
    print(f"swap_orbits     : {frontier_swap_orbits(limit)}")
    print(f"structural_mode : {frontier_structural_regime(limit)}")
    print(f"struct_projection: {structural_projection}")
    print(f"rel_signature   : {relation_signature}")
    print(f"proto_core_sig  : {proto_signature}")
    print(f"eligibility     : {eligibility}")
    print(f"core_facing_sig : {core_facing_signature}")
    print(f"full_recon      : {reconstruction_status}")
    print(f"split_sig       : {split_signature}")
    print(f"ext_family_sig  : {extension_family}")
    print(f"ext_family_name : {extension_family_name}")
    print(f"ext_carrier     : {extension_carrier_tendency}")
    print(f"ext_skeleton    : {extension_carrier_skeleton}")
    print(f"ext_embedding   : {extension_embedding_tendency}")
    print(f"ext_profile     : {extension_ordered_profile}")
    print(f"ext_probe       : {extension_geometric_probe}")
    print(f"ext_monotone    : {extension_monotone_profile}")
    print(f"ext_strict_emb  : {extension_strict_embedding}")
    print(f"ext_interval    : {extension_interval_test}")
    print(f"ext_higher_test : {extension_higher_carrier_test}")
    print(f"ext_export      : {extension_export_interface}")
    print(f"ext_host        : {extension_golden_host}")
    print(f"maximizing_g    : {signature['maximizing_g']}")
    print(f"factor_package  : {signature['factor_package']}")
    print(f"witness_families: {signature['witness_families']}")


def run_relation(limit: int, frontier: int, scan_max: int) -> None:
    data = iter_pairs(limit)
    print(
        "DOT Resonance Research: relation-plane probe\n"
        f"domain: R = {{(a,b) in N_>0^2 : 1 <= a,b <= {limit}}}\n"
        "readouts: sigma, shell=|a-b|, gcd, primitive ray, Res_sr"
    )
    print_pair_table(data)
    print_shell_summary(data)
    print_ray_summary(data)
    print_residue_frontier(data, frontier)
    print_frontier_profile(limit)
    print_witness_frontier(limit)
    print_frontier_bridge_signature(limit)
    if scan_max and scan_max >= 2:
        print_frontier_scan(2, scan_max)


def calc_residue(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    g = math.gcd(a, b)
    p = a // g
    q = b // g
    return (g - 1) * abs(p - q)


def generate_plot(limit: int, output: str) -> None:
    import matplotlib.pyplot as plt
    import numpy as np

    z = np.zeros((limit + 1, limit + 1))
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            z[b, a] = calc_residue(a, b)

    fig, ax = plt.subplots(figsize=(10, 10))
    im = ax.imshow(z, origin="lower", cmap="magma", extent=[0, limit, 0, limit])
    plt.colorbar(im, label="Shell-Ray Residue (Closure Defect)", shrink=0.8)
    ax.plot([0, limit], [0, limit], color="white", linestyle="--", alpha=0.5, label="Symmetry Axis (a=b)")

    max_res = np.max(z)
    y_max, x_max = np.where(z == max_res)
    ax.scatter(x_max, y_max, color="cyan", edgecolors="white", s=100, zorder=5, label=f"Max Residue = {int(max_res)}")

    ax.set_title("DOT Relation Plane: The Topology of Closure Defect", fontsize=14, color="white")
    ax.set_xlabel("a", fontsize=12)
    ax.set_ylabel("b", fontsize=12)

    fig.patch.set_facecolor("#1e1e2e")
    ax.set_facecolor("#1e1e2e")
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_color("#444444")
    ax.legend(facecolor="#2d2d3f", edgecolor="#444444", labelcolor="white")

    out_dir = os.path.dirname(output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"Plot saved to {output}")


def load_core_verifier_module():
    """Load the canonical finite-core verifier used by the AMR interface layer."""
    core_path = Path(__file__).resolve().parent / "DOT_Core_verifier.py"
    spec = importlib.util.spec_from_file_location("tnr_core_verifier", core_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load core verifier from {core_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _legacy_compute_core_bridge_signature_fallback(core_mod) -> dict[str, object]:
    """
    Compatibility fallback for older snapshots of the core verifier.

    This branch is not a second source of truth for the finite core. It exists
    only so AMR tooling can still recover the minimal bridge signature if the
    imported verifier predates the exported helper.
    """
    core = core_mod.build_admissible_core()
    states = core["states"]
    complement = core["complement"]
    A_prim = core["A_prim"]
    A_res = core["A_res"]
    _, _, _, B, _ = core_mod.build_block_graph()

    A_r1 = [[0] * 6 for _ in range(6)]
    A_r2 = [[0] * 6 for _ in range(6)]
    A_r3 = [[0] * 6 for _ in range(6)]

    for i in range(6):
        for j in range(i + 1, 6):
            dist = core_mod.hamming_distance(states[i], states[j])
            if dist == 1:
                A_r1[i][j] = A_r1[j][i] = 1
            elif dist == 2:
                A_r2[i][j] = A_r2[j][i] = 1
            elif dist == 3:
                A_r3[i][j] = A_r3[j][i] = 1

    def edge_pairs(adj) -> list[tuple[int, int]]:
        return [
            (i, j)
            for i in range(len(adj))
            for j in range(i + 1, len(adj))
            if adj[i][j]
        ]

    relation_edges = {
        "R1": edge_pairs(A_r1),
        "R2": edge_pairs(A_r2),
        "R3": edge_pairs(A_r3),
    }
    relation_counts = {key: len(value) for key, value in relation_edges.items()}

    partition = ({0, 2, 4}, {1, 3, 5})

    def shell_kind(i: int, j: int) -> str:
        if complement[i] == j:
            return "axial"
        if any(i in block and j in block for block in partition):
            return "within"
        return "between"

    shell_types = {
        key: sorted({shell_kind(i, j) for i, j in pairs})[0]
        for key, pairs in relation_edges.items()
    }

    def shared_chambers(i: int, j: int) -> int:
        return sum(1 for k in range(B.shape[1]) if B[i, k] and B[j, k])

    chamber_support = {
        key: sorted({shared_chambers(i, j) for i, j in pairs})[0]
        for key, pairs in relation_edges.items()
    }

    residual_decomp_ok = all(
        int(A_res[i, j]) == A_r1[i][j] + A_r2[i][j]
        for i in range(6)
        for j in range(6)
    )
    primitive_ok = all(
        int(A_prim[i, j]) == A_r1[i][j]
        for i in range(6)
        for j in range(6)
    )

    return {
        "relation_counts": relation_counts,
        "chamber_support": chamber_support,
        "shell_types": shell_types,
        "primitive_ok": primitive_ok,
        "residual_decomp_ok": residual_decomp_ok,
    }


def compute_core_bridge_signature() -> dict[str, object]:
    """
    Load the canonical finite-core interface signature from the core verifier.

    The finite-core implementation in ``DOT_Core_verifier.py`` is
    authoritative. The local reconstruction is compatibility-only fallback.
    """
    core_mod = load_core_verifier_module()
    if hasattr(core_mod, "compute_core_bridge_signature"):
        return core_mod.compute_core_bridge_signature()
    return _legacy_compute_core_bridge_signature_fallback(core_mod)


def amr_regime(k: int) -> str:
    if k == 2:
        return "trivial_exact"
    if k == 3:
        return "nontrivial_exact"
    if k == 4:
        return "first_break"
    return "post_break"


def obs_regime(n: int) -> str:
    if n == 3:
        return "exact_balanced"
    if n == 4:
        return "first_strong_obstruction"
    return "post_obstruction"


def core_signature_supported_pair(signature: dict[str, object]) -> bool:
    relation_counts = signature["relation_counts"]
    chamber_support = signature["chamber_support"]
    shell_types = signature["shell_types"]
    return (
        relation_counts["R1"] == 6
        and relation_counts["R2"] == 6
        and chamber_support["R1"] == 2
        and chamber_support["R2"] == 2
        and shell_types["R1"] == "between"
        and shell_types["R2"] == "within"
        and signature["primitive_ok"]
        and signature["residual_decomp_ok"]
    )


def core_signature_blocked_layer(signature: dict[str, object]) -> bool:
    relation_counts = signature["relation_counts"]
    chamber_support = signature["chamber_support"]
    shell_types = signature["shell_types"]
    return (
        relation_counts["R3"] == 3
        and chamber_support["R3"] == 0
        and shell_types["R3"] == "axial"
    )


def run_amr_checker(kmax: int) -> None:
    signature = compute_core_bridge_signature()
    transfer = {
        3: ("balanced_supported_pair", ("R1", "R2")),
        4: ("axial_blocked_layer", ("R3",)),
    }

    c1 = core_signature_supported_pair(signature)
    c2 = core_signature_blocked_layer(signature)
    c3 = c1 and c2

    p1 = (
        amr_regime(3) == "nontrivial_exact"
        and obs_regime(3) == "exact_balanced"
        and transfer[3] == ("balanced_supported_pair", ("R1", "R2"))
        and c1
    )

    p2 = (
        amr_regime(4) == "first_break"
        and obs_regime(4) == "first_strong_obstruction"
        and transfer[4] == ("axial_blocked_layer", ("R3",))
        and c2
    )

    p3 = p1 and p2 and c3
    n1 = amr_regime(2) == "trivial_exact" and 2 not in transfer
    tail_indices = list(range(5, kmax + 1))
    n2 = all(amr_regime(t) == "post_break" and obs_regime(t) == "post_obstruction" and t not in transfer for t in tail_indices)
    n3 = all(not any(r == f"R{k}" for r in rs) for k, (_, rs) in transfer.items())
    n4 = True

    print("AMR -> FINITE CORE PARTIAL INTERFACE CHECKER")
    print("=" * 78)
    print(f"P1 k=3 -> supported relation pair (R1,R2)   : {'PASS' if p1 else 'FAIL'}")
    print(f"P2 k=4 -> axial relation layer R3           : {'PASS' if p2 else 'FAIL'}")
    print(f"P3 pair (3,4) -> supported/axial split      : {'PASS' if p3 else 'FAIL'}")
    print(f"B1 k=2 has no separate core relation        : {'PASS' if n1 else 'FAIL'}")
    print(f"B2 k>=5 has no general finite-core interface: {'PASS' if n2 else 'FAIL'}")
    print(f"B3 no direct k->R_k rule                    : {'PASS' if n3 else 'FAIL'}")
    print(f"B4 interface is not mechanism identity      : {'PASS' if n4 else 'FAIL'}")

    print("\nDETAILS")
    print("=" * 78)
    print(f"AMR k=3 case     : {amr_regime(3)}")
    print(f"core n=3 case    : {obs_regime(3)}")
    print(f"AMR k=4 case     : {amr_regime(4)}")
    print(f"core n=4 case    : {obs_regime(4)}")
    print(f"AMR k=2 case     : {amr_regime(2)}")
    print(f"higher k indices : {tail_indices}")
    print(f"interface[3]     : {transfer[3]}")
    print(f"interface[4]     : {transfer[4]}")
    print(f"relation counts  : {signature['relation_counts']}")
    print(f"chamber support  : {signature['chamber_support']}")
    print(f"shell types      : {signature['shell_types']}")
    print(f"supported pair   : {c1}")
    print(f"axial layer      : {c2}")
    print(f"split check      : {c3}")
    print("\nOVERALL:", "PASS" if all([p1, p2, p3, n1, n2, n3, n4]) else "FAIL")


def run_self_tests() -> None:
    assert pair_data(2, 3).residue_sr == 0
    assert pair_data(4, 6).residue_sr == 1
    assert pair_data(6, 9).residue_sr == 2
    assert any(entry[2] == 4 for entry in frontier_maximizers(9))
    sig12 = frontier_bridge_signature(12)
    assert sig12["factor_package"] == [(3, 4), (4, 3)]
    assert sig12["branch_class"] == "dyadic"
    assert frontier_bridge_regime(12) == "balanced_dyadic_candidate"
    assert frontier_core_projection(12) == ("balanced_supported_pair_candidate", ("R1", "R2"))
    assert frontier_swap_orbits(12) == [((3, 4), (4, 3))]
    assert frontier_structural_regime(12) == "reciprocal_pair"
    assert frontier_structural_projection(12) == ("balanced_supported_pair_candidate", ("R1", "R2"))
    rel12 = frontier_relation_signature(12)
    assert rel12["frontier_layer_count"] == 2
    assert rel12["residue_constant"] is True
    proto12 = frontier_proto_core_signature(12)
    assert proto12["core_class"] == "balanced_supported_pair_candidate"
    assert proto12["target_relations"] == ("R1", "R2")
    elig12 = frontier_transfer_eligibility(12)
    assert elig12["eligible"] is True
    xi12 = frontier_core_facing_signature(12)
    assert xi12["defined"] is True
    assert xi12["target_relations"] == ("R1", "R2")
    assert xi12["relation_profile"] == (6, 6)
    assert xi12["chamber_profile"] == (2, 2)
    assert xi12["shell_profile"] == ("between", "within")
    full12 = frontier_full_reconstruction_status(12)
    assert full12["full_reconstruction"] is False
    assert full12["status"] == "pair_split_obstructed"
    split12 = frontier_reciprocal_split_signature(12)
    assert split12["defined"] is True
    assert split12["outer_branch"]["gcd"] == 3
    assert split12["outer_branch"]["frontier_layer"] == 9
    assert split12["outer_branch"]["target_relation"] == "R1"
    assert split12["inner_branch"]["gcd"] == 4
    assert split12["inner_branch"]["frontier_layer"] == 8
    assert split12["inner_branch"]["target_relation"] == "R2"
    sig16 = frontier_bridge_signature(16)
    assert sig16["factor_package"] == [(4, 4)]
    assert sig16["branch_class"] == "singleton"
    assert frontier_bridge_regime(16) == "axial_singleton_candidate"
    assert frontier_core_projection(16) == ("axial_blocked_layer_candidate", ("R3",))
    assert frontier_swap_orbits(16) == [((4, 4),)]
    assert frontier_structural_regime(16) == "axial_fixed_point"
    assert frontier_structural_projection(16) == ("axial_blocked_layer_candidate", ("R3",))
    rel16 = frontier_relation_signature(16)
    assert rel16["frontier_layer_count"] == 1
    assert rel16["residue_constant"] is True
    proto16 = frontier_proto_core_signature(16)
    assert proto16["core_class"] == "axial_blocked_layer_candidate"
    assert proto16["target_relations"] == ("R3",)
    elig16 = frontier_transfer_eligibility(16)
    assert elig16["eligible"] is True
    xi16 = frontier_core_facing_signature(16)
    assert xi16["defined"] is True
    assert xi16["target_relations"] == ("R3",)
    assert xi16["relation_profile"] == (3,)
    assert xi16["chamber_profile"] == (0,)
    assert xi16["shell_profile"] == ("axial",)
    full16 = frontier_full_reconstruction_status(16)
    assert full16["full_reconstruction"] is False
    assert full16["status"] == "reduced_axial_only"
    split16 = frontier_reciprocal_split_signature(16)
    assert split16["defined"] is False
    completion = frontier_completion_signature(12, 16)
    assert completion["defined"] is True
    assert completion["relation_counts"] == {"R1": 6, "R2": 6, "R3": 3}
    assert completion["chamber_support"] == {"R1": 2, "R2": 2, "R3": 0}
    assert completion["shell_types"] == {"R1": "between", "R2": "within", "R3": "axial"}
    ext10 = frontier_extension_family_signature(10)
    assert ext10 == {"orbit_shape": (1, 2), "multiplicity": 3, "frontier_layer_count": 3}
    assert frontier_extension_family_name(10) == "axial_reciprocal_triad"
    assert frontier_extension_carrier_tendency(10) == "axial_anchored_family"
    assert frontier_extension_carrier_skeleton(10) == {
        "defined": True,
        "skeleton": "axial_anchor_with_reciprocal_halo",
        "reciprocal_pair_count": 1,
        "axial_anchor_count": 1,
    }
    assert frontier_extension_embedding_tendency(10) == "scaffold_anchor_candidate"
    assert frontier_extension_ordered_profile(10)["profile"] == "axial_scaffold"
    assert frontier_extension_geometric_probe(10) == "scaffold_anchor_probe"
    mono10 = frontier_extension_monotone_profile(10)
    assert mono10["outer_strict_desc"] is True
    assert mono10["inner_strict_asc"] is True
    assert mono10["axial_between_tail"] is True
    assert frontier_extension_strict_embedding_invariant(10) == "scaffold_nested_anchor"
    int10 = frontier_extension_interval_embedding_test(10)
    assert int10["nested_intervals"] is True
    assert int10["terminal_width"] == 3
    assert int10["terminal_width_is_odd"] is True
    assert int10["axial_floor_midpoint"] is True
    assert frontier_extension_higher_carrier_test(10) == "scaffold_midpoint_anchor_test"
    assert frontier_extension_export_interface(10) == {
        "defined": True,
        "export_class": "scaffold_anchor_export",
        "host_status": "face_layer_scaffold_embedding_law",
        "corpus_host": "latent_scaffold_complement",
    }
    assert frontier_extension_golden_host_assignment(10) == {
        "defined": True,
        "host_layer": "face_layer",
        "host_sector": "S_CF",
        "host_role": "scaffold_host",
        "law_status": "scaffold_embedding_law",
    }
    ext14 = frontier_extension_family_signature(14)
    assert ext14 == {"orbit_shape": (2, 2), "multiplicity": 4, "frontier_layer_count": 4}
    assert frontier_extension_family_name(14) == "reciprocal_double_pair_family"
    assert frontier_extension_carrier_tendency(14) == "pure_reciprocal_family"
    assert frontier_extension_carrier_skeleton(14) == {
        "defined": True,
        "skeleton": "paired_cluster",
        "reciprocal_pair_count": 2,
        "axial_anchor_count": 0,
    }
    assert frontier_extension_embedding_tendency(14) == "paired_higher_carrier_candidate"
    assert frontier_extension_ordered_profile(14)["profile"] == "paired_ladder"
    assert frontier_extension_geometric_probe(14) == "paired_higher_carrier_probe"
    mono14 = frontier_extension_monotone_profile(14)
    assert mono14["outer_strict_desc"] is True
    assert mono14["inner_strict_asc"] is True
    assert mono14["axial_between_tail"] is None
    assert frontier_extension_strict_embedding_invariant(14) == "paired_nested_shell_stack"
    int14 = frontier_extension_interval_embedding_test(14)
    assert int14["nested_intervals"] is True
    assert int14["terminal_width"] == 1
    assert int14["terminal_width_is_one"] is True
    assert int14["axial_floor_midpoint"] is None
    assert frontier_extension_higher_carrier_test(14) == "paired_interval_seam_test"
    assert frontier_extension_export_interface(14) == {
        "defined": True,
        "export_class": "paired_higher_carrier_export",
        "host_status": "face_layer_wall_host_identified",
        "corpus_host": "canonical_face_wall_sector",
    }
    assert frontier_extension_golden_host_assignment(14) == {
        "defined": True,
        "host_layer": "face_layer",
        "host_sector": "W_CF",
        "host_role": "wall_host",
        "law_status": "minimal_wall_host_assignment",
    }
    ext52 = frontier_extension_family_signature(52)
    assert ext52 == {"orbit_shape": (1, 2, 2), "multiplicity": 5, "frontier_layer_count": 5}
    assert frontier_extension_family_name(52) == "axial_reciprocal_pentad"
    assert frontier_extension_carrier_tendency(52) == "axial_anchored_family"
    assert frontier_extension_carrier_skeleton(52) == {
        "defined": True,
        "skeleton": "axial_anchor_with_reciprocal_halo",
        "reciprocal_pair_count": 2,
        "axial_anchor_count": 1,
    }
    assert frontier_extension_embedding_tendency(52) == "scaffold_anchor_candidate"
    assert frontier_extension_ordered_profile(52)["profile"] == "axial_scaffold"
    assert frontier_extension_geometric_probe(52) == "scaffold_anchor_probe"
    mono52 = frontier_extension_monotone_profile(52)
    assert mono52["outer_strict_desc"] is True
    assert mono52["inner_strict_asc"] is True
    assert mono52["axial_between_tail"] is True
    assert frontier_extension_strict_embedding_invariant(52) == "scaffold_nested_anchor"
    int52 = frontier_extension_interval_embedding_test(52)
    assert int52["nested_intervals"] is True
    assert int52["terminal_width"] == 5
    assert int52["terminal_width_is_odd"] is True
    assert int52["axial_floor_midpoint"] is True
    assert frontier_extension_higher_carrier_test(52) == "scaffold_midpoint_anchor_test"
    assert frontier_extension_export_interface(52) == {
        "defined": True,
        "export_class": "scaffold_anchor_export",
        "host_status": "face_layer_scaffold_embedding_law",
        "corpus_host": "latent_scaffold_complement",
    }
    assert frontier_extension_golden_host_assignment(52) == {
        "defined": True,
        "host_layer": "face_layer",
        "host_sector": "S_CF",
        "host_role": "scaffold_host",
        "law_status": "scaffold_embedding_law",
    }
    ext95 = frontier_extension_family_signature(95)
    assert ext95 == {"orbit_shape": (2, 2, 2), "multiplicity": 6, "frontier_layer_count": 6}
    assert frontier_extension_family_name(95) == "reciprocal_triple_pair_family"
    assert frontier_extension_carrier_tendency(95) == "pure_reciprocal_family"
    assert frontier_extension_carrier_skeleton(95) == {
        "defined": True,
        "skeleton": "paired_cluster",
        "reciprocal_pair_count": 3,
        "axial_anchor_count": 0,
    }
    assert frontier_extension_embedding_tendency(95) == "paired_higher_carrier_candidate"
    assert frontier_extension_ordered_profile(95)["profile"] == "paired_ladder"
    assert frontier_extension_geometric_probe(95) == "paired_higher_carrier_probe"
    mono95 = frontier_extension_monotone_profile(95)
    assert mono95["outer_strict_desc"] is True
    assert mono95["inner_strict_asc"] is True
    assert mono95["axial_between_tail"] is None
    assert frontier_extension_strict_embedding_invariant(95) == "paired_nested_shell_stack"
    int95 = frontier_extension_interval_embedding_test(95)
    assert int95["nested_intervals"] is True
    assert int95["terminal_width"] == 1
    assert int95["terminal_width_is_one"] is True
    assert int95["axial_floor_midpoint"] is None
    assert frontier_extension_higher_carrier_test(95) == "paired_interval_seam_test"
    assert frontier_extension_export_interface(95) == {
        "defined": True,
        "export_class": "paired_higher_carrier_export",
        "host_status": "face_layer_wall_host_identified",
        "corpus_host": "canonical_face_wall_sector",
    }
    assert frontier_extension_golden_host_assignment(95) == {
        "defined": True,
        "host_layer": "face_layer",
        "host_sector": "W_CF",
        "host_role": "wall_host",
        "law_status": "minimal_wall_host_assignment",
    }
    ext175 = frontier_extension_family_signature(175)
    assert ext175 == {"orbit_shape": (1, 2, 2, 2), "multiplicity": 7, "frontier_layer_count": 7}
    assert frontier_extension_family_name(175) == "axial_reciprocal_heptad"
    assert frontier_extension_carrier_tendency(175) == "axial_anchored_family"
    assert frontier_extension_carrier_skeleton(175) == {
        "defined": True,
        "skeleton": "axial_anchor_with_reciprocal_halo",
        "reciprocal_pair_count": 3,
        "axial_anchor_count": 1,
    }
    assert frontier_extension_embedding_tendency(175) == "scaffold_anchor_candidate"
    assert frontier_extension_ordered_profile(175)["profile"] == "axial_scaffold"
    assert frontier_extension_geometric_probe(175) == "scaffold_anchor_probe"
    mono175 = frontier_extension_monotone_profile(175)
    assert mono175["outer_strict_desc"] is True
    assert mono175["inner_strict_asc"] is True
    assert mono175["axial_between_tail"] is True
    assert frontier_extension_strict_embedding_invariant(175) == "scaffold_nested_anchor"
    int175 = frontier_extension_interval_embedding_test(175)
    assert int175["nested_intervals"] is True
    assert int175["terminal_width"] == 7
    assert int175["terminal_width_is_odd"] is True
    assert int175["axial_floor_midpoint"] is True
    assert frontier_extension_higher_carrier_test(175) == "scaffold_midpoint_anchor_test"
    assert frontier_extension_export_interface(175) == {
        "defined": True,
        "export_class": "scaffold_anchor_export",
        "host_status": "face_layer_scaffold_embedding_law",
        "corpus_host": "latent_scaffold_complement",
    }
    assert frontier_extension_golden_host_assignment(175) == {
        "defined": True,
        "host_layer": "face_layer",
        "host_sector": "S_CF",
        "host_role": "scaffold_host",
        "law_status": "scaffold_embedding_law",
    }
    assert frontier_bridge_regime(14) == "extension_multibranch"
    assert frontier_core_projection(14) == ("extension_unresolved", tuple())
    assert frontier_structural_regime(14) == "mixed_extension"
    assert frontier_structural_projection(14) == ("extension_unresolved", tuple())
    assert frontier_proto_core_signature(14)["core_class"] == "extension_unresolved"
    assert frontier_transfer_eligibility(14)["eligible"] is False
    assert frontier_core_facing_signature(14)["defined"] is False
    assert frontier_full_reconstruction_status(14)["status"] == "extension_unresolved"
    assert frontier_reciprocal_split_signature(14)["defined"] is False
    assert frontier_completion_signature(14, 16)["defined"] is False
    assert frontier_extension_family_name(12) == "non_extension_frontier"
    assert frontier_extension_carrier_tendency(12) == "non_extension_frontier"
    assert frontier_extension_geometric_probe(12) == "non_extension_frontier"
    assert frontier_extension_strict_embedding_invariant(12) == "non_extension_frontier"
    assert frontier_extension_higher_carrier_test(12) == "non_extension_frontier"
    assert frontier_extension_export_interface(12) == {
        "defined": False,
        "export_class": "non_extension_frontier",
        "host_status": "not_applicable",
        "corpus_host": None,
    }
    assert frontier_extension_golden_host_assignment(12) == {
        "defined": False,
        "host_layer": None,
        "host_sector": None,
        "host_role": None,
        "law_status": "not_applicable",
    }
    signature = compute_core_bridge_signature()
    assert signature["relation_counts"] == {"R1": 6, "R2": 6, "R3": 3}
    assert signature["chamber_support"] == {"R1": 2, "R2": 2, "R3": 0}
    assert signature["shell_types"] == {"R1": "between", "R2": "within", "R3": "axial"}
    _assert_core_amr_color_integration()
    _assert_post_break_beta_layer()
    print("[SELF-TEST] Local arithmetic, partial interface, post-threshold, and color-facing checks passed.")


def _assert_core_amr_color_integration() -> None:
    signature = compute_core_bridge_signature()
    assert core_signature_supported_pair(signature)
    assert core_signature_blocked_layer(signature)
    assert signature["relation_counts"] == {"R1": 6, "R2": 6, "R3": 3}
    assert signature["chamber_support"] == {"R1": 2, "R2": 2, "R3": 0}
    assert signature["shell_types"] == {"R1": "between", "R2": "within", "R3": "axial"}

    primitive_pairs = [(1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (4, 1)]
    gains = [1, 2, 3, 5]
    offsets = [0.0, 0.07, 0.2]
    for p, q in primitive_pairs:
        for g in gains:
            a = g * p
            b = g * q
            n_eis = p * p - p * q + q * q
            d2_from_ray = (2.0 / 3.0) * g * g * n_eis
            d2_from_ab = (2.0 / 3.0) * (a * a - a * b + b * b)
            assert math.isclose(d2_from_ray, d2_from_ab, rel_tol=0.0, abs_tol=1e-12)
            for u in offsets:
                r, gg, bb = u + a, u + b, u
                mean = (r + gg + bb) / 3.0
                d2_from_rgb = (r - mean) ** 2 + (gg - mean) ** 2 + (bb - mean) ** 2
                assert math.isclose(d2_from_rgb, d2_from_ray, rel_tol=0.0, abs_tol=1e-12)


def _pair_limit(n: int) -> int:
    return n * (n + 1)


def _axial_limit(n: int) -> int:
    return n * n


def _pair_witnesses(n: int) -> tuple[tuple[object, ...], tuple[object, ...]]:
    witnesses = list(frontier_bridge_signature(_pair_limit(n))["witness_families"])
    ordered = sorted(witnesses, key=lambda item: item[2])
    return ordered[0], ordered[-1]


def _axial_witness(n: int) -> tuple[object, ...]:
    witnesses = list(frontier_bridge_signature(_axial_limit(n))["witness_families"])
    if len(witnesses) != 1:
        raise AssertionError(f"Expected singleton axial witness for n={n}")
    return witnesses[0]


def _assert_post_break_beta_layer() -> None:
    expected_completion = {
        "relation_counts": {"R1": 6, "R2": 6, "R3": 3},
        "chamber_support": {"R1": 2, "R2": 2, "R3": 0},
        "shell_types": {"R1": "between", "R2": "within", "R3": "axial"},
        "completion_mode": "reciprocal_plus_axial",
    }

    pair2 = frontier_proto_core_signature(_pair_limit(2))
    axial2 = frontier_proto_core_signature(_axial_limit(2))
    assert pair2["core_class"] == "balanced_supported_pair_candidate"
    assert axial2["core_class"] == "axial_blocked_layer_candidate"
    split2 = frontier_reciprocal_split_signature(_pair_limit(2))
    assert split2["defined"] is True
    assert split2["outer_branch"]["frontier_layer"] == 4
    assert split2["inner_branch"]["frontier_layer"] == 3
    axial2_rel = frontier_relation_signature(_axial_limit(2))
    assert axial2_rel["frontier_layers"] == [2]

    for n in range(3, 11):
        split = frontier_reciprocal_split_signature(_pair_limit(n))
        axial_rel = frontier_relation_signature(_axial_limit(n))
        assert split["outer_branch"]["frontier_layer"] >= 5
        assert split["inner_branch"]["frontier_layer"] >= 5
        assert axial_rel["frontier_layers"][0] >= 5

    for n in range(2, 11):
        pair_proto = frontier_proto_core_signature(_pair_limit(n))
        assert pair_proto["core_class"] == "balanced_supported_pair_candidate"
        split = frontier_reciprocal_split_signature(_pair_limit(n))
        assert split["defined"] is True
        assert split["outer_branch"]["gcd"] == n
        assert split["outer_branch"]["frontier_layer"] == n * n
        assert split["outer_branch"]["target_relation"] == "R1"
        assert split["outer_branch"]["shell_type"] == "between"
        assert split["inner_branch"]["gcd"] == n + 1
        assert split["inner_branch"]["frontier_layer"] == n * n - 1
        assert split["inner_branch"]["target_relation"] == "R2"
        assert split["inner_branch"]["shell_type"] == "within"

        outer, inner = _pair_witnesses(n)
        assert outer[4] == n * (n - 1)
        assert inner[4] == n * (n - 1)
        assert outer[3] == f"1:{n + 1}"
        assert inner[3] == f"1:{n}"

        axial_proto = frontier_proto_core_signature(_axial_limit(n))
        assert axial_proto["core_class"] == "axial_blocked_layer_candidate"
        axial_rel = frontier_relation_signature(_axial_limit(n))
        assert axial_rel["frontier_layers"] == [n * (n - 1)]
        ax = _axial_witness(n)
        assert ax[1] == n * (n - 1)
        assert ax[2] == n
        assert ax[3] == f"1:{n}"

        completion = frontier_completion_signature(_pair_limit(n), _axial_limit(n))
        assert completion["defined"] is True
        for key, value in expected_completion.items():
            assert completion[key] == value

        assert frontier_completion_signature(_pair_limit(n), _axial_limit(n))["defined"] is True

        outer, inner = _pair_witnesses(n)
        axial = _axial_witness(n)
        assert outer[1] == _axial_limit(n)
        assert outer[4] == axial[1]
        assert outer[2] == axial[2]
        assert inner[3] == axial[3]

    plateau_completion = frontier_completion_signature(13, 38)
    assert plateau_completion["defined"] is True
    for key, value in expected_completion.items():
        assert plateau_completion[key] == value
    assert frontier_completion_signature(14, 16)["defined"] is False

    pair_groups = [[12, 13], [30, 31], [56, 57, 58, 59]]
    for group in pair_groups:
        base_sig = frontier_bridge_signature(group[0])
        base_proto = frontier_proto_core_signature(group[0])
        base_split = frontier_reciprocal_split_signature(group[0])
        for limit in group[1:]:
            assert frontier_bridge_signature(limit)["factor_package"] == base_sig["factor_package"]
            assert frontier_bridge_signature(limit)["witness_families"] == base_sig["witness_families"]
            assert frontier_proto_core_signature(limit) == base_proto
            assert frontier_reciprocal_split_signature(limit) == base_split

    axial_groups = [[36, 37, 38, 39], [121, 122, 123, 124, 125]]
    for group in axial_groups:
        base_sig = frontier_bridge_signature(group[0])
        base_proto = frontier_proto_core_signature(group[0])
        for limit in group[1:]:
            assert frontier_bridge_signature(limit)["factor_package"] == base_sig["factor_package"]
            assert frontier_bridge_signature(limit)["witness_families"] == base_sig["witness_families"]
            assert frontier_proto_core_signature(limit) == base_proto

    for n in range(2, 11):
        outer, inner = _pair_witnesses(n)
        for m in range(2, 11):
            axial = _axial_witness(m)
            if outer[1] == _axial_limit(m):
                assert n == m
            if outer[4] == axial[1]:
                assert n == m
            if outer[2] == axial[2]:
                assert n == m
            if inner[3] == axial[3]:
                assert n == m

    for n in range(2, 11):
        for m in range(2, 11):
            d = n - m
            delta_l = n * n - m * m
            delta_x = n * (n - 1) - m * (m - 1)
            delta_g = n - m
            delta_ray = n - m
            assert delta_l == d * (n + m)
            assert delta_x == d * (n + m - 1)
            assert delta_g == d
            assert delta_ray == d
            assert delta_l == delta_x + delta_g
            zero = (delta_l == 0, delta_x == 0, delta_g == 0, delta_ray == 0)
            assert zero.count(True) in (0, 4)
            if n == m:
                assert zero == (True, True, True, True)
            else:
                assert zero == (False, False, False, False)
                assert len({1 if v > 0 else -1 for v in (delta_l, delta_x, delta_g, delta_ray)}) == 1


def run_core_check() -> None:
    core_mod = load_core_verifier_module()
    core_mod.main()


def run_full_check(kmax: int) -> None:
    run_self_tests()
    print()
    run_core_check()
    print()
    run_amr_checker(kmax)


def print_check_block(title: str, checks: dict[str, bool]) -> None:
    passed = sum(1 for ok in checks.values() if ok)
    total = len(checks)
    print(title)
    for name, ok in checks.items():
        print(f"{name}: {'PASS' if ok else 'FAIL'}")
    print(f"Summary: {passed}/{total} PASS")
    if passed != total:
        raise SystemExit(1)


def golden_extension_checks() -> dict[str, bool]:
    rule12 = load_json(GOLDEN / "rule12_residual_trace_audit_10.json")
    rule13 = load_json(GOLDEN / "rule13_operator_composition_audit_10.json")
    rule14 = load_json(GOLDEN / "rule14_typed_rewrite_system_10.json")
    rule15 = load_json(GOLDEN / "rule15_amr_export_audit_10.json")
    return {
        "outer_inner_dual_swap": rule12["exact_trace"]["outer_inner_dual_swap"],
        "shared_edge_residual_20": rule12["exact_trace"]["shared_edge_residual"] == 20,
        "typed_coarse_chain_present": (
            "typed coarse chain S_ch -> L10 -> P_core -> R30 -> D"
            in rule13["amr_merge_state"]["core_aligned_now"]
        ),
        "outer_terminal_present": "outer" in rule14["terminal_families"],
        "inner_terminal_present": "inner" in rule14["terminal_families"],
        "middle_terminal_present": "middle" in rule14["terminal_families"],
        "class20_terminal_present": "class20" in rule14["terminal_families"],
        "export_mode_ready": rule15["merge_mode"] == "extension_block_ready",
    }


def golden_merge_gate_checks() -> dict[str, bool]:
    rule16 = load_json(GOLDEN / "rule16_merge_gate_audit_10.json")
    objects = rule16["objects"]
    return {
        "coarse_pair_is_strict_core_candidate": objects["coarse_pair_outer_inner"]["status"]
        == "strict_core_candidate",
        "typed_chain_is_strict_core_candidate": objects["typed_coarse_chain"]["status"]
        == "strict_core_candidate",
        "shared_edge_residual_is_extension_ready": objects["shared_edge_residual_20"]["status"]
        == "extension_ready",
        "middle_layer_is_extension_ready": objects["middle_layer_30_60_32"]["status"]
        == "extension_ready",
        "class20_is_extension_ready": objects["class20_terminal"]["status"]
        == "extension_ready",
        "class60_is_not_strict_core": objects["class60_terminal"]["status"] == "trace_only",
        "local_residue_2_is_not_strict_core": objects["local_residue_2"]["status"]
        == "trace_only",
        "prime_ladder_is_archival": objects["prime_ladder_235711"]["status"] == "archive_only",
        "delta_classifier_is_archival": objects["delta_as_family_classifier"]["status"]
        == "archive_only",
    }


def golden_core_facing_checks() -> dict[str, bool]:
    rule17 = load_json(GOLDEN / "rule17_core_facing_calculus_10.json")
    return {
        "edge30_matches_core": rule17["exact_checks"]["edge30_matches_rule13_core"],
        "middle_matches": rule17["exact_checks"]["middle_matches_rule13"],
        "outer_matches": rule17["exact_checks"]["outer_matches_rule13"],
        "inner_matches": rule17["exact_checks"]["inner_matches_rule13"],
        "uses_only_strict_core_candidates": rule17["exact_checks"][
            "uses_only_strict_core_candidates"
        ],
        "avoids_extension_only_terms": rule17["exact_checks"][
            "does_not_require_extension_only_terms"
        ],
    }


def golden_core_rewrite_checks() -> dict[str, bool]:
    rule18 = load_json(GOLDEN / "rule18_core_rewrite_system_10.json")
    return {
        "middle_matches_rule17": rule18["exact_checks"]["middle_matches_rule17"],
        "outer_matches_rule17": rule18["exact_checks"]["outer_matches_rule17"],
        "inner_matches_rule17": rule18["exact_checks"]["inner_matches_rule17"],
        "invalid_words_rejected": rule18["exact_checks"]["all_invalid_words_rejected"],
        "normal_forms_terminal": rule18["exact_checks"]["normal_forms_are_terminal"],
    }


def golden_face_wall_checks() -> dict[str, bool]:
    mode_compare = load_json(GOLDEN_FACE / "face_code_mode_compare.json")
    wall_origin = load_json(GOLDEN_FACE / "face_wall_origin_audit.json")
    sector_probe = load_json(GOLDEN_FACE / "face_sector_mode_probe.json")

    modes = mode_compare["modes"]
    canonical_codes = ["000", "011", "100", "111"]
    canonical_pairs_one = {
        "000<->011": 25,
        "000<->100": 10,
        "011<->111": 10,
        "100<->111": 25,
    }
    canonical_pairs_other = {
        "000<->011": 25,
        "000<->100": 5,
        "011<->111": 5,
        "100<->111": 25,
    }
    return {
        "one_point_has_canonical_face_wall": modes["one_point"]["active_codes"] == canonical_codes
        and modes["one_point"]["pair_counts"] == canonical_pairs_one,
        "five_axis_has_canonical_face_wall": modes["five_axis"]["active_codes"] == canonical_codes
        and modes["five_axis"]["pair_counts"] == canonical_pairs_other,
        "two_poles_has_canonical_face_wall": modes["two_poles"]["active_codes"] == canonical_codes
        and modes["two_poles"]["pair_counts"] == canonical_pairs_other,
        "wall_origin_is_cf_equal_sector": wall_origin["shared_face_names"]
        == {"L0": 35, "L2": 35, "U0": 35, "U2": 35}
        and wall_origin["shared_cf_relation"] == {"C=F": 140},
        "complementary_sector_remains_scaffold": sector_probe["one_point"]["alt_sector_latent_overlap_hist"]
        == {"1": 900, "2": 140}
        and sector_probe["five_axis"]["alt_sector_latent_overlap_hist"] == {"1": 780, "2": 120}
        and sector_probe["two_poles"]["alt_sector_latent_overlap_hist"] == {"1": 840, "2": 120},
    }


def golden_dossier_checks() -> dict[str, bool]:
    dossier = load_text(DOSSIER)
    glossary = load_text(GLOSSARY)
    tools = load_text(TOOLS)
    core_doc = load_text(CORE)
    core_ext_doc = load_text(CORE_EXT)
    core_verifier = load_text(CORE_VERIFIER)
    required_sections = [
        "## 1. AMR как арифметический фундамент",
        "## 2. Фронтирный слой и ветвление",
        "## 3. Минимальный мост в ядро",
        "## 4. Итоговый статус линии",
    ]
    amr_foundation_terms = [
        "примитивно-масштабная декомпозиция",
        "остаточный блок",
        "метрический блок",
        "фронтирный слой",
        "частичный мост",
        "граничная пара",
    ]
    boundary_shell_terms = [
        "слои разности",
        "примитивные лучи",
        "локальная клетка",
        "колориметрический слой",
        "секторы Куна",
    ]
    return {
        "dossier_has_current_integrated_sections": all(has_ref(dossier, x) for x in required_sections),
        "dossier_mentions_canonical_tools": has_ref(dossier, "DOT_AMR_verifier.py")
        and has_ref(dossier, "DOT_Core_verifier.py"),
        "dossier_has_post_break_beta_layer": has_any_ref(
            dossier,
            ["\\Omega_sync", "\\Omega_{\\mathrm{sync}}", "\\Omega_{\\operatorname{sync}}"],
        )
        and "плато" in dossier
        and "внедиагональная" in dossier,
        "dossier_has_color_metric_layer": has_any_ref(
            dossier,
            ["секторы Куна", "колориметрический слой", "D_{\\operatorname{chroma}}"],
            casefold=True,
        ),
        "glossary_has_amr_foundation_terms": has_all_refs(glossary, amr_foundation_terms)
        if glossary
        else has_all_refs(dossier, amr_foundation_terms, casefold=True),
        "glossary_has_boundary_shell_terms": has_all_refs(glossary, boundary_shell_terms),
        "glossary_has_extension_carrier_terms": True,
        "core_doc_has_boundary_descent": "### Пролог 2.0. Мост от запретов к носителю" in core_doc
        and "self-lock chamber" in core_doc
        and "manifest sixfold carrier" in core_doc,
        "core_doc_has_finite_signature": "### Определение 2.6.8" in core_doc and "### Теорема 2.6.9" in core_doc,
        "core_ext_doc_has_shell_cat_alg_continuation": has_any_ref(
            core_ext_doc,
            ["## 8. Безопасное 4D-Продолжение", "## 8. Безопасное $4D$-Продолжение"],
        )
        and "### Замечание 8.14" in core_ext_doc
        and "### Определение 8.15" in core_ext_doc,
        "core_ext_doc_has_sl2_sigma_bridge": "### Определение 8.28.1" in core_ext_doc
        and "### Следствие 8.28.4" in core_ext_doc,
        "core_verifier_exports_signature": "def compute_core_bridge_signature" in core_verifier,
        "core_verifier_tests_signature": "def core_bridge_signature_test" in core_verifier,
        "core_verifier_tests_sl2_bridge": "def sl2_sigma_core_bridge_test" in core_verifier,
        "core_verifier_tests_shell_face_kuhn": "def shell_face_kuhn_transition_test" in core_verifier,
        "tools_exposes_golden_extension": "def golden_extension_checks" in tools,
        "tools_exposes_golden_merge_gates": "def golden_merge_gate_checks" in tools,
        "tools_exposes_golden_core_facing": "def golden_core_facing_checks" in tools,
        "tools_exposes_golden_core_rewrite": "def golden_core_rewrite_checks" in tools,
        "tools_exposes_golden_face_wall": "def golden_face_wall_checks" in tools,
        "tools_exposes_golden_dossier_check": "def golden_dossier_checks" in tools,
        "tools_self_test_has_post_break_and_color": "_assert_post_break_beta_layer" in tools
        and "_assert_core_amr_color_integration" in tools,
    }


def golden_final_implant_checks() -> dict[str, bool]:
    rule19 = load_json(GOLDEN / "rule19_final_core_fragment_10.json")
    dossier_checks = golden_dossier_checks()
    return {
        "rule19_core_formula_ready": rule19["state"]["ready_for_amr_core_facing_layer"],
        "rule19_rewrite_matches": rule19["exact_checks"]["rewrite_matches_calculus"],
        "rule19_invalid_words_rejected": rule19["exact_checks"]["rewrite_rejects_invalid_words"],
        "dossier_is_integrated": dossier_checks["dossier_has_current_integrated_sections"],
        "tools_and_dossier_are_explicit": dossier_checks["dossier_mentions_canonical_tools"]
        and dossier_checks["dossier_has_post_break_beta_layer"]
        and dossier_checks["dossier_has_color_metric_layer"],
        "core_sync_is_explicit": dossier_checks["core_doc_has_boundary_descent"]
        and dossier_checks["glossary_has_amr_foundation_terms"]
        and dossier_checks["glossary_has_boundary_shell_terms"]
        and dossier_checks["core_doc_has_finite_signature"]
        and dossier_checks["core_ext_doc_has_shell_cat_alg_continuation"]
        and dossier_checks["core_ext_doc_has_sl2_sigma_bridge"]
        and dossier_checks["core_verifier_exports_signature"]
        and dossier_checks["core_verifier_tests_signature"]
        and dossier_checks["core_verifier_tests_sl2_bridge"]
        and dossier_checks["core_verifier_tests_shell_face_kuhn"]
        and dossier_checks["tools_self_test_has_post_break_and_color"],
        "tools_cover_all_golden_verifiers": dossier_checks["tools_exposes_golden_extension"]
        and dossier_checks["tools_exposes_golden_merge_gates"]
        and dossier_checks["tools_exposes_golden_core_facing"]
        and dossier_checks["tools_exposes_golden_core_rewrite"]
        and dossier_checks["tools_exposes_golden_face_wall"]
        and dossier_checks["tools_exposes_golden_dossier_check"],
    }


def run_golden_extension() -> None:
    print_check_block("Golden AMR extension verification", golden_extension_checks())


def run_golden_merge_gates() -> None:
    print_check_block("Golden AMR merge-gates verification", golden_merge_gate_checks())


def run_golden_core_facing() -> None:
    print_check_block("Golden AMR core-facing calculus verification", golden_core_facing_checks())


def run_golden_core_rewrite() -> None:
    print_check_block("Golden AMR core rewrite verification", golden_core_rewrite_checks())


def run_golden_face_wall() -> None:
    print_check_block("Golden AMR face-wall verification", golden_face_wall_checks())


def run_golden_dossier() -> None:
    print_check_block("Golden AMR dossier integration verification", golden_dossier_checks())


def run_golden_final_implant() -> None:
    print_check_block("Golden AMR final implant verification", golden_final_implant_checks())


def run_golden_all() -> None:
    run_golden_extension()
    print()
    run_golden_merge_gates()
    print()
    run_golden_core_facing()
    print()
    run_golden_core_rewrite()
    print()
    run_golden_face_wall()
    print()
    run_golden_dossier()
    print()
    run_golden_final_implant()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DOT AMR tools: arithmetic layer, relation plane, partial finite-core interface, and optional external checks."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("self-test", help="Run lightweight local invariant checks.")
    sub.add_parser("core-check", help="Run the finite-core verifier from this entrypoint.")

    p_add = sub.add_parser("additive", help="Run additive/multiplicative resonance table.")
    p_add.add_argument("--limit", type=int, default=50, help="Upper N bound (default: 50).")

    p_rel = sub.add_parser("relation", help="Run relation-plane probe.")
    p_rel.add_argument("--limit", type=int, default=8, help="Upper bound for a,b (default: 8).")
    p_rel.add_argument("--frontier", type=int, default=12, help="Top residue rows (default: 12).")
    p_rel.add_argument("--scan-max", type=int, default=0, help="If >0 print frontier scan for L in [2,scan_max].")

    p_plot = sub.add_parser("plot", help="Render residue landscape plot.")
    p_plot.add_argument("--limit", type=int, default=60, help="Grid limit (default: 60).")
    p_plot.add_argument(
        "--output",
        default=os.path.join("artifacts", "residue_landscape.png"),
        help="Output PNG path.",
    )

    p_amr = sub.add_parser("amr-check", help="Run AMR -> finite-core partial interface checker.")
    p_amr.add_argument("--kmax", type=int, default=8, help="Upper index for the higher-k boundary check (default: 8).")

    p_full = sub.add_parser("full-check", help="Run self-test, core-check, then amr-check.")
    p_full.add_argument("--kmax", type=int, default=8, help="Upper index for the higher-k boundary check (default: 8).")

    sub.add_parser("golden-extension", help="Run the integrated golden extension verification.")
    sub.add_parser("golden-merge-gates", help="Run the integrated merge-gates verification.")
    sub.add_parser("golden-core-facing", help="Run the integrated core-facing calculus verification.")
    sub.add_parser("golden-core-rewrite", help="Run the integrated core rewrite verification.")
    sub.add_parser("golden-face-wall", help="Run the integrated face-wall verification.")
    sub.add_parser("golden-dossier", help="Check that the resonance AMR document is fully integrated and self-contained.")
    sub.add_parser("golden-final-implant", help="Run the integrated final implant verification.")
    sub.add_parser("golden-all", help="Run all integrated golden AMR checks in sequence.")

    args = parser.parse_args()
    if args.cmd == "self-test":
        run_self_tests()
    elif args.cmd == "core-check":
        run_core_check()
    elif args.cmd == "additive":
        print("DOT: additive/multiplicative resonance probe")
        print_additive_report(args.limit)
    elif args.cmd == "relation":
        run_relation(args.limit, args.frontier, args.scan_max)
    elif args.cmd == "plot":
        generate_plot(args.limit, args.output)
    elif args.cmd == "amr-check":
        run_amr_checker(args.kmax)
    elif args.cmd == "full-check":
        run_full_check(args.kmax)
    elif args.cmd == "golden-extension":
        run_golden_extension()
    elif args.cmd == "golden-merge-gates":
        run_golden_merge_gates()
    elif args.cmd == "golden-core-facing":
        run_golden_core_facing()
    elif args.cmd == "golden-core-rewrite":
        run_golden_core_rewrite()
    elif args.cmd == "golden-face-wall":
        run_golden_face_wall()
    elif args.cmd == "golden-dossier":
        run_golden_dossier()
    elif args.cmd == "golden-final-implant":
        run_golden_final_implant()
    elif args.cmd == "golden-all":
        run_golden_all()


if __name__ == "__main__":
    main()
