# #1.1. Các nguyên lý 
# #Liệt kê cầu thủ bóng đá Việt Nam:
# bongda_VietNam= ['Văn Lâm','Tiến Dũng','Anh Đức','Công Phượng']
# for cau_thu in bongda_VietNam:
#     print('Tên cầu thủ:',cau_thu)
# # kq:  Tên cầu thủ: Văn Lâm    
# # Tên cầu thủ: Tiến Dũng  
# # Tên cầu thủ: Anh Đức    
# # Tên cầu thủ: Công Phượng
# # Liệt kê số cầu thủ bóng đá thế giới: 
# bongda_TG= ['Messi','Ronaldo','ThongLao','Mbappe']
# for cau_thu in bongda_TG:
#     print('Tên cầu thủ',cau_thu)
# # Tên cầu thủ Messi   
# # Tên cầu thủ Ronaldo 
# # Tên cầu thủ ThongLao
# # Tên cầu thủ Mbappe  
# # Từ đó, chúng ta có thể sử dụng vòng lặp lồng ghép vào nhau (nested loop) để tính toán cho
# # nguyên lý nhân. Ví dụ: Tìm sự tranh chấp Quả bóng vàng giữa cầu thủ Việt Nam và Thế giới là
# # sự chọn 1 từ mỗi tập, số trường hợp được liệt kê là tích của số lượng phần tử của 2 tập: 
# for bong_VN in bongda_VietNam:
#     for bong_TG in bongda_TG:
#         print("khả năng tranh chấp bóng vàng giữa:",bong_VN,"với",bong_TG)
# khả năng tranh chấp bóng vàng giữa: Văn Lâm với Messi
# khả năng tranh chấp bóng vàng giữa: Văn Lâm với Ronaldo
# khả năng tranh chấp bóng vàng giữa: Văn Lâm với ThongLao
# khả năng tranh chấp bóng vàng giữa: Văn Lâm với Mbappe
# khả năng tranh chấp bóng vàng giữa: Tiến Dũng với Messi
# khả năng tranh chấp bóng vàng giữa: Tiến Dũng với Ronaldo
# khả năng tranh chấp bóng vàng giữa: Tiến Dũng với ThongLao
# khả năng tranh chấp bóng vàng giữa: Tiến Dũng với Mbappe
# khả năng tranh chấp bóng vàng giữa: Anh Đức với Messi
# khả năng tranh chấp bóng vàng giữa: Anh Đức với Ronaldo
# khả năng tranh chấp bóng vàng giữa: Anh Đức với ThongLao
# khả năng tranh chấp bóng vàng giữa: Anh Đức với Mbappe
# khả năng tranh chấp bóng vàng giữa: Công Phượng với Messi
# khả năng tranh chấp bóng vàng giữa: Công Phượng với Ronaldo
# khả năng tranh chấp bóng vàng giữa: Công Phượng với ThongLao
# khả năng tranh chấp bóng vàng giữa: Công Phượng với Mbappe
#ví dụ 1:
# N = 4
# for i1 in range(0,N):
#     for i2 in range(0,N):
#         for i3 in range(0,N):
#             print(i1,i2,i3)
#             0 0 3
# 0 1 0
# 0 1 1
# 0 1 2
# 0 1 3
# 0 2 0
# 0 2 1
# 0 2 2
# 0 2 3
# 0 3 0
# 0 3 1
# 0 3 2
# 0 3 3
# 1 0 0
# 1 0 1
# 1 0 2
# 1 0 3
# 1 1 0
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 0
# 1 2 1
# 1 2 2
# 1 2 3
# 1 3 0
# 1 3 1
# 1 3 2
# 1 3 3
# 2 0 0
# 2 0 1
# 2 0 2
# 2 0 3
# 2 1 0
# 2 1 1
# 2 1 2
# 2 1 3
# 2 2 0
# 2 2 1
# 2 2 2
# 2 2 3
# 2 3 0
# 2 3 1
# 2 3 2
# 2 3 3
# 3 0 0
# 3 0 1
# 3 0 2
# 3 0 3
# 3 1 0
# 3 1 1
# 3 1 2
# 3 1 3
# 3 2 0
# 3 2 1
# 3 2 2
# 3 2 3
# 3 3 0
# 3 3 1
# 3 3 2
# 3 3 3
#Ví dụ 2: In ra các phương án chọn 3 số nguyên nhỏ hơn N không âm có thứ tự và không lặp:
# for i1 in range(0,N):
#     for i2 in range(0,N):
#         for i3 in range(0,N):
#             if i1 != i2 and i2 != i3 and i1 != i3:
#                 print(i1,i2,i3)
# 0 1 2
# 0 1 3
# 0 2 1
# 0 2 3
# 0 3 1
# 0 3 2
# 1 0 2
# 1 0 3
# 1 2 0
# 1 2 3
# 1 3 0
# 1 3 2
# 2 0 1
# 2 0 3
# 2 1 0
# 2 1 3
# 2 3 0
# 2 3 1
# 3 0 1
# 3 0 2
# 3 1 0
# 3 1 2
# 3 2 0
# 3 2 1
# Ví dụ 3: In ra các phương án chọn 3 số nguyên nhỏ hơn N không âm có tăng dần và không
# lặp:
# N = 4
# ketqua = []
# for i1 in range(0,N):
#     for i2 in range(i1+1,N):
#         for i3 in range(i2+1,N):
#             if i1 != i2 and i2 != i3 and i3 != i1:
#                 ketqua = ketqua + ([i1,i2,i3])
# print(ketqua)
# #[0, 1, 2, 0, 1, 3, 0, 2, 3, 1, 2, 3]
# print(ketqua[-1])
# print(ketqua[2])


#Ví dụ 4: In ra các phương án chọn 3 số nguyên nhỏ hơn N không âm có không giảm và có lặp:
# for i1 in range(0,N):
#     for i2 in range(i1,N):
#         for i3 in range(i2,N):
#             print(i1,i2,i3)
# 0 0 0
# 0 0 1
# 0 0 2
# 0 0 3
# 0 1 1
# 0 1 2
# 0 1 3
# 0 2 2
# 0 2 3
# 0 3 3
# 1 1 1
# 1 1 2
# 1 1 3
# 1 2 2
# 1 2 3
# 1 3 3
# 2 2 2
# 2 2 3
# 2 3 3
# 3 3 3
#Hoặc chúng ta có thể lưu lại các “phương án” lựa chọn trong danh sách, ví dụ: 
# N = 3
# ketqua = []
# for i1 in range(0,N):
#     for i2 in range(i1,N):
#         for i3 in range(i2,N):
#             ketqua = ketqua +[(i1,i2,i3)]
# print(ketqua[-1])
# print(ketqua[-2])
# (2, 2, 2)
# (1, 2, 2)

#1.2. Thể hiện biểu thức luận lý bằng Python
# def implies(a,b):
#     if a: #có nghĩa là điều kiện a khác 0
#         return b
#     else:
#         return True
# print(implies(10,11))
#11
# print(implies(1,11))
#11
# print(implies(0,11))
#True

#2. Lý thuyết tập hợp với kiểu dữ liệu list trong Python 
# N =3
# ketqua= []
# for i1 in range(0,N):
#     for i2 in range(i1,N):
#         for i3 in range(i2,N):
#             ketqua = ketqua +[(i1,i2,i3)]
# print((0,2,2)in ketqua)
# True
#Phép tìm tập hiệu (difference) giữa 2 tập A và B: 
# def difference(A,B):
#     ketqua = []
#     for x in A:
#         if x not in B:
#             ketqua = ketqua + [x]
#     return ketqua
# A = [0,1,2,3,4,5,6,7]
# B = [2,4,6,8,10]
# print(difference(A,B))
#[0, 1, 3, 5, 7]
#Xây dựng dữ liệu đầu vào 
sodiem_DL = 9
diadiem = ['Cần Giờ', 'Củ Chi', 'Chợ Bến Thành', 'Sở Thú', 'BV thẫm mỹ răng', 'Chí Hòa',
'Dinh Độc lập', 'Bào tàng', 'Trường Văn Lang']
thoigian = [1.0, 1.0, 0.6, 0.4, 1.5, 0.3, 0.3, 0.3, 0.6]
songay_dulich = 1.5 # Nghĩa là đoàn du lịch chỉ đi tham quan 1.5 ngày
thoigian_diadiem = [songay_dulich / sodiem_DL] * sodiem_DL
for i in range(sodiem_DL):
    print(f'Thời gian tham quan tại {diadiem[i]}: {thoigian_diadiem[i]} ngày')

def lietke_chuoinhiphan(n):
    danhsach = []
    #bat dau = 1
    for i in range(0,2**n):
        gia_tri = i
        chuoi_np = bin(gia_tri).replace('0b','')
        while(len(chuoi_np)<n):
            chuoi_np = '0'+chuoi_np
        danhsach.append(chuoi_np)
        #print(chuoi_np)
    return danhsach
# print(bin(10))
#0b1010
# print(bin(10).replace('0b', ''))
# 1010
n = 9
chuoi_np = bin(10).replace('0b','')
while (len(chuoi_np) < n):
    chuoi_np = '0' + chuoi_np
print(chuoi_np)
