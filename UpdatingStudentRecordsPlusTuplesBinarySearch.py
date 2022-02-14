import ast
student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()

def update_record(student_records, ID, record_title, data): 
    h = len(student_records)-1 
    l =0 
    pos = -1
    while h>=l:
        mid=(h+1)//2
        if ID == student_records[mid][0]:
            pos = mid
            break
        elif ID < student_records[mid][0]:
            h = mid - 1
        elif ID > student_records[mid][0]:
            l = mid + 1
    if pos == -1:
        return "Record not found"

    student_records[pos]= list(student_records[pos])
    if record_title ==  "ID":
        return("ID cannot be updated") 
    elif record_title == "Email":
        student_records[pos][1] = data
    elif record_title == "Mid1":
        student_records[pos][2] = int(data)
    elif record_title == "Mid2":
        student_records[pos][3] = int(data)
    student_records[pos] = tuple(student_records[pos]) 
    return (student_records)
             
    
print(update_record(student_records, ID, record_title, data))
    
    
