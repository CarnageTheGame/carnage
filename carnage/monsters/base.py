# MIT License
#
# Copyright (c) 2022, Rodolfo Olivieri
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""Module that represents the base of a monster."""
from functools import cached_property
from random import SystemRandom

from carnage.database.models.monster import MonsterModel


class BaseMonster:
    """Class that maps the essential methods and properties of a monster."""

    def __init__(self, monster: MonsterModel) -> None:
        """Default constructor for a monster class mapping.

        .. seealso::
            All formulas defined in this class are based on the ORK framework:
            https://orkframework.com/guide/tutorials/status-system-setup/05-formulas/

            Another good resource for damage formula calculations are:
            https://gamedev.stackexchange.com/questions/14309/how-to-develop-rpg-damage-formulas

        :param monster: The monster attributes and data.
        """
        self.monster = monster
        self.current_hitpoints = monster.hitpoints
        self.random = SystemRandom()

    def take_damage(self, damage: int) -> None:
        """Method to make the monster take a damage.

        :param damage: The amount of damage dealt to the monster.
        """
        if self.current_hitpoints > 0:
            resulting_damage = self.current_hitpoints - damage
            self.current_hitpoints = (
                resulting_damage if resulting_damage > 0 else 0
            )
        else:
            self.current_hitpoints = 0

    def attack(self, damage_type: int, player_defense: int) -> int:
        """Calculate the monster attack and return it's value.

        :param damage_type: The type of the damage to be used. Either normal
            attack (1) or critical attack (2)
        :param player_defense: The amount of defense the target has.
        """
        damage = damage_type * (
            self.prefered_attack_attribute
            * self.monster.base_damage
            / ((100 + player_defense) / 100)
        )

        return int(damage)

    def magical_attack(
        self,
        damage_type: int,
        player_magical_defense: int,
    ) -> int:
        """Calculate the monster magical attack and return it's value.

        :param damage_type: The type of the damage to be used. Either normal
            attack (1) or critical attack (2)
        :param player_magical_defense: The amount of magical defense the target
            has.
        """
        damage = damage_type * (
            self.prefered_magical_attack_attribute
            * (
                self.monster.base_magical_damage
                * self.monster.base_magical_damage
            )
            / (self.monster.base_magical_damage + player_magical_defense)
        )

        return int(damage)

    def can_perform_attack(self) -> bool:
        """Handler method to define if the monster can perform an attack."""
        # TODO(r0x0d): Improve this in the future.
        random_number = self.random.randint(0, 100)
        return random_number >= self.monster.attack_threshold

    def can_perform_critical_attack(self) -> bool:
        """Handler method to define if a critical attack will be performed."""
        # TODO(r0x0d): Improve this in the future.
        random_number = self.random.randint(0, 100)
        return random_number >= self.monster.critical_attack_threshold

    @cached_property
    def is_alive(self) -> bool:
        """Property that handles if the monster is alive or not."""
        return self.current_hitpoints > 0

    @cached_property
    def prefered_attack_attribute(self) -> int:
        """Property that holds prefered attribute for attack formulas."""
        return self.monster.strength

    @cached_property
    def prefered_magical_attack_attribute(self) -> int:
        """Property that holds prefered magical attribute for magic attack."""
        return self.monster.intelligence
