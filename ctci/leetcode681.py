def nextClosestTime(time_string):

    # 23:44 -> 22:22
    # 21:23
    # 12:33
    # 13:11
    digits = set()

    for c in time_string:
        if c.isnumeric():
            digits.add(int(c))

    if len(digits) == 1:
        return time_string

    hours, minutes = [int(_) for _ in time_string.split(":")]

    # find next minute that can be created from the digits
    diff = minutes
    for d1 in digits:
        for d2 in digits:
            if d1 < 6:
                new_minutes = 10 * d1 + d2
                if new_minutes > minutes:
                    diff = min(diff, new_minutes - minutes)
    if diff:
        return f"{hours:02d}:{minutes+diff}"
    diff = hours

    for d1 in digits:
        for d2 in digits:
            if d1 < 2 or d1 == 2 and d2 < 5:
                new_hours = 10 * d1 + d2
                if new_hours > hours:
                    diff = min(diff, new_hours - hours)
    if diff:
        return f"{new_hours}:{min(digits)}{min(digits)}"

    return f"{min(digits)}{min(digits)}:{min(digits)}{min(digits)}"


def main():
    time_string = input("Enter a time string: ")
    result = nextClosestTime(time_string)
    print("Next closest time:", result)


if __name__ == "__main__":
    main()
