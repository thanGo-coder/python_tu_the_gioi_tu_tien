# ### **Bài 12: Xác định quý trong năm**

# - **Mô tả**:
    
#     Nhập số tháng (1–12), in ra quý của tháng đó:
    
#     - Tháng 1–3: Quý 1
#     - Tháng 4–6: Quý 2
#     - Tháng 7–9: Quý 3
#     - Tháng 10–12: Quý 4
# - **Input**:
    
#     `month = 8`
    
# - **Output**:
    
#     `"Tháng 8 thuộc quý 3"`
thang=int(input("nhapthang     "))
if thang>=1 and thang<=3:
    print("quy1")
elif thang>=4 and thang<=6:
    print("quy2")
elif thang >=7 and thang<=9:
    print("quy3")
elif thang >=10 and thang <=12:
    print("quy4")
