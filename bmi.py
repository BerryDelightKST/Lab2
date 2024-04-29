def calculate_bmi(height,weight):
    print("Height = "+ str(height))
    print("Weight = "+ str(weight))
    bmi=weight/(height*height)
    print("BMI = "+ str(bmi))
    return bmi
def is_healthy(bmivalue):
    if(bmivalue<18.5):
        print("UnderWeight")
        return -1
    elif(bmivalue>25.0):
        print("OverWeight")
        return 1 
    else:
        print("Normal Weight")
        return  0

is_healthy(calculate_bmi(weight=10, height=1.73))