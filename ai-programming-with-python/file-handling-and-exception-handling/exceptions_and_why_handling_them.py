try:
    with open("./counter_of_string.txt") as file:
        data = file.read()

except FileNotFoundError:
    print("Dataset file was not found")

except OSError as e:
    print(f"Could not read the dataset: {e}")

else: 
    print("Dataset loaded successfully")
    print(data)

finally:
    print("Training attempt finished")

