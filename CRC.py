import re

def CRC(message, gen_pol):
    degree=len(gen_pol)
    for it in range(0,degree-1):
        message = message + '0'
    message_copy = message #M'(x)
    while len(message) >= degree:
        aux = message[:degree]
        rest = int(aux, 2) ^ int(gen_pol, 2)
        message =  message[degree:]
        message = '{0:b}'.format(rest) +  message
        while( message[0] != '1' and len(message) >= 2 ):
         message=message[1:]

    #print('{0:b}'.format(rest), message)
    message_copy = message_copy[:-len(message)]+message
    print('T(X): ' + message_copy)
    return message_copy

def checkCRC(message, gen_pol):
    degree = len(gen_pol)
    while len(message) >= degree:
        aux = message[:degree]
        rest = int(aux, 2) ^ int(gen_pol, 2)
        message =  message[degree:]
        message = '{0:b}'.format(rest)+  message
        while( message[0] != '1'  and len(message) >= 2 ):
            message=message[1:]

    #print (message,'{0:b}'.format(rest))
    return message

print('CRC------------')

message = input('Enter the message: ') #M(x)
generator_polynomial = input('Enter the generator polynomial:')  #C(x)

pattern = '^[01]+$'
result1 = re.match(pattern,message)
result2 = re.match(pattern,generator_polynomial)
if  result1 and result2 and len(generator_polynomial)>1:
    first_digit  = int(generator_polynomial[0])
    if (first_digit == 1 and int(generator_polynomial)%10 == 1) :
        print('Polinom generator valid')
        ok = True
    else:
        print('Polinom generator invalid')
        ok = None

    if(ok == True):
        coded_message = CRC(message,generator_polynomial) #T(X)
        if checkCRC(coded_message,generator_polynomial) == '0':
            print('Message without errors\n')
        else:
            print('Message with errors\n')
        ch = input('Do you want to change a bit?(Y/N) ')

        copy_coded_message = coded_message #Copy of T(x)
        if ch == 'y' or ch =='Y':
            pos = input('Bit number: ')
            if int(pos) >= 0 and int(pos) <= len(message): #Change one bit of T'(x)
                if  copy_coded_message[int(pos)] == '0':
                    copy_coded_message = copy_coded_message[:int(pos)] + '1' + copy_coded_message[int(pos) + 1:]
                elif  copy_coded_message[int(pos)] == '1':
                    copy_coded_message =  copy_coded_message[:int(pos)] + '0' +  copy_coded_message[int(pos) + 1:]

                if checkCRC(copy_coded_message, generator_polynomial) == '0':
                    print('Message without errors\n')
                else:
                    print('Message with errors\n')
            else:
              print('The chosen bit is out of range')
        else:
            pass
    else:
        pass
else:
    pass
    print('Wrong message or another Error')

