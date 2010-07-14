import wx
import entry

[wxID_FRAME, wxID_FRAMEBANKCHECKBOX1, wxID_FRAMEBANKSTATICTEXT,
 wxID_FRAMEDATESTATICTEXT, wxID_FRAMEDATETEXTCTRL1,
 wxID_FRAMELIBELLESTATICTEXT, wxID_FRAMELIBELLETEXTCTRL1,
 wxID_FRAMEMODESTATICTEXT, wxID_FRAMEMODETEXTCTRL1,
 wxID_FRAMEMONTANTSTATICTEXT, wxID_FRAMEMONTANTTEXTCTRL1,
 wxID_FRAMESCROLLEDWINDOW, wxID_FRAMESELECTCHECKBOX1,
 wxID_FRAMETOTALBANKTEXTCTRL, wxID_FRAMETOTALBANQUESTATICTEXT,
 wxID_FRAMETOTALSTATICTEXT, wxID_FRAMETOTALTEXTCTRL,
] = [wx.NewId() for _init_ctrls in range(17)]

class Line (object) :
    """
    One line in the account book
    """
    def __init__(self, par, entry, offset = 0) :
        self.dateTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEDATETEXTCTRL1,
              name=u'dateTextCtrl1', parent=par.scrolledWindow, pos=wx.Point(0,
              32+offset), size=wx.Size(99, 19), style=0, value=entry.date.__str__())
        self.dateTextCtrl1.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnDateTextCtrl1TextMaxlen, id=wxID_FRAMEDATETEXTCTRL1)
        self.dateTextCtrl1.Bind(wx.EVT_TEXT_URL, self.OnDateTextCtrl1TextUrl,
              id=wxID_FRAMEDATETEXTCTRL1)
        self.dateTextCtrl1.Bind(wx.EVT_TEXT_ENTER,
              self.OnDateTextCtrl1TextEnter, id=wxID_FRAMEDATETEXTCTRL1)
        self.dateTextCtrl1.Bind(wx.EVT_TEXT, self.OnDateTextCtrl1Text,
              id=wxID_FRAMEDATETEXTCTRL1)

        self.modeTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEMODETEXTCTRL1,
              name=u'modeTextCtrl1', parent=par.scrolledWindow,
              pos=wx.Point(100, 32+offset), size=wx.Size(129, 19), style=0,
              value=entry.mode)

        self.modeTextCtrl1.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnModeTextCtrl1TextMaxlen, id=wxID_FRAMEMODETEXTCTRL1)
        self.modeTextCtrl1.Bind(wx.EVT_TEXT_URL, self.OnModeTextCtrl1TextUrl,
              id=wxID_FRAMEMODETEXTCTRL1)
        self.modeTextCtrl1.Bind(wx.EVT_TEXT_ENTER,
              self.OnModeTextCtrl1TextEnter, id=wxID_FRAMEMODETEXTCTRL1)
        self.modeTextCtrl1.Bind(wx.EVT_TEXT, self.OnModeTextCtrl1Text,
              id=wxID_FRAMEMODETEXTCTRL1)

        self.libelleTextCtrl1 = wx.TextCtrl(id=wxID_FRAMELIBELLETEXTCTRL1,
              name=u'libelleTextCtrl1', parent=par.scrolledWindow,
              pos=wx.Point(230, 32+offset), size=wx.Size(799, 19), style=0,
              value=entry.label)
        self.libelleTextCtrl1.Bind(wx.EVT_TEXT_URL,
              self.OnLibelleTextCtrl1TextUrl, id=wxID_FRAMELIBELLETEXTCTRL1)
        self.libelleTextCtrl1.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnLibelleTextCtrl1TextMaxlen, id=wxID_FRAMELIBELLETEXTCTRL1)
        self.libelleTextCtrl1.Bind(wx.EVT_TEXT_ENTER,
              self.OnLibelleTextCtrl1TextEnter, id=wxID_FRAMELIBELLETEXTCTRL1)
        self.libelleTextCtrl1.Bind(wx.EVT_TEXT, self.OnLibelleTextCtrl1Text,
              id=wxID_FRAMELIBELLETEXTCTRL1)

        self.bankCheckBox1 = wx.CheckBox(id=wxID_FRAMEBANKCHECKBOX1, label=u'',
              name=u'bankCheckBox1', parent=par.scrolledWindow,
              pos=wx.Point(1048, 32+offset), size=wx.Size(19, 19), style=0)
        self.bankCheckBox1.SetValue(entry.bank)
        self.bankCheckBox1.Bind(wx.EVT_CHECKBOX, self.OnBankCheckBox1Checkbox,
              id=wxID_FRAMEBANKCHECKBOX1)
        self.bankCheckBox1.Bind(wx.EVT_HELP, self.OnBankCheckBox1Help,
              id=wxID_FRAMEBANKCHECKBOX1)

        self.montantTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEMONTANTTEXTCTRL1,
              name=u'montantTextCtrl1', parent=par.scrolledWindow,
              pos=wx.Point(1100, 32+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=entry.amount.__str__())

        self.montantTextCtrl1.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnMontantTextCtrl1TextMaxlen, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT_URL,
              self.OnMontantTextCtrl1TextUrl, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT_ENTER,
              self.OnMontantTextCtrl1TextEnter, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT, self.OnMontantTextCtrl1Text,
              id=wxID_FRAMEMONTANTTEXTCTRL1)

        self.selectCheckBox1 = wx.CheckBox(id=wxID_FRAMESELECTCHECKBOX1,
              label=u'', name=u'selectCheckBox1', parent=par.scrolledWindow,
              pos=wx.Point(1264, 32+offset), size=wx.Size(19, 19), style=0)
        self.selectCheckBox1.SetValue(False)

    def OnBankCheckBox1Checkbox(self, event):
        event.Skip()

    def OnBankCheckBox1Help(self, event):
        event.Skip()

    def OnDateTextCtrl1TextMaxlen(self, event):
        event.Skip()

    def OnDateTextCtrl1TextUrl(self, event):
        event.Skip()

    def OnDateTextCtrl1TextEnter(self, event):
        event.Skip()

    def OnDateTextCtrl1Text(self, event):
        event.Skip()

    def OnModeTextCtrl1TextMaxlen(self, event):
        event.Skip()

    def OnModeTextCtrl1TextUrl(self, event):
        event.Skip()

    def OnModeTextCtrl1TextEnter(self, event):
        event.Skip()

    def OnModeTextCtrl1Text(self, event):
        event.Skip()

    def OnLibelleTextCtrl1TextUrl(self, event):
        event.Skip()

    def OnLibelleTextCtrl1TextMaxlen(self, event):
        event.Skip()

    def OnLibelleTextCtrl1TextEnter(self, event):
        event.Skip()

    def OnLibelleTextCtrl1Text(self, event):
        event.Skip()

    def OnMontantTextCtrl1TextMaxlen(self, event):
        event.Skip()

    def OnMontantTextCtrl1TextUrl(self, event):
        event.Skip()

    def OnMontantTextCtrl1TextEnter(self, event):
        event.Skip()

    def OnMontantTextCtrl1Text(self, event):
        event.Skip()

class LastLine (object) :
    def __init__(self, prnt, offset = 0):
        self.totalBanqueStaticText = wx.StaticText(id=wxID_FRAMETOTALBANQUESTATICTEXT,
              label=u'Total banque', name=u'totalBanqueStaticText',
              parent=prnt.scrolledWindow, pos=wx.Point(900, 82+offset),
              size=wx.Size(129, 19), style=0)

        self.totalStaticText = wx.StaticText(id=wxID_FRAMETOTALSTATICTEXT,
              label=u'Total', name=u'totalStaticText',
              parent=prnt.scrolledWindow, pos=wx.Point(900, 62+offset),
              size=wx.Size(129, 20), style=0)

        self.totalTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALTEXTCTRL,
              name=u'totalTextCtrl', parent=prnt.scrolledWindow,
              pos=wx.Point(1100, 62+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=u'1000.05')

        self.totalBankTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALBANKTEXTCTRL,
              name=u'totalBankTextCtrl', parent=prnt.scrolledWindow,
              pos=wx.Point(1100, 82+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=u'982.14')
