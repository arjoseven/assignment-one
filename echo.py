#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    result = ""
    for i in range(repetitions, 0, -1):
        result += text[-i:] + '\n'
    return result

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))