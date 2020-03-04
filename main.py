import wx
import dlib
import tlist
import util
import manage
import details
import config
import prefs
import log
import sys
import state
import port
from forms import MainFrame, PrefDialog

app = wx.App()

manage_thread = manage.TorrentManageThread()

class FullMainFrame(MainFrame):
  def __init__(self, parent):
    MainFrame.__init__(self, parent)
    self.initListColumns()
    self.updateMenuItems(0)
    self.logsShown = False
    self.logsPaused = False

    self.renderFullList()

  def initListColumns(self):
    self.torrentList.AppendTextColumn('Name', width=250)
    self.torrentList.AppendTextColumn('Size', width=75)
    self.torrentList.AppendTextColumn('Status', width=125)
    self.torrentList.AppendProgressColumn('Progress', align=wx.ALIGN_CENTER, width=200)
    self.torrentList.AppendTextColumn('DL Rate', width=80)
    self.torrentList.AppendTextColumn('UL Rate', width=80)
    self.torrentList.AppendTextColumn('ETA', width=80)
    self.torrentList.AppendTextColumn('Infohash', width=200)

  def updateMenuItems(self, tid):
    if tid == 0:
      self.toolbar.EnableTool(self.resumeButton.GetId(), False)
      self.toolbar.EnableTool(self.pauseButton.GetId(), False)
      self.toolbar.EnableTool(self.deleteButton.GetId(), False)
      return
    isDownloading = tlist.is_active(tid)
    self.toolbar.EnableTool(self.resumeButton.GetId(), not isDownloading)
    self.toolbar.EnableTool(self.pauseButton.GetId(), isDownloading)
    self.toolbar.EnableTool(self.deleteButton.GetId(), True)

  def updateStatusBar(self):
    self.statusBar.SetStatusText('UPnP: {}, {}'.format(
      'Available' if port.port_info.upnp_avail else 'N/A',
      'port mapped' if port.port_info.mapped_port else 'mapping failed', 0))

    self.statusBar.SetStatusText('External IP/Port: {}:{}'.format(
      port.port_info.ip or 'Unknown', port.port_info.port or 'Unknown'), 1)

  def logToggle(self, event):
    self.logsShown = event.IsChecked()
    self.logPanel.Show(self.logsShown)
    self.SendSizeEvent()

  def statusLabel(self, torr_instance):
    return torr_instance.status.name.lower().capitalize()

  def addTorrentToList(self, tid, torr_instance):
    self.torrentList.AppendItem((str(torr_instance.contents.contents.name),
                                 util.human_byte_quantity(int(torr_instance.contents.contents.length), 'B'),
                                 self.statusLabel(torr_instance),
                                 0,
                                 '', '', '',
                                 bytes(torr_instance.contents.contents.infohash).hex()), tid)

  def updateTorrentInList(self, index, torr_instance):
    self.torrentList.SetValue(self.statusLabel(torr_instance), index, 2)
    is_active = tlist.is_active(None, torr_instance)
    upload_rate = ''
    download_rate = ''
    eta = ''

    progress = int(torr_instance.contents.contents.downloaded) / int(torr_instance.contents.contents.length) * 100
    self.torrentList.SetValue(progress, index, 3)

    if is_active:
      upload_rate = util.human_byte_quantity(int(torr_instance.contents.contents.upload_rate), 'B/s')
      download_rate = util.human_byte_quantity(int(torr_instance.contents.contents.download_rate), 'B/s')
      eta = util.eta(int(torr_instance.contents.contents.downloaded),
                     int(torr_instance.contents.contents.length),
                     int(torr_instance.contents.contents.download_rate))

    self.torrentList.SetTextValue(download_rate, index, 4)
    self.torrentList.SetTextValue(upload_rate, index, 5)
    self.torrentList.SetTextValue(eta, index, 6)

  def renderFullList(self):
    self.torrentList.DeleteAllItems()
    tlist.torrents_lock.acquire()
    for tid, torrent in tlist.torrents.items():
      self.addTorrentToList(tid, torrent)
    tlist.torrents_lock.release()

  def selectedTid(self):
    selected_item = self.torrentList.GetSelection()
    if selected_item:
      return self.torrentList.GetItemData(selected_item)
    return 0

  def logPause(self, event):
    self.logsPaused = event.IsChecked()

  def updateLogText(self):
    if not log.log_new or not self.logsShown or self.logsPaused:
      return
    log.log_new = False
    self.logText.SetValue(log.log_buf)
    self.logText.SetInsertionPoint(-1)

  def intervalUpdate(self, event):
    tlist.torrents_lock.acquire()
    selected_id = self.selectedTid()
    for i in range(self.torrentList.GetItemCount()):
      tid = self.torrentList.GetItemData(self.torrentList.RowToItem(i))
      torr_instance = tlist.torrents[tid]
      if not tlist.is_active(tid):
        continue
      if selected_id == tid:
        details.update_summary(torr_instance)
      self.updateTorrentInList(i, torr_instance)
      self.updateLogText()
    tlist.torrents_lock.release()

  def delTorrentFromList(self, index):
    self.torrentList.DeleteItem(index)

  def torrentSelected(self, event):
    tlist.torrents_lock.acquire()
    tid = self.selectedTid()
    self.updateMenuItems(tid)
    details.update_summary(tlist.get_torrent(tid), True)
    tlist.torrents_lock.release()

  def changeTorrentStatus(self, target_stat):
    tid = self.selectedTid()
    instance = tlist.change_status(tid, target_stat)
    tlist.torrents_lock.acquire()
    self.updateTorrentInList(self.torrentList.GetSelectedRow(), instance)
    details.update_summary(instance)
    self.updateMenuItems(tid)
    tlist.torrents_lock.release()

  def pauseTorrent(self, event):
    self.changeTorrentStatus(tlist.Status.PAUSED)

  def resumeTorrent(self, event):
    self.changeTorrentStatus(tlist.Status.DOWNLOADING)

  def deleteTorrent(self, event):
    tlist.delete_torrent(self.selectedTid())
    details.update_summary(None, True)
    self.delTorrentFromList(self.torrentList.GetSelectedRow())

  def addTorrent(self, event):
    dialog = wx.FileDialog(self, wildcard='Torrent files (*.torrent)|*.torrent', style=wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_CANCEL:
      return
    try:
      tid, torr_instance = tlist.add_torrent(dialog.GetPath())
    except Exception as e:
      wx.MessageDialog(self, 'Failed to load torrent: {}'.format(e), style=wx.OK | wx.ICON_ERROR).ShowModal()
      return
    self.addTorrentToList(tid, torr_instance)

  def logLevelChanged(self, event):
    tlist.torrents_lock.acquire()
    config.dtorr_config.log_level = event.GetSelection() + 1
    tlist.torrents_lock.release()

  def showPrefs(self, event):
    prefs.show_editor(self)

  def exitApp(self, event):
    manage_thread.stop()
    state.save_state()
    port.clean_port()
    sys.exit()

frame = FullMainFrame(None)

details.populate_notebook(frame.torrentDetailsNotebook)

frame.SetIcon(wx.Icon('icons/dt.png'))

if dlib.dtorr_init() != 0:
  frame.Show(True)
  wx.MessageDialog(frame, 'Failed to init library'.format(e), style=wx.OK | wx.ICON_ERROR).ShowModal()
  sys.exit(1)

port.prep_port()
if port.port_info.port == None:
  frame.Show(True)
  wx.MessageDialog(frame, 'Failed to find open port', style=wx.OK | wx.ICON_ERROR).ShowModal()
  sys.exit(1)

state.load_state()

frame.Show(True)
frame.updateStatusBar()
frame.renderFullList()

config.dtorr_config.port = port.port_info.port

manage_thread.start()

app.MainLoop()

