import random
print('rem holy shit we are finally doing it')
low = int(input('your lower number: '))
high = int(input('your highest number: '))

ch = 4
gc = 0
num = random.randint(low, high)

while gc < ch:
    gc = gc + 1
    g = int(input('ur guess?: '))

    if g == num:
        print('omg your superior!!! bravooo')
        break
    
    elif gc >= ch and g != num:
        print('again bitch it was ', num)
    elif g > num:
        print('way too high lower ur shit')
    elif g < num:
        print('way too low u should rise ur shit')

