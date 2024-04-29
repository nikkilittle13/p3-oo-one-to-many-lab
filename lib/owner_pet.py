class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.pet_type = pet_type
        self.all.append(self)
    pass

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self 
        else:
            raise Exception("Invalid pet type")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    pass