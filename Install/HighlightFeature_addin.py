import arcpy
import pythonaddins

class ButtonClass5(object):
    """Implementation for HighlightFeature_addin.button (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        try:
            t1, t2 = arcpy.ListFields(activelyr, activecol)[0].type, arcpy.ListFields(searchlyr, searchcol)[0].type
            types = ['String','SmallInteger','Double','Integer','Single','OID','Date']
            if t1 not in types or t2 not in types:
                return
            lyr0 = arcpy.MakeTableView_management(activelyr,'lyr0')
            lyr = arcpy.MakeTableView_management(lyr0,'lyr')
            arcpy.Delete_management(lyr0)
            sc = arcpy.SearchCursor(lyr)
            searchLst = []
            for row in sc:
                searchLst.append(row.getValue(activecol))
            del sc
            arcpy.Delete_management(lyr)
            query = ''
            for val in searchLst:
                if t1=='String':
                    query += " OR %s = '%s'" % (searchcol,str(val))
                elif t1 in ['SmallInteger','Integer','OID']:
                    query += " OR %s = %d" % (searchcol, int(val))
                elif t1 in ['Double','Single']:
                    query += " OR %s = %f" % (searchcol, float(val))
                else:
                    query += " OR %s = date '%s'" % (searchcol, str(val))
            query = query[4:]
            pythonaddins.MessageBox(query,'title')
            arcpy.SelectLayerByAttribute_management(searchlyr,'NEW_SELECTION',query)
            mxd = arcpy.mapping.MapDocument('CURRENT')
            df = arcpy.mapping.ListDataFrames(mxd)[0]
            df.zoomToSelectedFeatures()
            arcpy.RefreshActiveView()
        except:
            if arcpy.Exists('lyr0'):arcpy.Delete_management('lyr0')
            if arcpy.Exists('lyr'): arcpy.Delete_management('lyr')
            pass

class ComboBoxClass1(object):
    """Implementation for HighlightFeature_addin.combobox (ComboBox)"""

    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWWW'

    def onSelChange(self, selection):
        global activelyr
        activelyr = selection

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        try:
            mxd = arcpy.mapping.MapDocument('CURRENT')
            layers = arcpy.mapping.ListTableViews(mxd)
            self.items = []
            for lyr in layers:
                desc = arcpy.Describe(lyr)
                self.items.append(desc.name)
            layers = arcpy.mapping.ListLayers(mxd)
            for lyr in layers:
                desc = arcpy.Describe(lyr)
                self.items.append(desc.name)
        except:pass

    def onEnter(self):
        pass

    def refresh(self):
        pass

class ComboBoxClass2(object):
    """Implementation for HighlightFeature_addin.combobox_1 (ComboBox)"""
    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWWW'

    def onSelChange(self, selection):
        global activecol
        activecol = selection

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        try:
            desc = arcpy.Describe(activelyr)
            self.items = []
            for f in desc.fields:
                self.items.append(f.name)
        except:pass

    def onEnter(self):
        pass

    def refresh(self):
        pass

class ComboBoxClass3(object):
    """Implementation for HighlightFeature_addin.combobox_2 (ComboBox)"""

    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWWW'

    def onSelChange(self, selection):
        global searchlyr
        searchlyr = selection

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        try:
            mxd = arcpy.mapping.MapDocument('CURRENT')
            layers = arcpy.mapping.ListLayers(mxd)
            self.items = []
            for lyr in layers:
                desc = arcpy.Describe(lyr)
                self.items.append(desc.name)
        except:pass

class ComboBoxClass4(object):
    """Implementation for HighlightFeature_addin.combobox_3 (ComboBox)"""

    def __init__(self):
        self.items = []
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWWWWWWWWWWWWWWWWWWWW'
        self.width = 'WWWWWWWWWWWWWWW'

    def onSelChange(self, selection):
        global searchcol
        searchcol = selection

    def onEditChange(self, text):
        pass

    def onFocus(self, focused):
        try:
            desc = arcpy.Describe(searchlyr)
            self.items = []
            for f in desc.fields:
                self.items.append(f.name)
        except: pass

    def onEnter(self):
        pass

    def refresh(self):
        pass