import timeit


def main():
    print(
        timeit.timeit(
            "fib.fib(10)",
            setup="from number_cruncher import fib",
        )
    )
    print(
        timeit.timeit(
            "fib_faster.fib(10)",
            setup="from number_cruncher import fib_faster",
        )
    )


if __name__ == "__main__":
    main()
