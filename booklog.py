#!/usr/bin/python

import argparse

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


# do task based on input params

parser = argparse.ArgumentParser(prog='booklog', description='Log your books.')
parser.add_argument('-t','--title', metavar='<title>', help='title of a book')
parser.add_argument('-a', '--author', metavar='<author>', help='author of a book')
parser.add_argument('-n', '--note', help='edit book note')

args = parser.parse_args()

if args.title:
    print("Title: " + args.title)

if args.author:
    print("Author: " + args.author)
