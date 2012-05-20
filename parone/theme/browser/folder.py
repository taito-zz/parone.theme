from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from plone.memoize.instance import memoize
from Acquisition import aq_inner


class FolderViewWithOnePicView(BrowserView):
    __call__ = ViewPageTemplateFile('templates/folder_view_with_one_pic.pt')

    @memoize
    def text(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        path = u'/'.join(context.getPhysicalPath())
        brain = catalog(
            Title='teksti',
            path=dict(query=path, depth=1)
        )[0]
        return brain.getObject().getText()

    @memoize
    def pic(self):
        context = aq_inner(self.context)
        catalog = getToolByName(context, 'portal_catalog')
        path = u'/'.join(context.getPhysicalPath())
        brain = catalog(
            Title='pic01',
            path=dict(query=path, depth=1)
        )[0]
        obj = brain.getObject()
        return obj.getField('image').tag(obj, scale='preview')
