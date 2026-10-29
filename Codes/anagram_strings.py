def is_anagram(first, second):
    first_clean = first.replace(" ", "").lower()
    second_clean = second.replace(" ", "").lower()

    return sorted(first_clean) == sorted(second_clean)


if __name__ == "__main__":
    first = input("Enter first string: ")
    second = input("Enter second string: ")
    print("Is anagram:", is_anagram(first, second))