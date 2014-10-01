# -*- coding: utf-8 -*-
from Products.Archetypes.utils import shasattr
from oira.website.config import DEFAULT_TOOLS
from plone import api
import logging


log = logging.getLogger(__name__)

def install_datagridfield(context):
    api.portal.get_tool('portal_setup').runAllImportStepsFromProfile(
            'profile-collective.z3cform.datagridfield:default')


def add_tools_registry(context):
    """ Add and populate the OiRA Tools registry, which contains tools shown
        on the OiRA Tools page.
    """
    api.portal.get_tool('portal_setup').runImportStepFromProfile(
                'profile-oira.website:default', 'typeinfo')
    site = api.portal.get()
    # FIXME: id must be available-tools
    obj_id = 'oira-tools'
    if shasattr(site, obj_id):
        log.info("Abort upgrade step 'Add Tools Registry', there already is an "
                "object with id '%s' in the site root.")
        return
    types = api.portal.get_tool('portal_types')
    registry_type = types['oira.website.tools_registry']
    registry_type.global_allow = True
    site.invokeFactory(
        "oira.website.tools_registry",
        obj_id,
        **{
            'title': 'OiRA Tools',
            'tools': DEFAULT_TOOLS,
        }
    )
    registry_type.global_allow = False
