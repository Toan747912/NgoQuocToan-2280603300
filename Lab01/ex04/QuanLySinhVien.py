from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []
    
    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:
            maxId = max(sv._id for sv in self.listSinhVien) + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            sv._name = input("Nhập tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập chuyên ngành của sinh viên: ")
            sv._diemTB = float(input("Nhập điểm của sinh viên: "))
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại")

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)
    
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)
    
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)
    
    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None
    
    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]
    
    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False
    
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocluc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocluc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung bình"
        else:
            sv._hocluc = "Yếu"
    
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<12} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Điểm TB", "Học lực"))
        if listSV:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<12} {:<8.2f} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
            print()
    
    def getListSinhVien(self):
        return self.listSinhVien
