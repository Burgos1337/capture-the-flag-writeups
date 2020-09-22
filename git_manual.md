# Basic git commands

ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

git config --global user.name "your_username"
git config --global user.email "your_email@example.com"

git clone <your_repository>

cd <your_repository>
git init
git add --all
git commit -m "your_commit"
git pull
git push -u origin master