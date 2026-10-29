def find_intersection(set1, set2):
    return set1 & set2


if __name__ == "__main__":
    set1 = set(map(int, input("Enter first set elements: ").split()))
    set2 = set(map(int, input("Enter second set elements: ").split()))

    print("Intersection:", find_intersection(set1, set2))