import datetime
import random

from credit.models import Client, Account, Credit

c = Client(name='Berdiev N.D.', birth_year=datetime.date(1994,5,5), work_place='Codify')
c1 = Client(name='Belek O.A.', birth_year=datetime.date(1974,3,11), work_place='IT')

def create_account(namber):
    listt = []
    for i in range(namber):
        listt.append(random.randrange(1, 10))
    return listt


#a = Account.objects.create(number=create_account(16), client=Client(id=3))
#a1 = Account.objects.create(number=create_account(16), client=Client(id=3))
# a2 = Account.objects.create(number=create_account(16), client=Client(id=4))
# a3 = Account.objects.create(number=create_account(16), client=Client(id=4))

#c = Credit.objects.create(sum=1000, account=Account(id=1))
# c1 = Credit.objects.create(sum=10000, account=Account(id=2))
# c2= Credit.objects.create(sum=11000, account=Account(id=3))
# c3 = Credit.objects.create(sum=12000, account=Account(id=4))