class Employee:
    company ="UST"
    count =0;
    __name=""

    def __init__(self , name):
        self.__name=name;

    @property    
    def name(self):
        return self.__name;

    @name.setter   
    def name(self,val):
        self.__name = val;

    def employeeCount(self):
        global company
        global count
        print ("Working employee in {} are {}".format(company,count));