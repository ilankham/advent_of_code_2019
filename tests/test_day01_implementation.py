""" Unit tests for /solutions/day01_the_tyranny_of_the_rocket_equation.py """

from io import StringIO
import pytest

from solutions.day01_the_tyranny_of_the_rocket_equation import (
    SpacecraftModule,
    Spacecraft
)


EXAMPLE_VALUES1 = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]

EXAMPLE_VALUE_IDS1 = [
    f'mass={values_pair[0]}, fuel_required={values_pair[1]}'
    for values_pair
    in EXAMPLE_VALUES1
]

EXAMPLE_VALUES2 = [
    (12, 2),
    (14, 2),
    (1969, 966),
    (100756, 50346),
]

EXAMPLE_VALUE_IDS2 = [
    f'mass={values_pair[0]}, fuel_required={values_pair[1]}'
    for values_pair
    in EXAMPLE_VALUES2
]


@pytest.fixture(params=EXAMPLE_VALUES1, ids=EXAMPLE_VALUE_IDS1)
def example_modules_and_fuel_required1(request):
    return SpacecraftModule(request.param[0]), request.param[1]


@pytest.fixture(params=EXAMPLE_VALUES2, ids=EXAMPLE_VALUE_IDS2)
def example_modules_and_fuel_required2(request):
    return SpacecraftModule(request.param[0]), request.param[1]


@pytest.fixture()
def example_input_file():
    return StringIO(
        '\n'.join(str(values_pair[0]) for values_pair in EXAMPLE_VALUES1)
    )


@pytest.fixture()
def example_modules():
    return [
        SpacecraftModule(values_pair[0]) for values_pair in EXAMPLE_VALUES1
    ]


@pytest.fixture()
def example_total_fuel_required1():
    return sum(values_pair[1] for values_pair in EXAMPLE_VALUES1)


@pytest.fixture()
def example_total_fuel_required2():
    return sum(values_pair[1] for values_pair in EXAMPLE_VALUES2)


def test_SpacecraftModule_fuel_required_for_part1(
        example_modules_and_fuel_required1
):
    assert (
            example_modules_and_fuel_required1[0].fuel_required_for_part1 ==
            example_modules_and_fuel_required1[1]
    )


def test_SpacecraftModule_fuel_required_for_part2(
        example_modules_and_fuel_required2
):
    assert (
            example_modules_and_fuel_required2[0].fuel_required_for_part2 ==
            example_modules_and_fuel_required2[1]
    )


def test_Spacecraft_from_file(
        example_input_file,
        example_modules,
):
    assert (
            Spacecraft.from_file(example_input_file) ==
            example_modules
    )


def test_Spacecraft_fuel_required_for_part1(
    example_modules,
    example_total_fuel_required1,
):
    assert (
        Spacecraft(example_modules).fuel_required_for_part1 ==
        example_total_fuel_required1
    )


def test_Spacecraft_fuel_required_for_part2(
    example_modules,
    example_total_fuel_required2,
):
    assert (
        Spacecraft(example_modules).fuel_required_for_part2 ==
        example_total_fuel_required2
    )
