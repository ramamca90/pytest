import module
import pytest


@pytest.mark.parametrize('type1, type2, result',
                         [
                             (10, 20, 30),
                             (10.5, 20.5, 31),
                             ("Ramarao", " Amara", "Ramarao Amara")
                         ]
                         )
def test_add_types(type1, type2, result):
    assert module.add_types(type1, type2) == result


@pytest.mark.parametrize('type1, type2, result',
                         [
                             (10, 20, 30),
                             (10.5, 20.5, 31),
                             ("Ramarao", " Amara", "Ramarao Amara")
                         ]
                         )
def test_main(type1, type2, result):
    assert module.add_types(type1, type2) == result
