import math


def pythago(a: float, b: float) -> float:
    return math.sqrt(a * a + b * b)


def pythago_all(dsc: list[float]):
    for i in range(len(dsc) - 1):
        for j in range(i + 1, len(dsc)):
            print(f"a = {dsc[i]}, b = {dsc[j]}, c = {pythago(dsc[i], dsc[j]):.2}")


if __name__ == "__main__":
    pythago_all([1, 2, 3])
