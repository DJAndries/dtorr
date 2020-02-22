import wx
import dlib
import tlist
import util
from forms import MainFrame, SummaryPanel


app = wx.App()

# f = open('../dtorr/test/torrents/3.torrent', 'rb')
# torr = f.read()

# print(torr)
# dtorr_config = ctypeslib.dtorr_config(log_level=4, log_handler=ctypes.CFUNCTYPE(ctypeslib.UNCHECKED(None), ctypes.c_int, ctypeslib.String)(0))
# # torrentenc = ctypes.POINTER(ctypes.c_char)(ctypes.c_char('abcde'))
# try:
#   dec_torr = ctypeslib.load_torrent_metadata(ctypes.POINTER(ctypeslib.dtorr_config)(dtorr_config), ctypeslib.String(ctypeslib.UserString(torr)), ctypes.c_ulong(len(torr)))
#   ctypeslib.dtorr_init(ctypes.POINTER(ctypeslib.dtorr_config)(dtorr_config))
#   print('ye')
#   print(dec_torr.contents.name)
# except Exception as e:
#   print(e)
#   pass
class FullMainFrame(MainFrame):
  def __init__(self, parent):
    MainFrame.__init__(self, parent)
    self.initListColumns()
    self.updateMenuItems(wx.NOT_FOUND)

  def initListColumns(self):
    self.torrentList.AppendTextColumn('Name', width=250)
    self.torrentList.AppendTextColumn('Size', width=75)
    self.torrentList.AppendTextColumn('Status', width=125)
    self.torrentList.AppendProgressColumn('Progress', align=wx.ALIGN_CENTER, width=200)
    self.torrentList.AppendTextColumn('Infohash', width=200)

  def updateMenuItems(self, selectedRow):
    if selectedRow == wx.NOT_FOUND:
      self.toolbar.EnableTool(self.resumeButton.GetId(), False)
      self.toolbar.EnableTool(self.pauseButton.GetId(), False)
      self.toolbar.EnableTool(self.deleteButton.GetId(), False)
      return
    isDownloading = tlist.is_active(selectedRow)
    self.toolbar.EnableTool(self.resumeButton.GetId(), not isDownloading)
    self.toolbar.EnableTool(self.pauseButton.GetId(), isDownloading)
    self.toolbar.EnableTool(self.deleteButton.GetId(), True)

  def statusLabel(self, torr_instance):
    return 'Downloading' if torr_instance.active else 'Paused'

  def addTorrentToList(self, torr_instance):
    self.torrentList.AppendItem((str(torr_instance.contents.contents.name),
                                 util.human_byte_quantity(int(torr_instance.contents.contents.length), 'B'),
                                 self.statusLabel(torr_instance),
                                 0,
                                 bytes(torr_instance.contents.contents.infohash).hex()))

  def updateTorrentInList(self, index, torr_instance):
    self.torrentList.SetValue(self.statusLabel(torr_instance), index, 2)

  def delTorrentFromList(self, index):
    self.torrentList.DeleteItem(index)

  def torrentSelected(self, event):
    self.updateMenuItems(self.torrentList.GetSelectedRow())

  def pauseTorrent(self, event):
    index = self.torrentList.GetSelectedRow()
    self.updateTorrentInList(index, tlist.change_active(index, False))
    self.updateMenuItems(index)

  def resumeTorrent(self, event):
    index = self.torrentList.GetSelectedRow()
    self.updateTorrentInList(index, tlist.change_active(index, True))
    self.updateMenuItems(index)

  def deleteTorrent(self, event):
    index = self.torrentList.GetSelectedRow()
    tlist.delete_torrent(index)
    self.delTorrentFromList(index)

  def addTorrent(self, event):
    dialog = wx.FileDialog(self, wildcard='Torrent files (*.torrent)|*.torrent', style=wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_CANCEL:
      return
    try:
      torr_instance = tlist.add_torrent(dialog.GetPath())
    except Exception as e:
      wx.MessageDialog(self, 'Failed to load torrent: %s' % e, style=wx.OK | wx.ICON_ERROR).ShowModal()
      return
    self.addTorrentToList(torr_instance)

  def exitApp(self, event):
    quit()


frame = FullMainFrame(None)
frame.torrentDetailsNotebook.AddPage(SummaryPanel(frame.torrentDetailsNotebook), "Summary", True, 0)
frame.SetIcon(wx.Icon('icons/dt.png'))

frame.Show(True)
app.MainLoop()
