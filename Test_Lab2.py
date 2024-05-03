import lab2

def check_min_max():
    inputdata=[1,2,3,4,6]
    answer=lab2.calc_avg_temp(inputdata)
    expected=[1,5]
    assert(answer==expected)

def check_average():
    inputdata=[2,2,2,2,2]
    answer=lab2.calc_avg_temp(inputdata)
    expected=2
    assert(answer==expected)
