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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"dTorr", pos = wx.DefaultPosition, size = wx.Size( 1135,774 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

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

		self.exitButton = self.toolbar.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"icons/exit.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Exit", wx.EmptyString, None )

		self.toolbar.Realize()

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

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
		bSizer1.Add( self.m_splitter2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar3 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.addTorrent, id = self.addTorrentMenuItem.GetId() )
		self.Bind( wx.EVT_TOOL, self.addTorrent, id = self.addButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.deleteTorrent, id = self.deleteButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.resumeTorrent, id = self.resumeButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.pauseTorrent, id = self.pauseButton.GetId() )
		self.Bind( wx.EVT_TOOL, self.exitApp, id = self.exitButton.GetId() )
		self.torrentList.Bind( wx.dataview.EVT_DATAVIEW_SELECTION_CHANGED, self.torrentSelected, id = wx.ID_ANY )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def addTorrent( self, event ):
		event.Skip()


	def deleteTorrent( self, event ):
		event.Skip()

	def resumeTorrent( self, event ):
		event.Skip()

	def pauseTorrent( self, event ):
		event.Skip()

	def exitApp( self, event ):
		event.Skip()

	def torrentSelected( self, event ):
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

		bSizer10.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.progressText = wx.StaticText( self, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.progressText.Wrap( -1 )

		bSizer10.Add( self.progressText, 0, wx.ALL, 5 )


		bSizer9.Add( bSizer10, 0, 0, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 0 )
		bSizer9.Add( self.m_gauge1, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

	def __del__( self ):
		pass


