import time

def xor(text1, text2):
    process = text1 ^ text2
    to_bin = bin(process)
    res_b = [ i.replace('b','') for i in to_bin ]
    res_chr = chr(int(to_bin,2))

    return res_b, res_chr


def OR(text1, text2):
    process = text1 | text2
    to_bin = bin(process)
    res_b = [ i.replace('b','') for i in to_bin ]
    res_chr = chr(int(to_bin,2))

    return res_b, res_chr


def AND(text1, text2):
    process = text1 & text2
    to_bin = bin(process)
    res_b = [ i.replace('b', '') for i in to_bin ]
    res_chr = chr(int(to_bin,2))

    return res_b, res_chr


def NOT(text):
    process = ~text
    to_bin = bin(process)
    res_b = [ i.replace('b','') for i in to_bin ]
    res_chr = chr(int(to_bin,2))

    return res_b, res_chr


def shift_left(text,val):
    process = text << val
    to_bin = bin(process)
    res_b = [ i.replace('b','') for i in to_bin ]
    res_chr = chr(int(to_bin, 2))

    return res_b, res_chr


def shift_right(text,val):
    process = text >> val
    to_bin = bin(process)
    res_b = [ i.replace('b','') for i in to_bin ]
    res_chr = chr(int(to_bin, 2))

    return res_b, res_chr

print("Welcome!!")
time.sleep(2)
while True:
    to_do = input('What would you like to do?\n[1] XOR\n[2] OR\n[3] AND\n[4] NOT\n[5] Shift Left\n[6] Shift Right\n>> ')
    print('')
    if to_do == '1':
        time.sleep(1)
        bin_1 = int(input('Binary 1 : '),2)
        bin_2 = int(input('Binary 1 : '),2)
        a,b = xor(bin_1, bin_2)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    elif to_do == '2':
        time.sleep(1)
        bin_1 = int(input('Binary 1 : '),2)
        bin_2 = int(input('Binary 1 : '),2)
        a,b = OR(bin_1, bin_2)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    elif to_do == '3':
        time.sleep(1)
        bin_1 = int(input('Binary 1 : '),2)
        bin_2 = int(input('Binary 1 : '),2)
        a,b = AND(bin_1, bin_2)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    elif to_do == '4':
        time.sleep(1)
        bin_1 = int(input('Binary : '),2)
        a,b = NOT(bin_1)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    elif to_do == '5':
        time.sleep(1)
        bin_1 = int(input('Binary : '),2)
        shift = int(input('Shift Value : '))
        a,b = shift_left(bin_1, shift)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    elif to_do == '6':
        time.sleep(1)
        bin_1 = int(input('Binary : '),2)
        shift = int(input('Shift Value : '))
        a,b = shift_right(bin_1, shift)
        time.sleep(1)
        print('Result as binary :', *a,sep='')
        time.sleep(0.5)
        print('Result as character :', b)

    else:
        print('Invalid Input. Try Again')

    print('')
    time.sleep(2)
    cont = input('Would you like to continue? [y/n]\n>> ').lower()

    if cont == 'y':
        print('')
        continue
    else:
        time.sleep(1)
        print('Thank You. Have A Nice Day')
        break