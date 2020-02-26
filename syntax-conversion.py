# I like to write the rules in Vimwiki, but Vimwiki's markdown is a bit idiosyncratic.
# My solution is to convert the Vimwiki file to Github Flavored Markdown via a script
# This program takes in either a command line arg or stdin to convert

import fileinput
import re

header_space_pattern = re.compile('\\(#[^\\)]*\\)')

for line in fileinput.input():
    # Fix bold difference: Vimwiki uses *bold*, Github uses **bold**
    line = line.replace('*', '**')
    # When we print, we add extra newlines. I don't compose text with two line breaks between paragraphs!
    remaining = line
    match = header_space_pattern.search(remaining)
    line = ''
    while match:
        before = remaining[:match.start()]
        target = remaining[match.start():match.end()].replace(' ', '-').lower()
        remaining = remaining[match.end():]
        line += before + target
        match = header_space_pattern.search(remaining)
    print(line)
