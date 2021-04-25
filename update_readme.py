import os

readme_text = '''
# Project Euler Solutions

All problems are from [Project Euler](https://projecteuler.net).

Solutions in this repository is my own way of solving the problems. You may find your own solution to the problems.


'''

problem_list = sorted(os.listdir('python'))

for problem in problem_list:
    problem_text = problem.replace('.py', '').replace('-', ' ').title()
    adding_text = f'[{problem_text}](python/{problem})\n\n'
    readme_text += adding_text

print(readme_text)

with open('README.md', mode = 'w') as f:
    f.write(readme_text)

