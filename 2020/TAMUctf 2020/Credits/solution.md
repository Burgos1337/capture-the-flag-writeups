# Credits writeup

After the registration we have entered the store, where we need to get 2000000000 credits for purchasing the flag:

![Credits(0)](https://user-images.githubusercontent.com/57829161/78355259-15e44300-75b6-11ea-9514-93c828a178f0.png)

Then I have used BurpSuite to check if there any POST headers sent to the server and found the increment value, that equals 1 by default.
I have changed the increment value to 2000000000 and got the required number of credits on the account:

![Credits(1)](https://user-images.githubusercontent.com/57829161/78355590-9dca4d00-75b6-11ea-9bd2-1892a09a38b2.png)

![Credits(2)](https://user-images.githubusercontent.com/57829161/78355606-a3279780-75b6-11ea-97cb-7acb6132017f.png)

![Credits(3)](https://user-images.githubusercontent.com/57829161/78355614-a6bb1e80-75b6-11ea-85f5-c72d74219339.png)

Well, now we need just to buy the flag and check it in the inventory list:

![Credits(4)](https://user-images.githubusercontent.com/57829161/78355857-234dfd00-75b7-11ea-83d1-addf2ac5b326.png)

![Credits(flag)](https://user-images.githubusercontent.com/57829161/78355862-2812b100-75b7-11ea-9156-b1a469a8fc4d.png)

Flag: gigem{serverside_53rv3r5163_SerVeRSide}
