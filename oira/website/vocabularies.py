# -*- coding: utf-8 -*-
from collections import OrderedDict
from oira.website import _
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

BASE_COUNTRIES = [
    'Austria',
    'Belgium',
    'Bulgaria',
    'Croatia',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Estonia',
    'Finland',
    'France',
    'Germany',
    'Greece',
    'Hungary',
    'Iceland',
    'Ireland',
    'Italy',
    'Latvia',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Malta',
    'Netherlands',
    'Norway',
    'Poland',
    'Portugal',
    'Romania',
    'Slovakia',
    'Slovenia',
    'Spain',
    'Sweden',
    'Switzerland',
    'United Kingdom',
]

COUNTRIES = ['Pan-European'] + BASE_COUNTRIES

countries = SimpleVocabulary(
    [SimpleTerm(value=item, title=_(item)) for item in COUNTRIES]
)

LANGUAGES = OrderedDict(sorted({
    "bg": "Bulgarian",
    "ca": "Catalan",
    "cs": "Czech",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "hu": "Hungarian",
    "is": "Icelandic",
    "it": "Italian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mt": "Maltese",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sv": "Swedish"
}.items(), key=lambda t: t[0]))

@implementer(IVocabularyFactory)
class LanguagesVocabulary(object):
    """ """
    def __call__(self, context):
        return SimpleVocabulary(
            [SimpleTerm(value=lang, title=name) for
                (lang, name) in LANGUAGES.items()])
