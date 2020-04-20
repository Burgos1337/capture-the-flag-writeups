# Password Extraction writeup

Firstly we need to check all the databases that are located on the server (so the sqlmap tool will help us to do this):

![pe(1)](https://user-images.githubusercontent.com/57829161/78356887-1f22df00-75b9-11ea-9259-0ce9b30c26e4.png)

![pe(2)](https://user-images.githubusercontent.com/57829161/78356938-319d1880-75b9-11ea-99cb-55e92d970903.png)

The same way we are able to retrieve the table `accounts` in the `db` database and then dump it and get the flag:

![pe(3)](https://user-images.githubusercontent.com/57829161/78357018-57c2b880-75b9-11ea-8555-f06985759784.png)

![pe(flag)](https://user-images.githubusercontent.com/57829161/78357025-5b563f80-75b9-11ea-98d1-3330e10b26df.png)

Flag: gigem{h0peYouScr1ptedTh1s}
