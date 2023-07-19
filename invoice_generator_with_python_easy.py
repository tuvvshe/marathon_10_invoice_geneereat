product1_name, product1_price = 'Ram', 55.99
product2_name, product2_price = 'Hard drive', 249.99
product3_name, product3_price = 'Headset', 199.99

company_name = 'HSMW, CB.'
company_address = '09648 Mittweida, Germany'
company_state = 'Saxon'

message = 'Thank you for shopping in our Mall Today, See you new time!'

print('*' * 50)

print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))
print('\t\t{}'.format(company_city.title()))

print('=' * 50)


print('\tProduct Name\tProduct Price')

print('\t{}\t\t${}'.format(product1_name.title(), product1_price))
print('\t{}\t${}'.format(product2_name.title(), product2_price))
print('\t{}\t\t${}'.format(product3_name.title(), product3_price))

print('=' * 50)


print('\t\t\tTotal')

total = product1_price + product2_price + product3_price
print('\t\t\t${}'.format(total))


print('=' * 50)

print('\n\t{}\n'.format(message))

print('*' * 50)
