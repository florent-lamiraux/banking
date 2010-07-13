#Boa:Frame:Frame

import wx
import account
from line import *

def create(parent):
    return Frame(parent)

[wxID_FRAMEFILEOPEN, wxID_FRAMEFILEQUIT, wxID_FRAMEFILESAVE,
] = [wx.NewId() for _init_coll_File_Items in range(3)]

[wxID_FRAMEMENUFILECLOSE, wxID_FRAMEMENUFILEOPEN, wxID_FRAMEMENUFILEQUIT, 
 wxID_FRAMEMENUFILESAVE, wxID_FRAMEMENUFILESAVEAS, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(5)]

class Frame(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title=u'Fichier')

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Ouvrir un fichier de comptes',
              id=wxID_FRAMEMENUFILEOPEN, kind=wx.ITEM_NORMAL, text=u'Ouvrir')
        parent.Append(help=u'Enregistrer les ecritures dans un fichier',
              id=wxID_FRAMEMENUFILESAVE, kind=wx.ITEM_NORMAL,
              text=u'Enregistrer')
        parent.Append(help='', id=wxID_FRAMEMENUFILESAVEAS, kind=wx.ITEM_NORMAL,
              text=u'Enregistrer sous')
        parent.Append(help='', id=wxID_FRAMEMENUFILECLOSE, kind=wx.ITEM_NORMAL,
              text=u'Fermer')
        parent.Append(help=u"Quitter l'application", id=wxID_FRAMEMENUFILEQUIT,
              kind=wx.ITEM_NORMAL, text=u'Quitter')
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
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME, name='', parent=prnt,
              pos=wx.Point(0, 25), size=wx.Size(1910, 1114),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Comptes')
        self._init_utils()
        self.SetClientSize(wx.Size(1910, 1114))
        self.SetMenuBar(self.menuBar1)

        self.scrolledWindow = wx.ScrolledWindow(id=wxID_FRAMESCROLLEDWINDOW,
              name=u'scrolledWindow', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(1910, 1085), style=wx.HSCROLL | wx.VSCROLL)

        self.dateStaticText = wx.StaticText(id=wxID_FRAMEDATESTATICTEXT,
              label=u'Date', name=u'dateStaticText', parent=self.scrolledWindow,
              pos=wx.Point(0, 8), size=wx.Size(100, 20), style=wx.ALIGN_CENTRE)
        self.dateStaticText.SetBackgroundColour(wx.Colour(4, 0, 0))

        self.modeStaticText = wx.StaticText(id=wxID_FRAMEMODESTATICTEXT,
              label=u'Mode de Paiement', name=u'modeStaticText',
              parent=self.scrolledWindow, pos=wx.Point(100, 8),
              size=wx.Size(130, 20), style=wx.ALIGN_CENTRE)

        self.montantStaticText = wx.StaticText(id=wxID_FRAMEMONTANTSTATICTEXT,
              label=u'Montant', name=u'montantStaticText',
              parent=self.scrolledWindow, pos=wx.Point(1100, 8),
              size=wx.Size(150, 20), style=wx.ALIGN_CENTRE)

        self.bankStaticText = wx.StaticText(id=wxID_FRAMEBANKSTATICTEXT,
              label=u'Banque', name=u'bankStaticText',
              parent=self.scrolledWindow, pos=wx.Point(1030, 8),
              size=wx.Size(70, 20), style=wx.ALIGN_CENTRE)
        self.bankStaticText.SetHelpText(u'Cette entr\xe9e est-elle prise en compte par la banque ?')

        self.libelleStaticText = wx.StaticText(id=wxID_FRAMELIBELLESTATICTEXT,
              label=u'Libell\xe9', name=u'libelleStaticText',
              parent=self.scrolledWindow, pos=wx.Point(230, 8),
              size=wx.Size(800, 20), style=wx.ALIGN_CENTRE)

        self.line = Line(self, entry.Entry(u'25/11/2010',
                                           u'CB Aur\xe9lie',
                                           u'Chronodrive.com',
                                           u'-83.56'))

        self.totalBanqueStaticText = wx.StaticText(id=wxID_FRAMETOTALBANQUESTATICTEXT,
              label=u'Total banque', name=u'totalBanqueStaticText',
              parent=self.scrolledWindow, pos=wx.Point(900, 82),
              size=wx.Size(129, 19), style=0)

        self.totalStaticText = wx.StaticText(id=wxID_FRAMETOTALSTATICTEXT,
              label=u'Total', name=u'totalStaticText',
              parent=self.scrolledWindow, pos=wx.Point(900, 62),
              size=wx.Size(129, 20), style=0)

        self.totalTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALTEXTCTRL,
              name=u'totalTextCtrl', parent=self.scrolledWindow,
              pos=wx.Point(1100, 62), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=u'1000.05')

        self.totalBankTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALBANKTEXTCTRL,
              name=u'totalBankTextCtrl', parent=self.scrolledWindow,
              pos=wx.Point(1100, 82), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=u'982.14')

    def __init__(self, parent):
        self._init_ctrls(parent)
        # My code
        self.account = account.Account()
        self.filename = None
    
    def OnFileItems0Menu(self, event):
        event.Skip()

    def OnFileOpenMenu(self, event):
        dlg = wx.FileDialog(self, 'Choisissez un fichier', '.', '', '*.cpt', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.account.read(filename)
                self.filename = filename
                self.SetTitle(("Fichier %s") % filename)
        finally:
            dlg.Destroy()
        event.Skip()

    def OnFileSaveMenu(self, event):
        if self.filename == None:
            return self.OnFileSaveAsMenu(envent)
        else:
            self.account.save(filename)
    
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

