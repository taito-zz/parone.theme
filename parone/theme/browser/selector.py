from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from Products.LinguaPlone.browser.selector import TranslatableLanguageSelector


class LanguageSelector(TranslatableLanguageSelector):
    """Language selector.
    """

    render = ZopeTwoPageTemplateFile('templates/info.pt')
