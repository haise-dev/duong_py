import random 
low = 1
high = 100
guesses = 0

number = random.randint(low, high)

while True:
    guess = int(input(f"Nhap mot so tu ({low} - {high}):"))
    guesses += 1

    if guess<number:
        print(f"{guess} qua thap")
    elif guess>number:
        print(f"{guess} qua cao")
    else:
        print(f"{guess} la con so chinh xac!")
        break

print(f"ban da doan {guesses} lan ")
