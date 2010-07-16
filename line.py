import wx
import datetime as dt
import decimal
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
    def __init__(self, par, e, offset = 0) :
        self.entry = e
        self.frame = par
        self.dateTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEDATETEXTCTRL1,
              name=u'dateTextCtrl1', parent=par.scrolledWindow, pos=wx.Point(0,
              32+offset), size=wx.Size(99, 19), style=0, value=str(entry.dateToString(e.date)))
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
              value=e.mode)

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
              value=e.label)
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
        self.bankCheckBox1.SetValue(e.bank)
        self.bankCheckBox1.Bind(wx.EVT_CHECKBOX, self.OnBankCheckBox1Checkbox,
              id=wxID_FRAMEBANKCHECKBOX1)
        self.bankCheckBox1.Bind(wx.EVT_HELP, self.OnBankCheckBox1Help,
              id=wxID_FRAMEBANKCHECKBOX1)

        self.montantTextCtrl1 = wx.TextCtrl(id=wxID_FRAMEMONTANTTEXTCTRL1,
              name=u'montantTextCtrl1', parent=par.scrolledWindow,
              pos=wx.Point(1100, 32+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=str(e.amount))

        self.montantTextCtrl1.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnMontantTextCtrl1TextMaxlen, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT_URL,
              self.OnMontantTextCtrl1TextUrl, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT_ENTER,
              self.OnMontantTextCtrl1TextEnter, id=wxID_FRAMEMONTANTTEXTCTRL1)
        self.montantTextCtrl1.Bind(wx.EVT_TEXT, self.OnMontantTextCtrl1Text,
              id=wxID_FRAMEMONTANTTEXTCTRL1)

    def OnBankCheckBox1Checkbox(self, event):
        self.entry.bank = self.bankCheckBox1.GetValue()

    def OnBankCheckBox1Help(self, event):
        print "OnBankCheckBox1Help"

    def OnDateTextCtrl1TextMaxlen(self, event):
        print "OnDateTextCtrl1TextMaxlen"

    def OnDateTextCtrl1TextUrl(self, event):
        print "OnDateTextCtrl1TextUrl"

    def OnDateTextCtrl1TextEnter(self, event):
        print "OnDateTextCtrl1TextEnter"

    def OnDateTextCtrl1Text(self, event):
        newDate = self.dateTextCtrl1.GetValue()
        self.entry.date = entry.stringToDate(newDate)

    def OnModeTextCtrl1TextMaxlen(self, event):
        print "OnModeTextCtrl1TextMaxlen"

    def OnModeTextCtrl1TextUrl(self, event):
        print "OnModeTextCtrl1TextUrl"

    def OnModeTextCtrl1TextEnter(self, event):
        print "OnModeTextCtrl1TextEnter"

    def OnModeTextCtrl1Text(self, event):
        self.entry.mode = self.modeTextCtrl1.GetValue()

    def OnLibelleTextCtrl1TextUrl(self, event):
        print "OnLibelleTextCtrl1TextUrl"

    def OnLibelleTextCtrl1TextMaxlen(self, event):
        print "OnLibelleTextCtrl1TextMaxlen"

    def OnLibelleTextCtrl1TextEnter(self, event):
        print "OnLibelleTextCtrl1TextEnter"

    def OnLibelleTextCtrl1Text(self, event):
        self.entry.label = self.libelleTextCtrl1.GetValue()

    def OnMontantTextCtrl1TextMaxlen(self, event):
        print "OnMontantTextCtrl1TextMaxlen"

    def OnMontantTextCtrl1TextUrl(self, event):
        print "OnMontantTextCtrl1TextUrl"

    def OnMontantTextCtrl1TextEnter(self, event):
        print "OnMontantTextCtrl1TextEnter"

    def OnMontantTextCtrl1Text(self, event):
        self.entry.amount = decimal.Decimal(self.montantTextCtrl1.GetValue())

    def destroy(self) :
        self.dateTextCtrl1.Destroy()
        self.dateTextCtrl1 = None
        self.modeTextCtrl1.Destroy()
        self.modeTextCtrl1 = None
        self.libelleTextCtrl1.Destroy()
        self.libelleTextCtrl1 = None
        self.bankCheckBox1.Destroy()
        self.bankCheckBox1 = None
        self.montantTextCtrl1.Destroy()
        self.montantTextCtrl1 = None

class LineSelect (Line) :
    def __init__(self, par, e, offset = 0) :
        Line.__init__(self, par, e, offset)
        self.selectCheckBox1 = wx.CheckBox(id=wxID_FRAMESELECTCHECKBOX1,
              label=u'', name=u'selectCheckBox1', parent=par.scrolledWindow,
              pos=wx.Point(1264, 32+offset), size=wx.Size(19, 19), style=0)
        self.selectCheckBox1.SetValue(False)

    def destroy(self) :
        self.selectCheckBox1.Destroy()
        self.selectCheckBox1 = None
        Line.destroy(self)

class LastLine (object) :
    """
    Last line of the book with balance and bank balance
    """
    def __init__(self, prnt, total, totalBank, offset = 0):
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
              value=str(total))

        self.totalBankTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALBANKTEXTCTRL,
              name=u'totalBankTextCtrl', parent=prnt.scrolledWindow,
              pos=wx.Point(1100, 82+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=str(totalBank))

    def destroy(self):
        self.totalBanqueStaticText.Destroy()
        self.totalBanqueStaticText = None
        self.totalStaticText.Destroy()
        self.totalStaticText = None
        self.totalTextCtrl.Destroy()
        self.totalTextCtrl = None
        self.totalBankTextCtrl.Destroy()
        self.totalBankTextCtrl = None
