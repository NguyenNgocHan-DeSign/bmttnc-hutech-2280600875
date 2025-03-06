#Hàm kiểm tra số nhị phân có chia hết cho 5 hay không
def chia_het_cho_5(so_nhi_phan):
    #chuyển số nhị phân sang số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    #kiểm tra xem sô thập phân có chia hết cho 5 hay không
    if so_thap_phan % 5 ==0:
        return True
    else:
        return False
    #Nhập chuỗi
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấU phẩy): ")
    #tách chuỗi
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
#in ra
if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("không có số nào chia hết cho 5 trong chuỗi đã nhập.")