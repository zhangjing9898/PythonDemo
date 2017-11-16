import itchat
itchat.auto_login(hotReload=True)
name='xysb'
name=name.decode('gb2312')
message_object=itchat.search_friends(name)[0]
msg="....hahah"
while True:
     message_object.send(msg)
