# Too Many Credits 1 writeup

Inherently all that we have in this task is a simple service which adds 1 credit to our account when we just click the button:

![too_many_credits(0)](https://user-images.githubusercontent.com/57829161/78353503-d6682780-75b2-11ea-920c-0db68526b3c7.png)

Primarily we need to check the debug panel, more precisely, the cookies:

![too_many_credits(1)](https://user-images.githubusercontent.com/57829161/78353450-b89ac280-75b2-11ea-94c2-cce8e6d111f2.png)

Every time we click the button, the exact part of the cookie string modifies (so we need to use BurpSuite to change this string and
send the required one to the server):

![too_many_credits(flag)](https://user-images.githubusercontent.com/57829161/78353790-55f5f680-75b3-11ea-95b2-9121af76df87.png)

Flag: gigem{l0rdy_th15_1s_mAny_cr3d1ts}
