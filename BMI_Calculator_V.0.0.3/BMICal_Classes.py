class name:
    'This is for insert name'
    in_name=''
class weight_height:
    'This is for calculate BMI'
    def __init__(self,height=0,weight=0):
        self.height = float(height)
        self.weight = float(weight)
    def dispWHValue(self):
        print('Your height is:',self.height,'\nYour weight is: ',self.weight)
    def calBMI_Value(self,BMI=0,MaxWeight=0,MinWeight=0):
        self.BMI = self.weight/self.height**2
        self.MaxWeight = 22.9*self.height**2
        self.MinWeight = 18.5*self.height**2
        return(self.BMI,self.MaxWeight,self.MinWeight)

class BMIResult(weight_height):
    'BMI and MaxMinWeight results need to be calculated first (via calBMI_Value and calMaxMinWeight_Value)'
    def dispBMIResult(self):
        print('\nYour BMI result is:',self.BMI)
        if self.BMI >= 30:
            print('\nYou\'re experiencing dangerous Obesity')
            print('You shouldn\'t weight more than',self.MaxWeight)
        elif self.BMI >= 25 and self.BMI <= 29.9:
            print('\nYou\'re experiencing Obesity')
            print('You shouldn\'t weight more than',self.MaxWeight)
        elif self.BMI >= 23 and self.BMI <=24.9:
            print('\nYou\'re Overweight')
            print('You shouldn\'t weight more than',self.MaxWeight)
        elif self.BMI >= 18.5 and self.BMI <=22.9:
            print('\nYou\'re in overall good shape')
        else:
            print('\nYou\'re Underweight')
            print('You shouldn\'t weight less than',self.MinWeight)

#these objects will be called in MainProgram

#Place holder for debugging program
#a = BMIResult(1.5,100)
#a.calBMI_Value()
#a.dispBMIResult()
