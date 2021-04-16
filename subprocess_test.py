#!/usr/bin/python3

import subprocess

sub = subprocess.run(
        ['ls', '-l', '/etc/group', '/nonexistent'], # programma + argumenten
        stdout=subprocess.PIPE, # capture stdout
        stderr=subprocess.PIPE, # capture stderr
        universal_newlines=True # input and output in text mode
        )

print('Program: ', sub.args[0], '\n\nArgs: ', sub.args[1:], sep='')
print('\nExit code:', sub.returncode)
print('\nStdout:\n', sub.stdout, sep='')
print('Stderr:\n', sub.stderr, sep='')
