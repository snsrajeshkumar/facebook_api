#pip install requests
#pip install facebook-sdk


import requests
import os

access_token = 'EAAC2FZC0hankBAKM66g8kapsCC57srDpswyLnGD3ZBH1wJ4BWK2DKxShwCLNcrcDZC7Smz3XIjFl2Lj9ZApTj86S3UCeI5gIv1zWQGxxcsPyam5QZAeNv1ZBZCCeTiHT2Utrrv1MBZAKZCO36dGOZA5TU54QRJ9IGDGMdfJURZCANAkY4aoAr3EqdXxlGH6CsOghQjLpVbZC3UQGkAZDZD'
base_url = 'https://graph.facebook.com/'

#user_details
url = base_url + '/100001854737773?access_token='+access_token
response = requests.get(url)
profile = response.json()
name = profile['name']
print(name)


#post_details
url = base_url + '/465990703873939/feed?access_token='+access_token
response = requests.get(url)
profile = response.json()
data = profile['data']
for messages in data:
    message = messages['message'] if 'message' in messages else ''
    print(message)

