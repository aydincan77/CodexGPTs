import argparse

def calculate(a: float, op: str, b: float) -> float:
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    raise ValueError(f"Unsupported operation: {op}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Basit hesap makinesi")
    parser.add_argument("a", type=float, help="ilk sayi")
    parser.add_argument("op", choices=['+', '-', '*', '/'], help="islem")
    parser.add_argument("b", type=float, help="ikinci sayi")
    args = parser.parse_args()
    result = calculate(args.a, args.op, args.b)
    print(result)


if __name__ == "__main__":
    main()
