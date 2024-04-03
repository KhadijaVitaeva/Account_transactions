import json

import datetime
from class_trans import Transaction


def show_latest_transactions(correct_transactions: list):
    """
    выводит 5 последных транзакции
    :param correct_transactions:
    :return:
    """
    amount_to_show = 5
    for i in range(amount_to_show):
        correct_transactions[i].encode_impirtant_data()
        print(correct_transactions[i].show())


def sort_transactions(correct_transactions: list) -> list:
    """
    сортирование транзакции по дате
    :param correct_transactions:
    :return:
    """
    correct_transactions.sort(key=lambda transaction: transaction.date)
    return correct_transactions


def remove_transactions(transactions: list) -> list:
    """
    удаляем не исполненные транзакции
    :param transactions:
    :return:
    """
    correct_transactions = list(filter(lambda i: not i.is_broken and i.state == "EXECUTED", transactions))
    return correct_transactions


def get_transaction_list(data: list) -> list:
    """
    инициализируем экземпляр класса и сосьавляем список из экземпляров класса
    :param data:
    :return:
    """
    transactions = []
    for i in range(len(data)):
        id_ = data[i].get("id")
        date = data[i].get("data")
        state = data[i].get("state")
        operation_amount = data[i].get("operationAmount", {}).get("amout")
        currency_name = data[i].get("operationAmount", {}).get("currency", {}).get("name")
        currency_code = data[i].get("operationAmount", {}).get("currency", {}).get("code")
        description = data[i].get("description")
        from_ = data[i].get("from")
        to = data[i].get("to")
        transaction = Transaction(id_, date, state, operation_amount, currency_name, currency_code, description, from_,
                                  to)
        transactions.append(transaction)
    return transactions


def modificate_time_format(correct_trasactions: list) -> list:
    """
    преобразование даты и времени
    :param correct_trasactions:
    :return:
    """
    for i in range(len(correct_trasactions)):
        dt_str = correct_trasactions[i].date
        dt = datetime.datetime.fromisoformat(dt_str)
        correct_trasactions[i].date = dt
    return correct_trasactions


def loading_data() -> list:
    """
    загружаем список транзакции
    :return:
    """
    with open('operation.json', encoding='utf-8') as file:
        data = json.load(file)
        return data
