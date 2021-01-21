""" Solutions for https://adventofcode.com/2019/day/1 """

from __future__ import annotations
from collections import UserList
from dataclasses import dataclass
from typing import TextIO


@dataclass
class SpacecraftModule:
    """ Data Model for a Spacecraft Module """
    mass: int

    @property
    def fuel_required_for_part1(self) -> int:
        """ Return spacecraft module fuel requirement for Part 1 """
        return self.mass//3 - 2

    @property
    def fuel_required_for_part2(self) -> int:
        """ Return spacecraft module fuel requirement for Part 2 """
        total_fuel_required = added_fuel_required = self.mass//3 - 2
        while (added_fuel_required := added_fuel_required//3 - 2) > 0:
            total_fuel_required += added_fuel_required
        return total_fuel_required


class Spacecraft(UserList):
    """ Data Model for a Spacecraft composed of Modules """

    @classmethod
    def from_file(cls, file_pointer: TextIO) -> Spacecraft:
        """ Create multiple Spacecraft Modules from file """
        return cls(
            SpacecraftModule(int(line))
            for line
            in file_pointer
        )

    @property
    def fuel_required_for_part1(self) -> int:
        """ Return spacecraft fuel requirement for Part 1 """
        return sum(
            module.fuel_required_for_part1
            for module
            in self
        )

    @property
    def fuel_required_for_part2(self) -> int:
        """ Return spacecraft fuel requirement for Part 2 """
        return sum(
            module.fuel_required_for_part2
            for module
            in self
        )


if __name__ == '__main__':

    # Read module information from provided data file.
    with open('../data/day01-data.txt') as fp:
        spacecraft = Spacecraft.from_file(fp)

    # Part 1: What is the sum of the fuel requirements for all of the modules
    # in the provided data file?
    print(
        f'Number of Spacecraft Modules read from data file: {len(spacecraft)}'
    )
    print(
        f'Fuel requirements for Part 1: {spacecraft.fuel_required_for_part1}'
    )

    # Part 2: What is the sum of the fuel requirements for all of the modules
    # in the provided data file when also taking into account the mass of the
    # added fuel?
    print(
        f'Fuel requirements for Part 2: {spacecraft.fuel_required_for_part2}'
    )
