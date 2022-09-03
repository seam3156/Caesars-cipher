#! /bin/python

def decipherS(cipher, n):
    ciphertext = []
    for letter in cipher:
        asc = ord(letter)
        if (asc + n) > 122:
            asc = (asc + n) - 26
        elif asc == 32:
            asc = asc
        else:
            asc = asc + n
        letter = chr(asc)
        ciphertext.append(letter)
    plaintext = "".join(ciphertext)
    print(f"\n{n}. {plaintext}")


def decipherA(cipher):
    for counter in range(26):
        ciphertext = []
        for letter in cipher:
            asc = ord(letter)
            if (asc + counter) > 122:
                asc = (asc + counter) - 26
            elif asc == 32:
                asc = asc
            else:
                asc = asc + counter
            letter = chr(asc)
            ciphertext.append(letter)
        plaintext = "".join(ciphertext)
        print(f"{counter}. {plaintext}")

invalid = 1
print("ceasers cipher decoder")

cipher = input("enter cipher text(a -> z only): ")
cipher = cipher.lower()

while invalid != 0:
    invalid = 0
    for each in cipher:
        if (ord(each) < 96 or ord(each) > 122) and ord(each) != 32:
            cipher = input(("enter valid cipher(a -> z only): "))
            cipher = cipher.lower()
            invalid += 1

choise = input("brute force[b] | select character shift [s]: ")
if choise == "b":
    decipherA(cipher)
elif choise == "s":
    n = 0
    while n < 1 or n > 25:
        n = int(input("how many characters?: "))
    decipherS(cipher, n)