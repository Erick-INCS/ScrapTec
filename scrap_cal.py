#!/usr/bin/env python3
""" Fetchs scholar calendar info """

from os import system as cmd
import lxml
from Resource import Resource, ResourceList


def is_my_calendar(name):
    """ Validation func """
    name = name.text.upper()
    return ('2021-2' in name) or \
           ('2021' in name and (
                   'AGOSTO' in name or
                   'SEPTIEMBRE' in name or
                   'ENERO' in name or
                   # 'FEBRERO' in name or # For testing only
                   'DICIEMPRE' in name))


SOURCES = ResourceList([
        Resource('https://sites.google.com/tectijuana.edu.mx/' +
                 'dsc-depto-de-sistemas-y-comp/calendarios',
                 '//section[2]//h3/div/span/a',
                 name_extractor=lambda e:e.text,
                 url_extractor=lambda e:e.attrib['href'])

        # TODO: Add another sources
        ], validation=is_my_calendar)


def show_page(obj):
    """ Shows the fetched page in the web browser """
    with open('page.html', 'w') as page:
        page.write(str(lxml.html.tostring(obj)))
        print('\t"page.html" saved.')
        cmd('brave-browser page.html')


def start():
    """ Start point """
    return SOURCES.fetch()


if __name__ == '__main__':
    result = start()
    list(map(lambda e: print(f'{e[0]}:\n\t{e[1]}\n'), result))

    if not result:
        print('\n\tAun no esta el calendario :|')