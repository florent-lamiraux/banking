import wx
import datetime as dt
import decimal
import entry

[wxID_FRAME, wxID_FRAMEBANKSTATICTEXT, wxID_FRAMEDATESTATICTEXT,
 wxID_FRAMELABELSTATICTEXT, wxID_FRAMEMODESTATICTEXT,
 wxID_FRAMEAMOUNTSTATICTEXT, wxID_FRAMEUPPERPANEL,
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
        self.labelTextCtrl = wx.TextCtrl(id=newId,
              name=u'labelTextCtrl', parent=par,
              pos=wx.Point(230, 32+offset), size=wx.Size(799, 19), style=0,
              value=e.label)
        self.labelTextCtrl.Bind(wx.EVT_TEXT_URL,
              self.OnLabelTextCtrlTextUrl, id=newId)
        self.labelTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnLabelTextCtrlTextMaxlen, id=newId)
        self.labelTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnLabelTextCtrlTextEnter, id=newId)
        self.labelTextCtrl.Bind(wx.EVT_TEXT, self.OnLabelTextCtrlText,
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
        self.amountTextCtrl = wx.TextCtrl(id=newId,
              name=u'amountTextCtrl', parent=par,
              pos=wx.Point(1100, 32+offset), size=wx.Size(149, 19),
              style=wx.TE_RIGHT|wx.TE_PROCESS_ENTER,
              value=str(e.amount))

        self.amountTextCtrl.Bind(wx.EVT_TEXT_MAXLEN,
              self.OnAmountTextCtrlTextMaxlen, id=newId)
        self.amountTextCtrl.Bind(wx.EVT_TEXT_URL,
              self.OnAmountTextCtrlTextUrl, id=newId)
        self.amountTextCtrl.Bind(wx.EVT_TEXT_ENTER,
              self.OnAmountTextCtrlTextEnter, id=newId)
        self.amountTextCtrl.Bind(wx.EVT_TEXT, self.OnAmountTextCtrlText,
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

    def OnLabelTextCtrlTextUrl(self, event):
        print "OnLabelTextCtrlTextUrl"

    def OnLabelTextCtrlTextMaxlen(self, event):
        print "OnLabelTextCtrlTextMaxlen"

    def OnLabelTextCtrlTextEnter(self, event):
        print "OnLabelTextCtrlTextEnter"

    def OnLabelTextCtrlText(self, event):
        self.entry.label = self.labelTextCtrl.GetValue()

    def OnAmountTextCtrlTextMaxlen(self, event):
        print "OnAmountTextCtrlTextMaxlen"

    def OnAmountTextCtrlTextUrl(self, event):
        print "OnAmountTextCtrlTextUrl"

    def OnAmountTextCtrlTextEnter(self, event):
        try:
            self.entry.amount = decimal.Decimal(self.amountTextCtrl.GetValue())
        except:
            self.amountTextCtrl.SetValue(str(self.entry.amount))

    def OnAmountTextCtrlText(self, event):
        pass

    def bind_entry(self, e) :
        self.entry = e
        self.dateTextCtrl.SetValue(entry.dateToString(e.date))
        self.modeTextCtrl.SetValue(e.mode)
        self.labelTextCtrl.SetValue(e.label)
        self.bankCheckBox.SetValue(e.bank)
        self.amountTextCtrl.SetValue(str(e.amount))

    def destroy(self) :
        self.dateTextCtrl.Destroy()
        self.dateTextCtrl = None
        self.modeTextCtrl.Destroy()
        self.modeTextCtrl = None
        self.labelTextCtrl.Destroy()
        self.labelTextCtrl = None
        self.bankCheckBox.Destroy()
        self.bankCheckBox = None
        self.amountTextCtrl.Destroy()
        self.amountTextCtrl = None

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
