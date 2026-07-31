#smart Thermometer:
class Thermometer:
    def __init__(self,temp):
        self._temperature=temp
    def get_fahrenheit(self):
        return(self._temperature*9/5)+32
    def set_temperature(self,new_temp):
        if new_temp>=-273.15:
            self._temperature=new_temp
        else:
            print("Invalid Temperature")
t=Thermometer(25)
print("Fahrenheit=",t.get_fahrenheit())
t.set_temperature(-300)
       