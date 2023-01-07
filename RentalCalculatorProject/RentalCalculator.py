class RentalIncomeCalc():
    def IncomeIntake(self):
        self.income = int(input('Income?'))
        # print(income)
        return self.income

    def ExpensesIntake(self):
        self.tax = int(input('Taxes?'))
        # print(tax)

        self.insurance = int(input('Insurance?'))
        # print(insurance)

        self.util = int(input('Utilities?'))
        # print(util)

        self.hoa = int(input('HOA?'))
        # print(hoa)

        self.lawn = int(input('Lawn/Snow?'))
        # print(lawn)

        self.vacancy = int(input('Vacancy?'))
        # print(vacancy)

        self.repairs = int(input('Repairs?'))
        # print(repairs)

        self.capex = int(input('Capex?'))
        # print(capex)

        self.property_mgmt = int(input('Property Management?'))
        # print(property_mgmt)

        self.mortgage = int(input('Monthly mortgage?'))
        # print(mortgage)

        self.expenses =  self.tax + self.insurance + self.util + self.hoa + self.lawn + self.vacancy + self.repairs + self.capex + self.property_mgmt + self.mortgage
        return self.expenses

        # return self.tax, self.insurance, self.util, self.hoa, self.lawn, self.vacancy, self.repairs, self.capex, self.property_mgmt, self.mortgage

    # def SumExpenses(self):
    #     self.expenses =  self.tax + self.insurance + self.util + self.hoa + self.lawn + self.vacancy + self.repairs + self.capex + self.property_mgmt + self.mortgage
    #     return self.expenses

    def CashFlowCalc(self):
        self.cashflow = self.income - self.expenses 
        return self.cashflow

    def IntakeInvestments(self):
        self.downpayment = int(input('How much money are you putting down for downpayment?'))
        # print(downpayment)

        self.closing_costs = int(input('How much money are you putting down for closing_costs?'))
        # print(closing_costs)

        self.budget = int(input('How much money are you putting down for budget?'))
        # print(budget)

        self.misc = int(input('How much money are you putting down for misc?'))
        # print(misc)

        self.investments = self.downpayment + self.closing_costs + self.budget + self.misc
        return self.investments

    # def SumInvestments(self):
    #     self.investments = self.downpayment + self.closing_costs + self.budget + self.misc
    #     return self.investments

    def RoiCalculator(self):
        self.yearly_cashflow = self.cashflow * 12
        self.roi = (self.yearly_cashflow/self.investments)*100
        print(self.roi)
        return self.roi

    def driverCode(self):
        # Get income from user
        self.income = self.IncomeIntake()
        
        # Get expenses from user
        self.expenses = self.ExpensesIntake()
        
        # Calculate cash flow
        self.cashflow = self.CashFlowCalc()
        
        # Get investments from user
        self.investments = self.IntakeInvestments()
        
        # Calculate ROI
        self.roi = self.RoiCalculator()

        print("Income:", self.income)
        print("Expenses:", self.expenses)
        print("Cash flow:", self.cashflow)
        print("Investments:", self.investments)
        print("ROI:", self.roi +"%")    
        

# myRoi = RentalIncomeCalc()
# myRoi.IncomeIntake()
# myRoi.ExpensesIntake()
# myRoi.SumExpenses()
# myRoi.RoiCalculator()

Testrun = RentalIncomeCalc()
Testrun.driverCode()


