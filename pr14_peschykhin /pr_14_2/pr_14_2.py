import json

with open('pr_14/pr_14_2/annotations/image_info_test-dev2017.json') as f:
    data = json.load(f)

amount_of_images = len(data['images'])

print(f'\nКількість фотографій: {amount_of_images}')

categories = len(data['categories'])
a=[]
for i in data['categories']:
    a.append(i["name"])
print(f'Кількість категорій фотографій: {categories}\n\nСам список категорій: {a}')


for i in data['images']:
    if (i["file_name"]) == "000000000001.jpg":
        link = i["coco_url"]
        height = i["height"]
        width = i["width"]        
        id = i["id"]

        print(f"\nПосилання на фото: link{link}\nЇЇ висота: {height}\nЇЇ ширина: {width}\nЇЇ ідентифікатор: {id}")

ids = ([i['id'] for i in data['images']])
for i in data["images"]:
    if i["id"] == max(ids):
        name = i["file_name"]
        print(f"\nНазва фото з найбільшим номером - {name}")
