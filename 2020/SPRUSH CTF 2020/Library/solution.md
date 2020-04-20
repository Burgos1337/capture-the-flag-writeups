# Library writeup

So many useful books here...

![lib(1)](https://user-images.githubusercontent.com/57829161/78889894-440dcb00-7a6d-11ea-8068-69e91f651a03.png)

Let's try to click in one of them and check the request in BurpSuite:

![lib(2)](https://user-images.githubusercontent.com/57829161/78889902-48d27f00-7a6d-11ea-96e6-9097d90d2520.png)

![lib(3)](https://user-images.githubusercontent.com/57829161/78889907-4b34d900-7a6d-11ea-8aa0-37b97ae50bdb.png)

The main idea is just to read the ```flag.txt``` file on the server, so let's make our payload and check the output in BurpSuite:

![lib(4)](https://user-images.githubusercontent.com/57829161/78889913-4f60f680-7a6d-11ea-95bc-e4f625e02041.png)

![lib(flag)](https://user-images.githubusercontent.com/57829161/78889921-525be700-7a6d-11ea-8886-0d3acddf3c06.png)

Flag: SPR{G00D_H4CK3R_R3AD_G00D_B00KS}
