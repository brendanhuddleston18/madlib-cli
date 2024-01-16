import re 
dark_stormy_night_path = "assets/dark_and_stormy_night_template.txt"

print("""Welcome to Brendan's Madlib Adventure
------------------------------------------------
Here you will be prompted to enter words
based on the type of word needed!
When Complete you will have a hilarious
story to show to your friends and family! \n""")

madlib_template = ''
split_word_types = []
user_answers = []
empty_template = ''

def madlib():
  start = input("Are you ready to start? \nyes/no\n> ")
  while start.lower() != 'yes':
    start = input("Are you ready to start? yes/no")
  if start.lower() == 'yes':
    read_template(dark_stormy_night_path)
    parse_template(madlib_template)
    for word_type in split_word_types[0]:
      user_answers.append(input(f'Enter a {word_type}\n> '))
    merge(empty_template, user_answers)


def read_template(path):
  global madlib_template
  with open (path, 'r') as template:
    madlib_template =  template.read()
    return madlib_template

def parse_template(template):
  global empty_template
  # Ekow helped me with this 
  pattern = re.compile(r'{(.*?)}')
  parts = pattern.findall(template)
  split_word_types.append(parts)
  empty_template = re.sub(r'{(.*?)}', '{}', template)
  return empty_template, tuple(parts)

def merge(template, user_answers):
  complete_madlib = template.format(*user_answers)
  print(complete_madlib)
  return complete_madlib

if __name__ == "__main__":
  madlib()