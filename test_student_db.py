from student_db import StudentDB
import pytest


@pytest.fixture(scope="module")
def db():
    print("Just opened DB")
    db = StudentDB()
    db.connect('data.json')
    yield db
    print("closing DB")
    db.close()


def test_ramarao_data(db):
    ramarao_data = db.get_data("Ramarao Amara")
    assert ramarao_data["id"] == 1111
    assert ramarao_data["name"] == "Ramarao Amara"
    assert ramarao_data["result"] == "PASS"


def test_roja_data(db):
    ramarao_data = db.get_data("Roja Amara")
    assert ramarao_data["id"] == 2222
    assert ramarao_data["name"] == "Roja Amara"
    assert ramarao_data["result"] == "FAIL"
