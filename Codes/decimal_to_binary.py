def decimal_to_binary(n):
    if n == 0:
        return "0"

    if n < 0:
        return "-" + decimal_to_binary(-n)

    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


if __name__ == "__main__":
    num = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(num))