import re
import numpy as np

def make_matrix(message:str)->str:

    array=np.array(list(message)) #array cu caracterele stringului
    matrix=np.reshape(array,(-1,7)) #formez matricea separand array-ul in cate 7 elemtente pe linie
    print('Initial matrix---------\n',matrix)

    column=np.where((matrix == '1').sum(axis=1)%2!=0,1,0) #formez coloana avand in vedere numarul de 1 de pe fiecare linie
    column=column.reshape(-1,1) #o fac coloana
    matrix = np.concatenate((matrix, column), axis=1) #concatenez matricea cu coloana
    #print(column)
    line=np.where((matrix == '1').sum(axis=0)%2==0,0,1)#formez linia avand in vedere numarul de 1 pe fiecare coloana
    line=line.reshape(1,8)
    matrix=np.concatenate((matrix,line),axis=0) #concatenez matricea cu linia


    print('Matrix after counting bits-------\n',matrix)
    new_message=''.join(''.join('%0.3c'%x for x in y) for y in matrix) #formez stringul din matrice

    return new_message #T(x)

def check(message:str)->bool:
    ok = True
    splited_list=[message[group:group+8] for group in range(0,len(message),8)] #Formez o lista de cuvinte cu lungime de 8 caractere
    #print(splited_list)
    for group in splited_list: #in fiecare grup verific daca ultimul caracter este valabil, adica daca suma de 1 e para atunci ultimul caracter trb sa fie 0, 1 in caz contrar
        last_val=group[len(group)-1]
        sum=group[:-1].count('1')
        if sum % 2 == 0:
            check_val = '0'
        else:
            check_val = '1'
        if check_val != last_val:
            ok=False

    return  ok




print('Biti paritate bidimensional------------')

message = input('Enter the message: ') #M(x)
pattern = '^[01]+$' #verifica daca e format doar din 0 si 1
result = re.match(pattern,message)
if  result and  len(message) % 7 == 0: #verific daca e multiplu de 7
    print('Mesaj valid')
    new_message=make_matrix(message)
    print(new_message)
    if check(new_message):
        print('Mesaj transmis fara erori\n')
    else:
        print('Mesaj transmis cu erori\n')
    ch = input('Do you want to change a bit?(Y/N) ')
    if ch == 'y' or ch == 'Y':
        copy_coded_message = new_message  # Copie T(x)
        pos = input('Bit number: ')
        if int(pos) % 7 != 0:
            if copy_coded_message[int(pos)] == '0':
                copy_coded_message = copy_coded_message[:int(pos)] + '1' + copy_coded_message[int(pos) + 1:]
            elif copy_coded_message[int(pos)] == '1':
                copy_coded_message = copy_coded_message[:int(pos)] + '0' + copy_coded_message[int(pos) + 1:]
                if check(copy_coded_message):
                    print('Mesaj transmis fara erori\n')
                else:
                    print('Mesaj transmis cu erori\n')
        else:
            print('Invalid input')
    else:
        pass
else:
    print('Mesaj invalid')
    ok = None