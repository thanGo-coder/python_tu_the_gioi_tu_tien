# ### **Bài 11: Giải phương trình bậc 1**

# - **Mô tả**:
    
#     Nhập `a` và `b` của phương trình `ax + b = 0`. Giải và in nghiệm hoặc kết luận vô nghiệm.
    
# - **Input**:
    
#     `a = 2, b = -4`
    
# - **Output**:
    
#     `"Nghiệm là x = 2"`

a=int(input("nhaphesoA  "))
b=int(input("nhaphesoB  "))
x='?'
if a==0:
    if b==0:
        print("vo_so_nghiem")
    else:
        print("vo_nghiem")
else:
    x=-a/b
    print(f"nghiem {x} ")


