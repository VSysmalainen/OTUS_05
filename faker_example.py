import json
from faker import Faker
from faker.providers import internet
from faker.providers.address.ru_RU import Provider as RuAddress
from faker.providers.person.ru_RU import Provider as RuPerson


fake = Faker()
fake.add_provider(internet)
fake.add_provider(RuAddress)
fake.add_provider(RuPerson)

with open('result.json', 'w', newline='') as json_file:
    writer = json.dump(json_file, data)







