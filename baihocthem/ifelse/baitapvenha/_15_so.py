# ### **Bài 15: Tính tiền điện**

# - **Mô tả**:
    
#     Nhập số kWh điện tiêu thụ, tính tiền điện:
    
#     - <= 50 kWh: 1,700đ/kWh
#     - 51–100: 2,000đ/kWh
#     - 100: 2,500đ/kWh
# - **Input**:
    
#     `sodien = 120`
    
# - **Output**:
    
#     `"Tiền điện: 290,000đ"`
dien=int(input("nhapsodienbandadung          "))
tien=int(input("nhapsotien/kwh     "))
nop=(tien*dien)
print(nop)





