

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname}, Superpower: {self.superpower}, Health: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Bruce Wayne", "Batman", "Rich", 100, "I'm Batman!")


print("Hero's name:", hero.get_name())
print("Hero's health before:", hero.health_points)
hero.double_health()
print("Hero's health after doubling:", hero.health_points)
print("Hero's details:", hero)
print("Length of hero's catchphrase:", len(hero.catchphrase))