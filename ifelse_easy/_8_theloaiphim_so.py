# ### **Bài 8: Quyết định xem phim theo tuổi và thể loại**

# - **Mô tả:** Cho tuổi của người xem `tuoi_xem` và thể loại phim `the_loai` (chuỗi: "kinh dị", "hành động", "hài hước").
#     - Phim kinh dị yêu cầu tuổi từ 18 trở lên.
#     - Phim hành động yêu cầu tuổi từ 13 trở lên.
#     - Phim hài hước không giới hạn tuổi.
# - **Yêu cầu:** In ra "Có thể xem phim" hoặc "Không thể xem phim".
# - **Thiết lập ban đầu:**
    
#     **Python**
    
#     `tuoi_xem = 15 # Thay đổi giá trị này
#     the_loai = "hành động" # Thay đổi giá trị này`
    
# - **Ví dụ kiểm thử:**
#     - **Input:** `tuoi_xem = 20, the_loai = "kinh dị"` **Output:** `Có thể xem phim`
#     - **Input:** `tuoi_xem = 15, the_loai = "kinh dị"` **Output:** `Không thể xem phim`
#     - **Input:** `tuoi_xem = 12, the_loai = "hành động"` **Output:** `Không thể xem phim`
#     - **Input:** `tuoi_xem = 15, the_loai = "hành động"` **Output:** `Có thể xem phim`
#     - **Input:** `tuoi_xem = 10, the_loai = "hài hước"` **Output:** `Có thể xem phim`
tuoi=int(input("nhaptuoicuaban     "))
theloai=(input("nhaptheloaiphim     "))
if tuoi>=18 and theloai== "phimkinhdi":
    print("true")
elif tuoi >=13 and theloai== "phimhanhdong":
    print("true")
elif tuoi>0 and theloai=="phimhai":
    print("true")
else:
    print("False")
