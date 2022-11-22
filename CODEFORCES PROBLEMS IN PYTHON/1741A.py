#1741A
for _ in range(int(input())):
    a, b = map(str, input().split())
    if "S" in a and "S" in b:
        a = a.split("S");b = b.split("S")
        a = "".join(a);b = "".join(b)
        if len(a) > len(b):
            print("<")
        elif len(a) == len(b):
            print("=")
        else:
            print(">")
    elif "S" in a and "S" not in b:
        print("<")
    elif "S" not in a and "S" in b:
        print(">")
    elif "M" in a and "M" in b:
        print("=")

    elif "M" in a and "M" not in b:
        if "L" in b:
            print("<")
        else:
            print(">")
    elif "M" not in a and "M" in b:
        if "L" in a:
            print(">")
        else:
            print("<")
    elif "L" in a and "L" in b:
        a = a.split("L");b = b.split("L")
        a = "".join(a);b = "".join(b)
        if len(a) > len(b):
            print(">")
        elif len(a) == len(b):
            print("=")
        else:
            print("<")

    elif "L" in a and "L" not in b:
        print(">")
    elif "L" not in a and "L" in b:
        print("<")
