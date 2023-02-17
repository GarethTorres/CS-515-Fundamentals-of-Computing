#Guizhi Xu
DIM = [31,28,31,30,31,30,31,31,30,31,30,31]
names_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
tlist = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
class Date(object):
# Question 1: Verify the constructor and string methods work #
    def __init__(self,month,day,year):
        self.month = month
        self.day = day
        self.year = year

    def __str__(self):
        if self.month < 10 :
            monthStr = '0' + str(self.month)
        else :
            monthStr = str(self.month)
        if self.day < 10 :
            dayStr = '0' + str(self.day)
        else :
            dayStr = str(self.day)
        yearStr = str(self.year)
        return monthStr + '/' + dayStr + '/' + yearStr

# Question 2: Create the equal operator #
    def __eq__(self,other):
        if type(self) == type(other) and self.month == other.month and self.day == other.day and self.year == other.year :
            return True
        else :
            return False 

# Question 3: Write a leap year function #
    def isLeapYear(self):
        if (self.year % 100 == 0) and (self.year % 400 == 0):
            return True
        elif (self.year % 100 != 0) and (self.year % 4 == 0):
            return True
        else:
            return False

# Question 4: Write a before function #
    def isBefore(self, d2) :
        if self.year < d2.year :
            return True
        elif self.year == d2.year and self.month < d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return True
        else :
            return False

# Question 5: Write a tomorrow function #
    def tomorrow(self):
        if  self.day == 31 and self.month == 12 :
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.day == DIM[self.month - 1] :
            self.month += 1
            self.day = 1
        else :
            self.day += 1

# Question 6: Write a day of the week function #
    def dayOfWeek(self):
        if self.month < 3:
           self.year = self.year - 1
           self.month = self.month + 10
           index = int((self.day + (2.6 * (self.month) - 0.2) + 5 * ((self.year % 100) % 4) + 3 * (self.year % 100) + 5 * ( int((self.year // 100)) % 4)) % 7)
        else :
           index = int((self.day + (2.6 * (self.month - 2) - 0.2) + 5 * ((self.year % 100) % 4) + 3 * (self.year % 100) + 5 * ( int((self.year // 100)) % 4)) % 7)
#        index = (self.year + self.year//4 - self.year//100 + self.year//400 + tlist[self.month - 1] + self.day) % 7
        return names_of_week[index - 1]

# Question 7: Create a days apart function #
    
    def daysApart(self, other) :
        n1 = self.year * 365 + self.day
        for i in range(0, self.month - 1) :
            n1 += DIM[i] 
        n1 += self.countLeapYears(self) 

        n2 = other.year * 365 + other.day
        for i in range(0, other.month - 1) :
            n2 += DIM[i]
        n2 += self.countLeapYears(other)
        if n2 < n1:
            return n1 - n2
        return (n2 - n1)

    def countLeapYears(self,day) :
        if day.month < 3 :
            day.year -= 1
        return int(day.year / 4) - int(day.year / 100) + int(day.year / 400)    

# Question 8: Create a Sub-Class Quantum- Date #
#class QuantumDate:
#    def randomize(self):



d = Date(11, 4, 2021) 

# >>> d = Date(11, 4, 2021) 
# >>> d.dayOfWeek() 
# ’Thursday’

print(Date(11, 4, 2021))
#>>> d = Date(11, 4, 2021) 
#>>> str(d)
#’11/04/2021’

d1 = Date(1, 1, 2000)
d2 = Date(1, 1, 2000)
d3 = Date(1, 1, 2001)

print(d1 == d2) 
print(d1.__eq__(d3))
#>>> d1 = Date(1, 1, 2000)
#>>> d2 = Date(1, 1, 2000)
#>>> d3 = Date(1, 1, 2001)
#>>> d1 == d2 True
#>>> d1 == d3 False

d1 = Date(1,1,1900)
d2 = Date(1,1,2020)
d3 = Date(1,1,2000)

print(d1.isLeapYear())
print(d2.isLeapYear())
print(d3.isLeapYear())

#>>> d1 = Date(1,1,1900)
#>>> d2 = Date(1,1,2020)
#>>> d3 = Date(1,1,2000)
#>>> d1.isLeapYear() False
#>>> d2.isLeapYear() True
#>>> d3.isLeapYear() True

d1 = Date(1,1,2000)
d2 = Date(1,1,2001)

print(d1.isBefore(d2))
print(d2.isBefore(d1))
print(d1.isBefore(d1))

#>>> d1 = Date(1,1,2000)
#>>> d2 = Date(1,1,2001)
#>>> d1.isBefore(d2) True
#>>> d2.isBefore(d1) False
#>>> d1.isBefore(d1) False


d = Date(12, 30, 2010) 
d.tomorrow()
print(d)
d = Date(2, 28, 2011) 
d.tomorrow()
print(d)
d.tomorrow()
print(d)
#>>> d = Date(12, 30, 2010) 
#>>> str(d)
#12/30/2010
#>>> d.tomorrow()
#>>> str(d)
#12/31/2010

#>>> d = Date(2, 28, 2011) 
#>>> d.tomorrow()
#>>> str(d)
#03/01/2011
#>>> d.tomorrow()
#>>> str(d)
#03/02/2011

d = Date(2, 12, 2022) 

print(d.dayOfWeek())
#>>> d = Date(11, 4, 2021) 
#>>> d.dayOfWeek() ’Thursday’

d1 = Date(1, 1, 2021) 
d2 = Date(1, 10, 2021) 

print(d1.daysApart(d2))
print(d2.daysApart(d1))

# >>> d1.daysApart(d2) 9
# >>> d2.daysApart(d1) 9



