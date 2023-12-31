#!/usr/bin/python3
arg = 'name=philip'
my_dict = {"State.53dac5a1-b9b9-4970-bd4c-ca516dfae28f": {"id": "53dac5a1-b9b9-4970-bd4c-ca516dfae28f", "created_at": "2023-12-31T06:22:18.529286", "updated_at": "2023-12-31T06:22:18.529301", "name": "California", "__class__": "State"}, "State.ebb6e114-5086-47c8-a1b2-0c43d294298d": {"id": "ebb6e114-5086-47c8-a1b2-0c43d294298d", "created_at": "2023-12-31T06:22:18.532637", "updated_at": "2023-12-31T06:22:18.532644", "name": "Arizona",
                                                                                                                                                                                                                                                                                            "__class__": "State"}, "Place.f0f921cd-3dde-4e5f-b55e-1a5ff2d0159f": {"id": "f0f921cd-3dde-4e5f-b55e-1a5ff2d0159f", "created_at": "2023-12-31T06:22:18.533190", "updated_at": "2023-12-31T06:22:18.533195", "city_id": "0001", "user_id": "0001", "name": "My little house", "number_rooms": 4, "number_bathrooms": 2, "max_guest": 10, "price_by_night": 300, "latitude": 37.773972, "longitude": -122.431297, "__class__": "Place"}}
for key, val in my_dict.items():
    print(f'{key}: {val}')
new_dict = {}
print('-------------------------------------------------')
for key, val in my_dict.items():
    if 'State' in key:
        new_dict[key] = val
print(new_dict)
