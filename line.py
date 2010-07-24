import wx
import datetime as dt
import decimal
import entry

[wxID_FRAME, wxID_FRAMEBANKSTATICTEXT, wxID_FRAMEDATESTATICTEXT,
 wxID_FRAMELIBELLESTATICTEXT, wxID_FRAMEMODESTATICTEXT,
 wxID_FRAMEMONTANTSTATICTEXT, wxID_FRAMEUPPERPANEL,
 wxID_FRAMESCROLLEDWINDOW, wxID_FRAMETOTALBANKTEXTCTRL, wxID_FRAMELOWERPANEL,
 wxID_FRAMETOTALBANQUESTATICTEXT, wxID_FRAMETOTALSTATICTEXT,
 wxID_FRAMETOTALTEXTCTRL,
] = [wx.NewId() for _init_ctrls in range(13)]

class Line (object) :
    """
    One line in the account book
    """
    def __init__(self, par, e, offset = 0) :
        self.entry = e
        self.frame = par
        newId = wx.NewId()
        self.dateTextCtrl = wx.TextCtrl(id=newId,
              name=u'dateTextCtrl', parent=par, pos=wx.Point(0,
              32+offset), size=wx.Size(99, 19), style=wx.TE_PROCESS_ENTER,
              value=str(entry.dateToString(e.date)))
        self.dateTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnDateTextCtrlTextMaxlen, id=newId)
        self.dateTextCtrl.Bind(wx.EVT_TEXT_URL, self.OnDateTextCtrlTextUrl,
              id=newId)
        self.dateTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnDateTextCtrlTextEnter, id=newId)
        self.dateTextCtrl.Bind(wx.EVT_TEXT, self.OnDateTextCtrlText,
              id=newId)

        newId = wx.NewId()
        self.modeTextCtrl = wx.TextCtrl(id=newId,
              name=u'modeTextCtrl', parent=par,
              pos=wx.Point(100, 32+offset), size=wx.Size(129, 19), style=0,
              value=e.mode)

        self.modeTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnModeTextCtrlTextMaxlen, id=newId)
        self.modeTextCtrl.Bind(wx.EVT_TEXT_URL, self.OnModeTextCtrlTextUrl,
              id=newId)
        self.modeTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnModeTextCtrlTextEnter, id=newId)
        self.modeTextCtrl.Bind(wx.EVT_TEXT, self.OnModeTextCtrlText,
              id=newId)

        newId = wx.NewId()
        self.libelleTextCtrl = wx.TextCtrl(id=newId,
              name=u'libelleTextCtrl', parent=par,
              pos=wx.Point(230, 32+offset), size=wx.Size(799, 19), style=0,
              value=e.label)
        self.libelleTextCtrl.Bind(wx.EVT_TEXT_URL,
              self.OnLibelleTextCtrlTextUrl, id=newId)
        self.libelleTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnLibelleTextCtrlTextMaxlen, id=newId)
        self.libelleTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnLibelleTextCtrlTextEnter, id=newId)
        self.libelleTextCtrl.Bind(wx.EVT_TEXT, self.OnLibelleTextCtrlText,
              id=newId)

        newId = wx.NewId()
        self.bankCheckBox = wx.CheckBox(id=newId, label=u'',
              name=u'bankCheckBox', parent=par,
              pos=wx.Point(1048, 32+offset), size=wx.Size(19, 19), style=0)
        self.bankCheckBox.SetValue(e.bank)
        self.bankCheckBox.Bind(wx.EVT_CHECKBOX, self.OnBankCheckBoxCheckbox,
              id=newId)
        self.bankCheckBox.Bind(wx.EVT_HELP, self.OnBankCheckBoxHelp,
              id=newId)

        newId = wx.NewId()
        self.montantTextCtrl = wx.TextCtrl(id=newId,
              name=u'montantTextCtrl', parent=par,
              pos=wx.Point(1100, 32+offset), size=wx.Size(149, 19),
              style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER,
              value=str(e.amount))

        self.montantTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnMontantTextCtrlTextMaxlen, id=newId)
        self.montantTextCtrl.Bind(wx.EVT_TEXT_URL,
              self.OnMontantTextCtrlTextUrl, id=newId)
        self.montantTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnMontantTextCtrlTextEnter, id=newId)
        self.montantTextCtrl.Bind(wx.EVT_TEXT, self.OnMontantTextCtrlText,
              id=newId)

    def OnBankCheckBoxCheckbox(self, event):
        self.entry.bank = self.bankCheckBox.GetValue()

    def OnBankCheckBoxHelp(self, event):
        print "OnBankCheckBoxHelp"

    def OnDateTextCtrlTextMaxlen(self, event):
        print "OnDateTextCtrlTextMaxlen"

    def OnDateTextCtrlTextUrl(self, event):
        print "OnDateTextCtrlTextUrl"

    def OnDateTextCtrlTextEnter(self, event):
        newDate = self.dateTextCtrl.GetValue()
        try:
            self.entry.date = entry.stringToDate(newDate)
        except:
            self.dateTextCtrl.SetValue(entry.dateToString(self.entry.date))

    def OnDateTextCtrlText(self, event):
        pass

    def OnModeTextCtrlTextMaxlen(self, event):
        print "OnModeTextCtrlTextMaxlen"

    def OnModeTextCtrlTextUrl(self, event):
        print "OnModeTextCtrlTextUrl"

    def OnModeTextCtrlTextEnter(self, event):
        print "OnModeTextCtrlTextEnter"

    def OnModeTextCtrlText(self, event):
        self.entry.mode = self.modeTextCtrl.GetValue()

    def OnLibelleTextCtrlTextUrl(self, event):
        print "OnLibelleTextCtrlTextUrl"

    def OnLibelleTextCtrlTextMaxlen(self, event):
        print "OnLibelleTextCtrlTextMaxlen"

    def OnLibelleTextCtrlTextEnter(self, event):
        print "OnLibelleTextCtrlTextEnter"

    def OnLibelleTextCtrlText(self, event):
        self.entry.label = self.libelleTextCtrl.GetValue()

    def OnMontantTextCtrlTextMaxlen(self, event):
        print "OnMontantTextCtrlTextMaxlen"

    def OnMontantTextCtrlTextUrl(self, event):
        print "OnMontantTextCtrlTextUrl"

    def OnMontantTextCtrlTextEnter(self, event):
        try:
            self.entry.amount = decimal.Decimal(self.montantTextCtrl.GetValue())
        except:
            self.montantTextCtrl.SetValue(str(self.entry.amount))

    def OnMontantTextCtrlText(self, event):
        pass

    def bind_entry(self, e) :
        self.entry = e
        self.dateTextCtrl.SetValue(entry.dateToString(e.date))
        self.modeTextCtrl.SetValue(e.mode)
        self.libelleTextCtrl.SetValue(e.label)
        self.bankCheckBox.SetValue(e.bank)
        self.montantTextCtrl.SetValue(str(e.amount))

    def destroy(self) :
        self.dateTextCtrl.Destroy()
        self.dateTextCtrl = None
        self.modeTextCtrl.Destroy()
        self.modeTextCtrl = None
        self.libelleTextCtrl.Destroy()
        self.libelleTextCtrl = None
        self.bankCheckBox.Destroy()
        self.bankCheckBox = None
        self.montantTextCtrl.Destroy()
        self.montantTextCtrl = None

class LineSelect (Line) :
    def __init__(self, par, e, offset = 0) :
        Line.__init__(self, par, e, offset)
        self.selectCheckBox = wx.CheckBox(id=wx.NewId(),
              label=u'', name=u'selectCheckBox', parent=par,
              pos=wx.Point(1264, 32+offset), size=wx.Size(19, 19), style=0)
        self.selectCheckBox.SetValue(False)

    def destroy(self) :
        self.selectCheckBox.Destroy()
        self.selectCheckBox = None
        Line.destroy(self)

class LastLine (object) :
    """
    Last line of the book with balance and bank balance
    """
    def __init__(self, prnt, total, totalBank, offset = 0):
        self.totalBanqueStaticText = wx.StaticText(id=wxID_FRAMETOTALBANQUESTATICTEXT,
              label=u'Total banque', name=u'totalBanqueStaticText',
              parent=prnt, pos=wx.Point(900, 82+offset),
              size=wx.Size(129, 19), style=0)

        self.totalStaticText = wx.StaticText(id=wxID_FRAMETOTALSTATICTEXT,
              label=u'Total', name=u'totalStaticText',
              parent=prnt, pos=wx.Point(900, 62+offset),
              size=wx.Size(129, 20), style=0)

        self.totalTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALTEXTCTRL,
              name=u'totalTextCtrl', parent=prnt,
              pos=wx.Point(1100, 62+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=str(total))

        self.totalBankTextCtrl = wx.TextCtrl(id=wxID_FRAMETOTALBANKTEXTCTRL,
              name=u'totalBankTextCtrl', parent=prnt,
              pos=wx.Point(1100, 82+offset), size=wx.Size(149, 19), style=wx.TE_RIGHT,
              value=str(totalBank))

    def set_values(self, total, totalBank) :
        self.totalTextCtrl.SetValue(str(total))
        self.totalBankTextCtrl.SetValue(str(totalBank))

    def destroy(self):
        self.totalBanqueStaticText.Destroy()
        self.totalBanqueStaticText = None
        self.totalStaticText.Destroy()
        self.totalStaticText = None
        self.totalTextCtrl.Destroy()
        self.totalTextCtrl = None
        self.totalBankTextCtrl.Destroy()
        self.totalBankTextCtrl = None
