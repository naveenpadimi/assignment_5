# Challenge 1: Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)

input_list = list(map(int, input("Enter three numbers separated by ',': ").split(",")))

p = Point(*input_list)

sum_of_squares = p.sqSum()

print("The sum of squares is:", sum_of_squares)


# Challenge 2: Implement a Calculator Class
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num2 / self.num1


obj = Calculator(10, 94)

print("Addition:", obj.add())        
print("Subtraction:", obj.subtract())   
print("Multiplication:", obj.multiply())   
print("Division:", obj.divide())      


# Challenge 3: Implement the Complete Student Class

class Student:
    def __init__(self):
        self.__name = ""
        self.__rollNumber = ""
    
    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
    
    def getRollNumber(self):
        return self.__rollNumber




student = Student()

student.setName("Naveen")
student.setRollNumber("01223")


print("Name:", student.getName())          
print("Roll Number:", student.getRollNumber())

# Challenge 4: Implement a Banking Account

class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
acc = Account("Ashish", 5000)
savings_acc = SavingsAccount("Ashish", 5000, 5)

# Challenge 5: Handling a Bank Account


class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance
        
    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        
    def withdrawal(self, amount):
        self.balance -= amount

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interest_rate=0):
        super().__init__(title, balance)
        self.interest_rate = interest_rate
        
    def interestAmount(self):
        return (self.balance * self.interest_rate) / 100

acc = Account("Ashish", 2000)
acc.deposit(500)

balance = acc.getBalance()
print(balance)  
acc.withdrawal(500)
balance = acc.getBalance()
print(balance)  

savings_acc = SavingsAccount("Ashish", 2000, 5)
interest = savings_acc.interestAmount()
print("the interest :",interest)  





