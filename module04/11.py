# Caeser cipher k=3 / Affine cipher k==10000, -12, 45 (зміщення 1 букви на перед)

def encrypt(key, message):
    message = message.upper()
    result = ""
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result += alpha[letter_index]
        else:
            result += letter

    return result

encrypted_msg = encrypt(-2433, "HRUTE IS A KILLER ANB GORRIHLE SON")
print(encrypted_msg)

