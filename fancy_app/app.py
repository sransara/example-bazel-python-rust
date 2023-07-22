import timeit
from number_cruncher import fib
from number_cruncher import fib_native


def main():
    print(f"fib.fib(10) = {fib.fib(10)}")
    print(
        "fib.fib(10) timeit: "
        + str(
            timeit.timeit(
                "fib.fib(10)",
                setup="from number_cruncher import fib",
            )
        )
    )

    print(f"fib_native.fib(10) = {fib_native.fib(10)}")
    print(
        "fib_native.fib(10) timeit: "
        + str(
            timeit.timeit(
                "fib_native.fib(10)",
                setup="from number_cruncher import fib_native",
            )
        )
    )


if __name__ == "__main__":
    main()
