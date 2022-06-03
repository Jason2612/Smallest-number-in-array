arry_num = [24,4,6,90,55,44,23,59,20]

def min_number(arry_num):
    smallest = arry_num[0]
    for numb in arry_num:
        if smallest > numb:
            smallest = numb
    return smallest
rs = min_number(arry_num)
print("So nho nhat trong mang: " + str(rs))