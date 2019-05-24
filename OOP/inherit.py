class Car():
    def __init__(self,model,year,topSpeed):
        self.model=model 
        self.year=year
        self.topSpeed=topSpeed

    def gearChange(self):
        print("GearChanged")

class MyCar(Car):
    def __init__(self,model,year,topSpeed,bal,sal):
        super().__init__(model,year,topSpeed)
        self.bal=bal
        self.sal=sal
