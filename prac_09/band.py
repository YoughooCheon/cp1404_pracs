from musician import Musician

class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add(self, musician: Musician):
        self.members.append(musician)

    def __str__(self):
        return f"{self.name} ({', '.join(str(member) for member in self.members)})"

    def play(self):
        return "\n".join(member.play() for member in self.members)