gust = ['ALI','AHMED','TAHA','OSMAN','Baber']
message ="dear {}, you are invited  on dinner "
for i in gust:
    print(message.format(i))


print("ali is in hospital .he is not coming. so, i am adding new member")
gust[0]='nomi'



for i in gust:
    print(message.format(i))


print("adding new members")
gust.append('umer')
gust.insert(0, 'akram')
gust.insert(3,'Nasir')
for i in gust:
    print(message.format(i))