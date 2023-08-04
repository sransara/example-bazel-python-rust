load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "bazel_skylib",
    sha256 = "66ffd9315665bfaafc96b52278f57c7e2dd09f5ede279ea6d39b2be471e7e3aa",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.2/bazel-skylib-1.4.2.tar.gz",
    ],
)

http_archive(
    name = "rules_python",
    sha256 = "0a8003b044294d7840ac7d9d73eef05d6ceb682d7516781a4ec62eeb34702578",
    strip_prefix = "rules_python-0.24.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.24.0/rules_python-0.24.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python3",
    python_version = "3.11",
)

load("@python3//:defs.bzl", py_intepreter = "interpreter")
load("@rules_python//python:pip.bzl", "pip_parse")

# bazel run //:requirements.update
pip_parse(
    name = "pypi",
    python_interpreter_target = py_intepreter,
    quiet = False,
    requirements_lock = "//:pip_requirements.lock",
)

load("@pypi//:requirements.bzl", install_py_deps = "install_deps")

install_py_deps()

http_archive(
    name = "rules_rust",
    sha256 = "4a9cb4fda6ccd5b5ec393b2e944822a62e050c7c06f1ea41607f14c4fdec57a2",
    urls = ["https://github.com/bazelbuild/rules_rust/releases/download/0.25.1/rules_rust-v0.25.1.tar.gz"],
)

load("@rules_rust//rust:repositories.bzl", "rules_rust_dependencies", "rust_register_toolchains")

rules_rust_dependencies()

rust_register_toolchains(edition = "2021")

load("@rules_rust//crate_universe:defs.bzl", "crate", "crates_repository")

# CARGO_BAZEL_REPIN=1 bazel sync --only=crate_index
crates_repository(
    name = "crate_index",
    annotations = {
        "pyo3-build-config": [
            crate.annotation(
                # https://pyo3.rs/v0.19.2/building_and_distribution#configuring-the-python-version
                build_script_env = {
                    "PYO3_PYTHON": "$(location @python3//:python3)",
                },
                build_script_tools = ["@python3//:python3"],
            ),
        ],
    },
    cargo_lockfile = "//:cargo.bazel.lock",
    lockfile = "//:cargo.bazel.lock.json",
    manifests = ["//number_cruncher:Cargo.toml"],
)

load("@crate_index//:defs.bzl", "crate_repositories")

crate_repositories()

load("@rules_rust//tools/rust_analyzer:deps.bzl", "rust_analyzer_dependencies")

# bazel run @rules_rust//tools/rust_analyzer:gen_rust_project
rust_analyzer_dependencies()
