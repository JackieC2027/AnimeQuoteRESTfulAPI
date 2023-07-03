import requests

# Base URL of the Flask API
base_url = 'http://localhost:5000'

# GET request to retrieve all quotes
response = requests.get(f'{base_url}/quotes')
print('GET All Quotes:')
print(response.json())
print('')

# GET request to retrieve a specific quote
quote_id = 'quote1'
response = requests.get(f'{base_url}/quotes/{quote_id}')
print(f'GET Quote {quote_id}:')
print(response.json())
print('')

# POST request to create a new quote
data = {'quote': 'New quote content'}
response = requests.post(f'{base_url}/quotes', data=data)
print('POST New Quote:')
print(response.json())
print('')

# PUT request to update an existing quote
quote_id = 'quote1'
data = {'quote': 'Updated quote content'}
response = requests.put(f'{base_url}/quotes/{quote_id}', data=data)
print(f'PUT Updated Quote {quote_id}:')
print(response.json())
print('')

# DELETE request to delete a quote
quote_id = 'quote2'
response = requests.delete(f'{base_url}/quotes/{quote_id}')
print(f'DELETE Quote {quote_id}:')
print(response.status_code)
print('')

# GET request to retrieve all quotes after modifications
response = requests.get(f'{base_url}/quotes')
print('GET All Quotes after Modifications:')
print(response.json())