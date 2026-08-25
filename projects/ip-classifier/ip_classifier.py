ip = input("Enter IP: ")

parts = ip.split(".")

valid = True

if len(parts) != 4:
    valid = False
else:
    for part in parts:
        if not part.isdigit():
            valid = False
            break

        number = int(part)

        if number < 0 or number > 255:
            valid = False
            break

if valid:
    first = int(parts[0])
    second = int(parts[1])

    print("IPv4")

    if first == 10:
        print("Private address")

    elif first == 172 and 16 <= second <= 31:
        print("Private address")

    elif first == 192 and second == 168:
        print("Private address")

    else:
        print("Public address")

else:
    print("Invalid IPv4")
