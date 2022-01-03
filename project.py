from operator import itemgetter
class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

''' First Task - Mission List Decoding '''
def add_alphabet(deque, alphabet):
    for letter in alphabet:
        deque.add_front(letter)
    return None

def decifrar(deque, encrypted_text, key):
    # insira seu código aqui
    decode_dic = {}
    key2 = key
    cont = 0
    cont2 = 0
    dic_alphabet = {}
    string = ''
    while key != 0:
        removed = deque.remove_front()
        deque.add_rear(removed)
        key -= 1
    size = deque.size()
    while cont != size:
        removed = deque.remove_rear() 
        decode_dic[removed] = cont
        deque.add_front(removed)
        cont += 1
    while key2 != 0:
        removed = deque.remove_rear()
        deque.add_front(removed)
        key2 -= 1
    while cont2 != size:
        removed = deque.remove_rear()
        dic_alphabet[removed] = cont2
        deque.add_front(removed)
        cont2 += 1
    for letter in encrypted_text:
        ind = dic_alphabet[letter]
        for letter, value in decode_dic.items():
            if value == ind:
                string += letter                                                                   
                break                               
        
    return string


''' Second Task - Select Quest Subset '''
def bottomup(mission_list,hours,m):
    for j in range(1,len(mission_list)+1):
        for x in range(hours+1):
            name, time, value, dificulty = mission_list[j-1].split(',')
            time, value = int(time), int(value)
            if time > x:
                m[j][x] = m[j-1][x]
            else:
                usa = value + m[j-1][x-time]
                naousa = m[j-1][x]
                m[j][x] = max(usa,naousa)
    return m[len(mission_list)][hours]
            

                
def ordering(lista,order):
    new_list = []
    for mission in lista:
        name, time, value, dificulty = mission.split(',')
        new_list.append((name,time,value,dificulty))
    if order == 0:
        new_list = sorted(new_list, key=itemgetter(0, 1, 2, 3))   
    if order == 1:
        new_list = sorted(new_list, key=itemgetter (1, 0, 2, 3))
    if order == 2:
        new_list = sorted(new_list, key=itemgetter(2, 0, 1, 3))
    if order == 3:
        new_list = sorted(new_list, key=itemgetter(3, 0, 1, 2)) 
    return new_list        

    
def select_missions():
    d = Deque()
    hours = int(input())
    permission = int(input())
    order = int(input())
    alphabet = input()
    key = int(input())
    num_mission = int(input())
    mission_list = []
    while num_mission != 0:
        mission = input()
        mission = mission[1:-1]
        add_alphabet(d, alphabet)
        mission = decifrar(d, mission, key)
        mission_list.append(mission)
        num_mission -= 1
    if hours == 0:
        print(f'Time left: 0')
        print(f'value: 0')
        return None
    m = []
    for i in range(len(mission_list)+1):
        linha = []
        for j in range(hours+1):
            linha.append(0)
        m.append(linha)    
    final_value = bottomup(mission_list,hours,m)
    mission_sel = []
    x = hours
    j = len(mission_list)
    while j >= 1:
        name, time, value, dificulty = mission_list[j-1].split(',')
        time = int(time)
        value = int(value)
        if m[j][x] == m[j-1][x-time] + value:
            mission_sel.append(mission_list[j-1])
            x = x - time
        j = j - 1
    missions_time = 0
    for mission in mission_sel:
        missions_time += int(mission.split(',')[1])
    time_left = hours - missions_time
    if permission == 1:
        new_list = ordering(mission_sel,order)
        for mission in new_list:
            name, time, value, dificulty = mission
            string = name + ', ' + time + ', ' + value + ', ' + dificulty
            print(string)
        print(f'Time left: {time_left}')
        print(f'value: {final_value}')
    else:
        print(f'Time left: {time_left}')
        print(f'value: {final_value}')

    return None

if __name__ == "__main__":
    select_missions()
