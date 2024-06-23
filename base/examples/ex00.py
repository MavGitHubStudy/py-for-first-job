def return_tuple(tuple_range: int) -> tuple[int, ...]:
    data = [_ for _ in range(tuple_range)]
    # return tuple(data)
    return *data,  # начиная с Python >= 3.5
    # (немного быстрее, но страдает удобочитаемость)


def multiply(x, y):
    return x * y


class MyClass:
    def __init__(self):
        print("MyClass")


class MyCallableClass:
    def __init__(self):
        print("MyCallableClass")

    def __call__(self, *args, **kwargs):
        print("MyCallableClass")


def main():
    print(return_tuple(0))
    print(return_tuple(1))
    print(return_tuple(2))

    print(f"{callable(multiply)= }")
    obj1 = MyClass()
    print(f"{callable(obj1)= }")
    obj2 = MyCallableClass()
    print(f"{callable(obj2)= }")


if __name__ == '__main__':
    main()
