#!/usr/bin/python

import argparse
from book import Book

# parse some input params
# $booklog <title>: show status of book (if book exists or not, show similar titles to fix misspell)
# -h, --help: show help info
# -n, --note <title>: Edit book notes 
# -a, --author <firstname lastname>: author name
# -i, --isbn <number>: isbn number of book
# -e, --edit <title>
# -t, --tag <tag>: add tag to book

# example
# $booklog -n The Way of Kings -a brandon sanderson -t fantasy fiction

# $booklog "The Way of Kings"
# >> The Way of Kings by Brandon Sanderson
# >> Tags: Fantasy, Fiction
# >> Notes: ...


parser = argparse.ArgumentParser(prog='booklog', description='Log your books.')

# Optionals
parser.add_argument('-t','--title', help='title of a book')
parser.add_argument('-a', '--author', help='author of a book')
parser.add_argument('-n', '--note', help='edit book note')
parser.add_argument('-l', '--list', help='add book to list')
args = parser.parse_args()

if args.title:
    bk1 = Book(args.title, args.author, args.list)
    bk1.writeBook()
