from five import grok
from oira.website.content.tools import IToolsRegistry
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collections import OrderedDict
from oira.website import vocabularies 
from zope import component

grok.templatedir('templates')


class OiRAToolsView(grok.View):
    grok.name('view')
    grok.context(IToolsRegistry)
    grok.require('zope2.View')
    _template = ViewPageTemplateFile('templates/available_tools.pt')
    vocabularies = vocabularies

    def render(self):
        return self._template()

    def get_tools_by_country(self):
        tdict = OrderedDict([(c, {'tools': []}) for c in vocabularies.COUNTRIES])
        for t in self.context.tools:
            tdict[t['country']]['tools'].append(t)
        for key, value in tdict.items():
            value['tools'] = sorted(value['tools'], key=lambda t: t['sector'])
            langs = list(set([t['language'] for t in value['tools']]))
            if not len(langs):
                continue
            cond = ''.join(["language='%s' or " % lang for lang in langs])
            tdict[key]['condition'] = "action:show; condition:(country='"+key+"' or country=all) and ("+cond+" language=all)"
        return tdict

    def get_current_language(self):
        """ @return: Two-letter string, the active language code
        """
        return component.getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state').language()
