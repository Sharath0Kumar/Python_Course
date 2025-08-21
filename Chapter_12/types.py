from typing import List, Tuple, Dict, Union

n : int = 5

name : str = "Sharath"


def sum(a: int ,b : int ) -> int :
    return a+b

number : List [int] = [1, 2, 3, 4, 5]

person : Tuple[str, int] = ("Sharath", 25)

scores : Dict[str, int] = {"Sharath" : 90, "John": 85}

identifier : Union[str, int] = "Sharath"
identifier = 12345  # Now it's an int