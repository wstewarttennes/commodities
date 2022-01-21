from main.commodities.forest.forest import Forest

class Hardwood(Forest):

    commodity = "Hardwood"

    commodity_forms = ['Lumber', 'Logs', 'Plywood']

    default_attributes = {
        'thickness': {
            'name': 'Thickness',
            'description': '',
            'has_price': True,
            'priority': 1,
            'values': [
                '3/4', '4/4', '5/4', '6/4', '7/4', '8/4', '9/4', '10/4', '12/4', '16/4'
            ]
        },
        'grade': {
            'name': 'NHLA Grade',
            'description': '',
            'has_price': True,
            'priority': 2,
            'values': [
                'FAS', 'FAS/1F', 'Select', 'Select & Better', 'Prime', 'COM/SEL', '#1 COM', 
                '#2 COM', '#2A COM', '#2B COM', '#3A COM', '#3B COM', 'Frame', 'Millrun'
            ]
        },
        'drying': {
            'name': 'Drying',
            'description': '',
            'priority': 3,
            'values': [
                'Green', 'Air Dried', 'Kiln Dried'
            ]
        },
        'color': {
            'name': 'Color',
            'description': '',
            'priority': 4,
            'values': [
                'Stain', '90/90', '90/80+', '90/70+', '90/50+', 'Wheat', 'Natural', 'Unselected', 
                'Sap/Btr', '#1 White', '#2 White', '#1&2 White'
            ]
        },
        # 'region': {
        #     'name': 'Region',
        #     'description': '',
        #     'values': [
        #         'Western', 'Northern', 'Southern', 'Northern', 'Glacial'
        #     ]
        # }
        # 'width': {
        #     'name': 'Width',
        #     'description': '',
        #     'values': [
        #         'Random Width', '4"+', '5"+', '6"+', '7"+', '8"+', '9"+', '10"+', '12"+', 
        #         'Custom Pull'
        #     ]
        # },
        # 'length': {
        #     'name': 'Length',
        #     'description': '',
        #     'values': [
        #         'Random Length', '4"+', '6"+', '7"+', '8"+', '9"+', '10"+', '12"+', '14"+', 
        #         '16"+','Custom Pull'
        #     ]
        # },
        # 'wha_alder_grade': {
        #     'name': 'WHA Alder Grade',
        #     'description': '',
        #     'values': [
        #         'Superior', 'Superior 1 Face', 'Superior Color', 'Custom Jacket Board', 
        #         'Cabinet', 'Cabinet Color', 'Custom Shop', 'Custom Shop Color', 'Common Shop',
        #         'Com2','Jacket Board', 'Premium Frame', 'K-Strip', 'Character', 'Rustic', 
        #         'Standard Frame', '#3 Shop', 'Economy', 'Utility'
        #     ]
        # },
        # 'wha_pc_mape_grade': {
        #     'name': 'WHA PC Mape Grade',
        #     'description': '',
        #     'values': [
        #         'Select', '#1 Shop', '#2 Shop', '#3 Shop', 'Standard Frame'
        #     ]
        # },
    }


