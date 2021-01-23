""" Solutions for https://adventofcode.com/2019/day/2 """

from __future__ import annotations
from collections import UserList
from typing import TextIO, Tuple


class IntCodeProgram(UserList):
    """ Data Model for an IntCode Program """

    @classmethod
    def from_file(cls, file_pointer: TextIO) -> IntCodeProgram:
        """ Create IntCode Program from file """
        return cls(
            int(value)
            for value
            in file_pointer.read().rstrip().split(',')
        )

    def patch(self, noun: int = 12, verb: int = 2) -> IntCodeProgram:
        """ Return IntCode Program with specified patches """
        patched_intcode = self.copy()
        patched_intcode[1] = noun
        patched_intcode[2] = verb
        return patched_intcode

    @property
    def executed_until_halted(self) -> IntCodeProgram:
        """ Return IntCode Program after executing until halted """
        executed_intcode = self.copy()
        instruction_pointer = 0
        while (opcode := executed_intcode[instruction_pointer]) != 99:
            opcode_param1 = executed_intcode[
                executed_intcode[instruction_pointer + 1]
            ]
            opcode_param2 = executed_intcode[
                executed_intcode[instruction_pointer + 2]
            ]
            opcode_param3 = executed_intcode[instruction_pointer + 3]
            if opcode == 1:
                executed_intcode[opcode_param3] = opcode_param1 + opcode_param2
            elif opcode == 2:
                executed_intcode[opcode_param3] = opcode_param1 * opcode_param2
            instruction_pointer += 4
        return executed_intcode

    def find_patch_for_output(self, target_output: int) -> Tuple[int, int]:
        """ Return 'noun' and 'verb' needed to obtain specific 'output' """
        for noun in range(99):
            for verb in range(99):
                patched_intcode = self.copy().patch(noun, verb)
                try:
                    executed_intcode = patched_intcode.executed_until_halted
                except IndexError:
                    continue
                if executed_intcode[0] == target_output:
                    return executed_intcode[1], executed_intcode[2]


if __name__ == '__main__':

    # Read IntCode Program information from provided data file.
    with open('../data/day02-data.txt') as fp:
        intcode = IntCodeProgram.from_file(fp)

    # Part 1: What value is left in position 0 of the IntCode in the provided
    # data file after it's patched to "1202 program alarm" state and executed?
    intcode_with_1202_patch = intcode.patch()
    executed_patched_intcode = intcode_with_1202_patch.executed_until_halted
    print(
        f'Number of IntCode instructions read from data file: {len(intcode)}'
    )
    print(
        f'Value at Position 0 for Part 1: {executed_patched_intcode[0]}'
    )

    # Part 2: What values should be patched in place of position 1 (noun) and
    # position 2 (verb) of the IntCode in the provided data file so that the
    # value in position 0 becomes 19690720?
    noun2, verb2 = intcode.find_patch_for_output(19690720)
    print(f'Noun (position 1) value for Part 2: {noun2}')
    print(f'Verb (position 1) value for Part 2: {verb2}')
    print(f'The quantity 100 * noun + verb for Part 2: {100 * noun2 + verb2}')
