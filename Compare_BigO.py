# === When should I use each one? ===
"""
Structure   -   Khi nào dùng                            -               SDET
List        -   Dữ liệu có thứ tự                       -               Danh sách test cases, log entries
Tuple       -   Dữ liệu cố định, không đổi              -               Config values, hằng số, return nhiều giá trị
Set         -   Cần loại trùng, kiểm tra tồn tại nhanh, phép toán tập hợp   -   Kiểm tra fields, tags, unique values
Dict        -   Dữ liệu key-value, truy cập theo tên    -               API repone (JSON), config, test data, mapping
"""

# === Độ phức tạp Big O ===

"""
| Thao tác            | List       | Tuple      | Set      | Dict     |
|---------------------|------------|------------|----------|----------|
| Truy cập theo index | O(1)       | O(1)       | —        | —        |
| Truy cập theo key   | —          | —          | —        | O(1)     |
| Tìm kiếm            | O(n)       | O(n)       | O(1)     | O(1)     |
| Thêm cuối           | O(1)       | —          | O(1)     | O(1)     |
| Thêm đầu/giữa       | O(n)       | —          | O(1)     | O(1)     |
| Xóa theo giá trị    | O(n)       | —          | O(1)     | O(1)     |
| Xóa theo index      | O(n)       | —          | —        | —        |
| Sắp xếp             | O(n log n) | O(n log n) | —        | —        |
"""

# Chậm - tìm kiếm O(n) trên List
valid_code = [200, 201, 204, 301, 302]
if status_code in valid_code:           # Phải duyệt qua từng phần từ
    pass

# Nhanh - tìm kiếm O(1) trên set
valid_code = {200, 201, 204, 301, 302}
if status_code in valid_code:           # Truy cập trực tiếp qua hash
    pass