# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, contact):
        return f"{self.brand} {self.model} is calling {contact} 📞"

    def charge(self, amount):
        self.battery += amount
        return f"{self.model} charged. Battery is now {self.battery}% 🔋"

    def __str__(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%"

# Inheritance Example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        return f"{self.model} with {self.gpu} GPU is playing {game} 🎮"

    # Overriding method (Polymorphism)
    def charge(self, amount):
        self.battery += amount
        return f"{self.model} fast-charged with gaming mode. Battery: {self.battery}% ⚡"
