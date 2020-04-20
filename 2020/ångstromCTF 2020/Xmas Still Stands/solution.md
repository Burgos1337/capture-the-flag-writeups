# Xmas Still Stands writeup

In that task our purpose is to steal the admin's cookies via XSS-injection (it's convenient to use requestbin.com there):

![xmas(1)](https://user-images.githubusercontent.com/57829161/77068928-8147e580-69f8-11ea-9ee8-5aa7430e7054.png)

Now it's time to check our webhook:

![xmas(2)](https://user-images.githubusercontent.com/57829161/77069034-ba805580-69f8-11ea-8600-241e1e8666e0.png)

All that remains just to set the cookie values in the debug panel and get the flag:

![xmas(flag)](https://user-images.githubusercontent.com/57829161/77069184-003d1e00-69f9-11ea-8475-5833dfaacace.png)

Flag: actf{s4n1tize_your_html_4nd_your_h4nds}
