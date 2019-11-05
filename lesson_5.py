import requests
cnt = 0

with open("dataset_3378_2.txt", "r") as inf:
    s = inf.readline().strip()

file_url = requests.get(s)
text = file_url.text

for line in text:
    cnt += 1

print(text.count('\n'))