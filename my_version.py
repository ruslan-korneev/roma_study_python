# iphone 1, iphone 2, iphone 3, iphone 4, iphone 5, iphone 6, iphone 7, iphone 8, samsung 1, samsung 2, samsung 3, samsung 4, samsung 5, samsung 6, samsung 7, samsung 8, samsung 9, samsung 10
phones = input('Input phones: ').split(', ')

# sort to iphones and samsungs lists
iphones = [(phone.split(" ")[0], int(phone.split(" ")[1]))
           for phone in phones if phone.lower().startswith('iphone')]
samsungs = [(phone.split(" ")[0], int(phone.split(" ")[1]))
            for phone in phones if phone.lower().startswith('samsung')]

# which phones more
if len(iphones) > len(samsungs):
    print('iPhones more than Samsungs')
elif len(iphones) < len(samsungs):
    print('Samsungs more than iPhones')
else:
    print('The same lists')

# last models of iphone and samsung
print(f"Iphone last model: {max([model for _, model in iphones])}")
print(f"Samsung last model: {max([model for _, model in samsungs])}")
