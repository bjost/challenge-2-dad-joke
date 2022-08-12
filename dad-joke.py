import requests

url = "https://icanhazdadjoke.com/"
payload={}
headers = {
  'Accept': 'text/plain'
}


userResponse = input('Type a subject for a dad joke.\nPress Enter to get a random joke. ')

if userResponse == '':
    response = requests.request("GET", url, headers=headers, data=payload)
else:
    response = requests.request("GET", url+'/search?term='+userResponse, headers=headers, data=payload)

if response.text=='':
    print('Sorry, there are no dad jokes about', userResponse)
else:
    print(response.text)

