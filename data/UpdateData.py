import subprocess

commands = [
    'rm Gender.db',
    'python3 Mapping.py',
]

for command in commands:
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
