#!/usr/bin/env julia
# ==============================================================================
# MASTER VERIFICATION SUITE — DOT / TNR Canonical Trilogy v3.3 (EN & RU)
# Runs without external packages on standard Julia 1.12+ (Printf, SHA, LinearAlgebra)
#
# Usage:
#   julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl
#   julia --startup-file=no 01_Verification/run_all_trilogy_and_bridge_verifiers.jl --full
# ==============================================================================

using Printf

const REPO_ROOT = normpath(joinpath(@__DIR__, ".."))
const FULL_MODE = "--full" in ARGS
const JULIA_BIN = joinpath(Sys.BINDIR, Base.julia_exename())

const CORE_EN_SUITES = [
    ("Book I (EN): Observer, Distinction & Finite Core (23/23 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Book_I_EN", "11_verify_full_book_I_v3_3.jl")),
    ("Book II (EN): Memory, Continuation, Gluing & Quantum Scene (38/38 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Book_II_EN", "11_verify_full_book_II_v3_3.jl")),
    ("Book III (EN): Domain Bridges, Verifications & Next-Step Program (16/16 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Book_III_EN", "07_verify_full_book_III_v3_3.jl")),
]

const CORE_RU_SUITES = [
    ("Book I (RU): Observer, Distinction & Finite Core (23/23 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Книга_I", "11_verify_full_book_I_v3_3.jl")),
    ("Book II (RU): Memory, Continuation, Gluing & Quantum Scene (38/38 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Книга_II", "11_verify_full_book_II_v3_3.jl")),
    ("Book III (RU): Domain Bridges, Verifications & Next-Step Program (16/16 Exact Gates)",
     joinpath(REPO_ROOT, "00_Core", "Книга_III", "07_verify_full_book_III_v3_3.jl")),
]

const SUPPLEMENT_HEAVY_SUITES = [
    ("Supplement 01 (Hoggar, Fano & Zorn Octonions): 11 Single-Threaded Certificates",
     joinpath(REPO_ROOT, "02_Supplements", "01_Hoggar_Fano_Octonions_Certificates", "certificates_and_julia", "run_all_math_certificates.jl")),
]

function run_verifier(label::String, script_path::String)
    if !isfile(script_path)
        @printf("  [FAIL] %-82s (file not found: %s)\n", label, script_path)
        return false
    end
    t0 = time()
    env = copy(ENV)
    env["JULIA_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    cmd = Cmd(`$(JULIA_BIN) --startup-file=no --threads=1 $(script_path)`; env=env, dir=dirname(script_path))
    ok = success(pipeline(cmd, stdout=devnull, stderr=stderr))
    dt = time() - t0
    status = ok ? "PASS" : "FAIL"
    @printf("  [%s] %-82s (%6.2f s)\n", status, label, dt)
    flush(stdout)
    return ok
end

function verify_bilingual_files()
    t0 = time()
    methodology_files = [
        joinpath(REPO_ROOT, "00_Methodology", "README.md"),
        joinpath(REPO_ROOT, "00_Methodology", "README_RU.md"),
    ]
    consolidated_files = [
        joinpath(REPO_ROOT, "00_Core", "01_BOOK_I_OBSERVER_DISTINCTION_AND_FINITE_CORE_V3_3_FULL_EN.md"),
        joinpath(REPO_ROOT, "00_Core", "02_BOOK_II_MEMORY_CONTINUATION_GLUING_AND_QUANTUM_SCENE_V3_3_FULL_EN.md"),
        joinpath(REPO_ROOT, "00_Core", "03_BOOK_III_DOMAIN_BRIDGES_VERIFICATIONS_AND_NEXT_STEP_V3_3_FULL_EN.md"),
        joinpath(REPO_ROOT, "00_Core", "09_ARTICLE_BY_ARTICLE_REGISTRY_OF_103_STATEMENTS_EN.md"),
        joinpath(REPO_ROOT, "00_Core", "01_КНИГА_I_НАБЛЮДАТЕЛЬ_РАЗЛИЧЕНИЕ_И_КОНЕЧНОЕ_ЯДРО_V3_3_ПОЛНЫЙ_ТОМ.md"),
        joinpath(REPO_ROOT, "00_Core", "02_КНИГА_II_ПАМЯТЬ_НЕПРЕРЫВНОЕ_ПРОДОЛЖЕНИЕ_СКЛЕЙКА_И_КВАНТОВАЯ_СЦЕНА_V3_3_ПОЛНЫЙ_ТОМ.md"),
        joinpath(REPO_ROOT, "00_Core", "03_КНИГА_III_ПРЕДМЕТНЫЕ_МОСТЫ_ПРОВЕРКИ_И_ПРОГРАММА_СЛЕДУЮЩЕГО_ШАГА_V3_3_ПОЛНЫЙ_ТОМ.md"),
        joinpath(REPO_ROOT, "00_Core", "09_ПОСТАТЕЙНЫЙ_РЕЕСТР_103_ФОРМУЛИРОВОК.md"),
    ]
    ok = all(f -> isfile(f) && filesize(f) > 5_000, methodology_files) &&
         all(f -> isfile(f) && filesize(f) > 50_000, consolidated_files)
    dt = time() - t0
    status = ok ? "PASS" : "FAIL"
    @printf("  [%s] %-82s (%6.2f s)\n", status, "Bilingual Methodology, 6 Full Volumes & 103-Statement Registries (EN & RU)", dt)
    return ok
end

function strip_fenced_code(md::String)
    out = IOBuffer()
    in_fence = false
    for line in eachline(IOBuffer(md))
        s = lstrip(line)
        if startswith(s, "```")
            in_fence = !in_fence
            continue
        end
        if !in_fence
            println(out, line)
        end
    end
    return String(take!(out))
end

function verify_repository_integrity()
    t0 = time()
    py_files = String[]
    md_files = String[]
    for (root, dirs, files) in walkdir(REPO_ROOT)
        filter!(d -> !startswith(d, "."), dirs)
        for fn in files
            startswith(fn, ".") && continue
            fp = joinpath(root, fn)
            if endswith(lowercase(fn), ".py")
                push!(py_files, fp)
            elseif endswith(lowercase(fn), ".md")
                push!(md_files, fp)
            end
        end
    end

    forbidden_tokens = [
        "_v3_1", "_V3_1", "__FORBID_v3_3__", "__FORBID_V3_3__",
        "J69-", "Opus 5.5", "правилу М21", "Rule M21",
        "[METH-", "[Lean-target]", "file:///Users/",
        "[Кл]", "[Cl]",
        "Ландауэр", "Landauer",
        "Менделеев", "Mendeleev",
        "дрозофил", "Drosophila",
        "Стандартной модели", "Standard Model",
        "нейросет", "нейронн", "трансформер",
        "neural network", "transformer", "language model",
        "MS 408", "Voynich", "Войнич",
        "чакр", "chakra", "DOTNet",
        "CervCon", "MuJoCo", "FlyWire", "MANC",
        "метамер", "metamer",
    ]

    broken_links = String[]
    forbidden_hits = String[]
    link_re = r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)"

    for fp in md_files
        raw = read(fp, String)
        rel_fp = relpath(fp, REPO_ROOT)
        for tok in forbidden_tokens
            if occursin(tok, raw)
                push!(forbidden_hits, "$(rel_fp) -> '$(tok)'")
            end
        end
        prose = strip_fenced_code(raw)
        # Also mask inline backtick spans so math/code expressions like [x](y) aren't parsed as URLs
        prose_no_code = replace(prose, r"`[^`]*`" => "CODE")
        for m in eachmatch(link_re, prose_no_code)
            target = strip(m.captures[1])
            if startswith(target, "http://") || startswith(target, "https://") ||
               startswith(target, "mailto:") || startswith(target, "#")
                continue
            end
            path_part = split(target, '#'; limit=2)[1]
            isempty(path_part) && continue
            resolved = normpath(joinpath(dirname(fp), path_part))
            if !ispath(resolved)
                push!(broken_links, "$(rel_fp) -> ($(target))")
            end
        end
    end

    ok = isempty(py_files) && isempty(broken_links) && isempty(forbidden_hits)
    dt = time() - t0
    status = ok ? "PASS" : "FAIL"
    label = "Global Repo Integrity ($(length(md_files)) .md files: 0 broken links, 0 stale stamps, 0 .py)"
    @printf("  [%s] %-82s (%6.2f s)\n", status, label, dt)
    if !ok
        for p in py_files
            println(stderr, "    [ERR .py] ", relpath(p, REPO_ROOT))
        end
        for b in broken_links
            println(stderr, "    [ERR link] ", b)
        end
        for h in forbidden_hits
            println(stderr, "    [ERR forbidden] ", h)
        end
    end
    return ok
end

function main()
    println("========================================================================================================")
    println("DOT / TNR v3.3 — MASTER VERIFICATION SUITE (Julia $(VERSION), Single-Threaded, Zero-Float Core)")
    println("Repository root: $(REPO_ROOT)")
    println("========================================================================================================")

    t_start = time()
    all_ok = true
    passed_count = 0
    total_count = 0

    println("\n--- PART 1A: CANONICAL THREE-VOLUME EDITION v3.3 — ENGLISH EDITION (77 / 77 EXACT GATES) ---")
    for (label, path) in CORE_EN_SUITES
        total_count += 1
        if run_verifier(label, path)
            passed_count += 1
        else
            all_ok = false
        end
    end

    println("\n--- PART 1B: CANONICAL THREE-VOLUME EDITION v3.3 — RUSSIAN EDITION (77 / 77 EXACT GATES) ---")
    for (label, path) in CORE_RU_SUITES
        total_count += 1
        if run_verifier(label, path)
            passed_count += 1
        else
            all_ok = false
        end
    end

    println("\n--- PART 1C: REPOSITORY-WIDE STRUCTURAL, LINK & HYGIENE INTEGRITY ---")
    for check_fn in (verify_bilingual_files, verify_repository_integrity)
        total_count += 1
        if check_fn()
            passed_count += 1
        else
            all_ok = false
        end
    end

    if FULL_MODE
        println("\n--- PART 2: EXTENDED EXHAUSTIVE CERTIFICATES (--full) ---")
        for (label, path) in SUPPLEMENT_HEAVY_SUITES
            total_count += 1
            if run_verifier(label, path)
                passed_count += 1
            else
                all_ok = false
            end
        end
    end

    println("========================================================================================================")
    @printf("SUMMARY: %d / %d suites PASSED in %.2f s.\n", passed_count, total_count, time() - t_start)
    println("========================================================================================================")
    exit(all_ok ? 0 : 1)
end

main()
