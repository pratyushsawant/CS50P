def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    zero_index=s[2:].find("0")
    if 6>=len(s)>=2 and s.isalnum() and s[:2].isalpha() and zero_index!=0:
        for i in s[2:]:
            if i.isdigit():
                index=s.index(i)
                if s[index:].isdigit():
                    return True
                else:
                    return False
        return True


main()
