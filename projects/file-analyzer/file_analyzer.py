def read_file(path):
    with open(path, "r") as file:
        return file.read()


def count_lines(content):
    return len(content.splitlines())


def count_characters(content):
    return len(content)


def analyze_file(path):
    try:
        content = read_file(path)

        lines = count_lines(content)
        characters = count_characters(content)

        print("File:", path)
        print("Lines:", lines)
        print("Characters:", characters)

    except FileNotFoundError:
        print("Error: file not found")


analyze_file("log.txt")