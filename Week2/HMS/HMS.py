import random as rd
from datetime import datetime

# Thông tin của khánh hàng
name = input("Enter customer name: ")
cccd = int(input("Enter customer CIC number: "))
phone = int(input("Enter customer phone number: "))

print()
print("Customer' name is", name)
print()
print("Customer' CIC number is", cccd)
print()
print("Customer' number phone is", phone)
print()

# Dịch vụ khách hàng chọn
time = int(input("How long customer books room: ")) # --> cost
level = int(input("Which level customer books: ")) # --> cost

print()
if time in [1, 7, 30]:
    if time == 1:
        print("Customer books", time, "day")
    else:
        print("Customer books", time, "days")
else:
    print("Error: Invalid time!")
print()
print("Room level customer books is", level)
print()

# Thông tin về thời gian check-in, check-out
# Nhập thời gian thứ nhất từ người dùng
time1_str = input("Enter check-in time (in format YYYY-MM-DD HH:MM:SS): ")
checkin = datetime.strptime(time1_str, "%Y-%m-%d %H:%M:%S")

print()
print("Customer check-in at", checkin)

# Hệ thống tầng, phòng của khách sạn theo level, time
if level in [1, 2, 3]:
    if 1 <= time <= 30:
        cost = 500000
        if 1 <= time < 7:
            if level == 1:
                floor = 1
                room = rd.randint(1,11)
                cost = cost*time
            elif level == 2:
                floor = 4
                room = rd.randint(31,41)
                cost = (130*cost/100)*time
            elif level == 3:
                floor = 7
                room = rd.randint(61,70)
                cost = (150*cost/100)*time
        elif 7 <= time < 30:
            if time % 7 == 0:
                if level == 1:
                    floor = 2
                    room = rd.randint(11,21)
                    cost = (560*cost/100)*(time/7)
                elif level == 2:
                    floor = 5
                    room = rd.randint(41,51)
                    cost = (590*cost/100)*(time/7)
                elif level == 3:
                    floor = 8
                    room = rd.randint(71,80)
                    cost = (610*cost/100)*(time/7)
            else:
                if level == 1:
                    floor = 2
                    room = rd.randint(11,21)
                    cost = (560*cost/100)*((time-(time%7))/7)
                elif level == 2:
                    floor = 5
                    room = rd.randint(41,51)
                    cost = (590*cost/100)*((time-(time%7))/7)
                elif level == 3:
                    floor = 8
                    room = rd.randint(71,80)
                    cost = (610*cost/100)*((time-(time%7))/7)
        else:
            if level == 1:
                floor = 3
                room = rd.randint(21,31)
                cost = 1800*cost/100
            elif level == 2:
                floor = 6
                room = rd.randint(51,50)
                cost = 1830*cost/100
            elif level == 3:
                floor = 9
                room = rd.randint(81,90)
                cost = 1850*cost/100
    else:
        print("Error: Invalid time!")
else:
    print("Error: Invalid level!")

print()
print("Room", room, "on the floor", floor, "is customer' room")
print()

name1 = input("Enter customer name: ")
cccd1 = int(input("Enter customer CIC number: "))
checkin_str = str(checkin)

# Nhập thời gian thứ hai từ người dùng
time2_str = input("Enter check-in time (in format YYYY-MM-DD HH:MM:SS): ")
checkout = datetime.strptime(time2_str, "%Y-%m-%d %H:%M:%S")
checkout_str = str(checkout)

# Tính hiệu của hai thời gian
difference = checkout - checkin # If-elif-else (diference vs time) --> costdelta

# Latencies --> costdelta
if difference.total_seconds() >= 0:
    if difference.total_seconds() == 0:
        cost = 0
    elif 0 < difference.total_seconds() < 86400*time + 1800:
        cost = cost
    elif 86400*time + 1800 < difference.total_seconds() < 86400*time + 3600:
        cost = 120*cost/100
    elif 86400*time + 3600 <= difference.total_seconds() < 86400*time + 7200:
        cost = 140*cost/100
    else:
        cost = 200*cost/100
else:
    print("Error: Invalid time!")

# Discount
if time in [1, 7, 30] and level in [2, 3]:
    discount_str = input("Enter discount code: ")
    if discount_str in ["HMS1", "HMS2", "HMS3", "HMS4"]:
        if discount_str == "HMS1":
            discount = 20/100
        elif discount_str == "HMS2":
            discount = 30/100
        elif discount_str == "HMS3":
            discount = 50/100
        else:
            discount = 70/10
    else:
        discount = 0
else:
    discount = 0


if cccd1 == cccd and name1 == name:
    print()
    print("Please pay your bill")
    b = " "
    print()
    print(f'{b*15}{"Hotel:......":<50}{"No:......":>50}{b*15}')
    print()
    print(f'{"Address":^130}')
    print(f'{"Hotline":^130}')
    print()
    print(f'{"VAT INVOICE":^130}')
    print()
    print(f'{"Customer: ":<10}{name:<120}')
    print(f'{"Phone number: ":<14}{phone:<116}')
    print(f'{"Check-in: ":<10}{checkin_str:<120}')
    print(f'{"Check-out: ":<11}{checkout_str:<119}')
    print()
    a = '-'
    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"No":^5}|{"Room":^10}|{"Check-in":^30}|{"Check-out":^30}|{"Discount":^15}|{"Price":^20}|{"Total":^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"1":^5}|{room:^10}|{checkin_str:^30}|{checkout_str:^30}|{discount:^15}|{cost:^20}|{cost-discount*cost:^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"2":^5}|{b:^10}|{b:^30}|{b:^30}|{b:^15}|{b:^20}|{b:^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"3":^5}|{b:^10}|{b:^30}|{b:^30}|{b:^15}|{b:^20}|{b:^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"4":^5}|{b:^10}|{b:^30}|{b:^30}|{b:^15}|{b:^20}|{b:^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"5":^5}|{b:^10}|{b:^30}|{b:^30}|{b:^15}|{b:^20}|{b:^20}|')

    print(f'+{a*5}+{a*10}+{a*30}+{a*30}+{a*15}+{a*20}+{a*20}+')
    print(f'|{"Grant total:":>115}|{cost-discount*cost:^20}|')
    print()
    print(f'{"Thành tiền đã bao gồm thuế GTGT (VAT)":<130}')
    print()
    print(f'{b*12}{"CUSTOMER":<50}{b}{"RECEPTIONIST":>50}{b*12}')
    print(f'{b*12}{"Sign, fullname":<50}{b}{"Sign, fullname":>50}{b*12}')