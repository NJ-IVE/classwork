numbers=[11,22,33,44,55,66,77,88,99]

key_value=88
found=False

for i in numbers:
    if numbers[i]==key_value:
        found=True
        break

if found is True:
    print(f"Element {key_value} found.")
else:
    print(f"Element {key_value} not found.")


