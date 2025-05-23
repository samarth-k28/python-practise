import data_manager
import pprint
import flight_search
iatta_codes = []
data_manager = data_manager.DataManager()
data=data_manager.get_data()
data_tabel= data['prices']
pprint.pprint(data_tabel)
for i in data_tabel:
    city = i['city']
    iatta = flight_search.FlightSearch.iata_code(f'{city}')
    iatta_codes.append(iatta)
print(iatta_codes)

