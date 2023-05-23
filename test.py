import requests
from tinydb import TinyDB
db = TinyDB('data.json')

tables = list(db.tables())
print(tables)
for i in range(len(tables)):
    table = db.table(tables[i])
    print(i)
    print(table)
    data = table.all()
    url = 'http://127.0.0.1:8000/api/add/'
    for i in data:
        idx1 = i['RAM'].find('G')
        idx2 = i['memory'].find('G')
        data = {
            "price": i['price'],
            "memory": int(i['memory'][:idx2]),
            "ram": int(i['RAM'][:idx1]),
            "color": i['color'],
            "img_url": i['img_url'],
            "name": i['name'],
            "model": i['company'],
        }

        response = requests.post(url, json=data)
        print(response.text)
