f = open('Lecture13_txt/average-latitude-longitude-countries.csv','r')

list_of_country_code_and_country_name = []
list_of_country_code_and_coordinate = []

for i in f:
    if i[1:4] == "ISO":
        continue
    i = i.strip()
    l = i.split('"')
    t = l.pop().split(',')
    l.extend(t)
    list_of_country_code_and_country_name.append((l[1],l[3]))
    list_of_country_code_and_coordinate.append((l[1],(float(l[5]),float(l[6]))))

for i in list_of_country_code_and_coordinate:
    if i[1][0] < 0:
        print(i[0])

enter_country_code = input().strip()

for i in list_of_country_code_and_country_name:
    if i[0] == enter_country_code:
        print(i[1])
        break

f.close()