import requests

try:
    response = requests.get('https://detik.com')
    if response.status_code == 200 :
        print("Success!", response)
        print("Content", response.text)
    else:
        print("Woooppps, Ada kesalahan")
except Exception as e:
    print("There is an Error")

