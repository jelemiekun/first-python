first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input ("Age: ")
age = int(age)
find_name = input("Find name: ")

message = f"{first_name} {last_name} is {age} years old."

print(message)
print(f"The above message contains {len(message)} characters")
print(message.lower().replace("john".lower(), "Johnnn"))

found = find_name.lower() in message.lower()

if found:
    print(f"{find_name} found.")
else:
    print(f"Unable to find {find_name}.")