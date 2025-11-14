# Lý thuyết

![image.png](attachment:8c9971d9-4701-4693-8db1-c3b184f0039a:image.png)

![image.png](attachment:9157ff9b-68c9-4fb7-9694-84c96550616b:image.png)

---

### **Chương 7: Hàm (Function) - Xây dựng các "Khối Lệnh Tái Sử Dụng"**

---

### **1. Hàm là gì & Tại sao lại quan trọng?**

- **Hàm là gì?**
    - Hãy tưởng tượng một cái **máy pha cà phê** ☕. Bạn chỉ cần cho nguyên liệu (hạt cà phê, nước) vào và bấm nút, nó sẽ tự động làm cà phê cho bạn. Bạn không cần biết bên trong nó hoạt động thế nào.
    - Hàm trong lập trình cũng vậy: Là một **khối mã được đặt tên**, thực hiện một **nhiệm vụ cụ thể**. Bạn "gọi" nó bằng tên, đưa cho nó "đầu vào" (nếu cần), và nó sẽ thực hiện công việc rồi có thể trả lại "kết quả".
- **Tại sao cần dùng Hàm?**
    1. **Tái sử dụng mã:** Viết code một lần, dùng nhiều nơi. **Không cần lặp lại (Don't Repeat Yourself - DRY)**!
    2. **Mã dễ đọc hơn:** Chia bài toán lớn thành các phần nhỏ, mỗi phần có một cái tên dễ hiểu (ví dụ: `tinh_tong()`, `kiem_tra_so_chan()`).
    3. **Dễ sửa lỗi:** Nếu có lỗi ở một chức năng, bạn chỉ cần sửa trong hàm đó, không cần tìm khắp nơi trong chương trình.
    4. **Tổ chức tốt:** Giúp chương trình của bạn gọn gàng, có cấu trúc như một ngôi nhà có các phòng riêng biệt.

---

### **2. "Định nghĩa" Hàm: `def`**

Để Python biết về "công cụ" bạn muốn tạo, bạn phải "định nghĩa" (hay khai báo) nó trước.

- **Cú pháp cơ bản:**
    
    ```python
    def ten_ham(tham_so_1, tham_so_2, ...):
        # 🎯 Các lệnh của hàm (PHẢI THỤT LỀ vào trong)
        #    ...
        # ↩️ (Tùy chọn) Có thể có lệnh 'return' để TRẢ LẠI KẾT QUẢ
    ```
    
    - `def`: Từ khóa **bắt buộc** để bắt đầu định nghĩa hàm.
    - `ten_ham`: **Tên** mà bạn đặt cho hàm (nên ngắn gọn, có ý nghĩa, dùng chữ thường và dấu gạch dưới).
    - `()`: Luôn có **dấu ngoặc đơn**. Bên trong là các **tham số** (đầu vào của hàm).
        - ***Tham số***: Các biến mà hàm nhận để làm việc. (Ví dụ: `ten` trong `chao_ten(ten)`). Tham số là **tùy chọn** (hàm có thể không có tham số nào).
    - `:`: Dấu hai chấm **kết thúc** dòng định nghĩa hàm.
    - **Thụt lề (Indentation):** **CỰC KỲ QUAN TRỌNG!** Tất cả các lệnh thuộc về hàm **phải được thụt lề** vào trong (thường là 4 dấu cách) để Python hiểu đây là một khối code của hàm.
- **Ví dụ trực quan:**Python
    
    ```python
    # Hàm 1: Không cần đầu vào, chỉ in lời chào
    def in_loi_chao_chung():
        print("Chào mừng bạn!")
    
    # Hàm 2: Cần 1 đầu vào (tên), để chào cá nhân
    def chao_theo_ten(ten_nguoi_dung):
        print(f"Xin chào, {ten_nguoi_dung}!")
    
    # Hàm 3: Cần 2 đầu vào (số1, số2), để tính và in tổng
    def hien_thi_tong_hai_so(so_thu_nhat, so_thu_hai):
        tong = so_thu_nhat + so_thu_hai
        print(f"Tổng là: {tong}")
    ```
    

---

### **3. "Gọi" Hàm: Sử dụng công cụ của bạn**

Sau khi định nghĩa, bạn có thể "gọi" (sử dụng) hàm bất cứ khi nào bạn cần nó thực hiện công việc.

- **Cú pháp:** `ten_ham(gia_tri_cho_tham_so_1, gia_tri_cho_tham_so_2, ...)`
    - ***Đối số***: Các giá trị thực tế mà bạn truyền vào khi gọi hàm. (Ví dụ: `"An"` khi gọi `chao_theo_ten("An")`).
- **Ví dụ trực quan:**Python
    
    ```python
    # ✅ Gọi hàm không tham số
    in_loi_chao_chung()
    # Output: Chào mừng bạn!
    
    # ✅ Gọi hàm với 1 đối số
    chao_theo_ten("Minh")
    # Output: Xin chào, Minh!
    
    ten_hoc_sinh = "Lan"
    chao_theo_ten(ten_hoc_sinh) # Có thể dùng biến làm đối số
    # Output: Xin chào, Lan!
    
    # ✅ Gọi hàm với 2 đối số
    hien_thi_tong_hai_so(5, 10)
    # Output: Tổng là: 15
    
    diem_a = 7
    diem_b = 9
    hien_thi_tong_hai_so(diem_a, diem_b)
    # Output: Tổng là: 16
    ```
    

---

### **4. Trả về Giá trị: Lệnh `return`**

Nhiều khi, hàm không chỉ in ra màn hình mà còn cần **trả lại một kết quả** để bạn có thể lưu trữ, sử dụng tiếp trong phép tính khác. Lệnh `return` làm điều này.

- **Ý nghĩa:** Khi Python gặp `return`, hàm sẽ **kết thúc ngay lập tức** và "gửi" giá trị đó về nơi nó được gọi.
- **Cú pháp:** `return gia_tri_can_tra_ve`
- **Ví dụ trực quan về `return`:**Python
    
    ```python
    # 🌟 Hàm này tính tổng VÀ TRẢ VỀ KẾT QUẢ
    def tinh_tong_va_tra_ve(so_a, so_b):
        ket_qua = so_a + so_b
        return ket_qua # 🎯 Trả về giá trị của 'ket_qua'
    
    # ✅ Gọi hàm và LƯU KẾT QUẢ vào một biến
    so_1 = 10
    so_2 = 20
    tong_nhan_duoc = tinh_tong_va_tra_ve(so_1, so_2)
    print(f"Tổng nhận được từ hàm là: {tong_nhan_duoc}")
    # Output: Tổng nhận được từ hàm là: 30
    
    # ✅ Có thể dùng kết quả trả về trong các phép tính khác
    tong_gap_doi = tinh_tong_va_tra_ve(3, 4) * 2
    print(f"Tổng gấp đôi là: {tong_gap_doi}")
    # Output: Tổng gấp đôi là: 14 (vì (3+4)*2)
    ```
    

---

### **💡 PHÂN BIỆT `print()` và `return` TRONG HÀM**

| **Tính năng** | **print() trong hàm** | **return trong hàm** |
| --- | --- | --- |
| **Mục đích** | **Hiển thị thông tin** ra màn hình (Console) cho người dùng nhìn thấy. | **Trả lại một giá trị** từ hàm về nơi hàm được gọi, để có thể sử dụng tiếp. |
| **Giá trị trả về** | ❌ Hàm không trả về giá trị để bạn có thể lưu trữ hay sử dụng tiếp. | ✅ Hàm trả về **chính xác giá trị** bạn chỉ định, có thể lưu vào biến hoặc dùng trong tính toán khác. |
| **Kết thúc hàm** | Hàm **tiếp tục chạy** các lệnh sau `print()` cho đến khi hết hàm hoặc gặp `return`. | Hàm **kết thúc NGAY LẬP TỨC** khi gặp `return`. Các lệnh sau `return` sẽ không được thực hiện. |
| **Ví dụ** | `def show_sum(a, b): print(a + b)    k = show_sum(2, 3) # k sẽ là Noneprint(k) # Output: 5\nNone` | `pythondef get_sum(a, b): return a + bk = get_sum(2, 3) # k sẽ là 5print(k) # Output: 5` |

---

---

### **5. Tham số mặc định (Default Parameters)**

Bạn có thể giúp hàm linh hoạt hơn bằng cách gán một giá trị mặc định cho tham số. Nếu khi gọi hàm mà bạn không truyền giá trị cho tham số đó, nó sẽ tự động dùng giá trị mặc định.

- **Cú pháp:** `def ten_ham(tham_so_bat_buoc, tham_so_mac_dinh=gia_tri_mac_dinh):`
    - **Quy tắc:** Các tham số có giá trị mặc định **phải được đặt sau** các tham số không có giá trị mặc định.
- **Ví dụ trực quan:**
    
    ```python
    def chao_nguoi_dung(ten="Khách"): # 👈 'ten' có giá trị mặc định là "Khách"
        print(f"Xin chào, {ten}!")
    
    # ✅ Trường hợp 1: Truyền giá trị cho 'ten'
    chao_nguoi_dung("Lan")
    # Output: Xin chào, Lan!
    
    # ✅ Trường hợp 2: KHÔNG truyền giá trị cho 'ten'
    chao_nguoi_dung()
    # Output: Xin chào, Khách! (sẽ dùng giá trị mặc định)
    
    # ✅ Ví dụ với nhiều tham số
    def tinh_gia(san_pham, so_luong=1, don_gia=100):
        thanh_tien = so_luong * don_gia
        print(f"Sản phẩm {san_pham}: {thanh_tien} VND")
    
    tinh_gia("Sách")                  # so_luong=1, don_gia=100
    # Output: Sản phẩm Sách: 100 VND
    tinh_gia("Bút", so_luong=5)       # don_gia=100
    # Output: Sản phẩm Bút: 500 VND
    tinh_gia("Vở", so_luong=2, don_gia=50)
    # Output: Sản phẩm Vở: 100 VND
    ```
    

---

### **Ứng dụng Thực tế của Hàm:**

Hàm là một công cụ không thể thiếu trong mọi chương trình lớn:

- **Tính toán:** `tinh_dien_tich_hinh_tron(ban_kinh)`, `tinh_bmi(can_nang, chieu_cao)`.
- **Kiểm tra điều kiện:** `kiem_tra_so_nguyen_to(so)`, `la_nam_nhuan(nam)`.
- **Xử lý dữ liệu:** `chuan_hoa_chuoi(chuoi)`, `tim_ki_tu_lon_nhat(chuoi)`.
- **Xây dựng trò chơi:** `di_chuyen_nguoi_choi(huong)`, `kiem_tra_thua_thang(ban_co)`.
- **Tạo menu tương tác:** `hien_thi_menu_chinh()`, `xu_ly_lua_chon_nguoi_dung()`.