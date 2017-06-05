from __future__ import print_function

import logging
import os
import random
import sys
import string

from attrdict import AttrDict

from testapp.models import Author, Quote

LOG_DATE_FORMAT     = '%Y-%m-%d %H:%M:%S'
LOG_MSG_FORMAT      = '%(asctime)s %(process)d %(levelname)s %(message)s'

FIRST_NAME_LEN_MIN  =    5
FIRST_NAME_LEN_MAX  =   25
LAST_NAME_LEN_MIN   =    5
LAST_NAME_LEN_MAX   =   25
NUM_AUTHORS_MIN     =  300
NUM_AUTHORS_MAX     = 2000
NUM_QUOTES_MIN      =  100
NUM_QUOTES_MAX      = 1000
QUOTE_LEN_MIN       =   30
QUOTE_LEN_MAX       =  200

#####

def generate_name(r):
    len_first_name = r.randrange(FIRST_NAME_LEN_MIN, FIRST_NAME_LEN_MAX)
    len_last_name  = r.randrange(LAST_NAME_LEN_MIN,  FIRST_NAME_LEN_MAX)

    logging.debug('{:<16} {}'.format('len_first_name', len_first_name))
    logging.debug('{:<16} {}'.format('len_last_name',  len_last_name))

    return AttrDict \
        ({
         'first_name'   : ''.join([ r.choice(string.lowercase) 
                                for i in range(len_first_name) ]).capitalize(),

         'last_name'    : ''.join([ r.choice(string.lowercase) 
                                for i in range(len_last_name) ]).capitalize(),
         })

#####

def generate_quote(r):
    len_quote = r.randrange(QUOTE_LEN_MIN, QUOTE_LEN_MAX)

    logging.debug('{:<16} {}'.format('len_quote',  len_quote))

    return AttrDict \
        ({
         'text'     : ''.join([ r.choice(string.lowercase + ' ') 
                            for i in range(len_quote) ])
         })

#####

def init_logging():
    formatter = logging.Formatter(LOG_MSG_FORMAT, LOG_DATE_FORMAT)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    logging.getLogger().setLevel(logging.INFO)
    logging.getLogger().addHandler(handler)
    return

#####

#####

def main(argv):
    '''Main function.'''

    #   Don't buffer standard output.
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

    init_logging()

    sys_rand = random.SystemRandom()

    num_authors = sys_rand.randrange(NUM_AUTHORS_MIN, NUM_AUTHORS_MAX)

    logging.info('{:<16} {}'.format('num_authors', num_authors))

    for a in range(num_authors):
        logging.info('author {} of {}'.format(1 + a, num_authors))

        author = generate_name(sys_rand)

        logging.debug('{:<16} {}'.format('last_name',  author.last_name))
        logging.debug('{:<16} {}'.format('first_name', author.first_name))

        author, created = Author.objects.get_or_create(**author)

        num_quotes = sys_rand.randrange(NUM_QUOTES_MIN, NUM_QUOTES_MAX)
        logging.info('{:<4}{:<16} {}'.format('', 'num_quotes', num_quotes))

        for q in range(num_quotes):
            quote = generate_quote(sys_rand)
            quote.update({ 'author_id' : author.id })

            logging.debug('{:<4}{:<16} {}'.format('', 'quote', quote.text))

            quote, created = Quote.objects.get_or_create(**quote)
        #   for q in range(num_quotes):

    return 0

#####

if __name__ == '__main__':
    sys.exit(main(sys.argv))
