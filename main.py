from exa_py import Exa

exa = Exa(api_key="b4a5de4a-673c-4688-92b2-2626ab6a8ba7")

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)
for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()