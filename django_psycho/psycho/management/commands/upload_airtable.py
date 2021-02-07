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
            # foto = 'https://dl.airtable.com/.attachments/fa70928a82a214d22c4b7a2eeace79d2/e5a12360/2.jpg'.split('/')[-1]

            if PsychoMaster.objects.filter(own_id=own_id).exists():
                print("True")
                data = PsychoMaster.objects.get(own_id=own_id)
                if name == data.name:
                    print('Имя не изменилось')
                else:
                    data.update(name=name)
                if f"images/{foto.split('/')[-1]}" == data.img:
                    print('Фото не изменилось')
                else:
                    img = requests.get(foto)
                    img_file = open(f"media/images/{foto.split('/')[-1]}", 'wb')
                    img_file.write(img.content)
                    img_file.close()
                    data.update(img=f"images/{foto.split('/')[-1]}")

                list_methods = [str(i) for i in Method.objects.filter(psycho_master=data)]

                if list_methods == methods:
                    print('Методы не изменились')
                else:
                    for method in methods:
                        list_methods.remove(method)
                        for _ in list_methods:
                            Method.objects.filter(psycho_master=data).update(method=_)
            else:
                img = requests.get(foto)
                img_file = open(f"media/images/{foto.split('/')[-1]}", 'wb')
                img_file.write(img.content)
                img_file.close()
                upload = PsychoMaster.objects.create(name=name, img=f"images/{foto.split('/')[-1]}", own_id=own_id)

                for method in methods:
                    Method.objects.create(psycho_master=upload, method=method)
                upload_2 = RawData.objects.create(name=name, own_id=own_id, img=f"images/{foto.split('/')[-1]}")
                for method in methods:
                    RawMethod.objects.create(psycho_master=upload_2, method=method)
