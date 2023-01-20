from __future__ import annotations
from abc import ABC, abstractmethod


# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from unit import BaseUnit

class Skill(ABC):
    """
    Базовый класс умения
    """
    user = None
    target = None

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @property
    @abstractmethod
    def required_stamina(self):
        pass

    @abstractmethod
    def skill_effect(self):
        pass

    @abstractmethod
    def use(self, user, target):
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла
        """
        if user.stamina > self.required_stamina:
            return self.skill_effect()
        return f"{user.name} попытался использовать {self.name}, но у него не хватило выносливости."


class FuryPunch(Skill):
    name = "Свирепый пинок"
    required_stamina = 6
    damage = 12

    def skill_effect(self) -> str:
        """логика использования скилла -> return str
        в классе нам доступны экземпляры user и target - можно использовать любые их методы
        именно здесь происходит уменшение стамины у игрока применяющего умение и
        уменьшение здоровья цели.
        результат применения возвращаем строкой"""
        self.user.stamina -= self.required_stamina
        self.target.get_damage(self.damage)
        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику'

    def use(self, user, target):
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла
        """
        self.target = target
        self.user = user
        if user.stamina > self.required_stamina:
            return self.skill_effect()

        return f"{user.name} попытался использовать {self.name}, но у него не хватило выносливости."


class HardShot(Skill):
    name = "Мощный укол"
    required_stamina = 5
    damage = 15

    def skill_effect(self) -> str:
        self.user.stamina -= self.required_stamina
        self.target.get_damage(self.damage)

        return f'{self.user.name} использует {self.name} и наносит {self.damage} урона сопернику'

    def use(self, user, target):
        """
        Проверка, достаточно ли выносливости у игрока для применения умения.
        Для вызова скилла
        """
        self.target = target
        self.user = user

        if user.stamina > self.required_stamina:
            return self.skill_effect()

        return f"{user.name} попытался использовать {self.name}, но у него не хватило выносливости."
