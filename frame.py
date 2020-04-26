#Boa:Frame:Frame

import wx
import account
from line import *
import datetime as dt

yOffset = yLineSize + 1
yBottomButtons = 150

xTotalSize = 1300
yFrameSize = 1000
xWindowSize = 1280
yWindowSize = yFrameSize - 254
# xTotalSize = 1200
# yFrameSize = 664
# xWindowSize = 1180
# yWindowSize = 450

def create(parent):
    return Frame(parent)

[wxID_FRAMEMENUFILECLOSE, wxID_FRAMEMENUFILEOPEN, wxID_FRAMEMENUFILEQUIT,
 wxID_FRAMEMENUFILESAVE, wxID_FRAMEMENUFILESAVEAS,
] = [wx.NewId() for _init_coll_menuFile_Items in range(5)]

[wxID_FRAMEADD, wxID_FRAMEDELETE,
 wxID_FRAMEREFRESH, wxID_FRAMEBANKORDER] = [wx.NewId() for _init_coll_buttons
                                            in range(4)]

class Frame(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'Fichier')

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(helpString=u'Ouvrir un fichier de comptes',
              id=wxID_FRAMEMENUFILEOPEN, kind=wx.ITEM_NORMAL, item=u'Ouvrir')
        parent.Append(helpString=u'Enregistrer les ecritures dans un fichier',
              id=wxID_FRAMEMENUFILESAVE, kind=wx.ITEM_NORMAL,
              item=u'Enregistrer')
        parent.Append(helpString='', id=wxID_FRAMEMENUFILESAVEAS,
                      kind=wx.ITEM_NORMAL, item=u'Enregistrer sous')
        parent.Append(helpString='', id=wxID_FRAMEMENUFILECLOSE,
                      kind=wx.ITEM_NORMAL, item=u'Fermer')
        parent.Append(helpString=u"Quitter l'application",
                      id=wxID_FRAMEMENUFILEQUIT,
                      kind=wx.ITEM_NORMAL, item=u'Quitter')
        self.Bind(wx.EVT_MENU, self.OnFileOpenMenu, id=wxID_FRAMEMENUFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnFileSaveMenu, id=wxID_FRAMEMENUFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnFileQuitMenu, id=wxID_FRAMEMENUFILEQUIT)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveasMenu,
              id=wxID_FRAMEMENUFILESAVEAS)
        self.Bind(wx.EVT_MENU, self.OnMenuFileCloseMenu,
              id=wxID_FRAMEMENUFILECLOSE)

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title=u'Fichier')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        self.lastLine = None
        self.addLine = None
        self.addButton = None
        self.deleteButton = None
        self.refreshButton = None
        self.bankOrderButton = None

        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name='', parent=prnt,
              pos=wx.Point(0, 25), size=wx.Size(xTotalSize, yFrameSize),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Comptes')
        self._init_utils()
        self.SetClientSize(wx.Size(xTotalSize, yFrameSize))
        self.SetMenuBar(self.menuBar1)

        self.upperPanel = wx.Panel(id=wxID_FRAMEUPPERPANEL,
                                   name=u'upper panel', parent=self,
                                   pos=wx.Point(0,0), size=wx.Size(xWindowSize,25))
        self.scrolledWindow = wx.ScrolledWindow\
            (parent=self, winid=wxID_FRAMESCROLLEDWINDOW,
             pos=wx.Point(0, 25), size=wx.Size(xTotalSize, yWindowSize),
             style=wx.HSCROLL | wx.VSCROLL, name=u'scrolledWindow')
        self.scrolledWindow.SetVirtualSize(size=wx.Size(xWindowSize, 300))
        self.scrolledWindow.SetScrollRate(10,10)

        self.lowerPanel = wx.Panel(id=wxID_FRAMELOWERPANEL,
                                   name=u'lower panel', parent=self,
                                   pos=wx.Point(0,yWindowSize), size=wx.Size(xWindowSize,225))

        self.dateStaticText = wx.StaticText(id=wxID_FRAMEDATESTATICTEXT,
              label=u'Date', name=u'dateStaticText', parent=self.upperPanel,
              pos=wx.Point(1, 8), size=wx.Size(100, 20), style=wx.ALIGN_CENTRE)
        self.dateStaticText.SetBackgroundColour(wx.Colour(4, 0, 0))

        self.modeStaticText = wx.StaticText(id=wxID_FRAMEMODESTATICTEXT,
              label=u'Mode de Paiement', name=u'modeStaticText',
              parent=self.upperPanel, pos=wx.Point(100, 8),
              size=wx.Size(130, 20), style=wx.ALIGN_CENTRE)

        self.amountStaticText = wx.StaticText(id=wxID_FRAMEAMOUNTSTATICTEXT,
              label=u'Montant', name=u'amountStaticText',
              parent=self.upperPanel, pos=wx.Point(xLabelSize+300, 8),
              size=wx.Size(150, 20), style=wx.ALIGN_CENTRE)

        self.bankStaticText = wx.StaticText(id=wxID_FRAMEBANKSTATICTEXT,
              label=u'Banque', name=u'bankStaticText',
              parent=self.upperPanel, pos=wx.Point(xLabelSize+230, 8),
              size=wx.Size(70, 20), style=wx.ALIGN_CENTRE)
        self.bankStaticText.SetHelpText(u'Cette entr\xe9e est-elle prise en compte par la banque ?')

        self.labelStaticText = wx.StaticText(id=wxID_FRAMELABELSTATICTEXT,
              label=u'Libell\xe9', name=u'labelStaticText',
              parent=self.upperPanel, pos=wx.Point(230, 8),
              size=wx.Size(xLabelSize, 20), style=wx.ALIGN_CENTRE)

        # Last line
        self.lowerPanel.balanceDate = dt.date.max
        self.lastLine = LastLine(self.lowerPanel, total = 0,
                                 totalBank = 0,
                                 offset = 0)

        # Add line
        addEntry = entry.Entry(entry.dateToString(dt.date.today()), "", "", 0)
        self.addLine = Line(self.lowerPanel, addEntry, 60)

        # Add button
        self.addButton = wx.Button(id=wxID_FRAMEADD, label=u'Ajouter',
                                   name=u'add', parent=self.lowerPanel,
                                   pos=wx.Point(1, yBottomButtons),
                                   size=wx.Size(85, 29), style=0)
        self.addButton.Bind(wx.EVT_BUTTON, self.OnAddButton, id=wxID_FRAMEADD)

        # Delete button
        self.deleteButton = wx.Button(id=wxID_FRAMEDELETE, label=u'Supprimer',
                                      name=u'delete', parent=self.lowerPanel,
                                      pos=wx.Point(100, yBottomButtons),
                                      size=wx.Size(85, 29), style=0)
        self.deleteButton.Bind(wx.EVT_BUTTON, self.OnDeleteButton,
                               id=wxID_FRAMEDELETE)

        # Refresh button
        self.refreshButton = wx.Button(id=wxID_FRAMEREFRESH,
                                       label=u'Recalculer',
                                       name=u'refresh',
                                       parent=self.lowerPanel,
                                       pos=wx.Point(200, yBottomButtons),
                                       size=wx.Size(85, 29), style=0)
        self.refreshButton.Bind(wx.EVT_BUTTON, self.OnRefreshButton,
                               id=wxID_FRAMEREFRESH)

        # BankOrder button
        self.bankOrderButton = wx.Button(id=wxID_FRAMEBANKORDER,
                                       label=u'Ordre relev\xe9',
                                       name=u'bankOrder',
                                       parent=self.lowerPanel,
                                       pos=wx.Point(295, yBottomButtons),
                                       size=wx.Size(100, 29), style=0)
        self.bankOrderButton.Bind(wx.EVT_BUTTON, self.OnBankOrderButton,
                                  id=wxID_FRAMEBANKORDER)


    def __init__(self, parent):
        self._init_ctrls(parent)
        # My code
        self.account = account.Account()
        self.filename = None
        self.lines = []
        self.writeLines()

    def OnFileItems0Menu(self, event):
        event.Skip()

    def OnFileOpenMenu(self, event):
        dlg = wx.FileDialog(parent=self, message='Choisissez un fichier',
                            defaultDir='.', defaultFile='', wildcard='*.cpt')
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.account.read(filename)
                self.filename = filename
                self.SetTitle(("Fichier %s") % filename)
                self.writeLines()
        finally:
            dlg.Destroy()
        event.Skip()

    def OnFileSaveMenu(self, event):
        if self.filename == None:
            return self.OnFileSaveAsMenu(event)
        else:
            self.account.save(self.filename)

    def OnFileQuitMenu(self, event):
        self.Close()

    def OnMenuFileSaveasMenu(self, event):
        dlg = wx.FileDialog(self, 'Enregistrer sous', '.', '', '*.*', wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.account.save(filename)
                self.filename = filename
                self.SetTitle(("Fichier %s") % filename)
        finally:
            dlg.Destroy()

    def OnMenuFileCloseMenu(self, event):
        self.account = account.Account()
        self.filename = None
        self.SetTitle(("Pas de fichier"))
        event.Skip()

    def OnAddButton(self, event):
        """
        Call back to add a line in the book
        """
        (x,y) = self.scrolledWindow.CalcScrolledPosition(0,0)
        self.scrolledWindow.Scroll(0,0)
        a = self.account
        newEntry = self.addLine.entry.copy()
        a.entries.append(newEntry)
        self.scrolledWindow.SetVirtualSize(size=wx.Size(xWindowSize,
                                                        yOffset*len(a.entries)
                                                        +100))
        # Create a new line
        offset = yOffset*(len(a.entries)-1)
        try:
            self.lines.append(LineSelect(self.scrolledWindow, newEntry, offset))
        except:
            pass
        finally:
            self.scrolledWindow.Scroll(-x,-y)

    def OnDeleteButton(self, event):
        """
        Call back for delete button: remove selected lines
        """
        a = self.account
        deleteLines = []
        for l in self.lines :
            if l.selectCheckBox.GetValue() :
                deleteLines.append(l)

        self.deleteLastLines(len(deleteLines))

        for l in deleteLines :
            a.entries.remove(l.entry)

        self.OnRefreshButton(event)

    def OnRefreshButton(self, event):
        a = self.account
        a.sort()
        for e, l in zip(a.entries, self.lines) :
            l.bind_entry(e)
            l.selectCheckBox.SetValue(False)
        # Get date of balance
        date = self.lowerPanel.balanceDate
        # recompute total
        self.lastLine.set_values(total = a.balance(date),
                                 totalBank = a.bank_balance)

    def OnBankOrderButton(self, event):
        a = self.account
        a.sort(account.bankOrder)
        for e, l in zip(a.entries, self.lines) :
            l.bind_entry(e)
        # Get date of balance
        date = self.lowerPanel.balanceDate
        # recompute total
        self.lastLine.set_values(total = a.balance(date),
                                 totalBank = a.bank_balance)

    def deleteLastLines(self, n):
        """
        Delete the last n lines
        """
        for l in self.lines[-n:]:
            l.destroy()
        self.lines = self.lines[:-n]

    def writeLines(self):
        """
        Write entries in lines
        """
        self.scrolledWindow.Scroll(0,0)
        # Destroy existing lines
        for l in self.lines :
            l.destroy()
        self.lines = []
        a = self.account
        a.sort()
        offset = 0
        # Entry lines
        for e in a.entries :
            self.lines.append(LineSelect(self.scrolledWindow, e, offset))
            offset += yOffset

        # Resize the window
        self.scrolledWindow.SetVirtualSize(size=wx.Size(xWindowSize,
                                                        yOffset*len(a.entries)
                                                        +100))
        # Get date of balance
        date = self.lowerPanel.balanceDate
        # recompute total
        self.lastLine.set_values(total = a.balance(date),
                                 totalBank = a.bank_balance)

        self.Refresh()
