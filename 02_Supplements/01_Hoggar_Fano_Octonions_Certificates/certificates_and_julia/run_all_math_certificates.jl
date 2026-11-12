# =============================================================================
# Мост 07: Единый однопоточный воспроизводитель всех математических теорем
# и контрпримеров (Исследование 41 + Независимая приёмка Codex DOT.XC №111)
#
# Запуск из корня Моста 07 или из папки certificates_and_julia/:
#   JULIA_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 julia --startup-file=no --threads=1 certificates_and_julia/run_all_math_certificates.jl
#
# По умолчанию исполняет все 11 автономных математических .jl-программ во
# временной песочнице (mktempdir), не перезаписывая эталонные .json-сертификаты
# Витрины (сохраняя их SHA-256), и сверяет ключевые числовые инварианты.
# Для перезаписи сертификатов на месте передайте флаг `--in-place`.
# =============================================================================

using LinearAlgebra, JSON, Printf

BLAS.set_num_threads(1)

const BASE_DIR = @__DIR__
const IN_PLACE = "--in-place" in ARGS

const STUDY41_MATH_SCRIPTS = [
    "01_ГЕНЕАЛОГИЯ_КУБИТА_ТОЧНЫЕ_ПРОВЕРКИ.jl",
    "04_ГЕОМЕТРИЯ_МАГИИ_ВЫНУЖДЕННОСТЬ_SIC_И_БАШНЯ_ПАУЛИ.jl",
    "06_ХОГГАР_ФАНО_И_ЧЁТНОСТЬ.jl",
    "10_ИДЕНТИФИКАЦИЯ_PSU33_И_ОКТОНИОНЫ_ЦОРНА.jl",
    "10b_КАНОНИЧЕСКИЙ_ФИДУЦИАЛ_ХОГГАРА.jl",
    "12_ФОРМУЛА_K_БЕЗ_ПЕРЕБОРА.jl",
]

const AUDIT111_MATH_SCRIPTS = [
    "03_ГРУППЫ_И_ЦОРН.jl",
    "04_ФАЗЫ_И_ФОРМУЛЫ.jl",
    "09_ФОРМЫ_И_ИДЕМПОТЕНТЫ.jl",
    "15_ПРЕДСТАВЛЕНИЯ_ATLAS.jl",
    "16_ВЕЩЕСТВЕННЫЕ_СТРУКТУРЫ.jl",
]

function run_suite(work_root::AbstractString)
    julia_bin = joinpath(Sys.BINDIR, Base.julia_exename())
    env = copy(ENV)
    env["JULIA_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"

    println("=========================================================================")
    println("Мост 07: Однопоточная проверка математического ядра (CPU=1, BLAS=1)")
    println("Julia $(VERSION) | threads=$(Threads.nthreads()) | work_root=$(work_root)")
    println("=========================================================================")

    t_total = time()

    for (subdir, scripts) in (("study_41", STUDY41_MATH_SCRIPTS), ("audit_111", AUDIT111_MATH_SCRIPTS))
        dir = joinpath(work_root, subdir)
        println("\n--- Пакет: $(subdir) ($(length(scripts)) программ) ---")
        for script in scripts
            path = joinpath(dir, script)
            @assert isfile(path) "Не найден скрипт: $(path)"
            t0 = time()
            cmd = Cmd(`$(julia_bin) --startup-file=no --threads=1 $(path)`; env=env, dir=dir)
            run(pipeline(cmd, stdout=devnull, stderr=stderr))
            dt = time() - t0
            @printf("  [PASS] %-58s (%.2f с)\n", script, dt)
            flush(stdout)
        end
    end

    # Контрольная сверка ключевых инвариантов приёмки №111
    d111 = joinpath(work_root, "audit_111")
    c03 = JSON.parsefile(joinpath(d111, "03_СЕРТИФИКАТ_ГРУПП_И_ЦОРНА.json"))
    c04 = JSON.parsefile(joinpath(d111, "04_СЕРТИФИКАТ_ФАЗ_И_ФОРМУЛ.json"))
    c09 = JSON.parsefile(joinpath(d111, "09_СЕРТИФИКАТ_ФОРМ_И_ИДЕМПОТЕНТОВ.json"))
    c15 = JSON.parsefile(joinpath(d111, "15_СЕРТИФИКАТ_ПРЕДСТАВЛЕНИЙ_ATLAS.json"))
    c16 = JSON.parsefile(joinpath(d111, "16_СЕРТИФИКАТ_ВЕЩЕСТВЕННЫХ_СТРУКТУР.json"))

    @assert c03["aut_order"] == 12096 && c03["unitary_order"] == 6048 && c03["antiunitary_order"] == 6048
    @assert c03["all_lift_compositions_checked"] == 146313216 && c03["aut_equals_hoggar_image"] == true
    @assert c03["lagrangians"] == 135 && c03["complementary_unordered_pairs"] == 4320 && c03["plus_forms"] == 36
    @assert c04["passed"] == 84
    @assert c09["idempotent_pairs"] == 36 && c09["Q0_unitary_stabilizer"] == 168 && c09["Q0_full_stabilizer"] == 336
    @assert c09["suborbits_on_plus_forms"] == Any[1, 7, 7, 21]
    @assert c15["unitary_generated_order"] == 6048 && c15["full_generated_order"] == 12096 && c15["all_relators_identity"] == true
    @assert length(c16["real_structures"]) == 36 && length(c16["quaternionic_structures"]) == 28 && c16["all_exact"] == true

    @printf("\nИТОГ: 11/11 математических программ и все контрольные инварианты ПОДТВЕРЖДЕНЫ за %.2f с.\n", time() - t_total)
end

if IN_PLACE
    run_suite(BASE_DIR)
else
    mktempdir() do tmp
        cp(joinpath(BASE_DIR, "study_41"), joinpath(tmp, "study_41"))
        cp(joinpath(BASE_DIR, "audit_111"), joinpath(tmp, "audit_111"))
        run_suite(tmp)
    end
end
