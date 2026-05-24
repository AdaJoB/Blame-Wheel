#==== State of Application Logic ====#

import json
from wheel import Wheel

current_wheel = None


def set_wheel(index):

    with open('wheels.json', 'r') as f:
        data = json.load(f)

    wheel_name = data['wheels'][index]['wheel_name']

    items = data['wheels'][index]['items']

    item_names = []
    item_weights = []
    for i in items:
        item_names.append(i['item_name'])
        item_weights.append(i['weight'])

    return Wheel(wheel_name, item_names, item_weights)
    
        
    

current_wheel = set_wheel(1)

print(current_wheel.spin())





    

    