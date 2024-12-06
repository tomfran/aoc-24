import inspect


def solution(fun):
    def wrapper(*args, **kwargs):
        day = inspect.getfile(fun).split("/")[-1].replace(".py", "")
        function_name = fun.__name__

        print(f"\n# Day {day} - {function_name}\n")
        return fun(*args, **kwargs)

    return wrapper
