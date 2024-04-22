def calculate_bmi(height,weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi=weight/(height*height)
    print("BMI = "+ str(bmi))
    return bmi
def is_healthy(bmivalue):
    if(bmivalue<18.5):
        print("UnderWeight")
    elif(bmivalue>25.0):
        print("OverWeight") 
    else:
        print("Normal Weight")

is_healthy(calculate_bmi(weight=10, height=1.73))