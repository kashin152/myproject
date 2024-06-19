import os
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable], Callable]:
    """Декоратор, который логирует вызов функции и ее результат в файл, в случае указания пути,
    или в консоль, в случае отсутствия пути."""

    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_str = f"{func.__name__} ok"
                if filename:
                    with open(os.path.join(r"logs", filename), "a") as file:
                        file.write(log_str + "\n")
                else:
                    print(log_str)
                return result

            except Exception as e:
                log_str = f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(os.path.join(r"logs", filename), "a") as file:
                        file.write(log_str + "\n")
                else:
                    print(log_str)
                raise

        return wrapper

    return decorator
