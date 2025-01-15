filename = 'brewster.dat'
fh = open(filename)
data = dict()
for line in fh:
    line = line.strip().split()
    id, amount = int(line[0]), float(line[1])
    if id in data.keys():
        data[id].append(amount)
    else:
        data[id] = [amount]

print('Brewster\'s Used Cars,  Inc.')
print('Sales Report')
print('\n{0:20s}{1:15s}'.format('Salesperson ID', 'Sales Amount'))
print('='*35)
total = 0
for key in data.keys():
    temp = 0
    for item in data[key]:
        print('{0:<20d}${1:<15.2f}'.format(key, item))
        temp += item
    print('Total sales for the salesperson: ${0:.2f}'.format(temp))
    total += temp
print('Total of all sales: ${0:.2f}'.format(total))