class Transaction:
    def __init__(self, id_, date, state, operation_amount, currency_name, currency_code, description, from_, to):
        self.id_ = id_
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.currency_name = currency_name
        self.currency_code = currency_code
        self.description = description
        self.from_ = from_
        self.to = to
        self.is_broken = False
        self.check()


def check(self):
    check_list = [self.id_, self.date, self.state, self.operation_amout, self.currency_name, self.currency_code,
                  self.descrition, self.from_, self.to]
    if None in check_list:
        self.is_broken = True


def encode_important_data(self):
    attrs_to_encode = ("from_", "to")

    for attr in attrs_to_encode:
        getted_attr = getattr(self, attr)
        if "счет" in getted_attr.lower():
            number = getted_attr.split()[1]
            encoded_schet = getted_attr.split()[0] + "**" + number[-4:]
            setattr(self, attr, encoded_schet)
        else:
            number = getted_attr.split()[-1]
            encoded_number = number[:4] + " " + number[4:6] + "**" + "****" + number[-4:]
            encoded_card = ' '.join(getted_attr.split()[:-1]) + ' ' + encoded_number
            setattr(self, attr, encoded_card)


def show(self):
    formatted_time = self.date.strftime("%d.%m.%Y")
    str1 = f'{formatted_time} {self.description}\n'
    str2 = f'{self.from_} -> {self.to}\n'
    str3 = f'{self.operation_amout} {self.currency_name}\n'
    return str1 + str2 + str3


def __repr__(self):
    attributes = []
    for k, v in self.__dict__.items():
        string = f"{k}={v}"
        attributes.append(string)
    attrs = ", ".join(attributes)
    return f'{self.__class__.__name__}({attrs})'


def __eq__(self, other):
    return self.__dict__ == other.__dict__
