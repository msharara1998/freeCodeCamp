from itertools import zip_longest


class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger = []

    def __str__(self):
        x = self.category_name.center(30, '*')
        for transact in self.ledger:
            if len(transact['description']) > 23:
                x += '\n' + transact['description'][:23].ljust(23) + "{:.2f}".format(transact['amount']).rjust(7)
            else:
                x += '\n' + transact['description'].ljust(23) + "{:.2f}".format(transact['amount']).rjust(7)
        x += '\nTotal: ' + "{:.2f}".format(self.get_balance())
        return x

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return float("{:.2f}".format(sum([x['amount'] for x in self.ledger])))

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + budget_category.category_name)
            budget_category.deposit(amount, "Transfer from " + self.category_name)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    # Obtain a list of withdrawals for each category
    categories_withdrawals = [[-transact['amount'] for transact in category.ledger if transact['amount'] < 0] for
                              category in categories]
    # Get the total withdrawals for each category
    total_withdrawals = [sum(withdrawals) for withdrawals in categories_withdrawals]
    # Get the percentage of withdrawals among total withdrawals of all categories
    percentage_spent = [int(10 * x / sum(total_withdrawals)+1) for x in total_withdrawals]
    x = ["Percentage spent by category"]
    # constructing labels of bar chart
    for i in range(110, 0, -10):
        x.append((str(i - 10) + '|').rjust(4))

    # filling the bar chart according to percentage spent
    for i in range(len(categories)):
        bars = ['o' * p for p in percentage_spent]
    vertical_bars = list(zip_longest(*bars, fillvalue=' '))
    vertical_bars.extend([(' ', ' ', ' ')] * (11 - len(vertical_bars)))

    for i in range(11):
        x[11 - i] += ' ' + '  '.join(vertical_bars[i])

    x.append('    ' + '--' * (2 + len(categories)))
    # constructing categories names
    names = [name.category_name for name in categories]
    vertical_names = zip_longest(*names, fillvalue=' ')
    for row in vertical_names:
        x.append('     ' + '  '.join(list(row)))
    return '\n'.join(x)
