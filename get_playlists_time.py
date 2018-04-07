import requests
from bs4 import BeautifulSoup

def convert_time(string):
	minuts = int(string.split(':')[0])
	seconds = int(string.split(':')[1])
	return 60*minuts + seconds

def format_time(time):
	minuts = int(time/60)
	seconds = time - minuts*60
	if(minuts > 60):
		hours = int(minuts/60)
		minuts -= hours*60
		return "{} hours, {} minuts e {} seconds".format(hours, minuts, seconds)
	return "{} minuts e {} seconds".format(minuts, seconds)


def main():
	time = 0
	url = input('Url: ')
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'html.parser')
	for texto in soup.findAll('div', {'class' : 'timestamp'}):			
		for content in texto.contents:						
			time += converte_time(content.string)
	print("time total: " + formata_time(time))
	input("Press <Enter> to continue...")		

if __name__ == '__main__':
	main()
