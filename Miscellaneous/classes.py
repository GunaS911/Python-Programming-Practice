class goa:
    name='' 
    drink=''
    def party(self):
        print('Lets Party')
    def beach(self):
        print('Enjoy beach')
Guna= goa()
virrupa= goa()

Guna.party()
virrupa.beach()
Guna.name='Guna'
virrupa.name='Viruppanathan'
Guna.drink='yes'
virrupa.drink='no'
print(Guna.name)
print('drink:',Guna.drink)
print(virrupa.name)
print('drink:',virrupa.drink)
 
