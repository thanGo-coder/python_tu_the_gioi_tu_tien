# Bài 4: Phân Loại Thời Tiết và Hoạt Động Gợi Ý
# Mô tả bài toán: Cho nhiệt độ nhiet_do (độ C) và trạng thái trời trang_thai_troi (chuỗi: "nang", "nhieu may", "mua", "tuyet").
# Input:
# nhiet_do: Một số thực.
# trang_thai_troi: Chuỗi ("nang", "nhieu may", "mua", "tuyet").
# Output: In ra dự báo thời tiết và gợi ý hoạt động.
# Ràng buộc: 50 <= nhiet_do <= 50
# Phân loại nhiệt độ:
# Nhiệt độ >= 30: "Nóng"
# Nhiệt độ 20-29: "Ấm áp"
# Nhiệt độ 10-19: "Mát mẻ"
# Nhiệt độ 0-9: "Lạnh"
# Nhiệt độ < 0: "Rất lạnh"
# Gợi ý hoạt động (dựa trên thời tiết tổng thể):
# Trời nắng (nang) và Nóng/Ấm áp: "Thích hợp đi chơi ngoài trời!"
# Trời mưa (mua): "Nên ở trong nhà, đọc sách hoặc xem phim."
# Trời tuyết (tuyet) và Rất lạnh: "Cẩn thận trượt ngã, mặc ấm và ở trong nhà."
# Các trường hợp còn lại: "Hoạt động bình thường."
# Ví dụ kiểm thử:
# Input: nhiet_do = 32, trang_thai_troi = "nang"
# Output: Thời tiết: Nóng. Gợi ý: Thích hợp đi chơi ngoài trời!

# Input: nhiet_do = 15, trang_thai_troi = "mua"
# Output: Thời tiết: Mát mẻ. Gợi ý: Nên ở trong nhà, đọc sách hoặc xem phim.

# Input: nhiet_do = -5, trang_thai_troi = "tuyet"
# Output: Thời tiết: Rất lạnh. Gợi ý: Cẩn thận trượt ngã, mặc ấm và ở trong nhà.

# Input: nhiet_do = 22, trang_thai_troi = "nhieu may"
# Output: Thời tiết: Ấm áp. Gợi ý: Hoạt động bình thường.
nhietdo=float(input("nhapnhietdongoaitroi                     "))
co=input("nhaploithoitiet             ")
if nhietdo<0:
    print("rất lạnh")
    print("can than truot nga mac am va o trong nha")
elif nhietdo>=0 and nhietdo <=9:
    print("lạnh")
    print("can than truot nga mac am va o trong nha")
elif nhietdo>=10 and nhietdo<=19:
    print("mát mẻ")
elif nhietdo>=20 and nhietdo<=29:
    print("ấm áp")
else:
    print("nóng")
