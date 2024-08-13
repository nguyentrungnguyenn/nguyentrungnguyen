# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 20:01:29 2024

@author: Nguyen Trung Nguyen
Bài 1: Khoảng cách
distance=float(input("Nhập độ dài đoạn đường đến trường (m): "))
if distance > 1200:
    print("Đường đến trường quá xa.")
else:
    print("Không xác định được xa-gần.")
Bài 2: Khoảng cách
distance=float(input("Nhập độ dài đoạn đường đến trường (m): "))
if distance < 300:
    print("Đường đến trường quá gần. Thôi! Đi bộ.")
elif distance > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy.")
elif distance >= 300 and distance <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp.")
else:
    print("Không xác định.")
Bài 3: GPA
GPA=float(input("Nhập điểm trung bình (GPA): "))
if GPA < 3.5:
    print("Học lực kém.")
elif GPA >= 3.5 and GPA < 5.0:
    print("Học lực yếu.")
elif GPA >= 5.0 and GPA < 7.0:
    print("Học lực trung bình.")
elif GPA >= 7.0 and GPA < 8.0:
    print("Học lực khá.")
elif GPA >= 8.0 and GPA < 9.0:
    print("Học lực giỏi.")
elif GPA >= 9.0 and GPA <= 10:
    print("Học lực xuất sắc.")
else:
    print("Không xác định.")
Bài 4: Phương trình
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a != 0 and b == 0:
    print("Phương trình có nghiệm a= 0")
elif a != 0 and b != 0:
    print("Phương trình có nghiệm x=", -b/a)
Bài 5: Phương trình bậc 2
import math
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
denta = b*b - 4*a*c
if a == 0: 
    print("Phương trình có nghiệm duy nhất x=", -b/c)
elif a != 0 and denta < 0:
    print("Phương trình vô nghiệm")
elif a != 0 and denta == 0:
    print("Phương trình phương trình có nghiệm kép x1=x2 =", -b/(2*a))
elif a != 0 and b*b - (4*a*b) > 0:
    print("Phương trình có 2 nghiệm phân biệt x1 = ", (-b + math.sprt(denta))/(2*a))
    print("Phương trình có 2 nghiệm phân biệt x2 = ", (-b - math.sprt(denta))/(2*a))
Bài 6: Chứng minh tam giác
a = float(input("Nhập a="))
b = float(input("Nhập b="))
c = float(input("Nhập c="))
if a + b > c and a + c > b and  + c > a:
    print("Đây là tam giác")
else:
    print("Đây không phải là tam giác.")
Bài 7: Tam giác đặc biệt
a=float(input("Nhập số a:"))
b=float(input("Nhập số b:"))
c=float(input("Nhập số c:"))
if (a + b > c and a+ c > b and b + c > a):
    if a == b == c:
        print("Tam giác đều.")
    elif a*a + b*b == c*c:
        print("Tam giác vuông.")
    elif a == b or b == c or b == c:
        print("Tam giác cân.")
    else:
        print("Đây là tam giác.")
else:
    print("Đây không là tam giác.") 
Bài 8: Taxi
d = float(input("Nhập quãng đường đi (km):"))
if d <= 1:
    print("Giá là 20k")
elif d > 1 and d <= 4:
    print("Giá là:", d*13000)
elif d >= 4 and d <= 8:
    print("Giá là:", (3*13000) + (d-3)*12000)
else:
    print("Giá là:", 39000 + 60000 + (d-8)*10000)
    m = 39000 + 60000 + (d-8)*10000
    if m >= 100000:
        print("Giá phải trả là:", m*0.92)
Bài 9: Kéo Búa Bao
import random 
choices = ["kéo", "búa", "bao"]
kq_nguoi_choi = input("Nhập kết quả người chơi:")
if kq_nguoi_choi not in ["kéo", "búa", "bao"]:
    print("Không hợp lệ vui lòng nhập lại.")
kq_may = random.choice(choices)
print("Kết quả máy:", kq_may)
if kq_nguoi_choi == kq_may:
    print("Hòa")
elif (kq_nguoi_choi == "kéo" and kq_may == "bao") or\
     (kq_nguoi_choi == "búa" and kq_may == "kéo") or\
     (kq_nguoi_choi == "bao" and kq_may == "búa"):
         print("Bạn thắng")
else:
    print("Bạn thua")
"""

