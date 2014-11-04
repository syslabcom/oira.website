# _+- coding: utf-8 -*-
from collective.z3cform.datagridfield import DataGridField
from collective.z3cform.datagridfield import DictRow
from oira.website import vocabularies
from plone.app.textfield import RichText
from plone.directives import form
from plone.supermodel import model
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from zope import component
from zope import interface
from zope import schema
from zope.schema.interfaces import IField


class ICustomTableWidget(interface.Interface):
    """Subclass the widget, required for template customization"""


@interface.implementer(ICustomTableWidget)
class CustomTableWidget(DataGridField):
    """This grid should be applied to an schema.List item which has
       schema.Object and an interface"""

    allow_insert = True
    allow_delete = True
    allow_reorder = True
    auto_append = True


@component.adapter(IField, interfaces.IFormLayer)
@interface.implementer(interfaces.IFieldWidget)
def CustomTableWidgetFactory(field, request):
    """IFieldWidget factory for DataGridField."""
    return FieldWidget(field, CustomTableWidget(request))


class ITableRowSchema(form.Schema):
    country = schema.Choice(
        title=u"Country",
        vocabulary=vocabularies.countries,
        required=False,
    )
    language = schema.Choice(
        title=u"Language",
        vocabulary='oira.languages',
        required=False,
    )
    sector = schema.TextLine(
        title=u"Sector Name",
        required=False,
    )
    sector_description = schema.TextLine(
        title=u"Sector Description",
        description=u"The sector description can be used to give extra context. "
        "Often, it will be used to provide an english name when the sector "
        "name is in a different language.",
        required=False
    )
    url = schema.URI(
        title=u"Link (URL) to the sector",
        description=u"If a URL is provided here, then the \"Sector Name\" will "
        "be made a hyperlink that points to that URL.",
        required=False,
    )


class IToolsRegistry(model.Schema):
    """ Content type to allow the user to specify which tools should appear
        on the OiRA Tools page.
    """
    title = schema.TextLine(
        title=u"Title",
        default=u"OiRA Tools"
    )
    text = RichText(
        title=u"Text",
        required=False,
        default=u"""
<p class="callout"><strong>All published tools by different sectors in
different EU Member states and EU organisations<br /></strong></p>
<p><em>This page is constantly updated with newly published
tools</em></p>
<p>To access the tool click on the link and register (you just need a
valid email address)</p>"""
    )
    tools = schema.List(
        title=u"Available OiRA Tools",
        required=False,
        value_type=DictRow(
            title=u"OiRA Tool",
            required=False,
            schema=ITableRowSchema,),
    )
    form.widget(tools=CustomTableWidgetFactory)
