from __future__ import unicode_literals

from django.db import models

#####

class Author(models.Model):

    #####

    class Meta:
        ordering        = [ 'last_name', 'first_name' ]
        unique_together = [ 'last_name', 'first_name' ]

    first_name  = models.CharField('author first name', max_length=30)
    last_name   = models.CharField('author last name',  max_length=30)

    #####

    def __unicode__(self):
        return self.last_name + ', ' + self.first_name

#####

class Quote(models.Model):
    #####

    class Meta:
        ordering        = [ 'text' ]

    author      = models.ForeignKey(Author, related_name='quotes')
    text        = models.CharField('text', max_length=2000, unique=True)

    #####

    def __unicode__(self):
        return self.text
