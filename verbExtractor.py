import requests

german_verb = 'brauchen'
connection_string = 'https://conjugator.reverso.net/conjugation-german-verb-{}.html'.format(
    german_verb)

r = requests.get(
    connection_string, auth=('user', 'pass'))
print(r.text)
