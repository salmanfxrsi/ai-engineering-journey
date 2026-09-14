# Problem: Your lab is prototyping a Smart Light that turns on only when the room is bright enough. You are given two real numbers: the current brightness and a threshold. If brightness ≥ threshold, print ON; otherwise print OFF.

input = input("Enter current brightness and threshold (separated by space): ").split()

brightness = float(input[0])
threshold = float(input[1])

if brightness >= threshold:
    print("ON")
else:
    print("OFF")

