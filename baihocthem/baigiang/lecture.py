


# ham tim so lon nhat trong day so

def timSoLonNhat(l)->int:
    max =l[0]
    for i in l:
        if i>max:
            max=i
    return max
# def tim_so_lon_nhat


l = [1,6,2,6,33,91]
# loi goi ham
ketQua = timSoLonNhat(l)
print(ketQua)
print(timSoLonNhat(l))


