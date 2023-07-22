# Minimal example for Bazel+Python+Rust

This is a minimal example for using Bazel to build Python libraries that depends on Rust (PyO3) based modules.

## Disclaimer:

This example is made for Unix systems and doesn't work with Windows.
Although with a little bit of digging in, it should be possible to support Windows shared libraries.

## Heavily borrowed from:

- https://github.com/bazelbuild/rules_rust/pull/753
- https://github.com/TheButlah/rules_pyo3

## To test

```
bazel run //fancy_app
```

### Sample output

(excluding outputs from initial setup of dependencies)

```
INFO: Analyzed target //fancy_app:fancy_app (0 packages loaded, 0 targets configured).
INFO: Found 1 target...
Target //fancy_app:fancy_app up-to-date:
  bazel-bin/fancy_app/fancy_app
INFO: Elapsed time: 0.157s, Critical Path: 0.02s
INFO: 1 process: 1 internal.
INFO: Build completed successfully, 1 total action
INFO: Running command line: bazel-bin/fancy_app/fancy_app
fib.fib(10) = 55
fib.fib(10) timeit: 15.856594335054979
fib_native.fib(10) = 55
fib_native.fib(10) timeit: 1.5149840901140124
```

## Development

Run the following to setup the envinronment:

```
# Update Cargo requirements
CARGO_BAZEL_REPIN=1 bazel sync --only=crate_index

# Create/update for rust analyzer
bazel run @rules_rust//tools/rust_analyzer:gen_rust_project

# Update any pip requirements
bazel run //:requirements.update
```
