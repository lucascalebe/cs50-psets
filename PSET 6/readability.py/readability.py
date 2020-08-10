from cs50 import get_string

txt = get_string("Text: ")

letters = 0
for i in range(len(txt)):
    txt = txt.upper()
    if txt[i].isupper():
        letters += 1

words = 0
for i in range(len(txt)):
    if txt[i].isspace():
        words += 1

sentences = 0
for i in range(len(txt)):
    if txt[i] == '.' or txt[i] == '!' or txt[i] == '?':
        sentences += 1

L = letters / words * 100
S = sentences / words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if (index < 1):
    print("Before Grade 1")

elif (index >= 16):
    print("Grade 16+")

else:
    print(f"Grade {index}")


