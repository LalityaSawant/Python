import datetime
import pytz

class Account:
    """ Simple class for maintaining account """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self.transaction_list = [(Account._current_time(), balance)]
        print('Account created for {} your initial balance is {}'.format(name, self.show_balance()))

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transaction_list.append((Account._current_time(), amount))
            print('After depositing {} your balance is {}'.format(amount, self.show_balance()))

    def withdrawal(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
            print('After withdrawal of {} your balance is {}'.format(amount, self.show_balance()))
        else:
            print('Current balance {}, Insufficient funds for withdrawal'.format(self.show_balance()))

    def show_balance(self):
        return self.__balance

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount >0:
                transaction_type = 'Deposited'
            else:
                transaction_type = 'Withdrawn'
                amount *= -1
            print('{:8} {} on {} (local time was {})'.format(amount,transaction_type, date, date.astimezone()))


if __name__ == '__main__':

    timsAccount = Account('Tim', 2000)
    timsAccount.deposit(1000)
    timsAccount.withdrawal(2000)
    timsAccount.withdrawal(500)
    timsAccount.show_transactions()
    timsAccount.__balance = -300
    print(timsAccount.show_balance())
    print(timsAccount.__dict__)
