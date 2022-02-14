import ast
points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())
def length_of_line(points_list, length):
    lengths_list = []
    for x in points_list:
        x1 = int(x[0][0])
        y1 = int(x[0][1])
        x2 = int(x[1][0])
        y2 = int(x[1][1])
        import math
        lengthofline = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        lengthofline = round(lengthofline,2)
        lengths_list.append(lengthofline)
    low = 0
    high = len(lengths_list) - 1
    mid = 0     
    while low <= high:
     
        mid = (high + low) // 2
     
        if lengths_list[mid] < length:
            low = mid + 1
     
        elif lengths_list[mid] > length:
            high = mid - 1
     
        else:
            return mid
            
                
     
    return -1

print(length_of_line(points_list, length))
