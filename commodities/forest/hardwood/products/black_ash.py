from main.commodities.forest.hardwood.hardwood import Hardwood

class BlackAsh(Hardwood):

    name = 'Black Ash'

    material = 'Black Ash'

    attributes = {
        'grade': {
            'name': 'NHLA Grade',
            'description': '',
            'has_price': True,
            'priority': 2,
            'values': [
                'Prime', 'COM/SEL', '#1 COM', '#2 COM', 
            ]
        },
        'drying': {
            'name': 'Drying',
            'description': '',
            'priority': 3,
            'values': [
                'Kiln Dried'
            ]
        }
    ]
