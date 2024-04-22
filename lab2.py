def display_main_menu():
    print("Enter some numbers separated by commas(e.g 5,67,32)")


def get_user_input():
    floatlist=[]
    inside=input()
    x=inside.split(",")
    floatlist = [float(value) for value in x]
    return floatlist

def calc_avg_temp(nu):
    average=sum(nu)/len(nu)
    print("Average is" , average)
    return average

def calc_min_max_temp(na):
    least=min(na)
    most=max(na)
    print("Max is ", most)
    print("Min is ", least)
    answer=[least,most]
    return answer
def median_id(ne):
    sorted(ne)
    if len(ne)%2==0:
        print("Even")
        answ=ne[int(len(ne)-len(ne)/2)]+ne[int(len(ne)-len(ne)/2)-1]
    else:
        answ=ne[int(len(ne)-len(ne)/2)]
        print("Odd")
    print("Median is ", answ)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python prog")
    display_main_menu()
    numy=get_user_input()
    calc_avg_temp(numy)
    calc_min_max_temp(numy)
    median_id(numy)


if __name__ == "__main__":
    main()