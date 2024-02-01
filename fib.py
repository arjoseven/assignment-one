# fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

times = []
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Finished in", str(elapsed_time)+"s: f("+str(args[0])+")-> "+ str(result))
        times.append(elapsed_time)
        return result
    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2) if n > 1 else n

def generate_plot():
    n_values = list(range(101))
    plt.plot(n_values, times, marker='o')
    plt.xlabel('n in Fibonacci number calculation')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time of Fibonacci Calculation')
    plt.savefig('fib.png')
    plt.show()

if __name__ == "__main__":
    fib(100)
    generate_plot()