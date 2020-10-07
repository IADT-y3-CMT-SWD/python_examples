#cold outside example
cold_input = int(input("If it\'s cold, type 1, otherwise type 0."))
if cold_input == 1:
    cold_outside = True
else:
    cold_outside = False

print(cold_outside)

if cold_outside == True:
    print("it is cold outside. Wear a coat")
else:
    print("It\'s a fine day!")