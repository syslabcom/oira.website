from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from oira.website import OrderedDict
from five import grok
from oira.website import vocabularies
from oira.website.content.tools import IToolsRegistry
from plone import api
from plone.memoize.instance import memoize
from zope import component

grok.templatedir('templates')


class OiRAToolsView(grok.View):
    grok.name('view')
    grok.context(IToolsRegistry)
    grok.require('zope2.View')
    _template = ViewPageTemplateFile('templates/available_tools.pt')
    vocabularies = vocabularies

    def render(self):
        self.__populate()
        return self._template()

    @memoize
    def __populate(self):
        """ Internal method.

            Populates datastructures containing tools per country as well as all
            languages tools are available in.
        """
        ldict = {}
        langtool = api.portal.get_tool('portal_languages')
        linfo = langtool.getAvailableLanguageInformation()
        tdict = OrderedDict([(c, {'tools': []}) for c in vocabularies.COUNTRIES])
        for t in self.context.tools:
            tdict[t['country']]['tools'].append(t)
            lang = t['language']
            if not lang:
                continue
            ldict[lang] = t['language_name'] = u"({0}) {1}".format(lang.upper(), linfo.get(lang)['native'])

        for key, value in tdict.items():
            value['tools'] = sorted(value['tools'], key=lambda t: t['sector'])
            langs = list(set([t['language'] for t in value['tools']]))
            if not len(langs):
                continue
            cond = ''.join(["language='%s' or " % lang for lang in langs])
            tdict[key]['condition'] = "action:show; condition:(country='"+key+"' or country=all) and ("+cond+" language=all)"

        self.languages = OrderedDict(sorted(
            ldict.items(), key=lambda t: t[1].lower()))
        self.tools_by_country = tdict

    def get_current_language(self):
        """ @return: Two-letter string, the active language code
        """
        return component.getMultiAdapter(
                (self.context, self.request),
                name=u'plone_portal_state').language()
