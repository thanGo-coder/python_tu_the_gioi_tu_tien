# ### **Bài 5: Kiểm tra năm nhuận**

# - **Mô tả**:
    
#     Nhập một năm, kiểm tra xem năm đó có phải **năm nhuận** hay không.
    
#     (Năm nhuận là năm chia hết cho 4 nhưng không chia hết cho 100, trừ khi chia hết cho 400.)
    
# - **Input**:
    
#     `n = 2024`
    
# - **Output**:
    
#     `"Là năm nhuận"`
nam=int(input("nhapsonam"))
if nam%4==0 and nam%100!=0 or nam%400==0:
    print("namnhuan")
else:
     print("namkonhuan")   
        
        
        
        
        
        






