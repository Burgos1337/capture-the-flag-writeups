# Spooky Store writeup

Initially we are dealing with the service that calculates the nearest coordinates:

![spooky-store(0)](https://user-images.githubusercontent.com/57829161/76204367-534cef00-6209-11ea-8895-e7c611897df5.png)

Let's take a quick look at the request in burp suite (with intercept on enabled):

![spooky-store(1)](https://user-images.githubusercontent.com/57829161/76204799-2220ee80-620a-11ea-9d78-7ccaced7944f.png)

Surely we have to exploit the XXE vulnerability, all that we need is to get an access to `/etc/passwd` file on the server:

![spooky-store(2)](https://user-images.githubusercontent.com/57829161/76205879-21895780-620c-11ea-87e9-8813f766248b.png)

After forwarding the request in burp suite we get the flag on the server:

![spooky-store(flag)](https://user-images.githubusercontent.com/57829161/76206075-6f9e5b00-620c-11ea-9268-f05919510595.png)



Flag: utflag{n3xt_y3ar_go1ng_bl1nd}
