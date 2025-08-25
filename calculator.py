import streamlit as st


def calculate(a: float, op: str, b: float) -> float:
    """Perform a basic arithmetic operation."""
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
    st.title("Basit Hesap Makinesi")
    a = st.number_input("İlk sayı", value=0.0)
    b = st.number_input("İkinci sayı", value=0.0)
    op = st.selectbox("İşlem", ['+', '-', '*', '/'])
    if st.button("Hesapla"):
        try:
            result = calculate(a, op, b)
            st.success(f"Sonuç: {result}")
        except Exception as e:
            st.error(str(e))


if __name__ == "__main__":
    main()

