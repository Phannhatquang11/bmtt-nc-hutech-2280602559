def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a': 1, 'b' : 2, 'c' : 3, 'd' : 4}   
key_to_delete = 'a'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phan tu da duoc xoa tu Dictionary:", my_dict)
else:
    print("khong tim thay phan tu can xoa trong dictionary.") 
