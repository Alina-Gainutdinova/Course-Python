route_dict_info = {'speed': 80, 'time': 30}
dict_info = {'color': 'blue'}
route_dict_info_2 = {'distance': 50}


def route_info(route_dict: dict):
    if 'distance' in route_dict and type(route_dict['distance']) == int:
        return f'Distance to your destination is {route_dict["distance"]}'
    elif 'speed' in route_dict and 'time' in route_dict:
        return f'Distance to your destination is {route_dict["speed"] * route_dict["time"]}'
    else:
        return f'No distance info is available'


print(route_info(route_dict_info_2))
