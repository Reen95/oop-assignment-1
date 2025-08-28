# main.py

from smartphone import Smartphone, GamingSmartphone
from vehicles import Car, Plane, Boat

# Activity 1 Test
phone1 = Smartphone("Samsung", "S24", 256, 80)
gaming_phone = GamingSmartphone("Asus", "ROG 7", 512, 65, "Adreno X2")

print(phone1)
print(phone1.call("Alice"))
print(phone1.charge(10))

print(gaming_phone)
print(gaming_phone.play_game("PUBG"))
print(gaming_phone.charge(20))

print("\n--- Activity 2: Polymorphism Challenge ---")
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    print(v.move())
