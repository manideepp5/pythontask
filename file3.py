text = "This is a test file.\nSecond line."
with open("output.txt", "w") as f:
    f.write(text)

print("File written successfully.")
