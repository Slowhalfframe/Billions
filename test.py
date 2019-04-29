str_1 = '1.23'
try:
    complex(str_1)
    print("是纯数字")
except:
    print("不是纯数字")