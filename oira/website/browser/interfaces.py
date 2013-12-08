# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer



class IOiRAWebsiteLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""

