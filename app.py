first_name = "Meow"
last_name = "Arf"
message = f"{first_name} [{last_name}]"

if len(message) > 15:
    print("Too many characters!")
else:
    print(message.upper())
