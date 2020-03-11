import wx
import dlib
import store
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
from list import FullListPanel

app = wx.App()

manage_thread = manage.TorrentManageThread()

class FullMainFrame(MainFrame):
  def __init__(self, parent):
    MainFrame.__init__(self, parent)
    self.updateMenuItems(0)
    self.logsShown = False
    self.logsPaused = False

    listPanelSizer = self.listPanelCtr.GetSizer()
    self.listPanel = FullListPanel(self.listPanelCtr, self)
    listPanelSizer.Add(self.listPanel, 1, wx.EXPAND)

  def updateMenuItems(self, tid):
    if tid == 0:
      self.toolbar.EnableTool(self.resumeButton.GetId(), False)
      self.toolbar.EnableTool(self.pauseButton.GetId(), False)
      self.toolbar.EnableTool(self.deleteButton.GetId(), False)
      return
    isDownloading = store.is_active(tid)
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

  def logPause(self, event):
    self.logsPaused = event.IsChecked()

  def updateLogText(self):
    if not log.log_new or not self.logsShown or self.logsPaused:
      return
    log.log_new = False
    self.logText.SetValue(log.log_buf)
    self.logText.SetInsertionPoint(-1)

  def intervalUpdate(self, event):
    store.torrents_lock.acquire()
    selected_id = self.listPanel.selectedTid()
    for i in range(self.listPanel.torrentList.GetItemCount()):
      tid = self.listPanel.torrentList.GetItemData(self.listPanel.torrentList.RowToItem(i))
      torr_instance = store.torrents[tid]
      if not store.is_active(tid):
        continue
      if selected_id == tid:
        details.update_summary(torr_instance)
      self.listPanel.updateTorrentInList(i, torr_instance)
      self.updateLogText()
    store.torrents_lock.release()

  def changeTorrentStatus(self, target_stat):
    tid = self.listPanel.selectedTid()
    instance = store.change_status(tid, target_stat)
    self.listPanel.renderFullList()
    store.torrents_lock.acquire()
    details.update_summary(instance)
    self.updateMenuItems(tid)
    store.torrents_lock.release()

  def pauseTorrent(self, event):
    self.changeTorrentStatus(store.Status.PAUSED)

  def resumeTorrent(self, event):
    self.changeTorrentStatus(store.Status.DOWNLOADING)

  def deleteTorrent(self, event):
    store.delete_torrent(self.listPanel.selectedTid())
    details.update_summary(None, True)
    self.listPanel.delTorrentFromList(self.listPanel.torrentList.GetSelectedRow())

  def addTorrent(self, event):
    dialog = wx.FileDialog(self, wildcard='Torrent files (*.torrent)|*.torrent', style=wx.FD_OPEN)
    if dialog.ShowModal() == wx.ID_CANCEL:
      return
    try:
      tid, torr_instance = store.add_torrent(dialog.GetPath())
    except Exception as e:
      wx.MessageDialog(self, 'Failed to load torrent: {}'.format(e), style=wx.OK | wx.ICON_ERROR).ShowModal()
      return
    self.listPanel.addTorrentToList(tid, torr_instance)

  def logLevelChanged(self, event):
    store.torrents_lock.acquire()
    config.dtorr_config.log_level = event.GetSelection() + 1
    store.torrents_lock.release()

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
frame.listPanel.renderFullList()

config.dtorr_config.port = port.port_info.port

manage_thread.start()

app.MainLoop()

