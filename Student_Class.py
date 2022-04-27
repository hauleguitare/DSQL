"""
Ý TƯỞNG: ÁP DỤNG TÍNH KẾ THỪA VÀ TÍNH ĐA HÌNH
- CLASS STUDENT KHỞI TẠO ĐỐI TƯỢNG:
    + THUỘC TÍNH:
        - ID
        - HỌ VÀ TÊN
        - NĂM SINH
        - KHỐI
        - ĐIỂM TRUNG BÌNH
        - XẾP LOẠI
    + PHƯƠNG THỨC:
        - HỌ VÀ TÊN HỌC SINH
        - NĂM SINH PHÂN LOẠI THEO KHỐI, 2003: LỚP 12; 2004: LỚP 11; 2005: LỚP 10
        - THỂ HIỆN THÔNG TIN HỌC SINH ĐIỂM TB VÀ XẾP LOẠI:
            + 8.0 >=: XẾP LOẠI GIỎI
            + 6.5 >= VÀ < 8.0: XẾP LOẠI KHÁ
            + 5.0 >= VÀ < 6.5: XẾP LOẠI TRUNG BÌNH
            + 3.5 >= VÀ < 5.0: XẾP LOẠI YẾU (THI LẠI CẬP NHẬT SAU)
            + < 3.5: XẾP LOẠI KÉM (LƯU BAN CẬP NHẬT SAU)
        - TỔNG SỐ HỌC SINH ĐANG HỌC

- CLASS STUDENT_10, STUDENT_11, STUDENT_12 KẾ THỪA STUDENT:
    + THUỘC TÍNH:
        - ID
        - HỌ VÀ TÊN
        - NĂM SINH
        - LỚP
        - ĐIỂM TRUNG BÌNH
        - XẾP LOẠI
    + PHƯƠNG THỨC:
        - HỌ VÀ TÊN HỌC SINH
        - CHIA LỚP THEO KHỐI
        - THỂ HIỂN THÔNG TIN HỌC SINH TRONG KHỐI VÀ XẾP LOẠI:
            + GIỎI NHẤT KHỐI
            + TẤT CẢ HỌC SINH ĐANG HỌC TRONG KHỐI
        - TỔNG SỐ HỌC SINH ĐANG HỌC

- CLASS STUDENT_ID:
    + THUỘC TÍNH:
        - ID
    + PHƯƠNG THỨC:
        - GEN ID THEO NĂM HỌC, KHỐI, LỚP VÀ SỐ THỨ TỰ
"""


from Course_Class import *
from Id_Class import *

class Student:

    # Constructor Object #
    def __init__(self, id, name:str,sex:str , year_born:int, course,classroom , m_score:float, rank:str):
        self.id = id
        self.name = name
        self.sex = sex
        self.year_born = year_born
        self.course = course
        self.classroom = classroom
        self.m_score = m_score
        self.rank = rank
        self.age = int(Course.CURRENT_YEAR - year_born)

    # Method set abttribute Object:
    def set_name(self, name):
        self.name = name

    def set_year_born(self, year_born):
        self.year_born = year_born

    def set_sex(self, sex):
        self.sex = sex

    def set_score(self, m_score):
        self.m_score = m_score

    # Method get abttribute Object:
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_score(self):
        return self.m_score

    def get_rank(self):
        return self.rank

    # Method Show information Object:
    def show_info(self):
        print("MÃ SỐ HỌC SINH: {}\nTÊN HỌC SINH: {}\nKHỐI: {}\nLỚP: {}\nĐIỂM TRUNG BÌNH: {}\nXẾP LOẠI: {}\n".format(self.id, self.name, self.course, self.classroom, self.m_score, self.rank))






hs1 = Course("12", "A1", 2022)
hs1 = Student("22A101","Đoàn Ngọc Nữ", "Nữ", 2003, hs1.get_course(),hs1.classroom, 8.0, "Giỏi")
hs1.show_info()
