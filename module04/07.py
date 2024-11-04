# форматування 1

# format_spec     ::= [[fill]aling] [sing] ["z"] ["#"] ["0"] [width] [grouping_option]
# fill            ::=  <any character>
# aling           ::= "<" | ">" | "=" | "^"
# sing            ::= "+" | "-" | " "
# width           ::= digit+
# grouping_option ::= "_" | ","
# precision       ::= digit+
# type            ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | 



x = 20

# print an empty line for spacing
print()

# print the original value of 'x' with a label
print("Original number:", x)

# format and print the value of 'x' with left alignment, a width of 10 characters, a ...
# print("Left aligned (width 10)  :=" + "{:< 10d}".format(x))
print(f"Left aligned (width 10)  :{x:< 10d}")

# format and print the value of 'x' with rigth alignment, a width of 10 characters, a ...
# print("Rigth aligned (width 10)  :=" + "{: 10d}".format(x))
print(f"Rigth aligned (width 10)  :{x: 10d}")

# format and print the value of 'x' with center alignment, a width of 10 characters, a ...
#print("center aligned (width 10)  :=" + "{:^ 10d}".format(x))
print(f"center aligned (width 10)  :{x:^ 10d}")

# print an empty line for spaing
print()
