import requests

with open('dataset_3378_3.txt', 'r') as inf:
    link = inf.readline().strip()

file = requests.get(link)
file_url = "https://stepic.org/media/attachments/course67/3.6.3/"
file_text = file.text

while file_text.find('We') == -1:
    
    file = requests.get(file_url + file.text)
    file_text = file.text 
    print(file.text)


#print(file_text)