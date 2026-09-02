def read_file(path):
    with open(path, "r") as file:
        return file.readlines()


def count_logs(lines):
    counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    for line in lines:
        for level in counts:
            if level in line:
                counts[level] += 1

    return counts


def analyze_logs(path):
    try:
        lines = read_file(path)
        counts = count_logs(lines)

        print("Log:", path)
        print("INFO:", counts["INFO"])
        print("WARNING:", counts["WARNING"])
        print("ERROR:", counts["ERROR"])

    except FileNotFoundError:
        print("Error: file not found")


analyze_logs("logs.txt")