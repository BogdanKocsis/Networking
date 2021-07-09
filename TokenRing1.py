
class token:
    history = ''
    def __init__(self, isArrived, message, IPSource, IPDestination, isFree): #constructor
        self.isArrived = isArrived
        self.message = message
        self.IPSource = IPSource
        self.IPDestination = IPDestination
        self.isFree = isFree

    def Reset(self):
        self.isArrived=False;
        self.history=''
        self.message=''
        self.IPDestination=''
        self.IPSource=''


    def IsArrived(self):
        return self.isArrived

    def setIsArrived(self, isArrived):
        self.isArrived= isArrived

    def IsFree(self):
        return  self.isFree
    def setIsFree(self,isFree):
        self.isFree=isFree

    def ToString(self):
       print('Token: is arrived= ', self.isArrived , ', message=' , self.message ,', IP source=' ,self.IPSource , 'IP Destination=' , self.IPDestination ,', is free=' , self.isFree , ' history= ')



class computer:
    def __init__(self, IPAddress, buffer): #constructor
        self.IPAddress=IPAddress
        self.buffer=buffer
    def setBuffer(self, buffer):
        self.buffer = buffer




def TokenRing(numberOfComputers,Source,Destination):

   # orientation = int(input('1 for ClockWise/ 0 for Anti-ClockWise: '))  # stabilim un sens de mers al jetonului
    computers = []
    for i in range(0,numberOfComputers):
        computers.append(computer(addresses[i],''))  # cream obiectele de tip computer

    posSource=addresses.index(Source)
    posDestination=addresses.index(Destination)

    if (posSource < posDestination):  # stabilim un sens de mers al jetonului in functie de poziitile lor in lista de adrese IP
        orientation = 1
    else:
        orientation = 0

    print('Position for source is: ',posSource,'\nPosition for destination is: ',posDestination)

    message = input('Enter the message: ') #introducem mesajul de trimis

    Token  = token(False,message,computers[posSource].IPAddress,computers[posDestination].IPAddress,False) #cream obiectul de tipul token



    if(orientation == 1):  #in functie de orientare(1 for ClockWise/ 0 for Anti-ClockWise) parcurgem calculatoarele din retea
        for i in range(posSource,posDestination+1):
            Token.history = Token.history +' '+ computers[i].IPAddress
            Token.ToString()  #afisam statusul token-ului
            print(Token.history,'\n',)
            if computers[posDestination].IPAddress == computers[i].IPAddress:  #verificam daca IP-ul unui computer coincide cu IP destinatie.
                computers[i].setBuffer(message)
                Token.setIsArrived(True)
                print('Message reached its destination\n')
        for i in range(posDestination,posSource-1,-1):
            if computers[posSource].IPAddress == computers[i].IPAddress:
                if Token.isArrived == True: #Daca a ajuns la destinatie, jetonul este eliberat
                    Token.setIsFree(True)
                    Token.Reset()
                    print('Token is free\n')

    else:
        for i in range (posSource,posDestination-1,-1):
            Token.history = Token.history +' ' + computers[i].IPAddress
            Token.ToString()  #afisam statusul token-ului
            print(Token.history, '\n', )
            if computers[posDestination].IPAddress == computers[i].IPAddress: # verificam daca IP-ul unui computer coincide cu IP destinatie.
                computers[i].setBuffer(message)
                Token.setIsArrived(True)
                print('Message reached its destination')
        for i in range(posDestination,posSource+1):
            if(computers[posSource].IPAddress == computers[i].IPAddress):
                if Token.isArrived == True: # Daca a ajuns la destinatie, jetonul este eliberat
                    Token.setIsFree(True)
                    Token.Reset()
                    print('Token is free\n')



    Token.ToString()  #afisam statusul token-ului eliberat

print('Token Ring ######################################################')

addresses = ['192.178.11.3', '192.178.14.7', '192.178.15.6', '192.178.24.1', '193.178.15.19','154.178.15.10', '129.178.15.21', '192.178.15.4', '192.178.15.25', '192.178.15.26', '192.178.15.28', '192.178.15.29', '192.178.15.35', '192.178.15.36', '192.178.15.37', '192.178.15.38', '192.178.15.39', '192.178.15.40']

numbers = int(input('Enter the number of computers: ')) #alegem numarul de calculoare din retea
Source = input('Enter Source:  ') # alegem sursa
Destination=input('Enter Destionation: ') #alegem destinatia


if(Source != Destination and (addresses.index(Destination)<numbers and addresses.index(Source)<numbers)): # ne asiguram ca sursa si destinatia nu coincid si ca fac parte din retea
    if(numbers < len(addresses)):
        TokenRing(numbers,Source,Destination)
    else:
        print('Choose a number under', len(addresses))
else:
     print('Source and Destination are same or Destination doesn t exist in network')

ch = input('Do you want to send another message?(Y/N) ') # avem posibilitatea de a trimite inca un mesaj, alegand  o alta  sursa si destinatie
if ch == 'y' or ch =='Y':
    Source = input('Enter Source:  ')
    Destination = input('Enter Destionation: ')
    if (Source != Destination and addresses.index(Destination) < numbers):
        if (numbers < len(addresses)):
            TokenRing(numbers, Source, Destination)
        else:
            print('Choose a number under', len(addresses))
    else:
        print('Source and Destinatio are same or Destination doesn t exist in network')