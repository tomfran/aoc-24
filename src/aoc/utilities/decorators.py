import time
import inspect
import io
import sys


def solution(fun):
    def wrapper(*args, **kwargs):
        day = inspect.getfile(fun).split("/")[-1].replace(".py", "")
        function_name = fun.__name__

        original_stdout = sys.stdout
        captured_output = io.StringIO()
        sys.stdout = captured_output

        start_time = time.time()
        fun(*args, **kwargs)
        end_time = time.time()

        sys.stdout = original_stdout
        output = captured_output.getvalue()
        captured_output.close()

        elapsed_time = (end_time - start_time) * 1000

        print(f"# Day {day} - {function_name} - time: {elapsed_time:.2f}ms\n")
        print(output)

    return wrapper
