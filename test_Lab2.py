import lab2
print("Testing lab2 codes")

def test_min_max():
    inputdata=[1,2,3,4,5]
    answer=lab2.calc_min_max_temp(inputdata)
    expected=[1,5]
    assert(answer==expected)

def test_average():
    inputdata=[2,2,2,2,2]
    answer=lab2.calc_avg_temp(inputdata)
    expected=2
    assert(answer==expected)

def test_median():
    inputdata1=[1,2,3,4,5]
    inputdata2=[1,2,3,4,5,6]
    answer1=lab2.median_id(inputdata1)
    answer2=lab2.median_id(inputdata2)
    expected1=3
    expected2=3.5
    assert(answer1==expected1 and answer2==expected2)