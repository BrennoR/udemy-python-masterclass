import datetime
import pytz


class Account:
    """ Simple account class with balance """           # <- Docstrings, good habit to get into

    @staticmethod
    def _current_time():    # underscore makes it clear that this method isn't intended to be used outside of the class
        utc_time = datetime.datetime.utcnow()   # also means, use method at own risk, may be removed or edited, etc...
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)]
        print("Account created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # must call self for attributes
            self.show_balance()     # must call self to use the method
            self._transaction_list.append((Account._current_time(), amount))     # use class name for static methods

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more than your account balance!")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


# technically speaking, the class constructor is the __new__ method which generally does not need to be defined
# except for in special cases

# Python 2 classes were different, old style. Only new style classes in Python 3

# self must be specified in Python!!

if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()

    tim.withdraw(500)
    # tim.show_balance()

    tim.show_transactions()

# The signature is the definition of the name and parameters of a function, as well as any returned value
# Use class name for using static methods, self can be used too but no advantage and performance actually suffers
# slightly, checking namespaces and so on

    steph = Account("Steph", 800)
    # steph._balance = 200        # no warning appears for our own classes!!
    steph.__balance = 200       # name mangling occurs :)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    print(steph.__dict__)
    # steph._Account__balance = 40        # this works
    # steph.show_balance()

# double underscore front and back does not get mangled, ex: __init__... single back does __hi_ √
