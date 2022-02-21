import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()
def sort_rectangles(rect_records, record_title):
    current = 1
    
    while current != len(rect_records):
        hold = rect_records[current][record_title]
        holdv = rect_records[current]
        walker = current - 1
        while walker >= 0 and hold < rect_records[walker][record_title]:
            rect_records[walker + 1] = rect_records[walker]
            walker = walker - 1
            
        rect_records[walker+1] = holdv
        current = current + 1

    return rect_records

print(sort_rectangles(rectangle_records, record_title))
