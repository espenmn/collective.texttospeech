# -*- coding: utf-8 -*-
"""Viewlets used on the package."""
from collective.texttospeech.interfaces import ITextToSpeechControlPanel
from plone import api
from plone.app.layout.viewlets.common import ViewletBase


class TextToSpeechViewlet(ViewletBase):

    """Viewlet with play button."""

    def enabled(self):
        portal_type = getattr(self.context, 'portal_type', None)
        if portal_type is None:
            return False

        enabled_content_types = api.portal.get_registry_record(
            ITextToSpeechControlPanel.__identifier__ + '.enabled_content_types')
        return portal_type in enabled_content_types

    def voice(self):
        return api.portal.get_registry_record(
            ITextToSpeechControlPanel.__identifier__ + '.voice'
        )
