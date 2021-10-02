import requests

TOKEN = '2619421814940190'

def test_request(hero_name):
	url = f'https://superheroapi.com/api/2619421814940190/search/{hero_name}/get'
	r = requests.get(url)
	return r.json()['results'][0]['powerstats']['intelligence']

if __name__ == '__main__':
	iq = {}
	iq['Hulk'] = test_request('Hulk')
	iq['Captain America'] = test_request('Captain America')
	iq['Thanos'] = test_request('Thanos')
	print(iq)

	iq_max = max(iq.values(), key=lambda i: int(i))
	for keys in iq:
		if iq[keys] == f'{iq_max}':
			print(f'{keys} is the smartest hero!')
			break
