import numpy as np
import re

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encryptMessage(key:str,message:str)->str:

    matrix = np.reshape(list(key), (-1, len(key))) #formez o matrice cu numarul de coloane egal cu lungimea cheii si adaug pe prima linie cheia
    sorted_word = sorted(key) #ordonez cheia in ordine lexicografica

    position_array = np.array([],dtype=str)

    for i in key:
        position_array=np.append(position_array,sorted_word.index(i)+1) #formez a doua linie din matrice prin care numerotez literele din cheie in functie de ordinea lor lexicografica

    matrix = np.vstack((matrix, position_array)) #adaug a doua linie in matrice

    message =re.sub(r"\s+","",message) #sterg toate spatiile din text(mesaj)

    splited_list=[message[group:group+len(key)] for group in range(0,len(message),len(key))] #formez o lista de cuvinte cu lungimea egala cu lungimea cheii

    if(len(splited_list[len(splited_list)-1]) % len(key)!=0):  #daca ultimul cuvant nu ar lungimea egala cu cea a cheii, nu s-ar completa ultima coloana
        difference = len(key)-len(splited_list[len(splited_list)-1]) #aflam cate litere din alfabet mai adaugam
        splited_list[len(splited_list) - 1]=splited_list[len(splited_list)-1]+alphabet[:difference] #adaugam litere din alfabet

    for group in splited_list: #pe urmatoarele linii se scrie textul ce urmeaza a fi criptat
        array = np.array(list(group))
        matrix = np.vstack((matrix, array))

    print('Matrix -----------------\n',matrix) #afisam matricea

    encryptedText=""
    for i in range(1,len(key)+1): #pornim de la prima coloana(prima litera a cheii, in ordine alfabetica)
        k,j = np.where(matrix==str(i))
        new_message=''.join(''.join('%0.3c'%x for x in y) for y in matrix[2:,j]) #formez stringul din coloana matricei
        encryptedText += new_message #formam textul criptat

    return encryptedText


key = input('Enter the key: ')
message = input('Enter the message: ')

result = re.match(r'^(?!.*(.).*\1)[A-Za-z]+$',key)#verific daca cheia are caractere unice sau nu
if(result):
    print('\nEncrypted message is: ',encryptMessage(key.upper(),message.upper()))
else :
    print('The key doesn t contain unique characters')
