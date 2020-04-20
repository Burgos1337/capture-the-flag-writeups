# Epic Admin Pwn writeup

After clicking the link we have to explore the form we got:

![epic(0)](https://user-images.githubusercontent.com/57829161/76207005-0c152d00-620e-11ea-8a01-944f1d6e1430.png)

![epic(1)](https://user-images.githubusercontent.com/57829161/76207012-0e778700-620e-11ea-8fa5-813f6d4a2edf.png)

Well, we had found out that this form is vulnerable to SQL injections! Let's take a look at the request in burp suite:

![epic(2)](https://user-images.githubusercontent.com/57829161/76207527-02d89000-620f-11ea-99a8-71c6006ad2fc.png)

So we have two post fields there - `username` and `pass`, after saving the request data in `request.txt` the sqlmap tool will help us to
dump the required table and get the flag:

![epic(3)](https://user-images.githubusercontent.com/57829161/76209173-4c76aa00-6212-11ea-96d2-874fa3c6fa14.png)

![epic(flag)](https://user-images.githubusercontent.com/57829161/76209274-834cc000-6212-11ea-8912-4aed85bd3cad.png)


Flag: utflag{dual1pa1sp3rf3ct}
