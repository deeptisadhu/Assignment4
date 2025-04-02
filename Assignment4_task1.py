try:
    with open("samplee.txt", "r") as file:
        for line in file:
            print(line.strip())  # Strip to remove any trailing newline characters
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")






