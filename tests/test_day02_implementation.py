""" Unit tests for /solutions/day02_1202_program_alarm.py """

from io import StringIO
import pytest

from solutions.day02_1202_program_alarm import (
    IntCodeProgram
)

EXAMPLE_INPUTS = [
    '1,9,10,3,2,3,11,0,99,30,40,50',
    '1,0,0,0,99',
    '2,3,0,3,99',
    '2,4,4,5,99,0',
    '1,1,1,4,99,5,6,0,99',
]

EXAMPLE_PATCH_OUTPUTS = [
    '1,12,2,3,2,3,11,0,99,30,40,50',
    '1,12,2,0,99',
    '2,12,2,3,99',
    '2,12,2,5,99,0',
    '1,12,2,4,99,5,6,0,99',
]

EXAMPLE_EXECUTION_OUTPUTS = [
    '3500,9,10,70,2,3,11,0,99,30,40,50',
    '2,0,0,0,99',
    '2,3,0,6,99',
    '2,4,4,5,99,9801',
    '30,1,1,4,2,5,6,0,99',
]

EXAMPLE_VALUE_IDS = [
    f'Example {n}'
    for n
    in range(1, len(EXAMPLE_INPUTS)+1)
]


@pytest.fixture(params=EXAMPLE_INPUTS, ids=EXAMPLE_VALUE_IDS)
def intcode_program_inputs(request):
    intcode_values = [int(value) for value in request.param.split(',')]
    return request.param, IntCodeProgram(intcode_values)


@pytest.fixture(
    params=zip(EXAMPLE_INPUTS, EXAMPLE_PATCH_OUTPUTS),
    ids=EXAMPLE_VALUE_IDS
)
def intcode_program_patches(request):
    input_values = [int(value) for value in request.param[0].split(',')]
    patch_values = [int(value) for value in request.param[1].split(',')]
    return IntCodeProgram(input_values), IntCodeProgram(patch_values)


@pytest.fixture(
    params=zip(EXAMPLE_INPUTS, EXAMPLE_EXECUTION_OUTPUTS),
    ids=EXAMPLE_VALUE_IDS
)
def intcode_program_execution_results(request):
    input_values = [int(value) for value in request.param[0].split(',')]
    output_values = [int(value) for value in request.param[1].split(',')]
    return IntCodeProgram(input_values), IntCodeProgram(output_values)


def test_IntCodeProgram_from_file(intcode_program_inputs):
    input_file = StringIO(intcode_program_inputs[0])
    assert (
        IntCodeProgram.from_file(input_file) ==
        intcode_program_inputs[1]
    )


def test_IntCodeProgram_patch(intcode_program_patches):
    assert (
        intcode_program_patches[0].patch() ==
        intcode_program_patches[1]
    )


def test_IntCodeProgram_executed_until_halted(
        intcode_program_execution_results
):
    assert (
            intcode_program_execution_results[0].executed_until_halted ==
            intcode_program_execution_results[1]
    )


def test_IntCodeProgram_find_patch_for_output():
    input_intcode = IntCodeProgram(
        int(value) for value in EXAMPLE_INPUTS[0].split(',')
    )
    output_intcode = IntCodeProgram(
        int(value) for value in EXAMPLE_EXECUTION_OUTPUTS[0].split(',')
    )
    noun = input_intcode[1]
    verb = input_intcode[2]
    output = output_intcode[0]
    assert (
        input_intcode.find_patch_for_output(output) ==
        (noun, verb)
    )
