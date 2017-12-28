img_pxl = []
while True:
    try:
        row_pxl_raw = raw_input().split()
        row_pxl = [sum(map(int, pxl.split(',')))/3.0 for pxl in row_pxl_raw]
        img_pxl.append(sum(row_pxl)/len(row_pxl))
    except EOFError:
        break;
mean = sum(img_pxl)/len(img_pxl)
print 'day' if mean >= 60 else 'night'
