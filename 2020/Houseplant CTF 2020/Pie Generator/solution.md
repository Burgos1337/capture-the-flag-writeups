# Pie Generator writeup

At the first sight this task may seem to be unsolvable by simple methods:

![Снимок экрана (627)](https://user-images.githubusercontent.com/57829161/80570163-ff89a580-8a02-11ea-9bd5-cb676ac65759.png)

![Снимок экрана (628)](https://user-images.githubusercontent.com/57829161/80570168-02849600-8a03-11ea-800e-971b8bf531f3.png)

Let's explore the request in BurpSuite:

![Снимок экрана (630)](https://user-images.githubusercontent.com/57829161/80570174-06181d00-8a03-11ea-9e1c-d48afe6596f2.jpg)

So we record the correct number and timestamp and then replay that resending the HTTP request with edited POST data:

![Снимок экрана (631)](https://user-images.githubusercontent.com/57829161/80570182-09130d80-8a03-11ea-9ceb-75f19519af4c.jpg)

Flag: `rtcp{w0w_s0_p53uD0}`
