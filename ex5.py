my_name = 'Robin L Sharpton'
my_age = 46
my_height = 69 # inches
my_weight = 195 # lbs
my_eyes = 'Grey'
my_teeth = 'White'
my_hair = 'Blond'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that is too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height}, and {my_weight} I get {total}.")

print("*******************************************")
print(f"My height in feet is {my_height // 12} with {my_height % 12} inches extra.")
