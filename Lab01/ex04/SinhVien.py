class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocluc = ""
from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    def generateID(self):
        maxId = 1
        if(self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if(maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
            return maxId
        def soLuongSinhVien(self):
            return self.listSinhVien.__len__()
        def nhapSinhVien(self):
            svId = self.generateID()
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viênviên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv = SinhVien(svId, name, sex, major, diemTB)
            self.xepLoaiHocLuc(sv)
            self.listSinhVien.append(sv)
            
    def updateSinhVien(self, ID):
        sv:SinhVien = self.finByID(ID)
        if(sv != None):
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            major = input("Nhập chuyên ngành của sinh viên: ")
            diemTB = float(input("Nhập điểm của sinh viên: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID = {} không tồn tại".format(ID))
    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
        
    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)
    
    def findByID(self, ID):
        searchResult = None
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if(self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    def deleteById(Self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if(sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def xepLoaiHocLuc(self, sv:SinhVien):
        if(sv._diemTB >= 8):
            sv._hocluc = "Giỏi"
        elif(sv._diemTB >= 6.5):
            sv._hocluc = "Khá"
        elif(sv._diemTB >= 5):
            sv._hocluc = "Trung bình"
        else:
            sv._hocluc = "Yếu"
            
    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Điểm TB", "Học lực"))
        if(list.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
                print("\n")
    def getListSinhVien(self):
        return self.listSinhVien