def make_shirt1(size: str, text: str):
    print(f"The size of the shirt is {size} and the text is {text}")


# make_shirt("small", "Wubulubbadubdub")


def make_shirt2(size: str = "large", text: str = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}")


# make_shirt()
# make_shirt("medium")
# make_shirt("XL", "I'm Pickle Riiiiiiiick!!")

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt3(size: str, text: str, *additional_text: tuple):
    text_on_shirt = text
    for text in additional_text:
        text_on_shirt += f'\n{text}'

    print(f"The size of the shirt is {size} and the text is {text_on_shirt}")

make_shirt3("Large", 'I love Python', 'Django', 'PostgreSQL', 'JS', 'Machine Learning', 'Sublime')