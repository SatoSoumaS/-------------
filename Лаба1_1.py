maikl = int(input("Сколько долларов у Майкла? "))
ivan = int(input("Сколько долларов у Ивана ? "))
x = 1000 # минимальная сумма для инвестиция
if x <= maikl and x > ivan:
    print("Вложиться может только Майкл") 
if x <= ivan and x > maikl: 
    print("Вложиться может только Иван") 
if x > maikl and x > ivan and x <= (maikl + ivan): 
    print("Можете влож ться только вместе") 
if x <= maikl and x <= ivan:
    print("С деньгами у вас все впорядке, вкладывайтесь )") 
    print("Удачи  ))") 
