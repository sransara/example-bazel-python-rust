use pyo3::prelude::*;

#[pyfunction]
fn fib(x: usize) -> usize {
    if x < 2 {
        x
    } else {
        fib(x - 1) + fib(x - 2)
    }
}

#[pymodule]
fn fib_native(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fib, m)?)?;
    Ok(())
}
