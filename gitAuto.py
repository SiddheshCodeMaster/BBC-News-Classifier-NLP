import os

lst = ['git pull','git add -A','git commit -m "First Commit"','git push']

for i in lst:
    os.system(i)