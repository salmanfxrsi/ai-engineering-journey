class Phone: 
    category = "Electronics"

    def __init__(self, model, battery, camera, battery_charge):
        self.model = model
        self.battery = battery
        self.camera = camera
        self.battery_charge = battery_charge

    def charge(self, hours):
        self.battery_charge += hours

    def capture(self, total_photo):
        if self.battery_charge > 0:
            self.battery_charge -= total_photo * 2
            print(f"Captured {total_photo} photos")
        else:
            print("Battery is too low to capture photos")

# creating object
apple = Phone("iPhone 13", "3095mAh", "12MP", 20)
blueberry = Phone("Blueberry 12", "3000mAh", "12MP", 0)
motorola = Phone("Motorola Edge", "4500mAh", "108MP", 100)

print(apple.capture(0))