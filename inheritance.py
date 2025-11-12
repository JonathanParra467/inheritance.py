
# Creating and using a Employee SuperClass
# Employee and a Her subclass
# along with instantiating (making objects)

class Employee:
    # Employee is a Superclass of the ProductionEmployee class
    def __init__(self,name, number):
        self.__name = name
        self.__number = number
    
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
    def set_name(self, name):
        self.__name = name
    
    def set_pet_id(self, number):
        self.__number = number


class ProductionWorker(Employee):
        
        def __init__(self, name, number, shift, hourly_pay_rate):
            super().__init__(name, number)

            self.__shift = shift

            self.__hourly_pay_rate = hourly_pay_rate

        def get_shift(self):
            return self.__shift
    
        def get_hourly_pay_rate(self):
            return self.__hourly_pay_rate
        
        def set_shift(self, shift):
            self.__shift = shift
    
        def set_hourly_pay_rate(self, hourly_pay_rate):
            self.__hourly_pay_rate = hourly_pay_rate


def main():

    name = input("enter employee name: ")
    employee_number = input("enter employee number: ")
    shift = input("enter shift number: ")
    pay_rate = input("enter pay rate: ")



    worker = ProductionWorker(name, employee_number, shift, pay_rate)

    print(worker.get_name())
    print(worker.get_number())
    print(worker.get_shift())
    print(worker.get_hourly_pay_rate())

main()


