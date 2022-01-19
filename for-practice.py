def screen_split(screen_number=80):
    print('-' * screen_number)


screen_split()
print('# for iterating over a list:')
sentence = ['I', 'want', 'to', 'eat', 'a', 'burger']

for word in sentence:
    print(word)


screen_split()
print('# for with range')
for number in range(5, 35, 5):
    print(number)


screen_split()
print('# create usernames')
names = ['Vinícius Cavalcante', 'Linda Cavalcante', 'Elvis Cavalcante']
usernames = []

for name in names:
    usernames.append(name.lower().replace(' ', '_'))

print(usernames)


screen_split()
print('# modify usernames')
for i in range(len(usernames)):
    usernames[i] = usernames[i].title().replace('_', ' ')

print(usernames)


screen_split()
print('# tag-counter')
tokens = ['<greeting>', 'Hello, World!', '</greeting>']
count = 0

for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)


screen_split()
print('# create an html list')
items = ['first string', 'second string']
html_str = '<ul>\n'

for item in items:
    html_str += '<li>{}</li>\n'.format(item)
html_str += '</ul>'
aaaaaaaa
print(html_str)