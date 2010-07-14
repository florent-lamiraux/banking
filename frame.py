#Boa:Frame:Frame

import wx
import account

def create(parent):
    return Frame(parent)

[wxID_FRAME, wxID_FRAMEBANKCHECKBOX1, wxID_FRAMEBANKSTATICTEXT, 
 wxID_FRAMEDATESTATICTEXT, wxID_FRAMEDATETEXTCTRL1, 
 wxID_FRAMELIBELLESTATICTEXT, wxID_FRAMELIBELLETEXTCTRL1, 
 wxID_FRAMEMODESTATICTEXT, wxID_FRAMEMODETEXTCTRL1, 
 wxID_FRAMEMONTANTSTATICTEXT, wxID_FRAMEMONTANTTEXTCTRL1, 
 wxID_FRAMESCROLLEDWINDOW, wxID_FRAMESELECTCHECKBOX1, 
 wxID_FRAMETOTALBANKTEXTCTRL, wxID_FRAMETOTALBANQUESTATICTEXT, 
 wxID_FRAMETOTALSTATICTEXT, wxID_FRAMETOTALTEXTCTRL, 
] = [wx.NewId() for _init_ctrls in range(17)]

[wxID_FRAMEFILEOPEN, wxID_FRAMEFILEQUIT, wxID_FRAMEFILESAVE, 
] = [wx.NewId() for _init_coll_File_Items in range(3)]

[wxID_FRAMEMENUFILEOPEN, wxID_FRAMEMENUFILEQUIT, wxID_FRAMEMENUFILESAVE, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(3)]

class Frame(wx.Frame):
    def _init_my_code(self, parent):
        self.account = account.Account()
    
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
        parent.Append(help=u"Quitter l'application", id=wxID_FRAMEMENUFILEQUIT,
              kind=wx.ITEM_NORMAL, text=u'Quitter')
        self.Bind(wx.EVT_MENU, self.OnFileOpenMenu, id=wxID_FRAMEMENUFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnFileSaveMenu, id=wxID_FRAMEMENUFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnFileQuitMenu, id=wxID_FRAMEMENUFILEQUIT)

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

        self.dateTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEDATETEXTCTRL1,
              name=u'dateTextCtrl1', parent=self.scrolledWindow, pos=wx.Point(0,
              32), size=wx.Size(99, 19), style=0, value=u'25/11/2010')

        self.modeTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEMODETEXTCTRL1,
              name=u'modeTextCtrl1', parent=self.scrolledWindow,
              pos=wx.Point(100, 32), size=wx.Size(129, 19), style=0,
              value=u'CB Aur\xe9lie')

        self.libelleTextCtrl1 = wx.TextCtrl(id=wxID_FRAMELIBELLETEXTCTRL1,
              name=u'libelleTextCtrl1', parent=self.scrolledWindow,
              pos=wx.Point(230, 32), size=wx.Size(799, 19), style=0,
              value=u'Chronodrive.com')

        self.bankCheckBox1 = wx.CheckBox(id=wxID_FRAMEBANKCHECKBOX1, label=u'',
              name=u'bankCheckBox1', parent=self.scrolledWindow,
              pos=wx.Point(1048, 32), size=wx.Size(19, 19), style=0)
        self.bankCheckBox1.SetValue(False)

        self.montantTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEMONTANTTEXTCTRL1,
              name=u'montantTextCtrl1', parent=self.scrolledWindow,
              pos=wx.Point(1100, 32), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=u'-83.56')

        self.selectCheckBox1 = wx.CheckBox(id=wxID_FRAMESELECTCHECKBOX1,
              label=u'', name=u'selectCheckBox1', parent=self.scrolledWindow,
              pos=wx.Point(1264, 32), size=wx.Size(19, 19), style=0)
        self.selectCheckBox1.SetValue(False)

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
        self._init_my_code(parent)
        self._init_ctrls(parent)

    def OnFileItems0Menu(self, event):
        event.Skip()

    def OnFileOpenMenu(self, event):
        dlg = wx.FileDialog(self, 'Choose a file', '.', '', '*.cpt', wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.account.read(filename)
        finally:
            dlg.Destroy()
        event.Skip()

    def OnFileSaveMenu(self, event):
        event.Skip()

    def OnFileQuitMenu(self, event):
        event.Skip()
