from dealership.customers import Customer, Employee
from dealership.vehicles import Car, Motorcycle, Truck

class Contract(object):
  def __init__(self , vehicle, customer):
    self.vehicle = vehicle
    self.customer = customer

class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        super(BuyContract, self).__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
        
    def total_value(self):
        discount = 0
        if(self.customer.is_employee()):
            discount = self.customer.DISCOUNT
        total = self.vehicle.sale_price() + (self.vehicle.INTREST_RATE * self.monthly_payments * self.vehicle.sale_price()/100)
        return total - (total * discount)
      
    def monthly_value(self):
        return self.total_value() / self.monthly_payments

class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        super(LeaseContract, self).__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
      discount = 0
      if(self.customer.is_employee()):
         discount = self.customer.DISCOUNT
      total = self.vehicle.sale_price() + (self.vehicle.sale_price() * self.vehicle.LEASE_MUTIPLIER / self.length_in_months)
      
      return total - ( total * discount)
        
    def monthly_value(self):
      return self.total_value() / self.length_in_months
