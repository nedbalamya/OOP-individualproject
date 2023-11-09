class Chair:
    def __init__(self, chair_id, color, material):
        self.chair_id = chair_id
        self.color = color
        self.material = material
        self.assigned_to = None

    def assign_chair(self, person):
        if self.assigned_to is None:
            self.assigned_to = person
            print(f"Chair {self.chair_id} assigned to {person.name}")
        else:
            print(f"Chair {self.chair_id} is already assigned.")

    def unassign_chair(self):
        if self.assigned_to is not None:
            print(f"Chair {self.chair_id} unassigned from {self.assigned_to.name}")
            self.assigned_to = None
        else:
            print(f"Chair {self.chair_id} is not currently assigned.")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ChairManager:
    def __init__(self):
        self.chairs = []

    def add_chair(self, chair):
        self.chairs.append(chair)

    def list_chairs(self):
        for chair in self.chairs:
            status = "Assigned to " + chair.assigned_to.name if chair.assigned_to else "Unassigned"
            print(f"Chair {chair.chair_id} - Color: {chair.color}, Material: {chair.material}, Status: {status}")
