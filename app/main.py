from __future__ import annotations


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        self.__class__.alive.append(self)

    def die(self, animal: Animal) -> None:
        self.alive.remove(animal)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = False if self.hidden else True


class Carnivore(Animal):
    def bite(self, animal: Animal) -> None:
        if animal.hidden is False and not isinstance(animal, Carnivore):
            animal.health -= 50
        if animal.health <= 0:
            self.die(animal)
