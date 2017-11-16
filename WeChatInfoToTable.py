import numpy
import matplotlib.pyplot as plt
import itchat
itchat.auto_login(hotReload=True)
friends_list=itchat.get_friends()
raw_city_list=[]
for i in friends_list[1:]:
    raw_city_list.append(i["City"])
pure_city_list=list(set(raw_city_list))
city_count_list=[]
for i in pure_city_list:
    city_count_list.append(raw_city_list.count(i))
plt.pie(city_count_list,labels=pure_city_list,autopct='%1.1f%%',)
plt.show()
