# I don't like needles writeup

For this challenge we’re given a link that redirects as to a login page, by the name we can conclure that we need to perform SQLi there:

![Снимок экрана (617)](https://user-images.githubusercontent.com/57829161/80566913-b59dc100-89fc-11ea-92c8-8a85d5008271.png)

Let's have a quick look at the source code:

![Снимок экрана (618)](https://user-images.githubusercontent.com/57829161/80566939-be8e9280-89fc-11ea-8132-70e88b61c57a.png)

And we find something intriguing there - our next daemon is to follow the link with the `?sauce=` in our browser:

![Снимок экрана (619)](https://user-images.githubusercontent.com/57829161/80566945-c3534680-89fc-11ea-945f-e6a6f01ef3e4.png)

There we are provided with the PHP source script of the application - it's pretty obvious now that we need to login as `flagman69` to get 
the flag:

![Снимок экрана (620)](https://user-images.githubusercontent.com/57829161/80566949-c64e3700-89fc-11ea-8bf0-11e04a0b5118.png)

![Снимок экрана (621)](https://user-images.githubusercontent.com/57829161/80566956-c8b09100-89fc-11ea-99e6-032bbcce54a1.png)

Flag: `rtcp{y0u-kn0w-1-didn't-mean-it-like-th@t}`
