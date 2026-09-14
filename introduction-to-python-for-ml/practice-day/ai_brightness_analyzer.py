# AI systems often analyze images by looking at the brightness of pixels. Each pixel has a brightness value, usually between 0 (dark) and 255 (bright). Let's simulate this concept!
# You are given a list of integers representing pixel brightness values. Your task is to find the average brightness and decide whether the image is Dark, Normal, or Bright.
# If the average brightness < 85 → print Dark Image
# If 85 ≤ average brightness ≤ 170 → print Normal Image
# If average brightness > 170 → print Bright Image

pixel_brightnesses = input().split()

total_pixel_brightness = 0
sum_pixel_brightness = 0

for pixel_brightness in pixel_brightnesses:
    total_pixel_brightness += 1
    sum_pixel_brightness += int(pixel_brightness)

average_pixel_brightness = sum_pixel_brightness / total_pixel_brightness

if average_pixel_brightness < 85:
    print("Dark Image")
elif average_pixel_brightness >= 85 and average_pixel_brightness <= 170:
    print("Normal Image")
else:
    print("Bright Image")
    
