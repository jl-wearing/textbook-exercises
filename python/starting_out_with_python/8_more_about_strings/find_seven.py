string = "Four score and seven years ago."

index = string.find('seven')

if index != -1:
    print(f"'seven' was found at index {index}")
else:
    print("'seven' was not found")