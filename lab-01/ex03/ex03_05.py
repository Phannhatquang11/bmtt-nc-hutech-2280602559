def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Nhap danh sach ca tu, cach nhau bang dau cach:")
worl_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(worl_list)
print("So lan xuat hien cac phan tu : ", so_lan_xuat_hien)
