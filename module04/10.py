# translate

morze_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    ord("D"): "-..",
    ord("E"): ",",
    "F": "..-.",
    "G": "--.",
    ord("H"): "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    ord("L"): ".-..",
    "M": "--",
    "N": "-.",
    ord("O"): "---",
    "P": ".--.",
    "Q": "--.-",
    ord("R"): ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    ord("W"): ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}

string = "Hel6lo world"
prepare = []
for ch in string:
    prepare.append(ch.upper().translate(morze_dict))
translated = " ".join(prepare)
print(translated)


