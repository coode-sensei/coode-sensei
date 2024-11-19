# main.py
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    name = input("Enter your name buddy: ")
    print(greet(name))
    print(farewell(name))
