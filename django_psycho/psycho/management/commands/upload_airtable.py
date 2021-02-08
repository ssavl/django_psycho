from psycho.models import RawData, RawMethod, PsychoMaster, Method
# from django_psycho.psycho.models import RawData, RawMethod, PsychoMaster, Method

from django.core.management import BaseCommand
import requests
from pprint import pprint
import json

URL_AIRTABLE = 'https://api.airtable.com/v0/appBvjqoOerxJZ004/Psychotherapists?'
API_KEY = 'keygmzWzN9mfdL7MC'
prms = {'api_key': API_KEY}


class Command(BaseCommand):

    def handle(self, *args, **options):
        raw_data = requests.get(URL_AIRTABLE, params=prms).text
        dump = json.loads(raw_data)

        for psycho in dump['records']:
            print('-' * 80)
            own_id = psycho['id']
            name = psycho['fields']['Имя']
            methods = psycho['fields']['Методы']
            foto = psycho['fields']['Фотография'][0]['url']

            if PsychoMaster.objects.filter(own_id=own_id).exists():
                print("True")
                data = PsychoMaster.objects.get(own_id=own_id)
                if name == data.name:
                    print('Имя не изменилось')
                else:
                    PsychoMaster.objects.filter(own_id=own_id).update(name=name)
                    print('Изменили имя')
                if f"images/{foto.split('/')[-1]}" == data.img:
                    print('Фото не изменилось')
                else:
                    img = requests.get(foto)
                    img_file = open(f"media/images/{foto.split('/')[-1]}", 'wb')
                    img_file.write(img.content)
                    img_file.close()
                    PsychoMaster.objects.filter(own_id=own_id).update(img=f"images/{foto.split('/')[-1]}")
                    print("Изменили фото")

                list_methods = [str(i) for i in Method.objects.filter(psycho_master=data)]

                if list_methods == methods:
                    print('Методы не изменились')
                else:
                    Method.objects.filter(psycho_master=data).all().delete()
                    for method in methods:
                        Method.objects.create(psycho_master=data, method=method)
                        print('Добавили новые методы')

                print('Создаем запись сырых данных')
                img = requests.get(foto)
                img_file = open(f"media/raw_images/{foto.split('/')[-1]}", 'wb')
                img_file.write(img.content)
                img_file.close()
                upload_2 = RawData.objects.create(name=name, own_id=own_id, img=f"images/{foto.split('/')[-1]}")
                for method in methods:
                    RawMethod.objects.create(psycho_master=upload_2, method=method)


            else:
                img = requests.get(foto)
                img_file = open(f"media/images/{foto.split('/')[-1]}", 'wb')
                img_file.write(img.content)
                img_file.close()
                img_file_raw = open(f"media/raw_images/{foto.split('/')[-1]}", 'wb')
                img_file_raw.write(img.content)
                img_file_raw.close()
                upload = PsychoMaster.objects.create(name=name, img=f"images/{foto.split('/')[-1]}", own_id=own_id)

                for method in methods:
                    Method.objects.create(psycho_master=upload, method=method)

                print('Создаем запись сырых данных')
                upload_2 = RawData.objects.create(name=name, own_id=own_id, img=f"raw_images/{foto.split('/')[-1]}")
                for method in methods:
                    RawMethod.objects.create(psycho_master=upload_2, method=method)














            # foto = 'https://dl.airtable.com/.attachments/fa70928a82a214d22c4b7a2eeace79d2/e5a12360/2.jpg'.split('/')[-1]

   # for method in methods:
                    #     print(f'Статус методов = {methods}')
                    #     if method not in list_methods:
                    #         print(f'Новый метод = {method}')
                    #         list_methods.append(method)
                    #         print(f'Новый статус методов = {methods}')
                    #         Method.objects.filter(psycho_master=data).update(method=list_methods)
                    #         Method.objects.filter(psycho_master=data).all().delete()
                    #         print('Добавили новые методы')
                    #     else:
                    #         pass
                        # list_methods.remove(method)
                        # for _ in list_methods:
                        #     Method.objects.filter(psycho_master=data).update(method=_)
