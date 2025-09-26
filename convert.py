def get_lsb_int(number:bytes):
    output = 0
    for i in range(4):
        output += number[i]*pow(2,8*i)
    return output

