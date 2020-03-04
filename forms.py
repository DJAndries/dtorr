# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"dTorr", pos = wx.DefaultPosition, size = wx.Size( 1546,893 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menubar1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menu1 = wx.Menu()
		self.addTorrentMenuItem = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Add Torrent", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.addTorrentMenuItem )

		self.m_menu1.AppendSeparator()

		self.exitMenuItem = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.exitMenuItem )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.prefMenuItem = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Preferences", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.prefMenuItem )

		self.m_menubar1.Append( self.m_menu2, u"Edit" )

		self.m_menu3 = wx.Menu()
		self.aboutMenuItem = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.aboutMenuItem )

		self.m_menubar1.Append( self.m_menu3, u"Help" )

		self.SetMenuBar( self.m_menubar1 )

		self.toolbar = self.CreateToolBar( wx.TB_FLAT|wx.TB_HORIZONTAL, wx.ID_ANY )
		self.toolbar.SetMargins( wx.Size( 16,16 ) )
		self.addButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/add.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Add Torrent", wx.EmptyString, None )

		self.deleteButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Delete", wx.EmptyString, None )

		self.toolbar.AddSeparator()

		self.resumeButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/resume.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.pauseButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/pause.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.toolbar.AddSeparator()

		self.prefButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/config.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Preferences", wx.EmptyString, None )

		self.m_tool7 = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/log.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_CHECK, u"Library Logs", wx.EmptyString, None )

		self.exitButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/exit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Exit", wx.EmptyString, None )

		self.toolbar.Realize()

		mainSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter2.SetSashGravity( 1 )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )

		self.m_panel2 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_splitter3 = wx.SplitterWindow( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter3.Bind( wx.EVT_IDLE, self.m_splitter3OnIdle )

		self.m_panel5 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.torrentStatusList = wx.TreeCtrl( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TR_DEFAULT_STYLE )
		bSizer7.Add( self.torrentStatusList, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer7 )
		self.m_panel5.Layout()
		bSizer7.Fit( self.m_panel5 )
		self.m_panel6 = wx.Panel( self.m_splitter3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.torrentList = wx.dataview.DataViewListCtrl( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.torrentList, 1, wx.ALL|wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer8 )
		self.m_panel6.Layout()
		bSizer8.Fit( self.m_panel6 )
		self.m_splitter3.SplitVertically( self.m_panel5, self.m_panel6, 229 )
		bSizer2.Add( self.m_splitter3, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		self.m_panel3 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.torrentDetailsNotebook = wx.Notebook( self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		bSizer6.Add( self.torrentDetailsNotebook, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		self.m_splitter2.SplitHorizontally( self.m_panel2, self.m_panel3, 450 )
		mainSizer.Add( self.m_splitter2, 2, wx.EXPAND, 5 )

		self.logPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.logPanel.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.logPanel.Hide()

		bSizer56 = wx.BoxSizer( wx.VERTICAL )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText22 = wx.StaticText( self.logPanel, wx.ID_ANY, u"Log Level:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )

		self.m_staticText22.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer25.Add( self.m_staticText22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		m_choice1Choices = [ u"1 - Error", u"2 - Warning", u"3 - Info", u"4 - Debug" ]
		self.m_choice1 = wx.Choice( self.logPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 2 )
		bSizer25.Add( self.m_choice1, 0, wx.ALL, 5 )


		bSizer25.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.logPauseBtn = wx.ToggleButton( self.logPanel, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.logPauseBtn, 0, wx.ALL, 5 )


		bSizer56.Add( bSizer25, 0, wx.EXPAND, 5 )

		self.logText = wx.TextCtrl( self.logPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP|wx.VSCROLL )
		self.logText.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.logText.SetForegroundColour( wx.Colour( 233, 233, 233 ) )
		self.logText.SetBackgroundColour( wx.Colour( 41, 41, 41 ) )

		bSizer56.Add( self.logText, 1, wx.ALL|wx.EXPAND, 5 )


		self.logPanel.SetSizer( bSizer56 )
		self.logPanel.Layout()
		bSizer56.Fit( self.logPanel )
		mainSizer.Add( self.logPanel, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainSizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 3, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.refreshTimer = wx.Timer()
		self.refreshTimer.SetOwner( self, wx.ID_ANY )
		self.refreshTimer.Start( 2500 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.exitApp )
		self.Bind( wx.EVT_MENU, self.addTorrent, id = self.addTorrentMenuItem.GetId() )
		self.Bind( wx.EVT_MENU, self.showPrefs, id = self.prefMenuItem.GetId() )
		self.Bind( wx.EVT_TOOL, self.addTorrent, id = self.addButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.deleteTorrent, id = self.deleteButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.resumeTorrent, id = self.resumeButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.pauseTorrent, id = self.pauseButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.showPrefs, id = self.prefButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.logToggle, id = self.m_tool7.GetId() )
		self.Bind( wx.EVT_TOOL, self.exitApp, id = self.exitButton.GetId() )
		self.torrentList.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.torrentSelected, id = wx.ID_ANY )
		self.m_choice1.Bind( wx.EVT_CHOICE, self.logLevelChanged )
		self.logPauseBtn.Bind( wx.EVT_TOGGLEBUTTON, self.logPause )
		self.Bind( wx.EVT_TIMER, self.intervalUpdate, id=wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def exitApp( self, event ):
		event.Skip()

	def addTorrent( self, event ):
		event.Skip()

	def showPrefs( self, event ):
		event.Skip()


	def deleteTorrent( self, event ):
		event.Skip()

	def resumeTorrent( self, event ):
		event.Skip()

	def pauseTorrent( self, event ):
		event.Skip()


	def logToggle( self, event ):
		event.Skip()


	def torrentSelected( self, event ):
		event.Skip()

	def logLevelChanged( self, event ):
		event.Skip()

	def logPause( self, event ):
		event.Skip()

	def intervalUpdate( self, event ):
		event.Skip()

	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 450 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )

	def m_splitter3OnIdle( self, event ):
		self.m_splitter3.SetSashPosition( 229 )
		self.m_splitter3.Unbind( wx.EVT_IDLE )


###########################################################################
## Class SummaryPanel
###########################################################################

class SummaryPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 1013,350 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Progress:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.progressText = wx.StaticText( self, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.progressText.Wrap( -1 )

		bSizer10.Add( self.progressText, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer10, 0, 0, 5 )

		self.progressBar = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.progressBar.SetValue( 0 )
		bSizer9.Add( self.progressBar, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer44 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer45 = wx.BoxSizer( wx.VERTICAL )

		bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer101.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.nameText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.nameText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer101.Add( self.nameText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer101, 0, wx.EXPAND, 5 )

		bSizer1012 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1012.Add( self.m_staticText32, 0, wx.ALL, 5 )

		self.sizeText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.sizeText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1012.Add( self.sizeText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer1012, 0, wx.EXPAND, 5 )

		bSizer1011 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Infohash:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1011.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.infohashText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.infohashText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1011.Add( self.infohashText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer1011, 0, wx.EXPAND, 5 )

		bSizer1014 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Piece size/count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		self.m_staticText34.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1014.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.pieceText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.pieceText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1014.Add( self.pieceText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer1014, 0, wx.EXPAND, 5 )

		bSizer1013 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"File count:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )

		self.m_staticText33.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1013.Add( self.m_staticText33, 0, wx.ALL, 5 )

		self.fileCountText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.fileCountText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer1013.Add( self.fileCountText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer1013, 0, wx.EXPAND, 5 )

		bSizer10141 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText341 = wx.StaticText( self, wx.ID_ANY, u"Download path:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText341.Wrap( -1 )

		self.m_staticText341.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer10141.Add( self.m_staticText341, 0, wx.ALL, 5 )

		self.downloadPathText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.downloadPathText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer10141.Add( self.downloadPathText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer10141, 0, wx.EXPAND, 5 )

		bSizer101411 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3411 = wx.StaticText( self, wx.ID_ANY, u"Announce URL:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3411.Wrap( -1 )

		self.m_staticText3411.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer101411.Add( self.m_staticText3411, 0, wx.ALL, 5 )

		self.announceUrlText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_READONLY|wx.BORDER_NONE )
		self.announceUrlText.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer101411.Add( self.announceUrlText, 1, wx.ALL, 5 )


		bSizer45.Add( bSizer101411, 0, wx.EXPAND, 5 )


		bSizer44.Add( bSizer45, 1, wx.EXPAND, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		bSizer44.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer47 = wx.BoxSizer( wx.VERTICAL )

		bSizer1015 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"DL Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		self.m_staticText35.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1015.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.dlRateText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dlRateText.Wrap( -1 )

		bSizer1015.Add( self.dlRateText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer1015, 0, wx.EXPAND, 5 )

		bSizer101622 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3622 = wx.StaticText( self, wx.ID_ANY, u"ETA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3622.Wrap( -1 )

		self.m_staticText3622.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer101622.Add( self.m_staticText3622, 0, wx.ALL, 5 )

		self.etaText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.etaText.Wrap( -1 )

		bSizer101622.Add( self.etaText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer101622, 0, wx.EXPAND, 5 )

		bSizer1016 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"UL Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )

		self.m_staticText36.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer1016.Add( self.m_staticText36, 0, wx.ALL, 5 )

		self.ulRateText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ulRateText.Wrap( -1 )

		bSizer1016.Add( self.ulRateText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer1016, 0, wx.EXPAND, 5 )

		bSizer10161 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText361 = wx.StaticText( self, wx.ID_ANY, u"Data downloaded:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText361.Wrap( -1 )

		self.m_staticText361.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer10161.Add( self.m_staticText361, 0, wx.ALL, 5 )

		self.dataDlText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataDlText.Wrap( -1 )

		bSizer10161.Add( self.dataDlText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer10161, 0, wx.EXPAND, 5 )

		bSizer10162 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText362 = wx.StaticText( self, wx.ID_ANY, u"Data uploaded:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText362.Wrap( -1 )

		self.m_staticText362.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer10162.Add( self.m_staticText362, 0, wx.ALL, 5 )

		self.dataUlText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dataUlText.Wrap( -1 )

		bSizer10162.Add( self.dataUlText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer10162, 0, wx.EXPAND, 5 )

		bSizer101621 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3621 = wx.StaticText( self, wx.ID_ANY, u"Peers:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3621.Wrap( -1 )

		self.m_staticText3621.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer101621.Add( self.m_staticText3621, 0, wx.ALL, 5 )

		self.peerCountText = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.peerCountText.Wrap( -1 )

		bSizer101621.Add( self.peerCountText, 1, wx.ALL, 5 )


		bSizer47.Add( bSizer101621, 0, wx.EXPAND, 5 )


		bSizer44.Add( bSizer47, 1, wx.EXPAND, 5 )


		bSizer9.Add( bSizer44, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class PrefDialog
###########################################################################

class PrefDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Preferences", pos = wx.DefaultPosition, size = wx.Size( 443,296 ), style = wx.DEFAULT_DIALOG_STYLE|wx.STAY_ON_TOP )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		bSizer27.SetMinSize( wx.Size( 443,296 ) )
		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.randomPortCheckBox = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"Choose random port", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.randomPortCheckBox.SetValue(True)
		bSizer30.Add( self.randomPortCheckBox, 0, wx.ALL, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText261 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Listening port:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText261.Wrap( -1 )

		bSizer32.Add( self.m_staticText261, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.listeningPortText = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.listeningPortText.Enable( False )

		bSizer32.Add( self.listeningPortText, 0, wx.ALL, 5 )


		bSizer30.Add( bSizer32, 0, wx.EXPAND, 5 )

		self.upnpCheckBox = wx.CheckBox( self.m_panel6, wx.ID_ANY, u"UPnP (Port Forwarding)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.upnpCheckBox.SetValue(True)
		bSizer30.Add( self.upnpCheckBox, 0, wx.ALL, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText27 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Download directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer33.Add( self.m_staticText27, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.downloadDirCtrl = wx.DirPickerCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer33.Add( self.downloadDirCtrl, 1, wx.ALL, 5 )


		bSizer30.Add( bSizer33, 0, wx.EXPAND, 5 )


		bSizer27.Add( bSizer30, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer28.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.saveBtn = wx.Button( self.m_panel6, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.saveBtn, 0, wx.ALL, 5 )

		self.cancelBtn = wx.Button( self.m_panel6, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer28.Add( self.cancelBtn, 0, wx.ALL, 5 )


		bSizer27.Add( bSizer28, 0, wx.EXPAND, 5 )


		self.m_panel6.SetSizer( bSizer27 )
		self.m_panel6.Layout()
		bSizer27.Fit( self.m_panel6 )
		bSizer35.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.randomPortCheckBox.Bind( wx.EVT_CHECKBOX, self.randomPortChanged )
		self.saveBtn.Bind( wx.EVT_BUTTON, self.save )
		self.cancelBtn.Bind( wx.EVT_BUTTON, self.cancel )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def randomPortChanged( self, event ):
		event.Skip()

	def save( self, event ):
		event.Skip()

	def cancel( self, event ):
		event.Skip()


