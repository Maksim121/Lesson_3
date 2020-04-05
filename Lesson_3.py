#Домашнее задание к Уроку №3
text='Новый текст, который использует этот текст на как новый - для ТЕСТИРОВАНИЯ на текст!'
print('Исходный текст:')
print(text)

#Задача №1
print('Задача №1_Убрать занки препинания')
puncts='.,\'-";!?"'
text1=text
for i1 in range(len(puncts)):
    a1=puncts[i1]
    text_no_punctuations=text1.replace(a1,' ')
    text1 = text_no_punctuations
print ("Текст без знаков препинания")
print (text_no_punctuations)
print ('__________________')
print (" ")

#Задача №2
print('Задача №2_сформировать list со словами (split)')
list2=text_no_punctuations.split()
list2=list(list2)
print(list2)
print ('__________________')
print (" ")

#Задача №3
print('Задача №3_привести все слова к нижнему регистру (map)')
list3=list(map(str.lower,list2))
print(list3)
print ('__________________')
print (" ")

#Задача №4
print('Задача №4_получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;')
dict4=dict.fromkeys(list3)
list4=list(dict4)
i4_4=0
i4_3=0
dict4_3={}
for i4_4 in range(len(list4)):
    k1=0
    n4=list4[i4_4]
    for i4_3 in range(len(list3)):
            if list4[i4_4]==list3[i4_3]:
                k1=k1+1
    dict4_3[n4]=k1
print(dict4_3)
print ('__________________')
print (" ")

#Задача №5
print('Задача №5_вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)')
#сортировка
dict5_1=dict4_3
print(dict5_1)
list_dict5_1_sort=sorted(dict5_1.values())
print(list_dict5_1_sort)
print(list_dict5_1_sort[-1])
for i5 in range (5):
    print(dict5_1.items())
    print(key)

# for value in dict5_1.values():
#     print(value)

# for key, value in dict5_1.items():
#     print(key,value)

#количество разных слов в тексте
set5_1=set(list3)
print(set5_1)
print('Количество разных слов в тексте =', len(set5_1))
print ('__________________')
print (" ")
