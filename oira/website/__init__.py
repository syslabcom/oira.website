from zope.i18nmessageid import MessageFactory

_ = OIRAMessageFactory = MessageFactory('oira')

# Make it also run under python2.6
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict


def initialize(context):
    """Intializer called when used as a Zope 2 product."""
    pass
