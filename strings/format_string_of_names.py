'''
Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, 
which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
'''


def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


names = [{'name': 'Bart'}, {'name': 'Lisa'}, {
    'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]

print(namelist(names))
