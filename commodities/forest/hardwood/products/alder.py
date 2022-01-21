from main.commodities.forest.hardwood.hardwood import Hardwood

class Alder(Hardwood):

    name = 'Alder'

    material = 'Alder'

    attributes = {
        'thickness': {
            'name': 'Thickness',
            'description': '',
            'has_price': True,
            'priority': 1,
            'values': [
                '3/4', '4/4',
            ]
        }
   ]
        
   excluded_attributes = ["color"]
