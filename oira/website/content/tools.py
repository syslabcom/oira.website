# _+- coding: utf-8 -*-
from collective.z3cform.datagridfield import DictRow
from osha.hwccontent import vocabularies
from osha.hwccontent.behaviors.moreabout import CustomTableWidgetFactory
from plone.app.textfield import RichText
from plone.directives import form
from plone.supermodel import model
from zope import schema


class ITableRowSchema(form.Schema):
    country = schema.Choice(
        title=u"Country",
        vocabulary=vocabularies.countries_no_pan_euro,
    )
    language = schema.Choice(
        title=u"Language",
        vocabulary='osha.languages',
    )
    attachment = schema.Text(
        title=u"Sector",
    )
    url = schema.URI(
        title=u"Sector Link (online)",
        required=False,
    )


class IToolsStorage(model.Schema):
    """ Content type to allow the user to specify which tools should appear
        on the OiRA Tools page.
    """
    title = schema.TextLine(
        title=u"Title",
    )
    text = RichText(
        title=u"Text",
        required=False,
    )
    eguides = schema.List(
        title=u"Available Tools",
        required=False,
        value_type=DictRow(
            title=u"tablerow",
            required=False,
            schema=ITableRowSchema,),
    )
    form.widget(eguides=CustomTableWidgetFactory)
