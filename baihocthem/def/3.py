# ### **Bài 3: Tìm số lớn nhất trong hai số**

# - **Mô tả:** Viết một hàm nhận vào hai số nguyên và trả về số lớn hơn.
# - **Signature:**
    
#     **Python**
    
#     `def tim_lon_nhat(x: int, y: int) -> int:
#         pass`
    
# - **Ví dụ:**
def tim_lon_nhat(e)->int:
    for i in e :
        max=e[0]# bug
        if i>max:
            max=i
    return (max)
print(max)




e=[100000,20000,2390,131]
end=tim_lon_nhat(e)



