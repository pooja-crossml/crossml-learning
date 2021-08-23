from django.db import models
from django.utils.timezone import now

EXPENSE_CHOICE = [
    ("Travel","Travel"),
    ("Education","Education"),
    ("Gifts_and_Donations","Gifts_and_Donations"),
    ("Investments","Investments"),
    ("Bills_and_Utilities","Bills_and_Utilities"),
    ("Food_and_Dining","Food_and_Dining"),
    ("Health_and_Fitness","Health_and_Fitness"),
    ("Personal_Care","Personal_Care"),
    ("Fees_and_Charges","Fees_and_Charges")
    ]

ADD_EXPENSE_TYPE = [
    ("Expense","Expense"),
    ("Income","Income")
]

class Budget(models.Model):
    budget = models.IntegerField()


class Expenses(models.Model):
    category = models.CharField(max_length=20, choices= EXPENSE_CHOICE)
    name = models.CharField(max_length=100)
    comments = models.TextField()
    add_money = models.CharField(max_length = 10 , choices = ADD_EXPENSE_TYPE )
    quantity = models.IntegerField()
    Date = models.DateField(default = now)

    def __str__(self):
        return self.category
