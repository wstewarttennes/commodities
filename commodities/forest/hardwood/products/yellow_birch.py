from main.commodities.forest.hardwood.hardwood import Hardwood

class YellowBirch(Hardwood):

    name = 'Yellow Birch'

    material = 'Yellow Birch'

    weight_per_board_foot = {
        'rought': 40,
        'fd': 32
    } 
    
    default_attributes = {
        'color': {
            'name': 'Color',
            'description': '',
            'priority': 4,
            'values': [
            ]
        },
    }