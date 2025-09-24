def get_lsb_int(number:bytes):
    output = 0
    for i in range(4):
        output += number[i]*(256**i)
    return output