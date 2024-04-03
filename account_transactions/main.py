from account_transactions import functions

data = functions.loading_data()
transactions = functions.get_transaction_list(data)
correct_transactions = functions.remove_transactions(transactions)
datetime_transactions = functions.modificate_time_format(correct_transactions)
sorted_transactions = functions.sort_transactions(datetime_transactions)
functions.show_latest_transactions(sorted_transactions)
