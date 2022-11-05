from typing import Tuple

def count_strings(names: Tuple) -> int:
    # You need to modify this function.
    # Return the correct answer
    return len(list(filter(lambda item: isinstance(item, str), names)))

