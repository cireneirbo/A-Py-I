import requests

def get_requests():
  #the api endpoint
  url = 'https://api.adviceslip.com/advice'

  try:
    #attempt the api request
    response = requests.get(url)

    #check if a positive return with status code being 200
    if response.status_code == 200:
      posts = response.json()
      return posts
    else:
      print('Error code:', response.status_code)
      return None
  except requests.exceptions.RequestException as e:
    print('Error:', e)
    return None

def main():
  #call the api
  posts = get_requests()
  #if it responds with data
  if posts:
    print('Id:', posts['slip']['id'])
    print('Advice:', posts['slip']['advice'])
  #if no data returns
  else:
    print('Failed to return the API data...')

if __name__ == '__main__': #this prevents calling any function other than 'main'. prevents bugs based on how python compiles imports.
  main()