import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'protoapp.settings'

from django import setup
from django.test import TestCase

from protoapp.models import Author, Quote

class AuthorTestCase(TestCase):

    #####

    def setUp(self):
        roma  = Author.objects.create(first_name='Jon', last_name='Roma')

        zippy = Author.objects.create \
            (first_name='Zippy the', last_name='Pinhead')
        return

    #####

    def test_author(self):
        self.assertEqual(Author.objects.count(), 2)

        author = Author.objects.get(first_name='Jon', last_name='Roma')
        self.assertEqual(author.first_name, 'Jon')
        self.assertEqual(author.last_name,  'Roma')
        return

class QuoteTestCase(TestCase):

    quote_roma = \
        [
        'It\'s basically a calendar, but primarily a clock.',
        'There\'s a turtle under the TV!',
        ]

    quote_zippy = \
        [
        'Are we having FUN yet...?',
        'Civilization is fun! Anyway, it keeps me busy!!',
        'Did I do an INCORRECT THING??',
        'Half a mind is a terrible thing to waste!',
        'I always have fun because I\'m out of my mind!!!',
        'I feel partially hydrogenated!',
        'I just had my entire INTESTINAL TRACT coated with TEFLON!',
        'I was making donuts and now I\'m on a bus!',
        'I\'m into SOFTWARE!',
        'I\'m in DIRECT daily contact with many advanced fun CONCEPTS.',
        'I\'m pretending I\'m pulling in a TROUT! Am I doing it correctly??',
        'Loni Anderson\'s hair should be LEGALIZED!!',
        'This is a NO-FRILLS flight -- hold th\' CANADIAN BACON!!',
        'Uh-oh!! I\'m having TOO MUCH FUN!!',
        'Yow! Am I having fun yet?',
        ]

    #####

    def bulk_add(self, author_id, quote_list):
        ql = []

        for quote in quote_list:
            ql.append(Quote(author_id=author_id, text=quote))

        Quote.objects.bulk_create(ql)
        return

    #####

    def setUp(self):
        roma = Author.objects.create(first_name='Jon', last_name='Roma')

        self.bulk_add(roma.id, self.quote_roma)

        zippy = Author.objects.create \
            (first_name='Zippy the', last_name='Pinhead')

        self.bulk_add(zippy.id, self.quote_zippy)

        return

    #####

    def test_quote(self):
        self.assertEqual(Quote.objects.count(), 17)
        roma  = Author.objects.get(first_name='Jon', last_name='Roma')
        zippy = Author.objects.get(first_name='Zippy the', last_name='Pinhead')

        #   Get query set containing all quotes containing the word 'fun'.
        qs_fun = Quote.objects.filter(author_id=zippy.id, text__contains='fun')
        self.assertEqual(qs_fun.count(), 6)
        return
