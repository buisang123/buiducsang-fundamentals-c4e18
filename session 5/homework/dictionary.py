import pprint
inventory = {

    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].remove('dagger')

# print(inventory['backpack'])
inventory['gold'] = 500, 50

for k,v in inventory.items():
    print(k,v)