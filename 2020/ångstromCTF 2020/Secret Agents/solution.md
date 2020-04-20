# Secret Agents writeup

Initially we access the service that filters our user-agent parameter:

![agents](https://user-images.githubusercontent.com/57829161/77067437-01208080-69f6-11ea-9ad6-7509b27dda48.png)

After the exploring the source code of the server (app.py) we use curl for making an injection in the user-agent parameter 

(the `res` length should equal 1) and get the flag:

![terminal(flag)](https://user-images.githubusercontent.com/57829161/77067904-bc491980-69f6-11ea-9eaa-6b7a54775a21.png)

Flag: actf{nyoom_1_4m_sp33d}
