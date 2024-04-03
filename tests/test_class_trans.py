from account_transactions.class_trans import Transaction
from datetime import datetime
import pytest


@pytest.fixture
def class_obj1():
    return Transaction(179194306, datetime(2019, 5, 19), "EXECUTED", "6381.58",
                       "USD", "USD", "Перевод торганизации",
                       "Visa Gold 8326537236216459", "Счет 58518872592028002662")


@pytest.fixture
def class_obj2():
    return Transaction(179194306, "2019-05-19T12:51:49.023880", "EXECUTED", "6381.58",
                       "USD", "USD", "Перевод организации",
                       " МИР 5211277418228469", None)


def test_check1(class_obj1):
    class_obj1.check()
    assert not class_obj1.is_broken


def test_check2(class_obj2):
    class_obj2.check()
    assert class_obj2.is_broken


def test_encode_important_data(class_obj1):
    class_obj1.encode_important_data()
    assert class_obj1.from_ == "Visa Gold 8326 53** **** 6459"


def test_encode_important_data2(class_obj1):
    class_obj1.encode_important_data()
    assert class_obj1.to == "Счет **2662"


def test_show(class_obj1):
    class_obj1.encode_important_data()
    assert class_obj1.show() == ('19.05.2019 Перевод организации\n\
                                 Visa Gold 8326 53** **** 6459 -> Счет **2662\n\
                                  6381.58 USD\n')
