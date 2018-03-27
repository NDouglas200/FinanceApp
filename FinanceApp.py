import sqlite3


class FinancesWeek:
    
    def __init__(self, date, WeekTotalInc):
        self.date = date
        self.WeekTotal = WeekTotalInc
        self.Budget = self.WeekTotal
        self.food = 0
        self.washing = 0
        self.predrinks = 0
        self.goingout = 0
        self.Cigaretts = 0
        self.other = 0
        
    def Food(self, foodAmount):
        self.food = foodAmount
        self.Budget = self.Budget - self.food
        print("The amount you spend on Food is now: ", self.food)
        # print("The total budget for the week is now: ", self.Budget)
            
    def Washing(self, washingAmount):
        self.washing = washingAmount
        self.Budget = self.Budget - self.washing
        print("The amount you spend on washing is now: ", self.washing)
        # print("The total budget for the week is now: ", self.Budget)
        
    def preDrinks(self, preDrinksAmount):
        self.predrinks = preDrinksAmount
        self.Budget = self.Budget - self.predrinks
        print("The amount you spend on pre drinks is now: ", self.predrinks)
        # print("The total budget for this week is now: ", self.Budget)
        
    def goingOut(self, goingOutAmount):
        self.goingout = goingOutAmount
        self.Budget = self.Budget - self.goingout
        print("The amount you spend on going out is now: ", self.goingout)
        # print("The total budget for this week is now: ", self.Budget)
        
    def cigaretts(self, cigAmount):
        self.Cigaretts = cigAmount
        self.Budget = self.Budget - self.Cigaretts
        print("The amount you spend on cigaretts is now: ", self.Cigaretts)
        # print("The total budget for this week is now: ", self.Budget)
    
    def Other(self, weedAmount):
        self.other = weedAmount
        self.Budget = self.Budget - self.other
        print("The amount you spend on weed is now: ", self.Weed)
        # print("The total budget for this week is now: ", self.Budget)
        
    def printInfo(self):
        self.totalOut = (self.food + self.washing + self.predrinks + self.goingout + self.Cigaretts + self.Weed)
        self.remainder = (self.WeekTotal - ((self.food + self.washing + self.predrinks + self.goingout + self.Cigaretts + self.Weed)))
        print("Total In: ", self.WeekTotal)
        print("Total Out: ", self.totalOut)
        print(" ")
        print("Food: ", self.food)
        print("Washing: ", self.washing)
        print("Pre-Drinks: ", self.predrinks)
        print("Going Out: ", self.goingout)
        print("Cigarettes: ", self.Cigaretts)
        print("Weed: ", self.Weed)
        print(" ")
        print("Remainder for the Week: ", self.remainder)
    
    def save(self):
        conn = sqlite3.connect('WeeklyFinData.db')
        c = conn.cursor()
        c.execute("INSERT INTO WeeklyFinData VALUES (?,?,?,?,?,?,?,?,?,?)", (self.date, self.food, self.washing, self.predrinks, self.goingout, self.Cigaretts, self.Weed, self.WeekTotal, self.totalOut, self.remainder))
        conn.commit()
        conn.close()
    
    def viewData(self):
        conn = sqlite3.connect('WeeklyFinData.db')
        c = conn.cursor()
        for row in c.execute('SELECT rowid,* FROM WeeklyFinData'):
            print(row)

        