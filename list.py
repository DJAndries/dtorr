import store
import details
import wx
import util
from forms import ListPanel

class FullListPanel(ListPanel):

  def __init__(self, parent, mainFrame):
    ListPanel.__init__(self, parent)

    self.initColumns()
    self.details = details
    self.mainFrame = mainFrame
    self.setupStatusList()

    self.filteredStatus = None

  def initColumns(self):
    self.torrentList.AppendTextColumn('Name', width=250)
    self.torrentList.AppendTextColumn('Size', width=75)
    self.torrentList.AppendTextColumn('Status', width=125)
    self.torrentList.AppendProgressColumn('Progress', align=wx.ALIGN_CENTER, width=200)
    self.torrentList.AppendTextColumn('DL Rate', width=80)
    self.torrentList.AppendTextColumn('UL Rate', width=80)
    self.torrentList.AppendTextColumn('ETA', width=80)
    self.torrentList.AppendTextColumn('Infohash', width=200)

  def addTorrentToList(self, tid, torr_instance):
    self.torrentList.AppendItem((str(torr_instance.contents.contents.name),
                                 util.human_byte_quantity(int(torr_instance.contents.contents.length), 'B'),
                                 self.statusLabel(torr_instance),
                                 0,
                                 '', '', '',
                                 bytes(torr_instance.contents.contents.infohash).hex()), tid)

  def updateTorrentInList(self, index, torr_instance):
    self.torrentList.SetValue(self.statusLabel(torr_instance), index, 2)
    is_active = store.is_active(None, torr_instance)
    upload_rate = ''
    download_rate = ''
    eta = ''

    progress = int(int(torr_instance.contents.contents.downloaded) / int(torr_instance.contents.contents.length) * 100)
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

  def statusLabel(self, torr_instance):
    return torr_instance.status.name.lower().capitalize()

  def renderFullList(self):
    self.torrentList.DeleteAllItems()
    store.torrents_lock.acquire()
    for tid, torrent in store.torrents.items():
      if self.filteredStatus != None and torrent.status != self.filteredStatus:
        continue
      self.addTorrentToList(tid, torrent)
    store.torrents_lock.release()

  def selectedTid(self):
    selected_item = self.torrentList.GetSelection()
    if selected_item:
      return self.torrentList.GetItemData(selected_item)
    return 0

  def torrentSelected(self, event):
    store.torrents_lock.acquire()
    tid = self.selectedTid()
    self.mainFrame.updateMenuItems(tid)
    details.update_summary(store.get_torrent(tid), True)
    store.torrents_lock.release()

  def delTorrentFromList(self, index):
    self.torrentList.DeleteItem(index)


  def setupStatusList(self):
    root = self.torrentStatusList.AddRoot('All')
    for status in store.Status:
      self.torrentStatusList.AppendItem(root, status.name.lower().capitalize(), data=status)
    self.torrentStatusList.Expand(root)

  def statusSelected(self, event):
    self.filteredStatus = self.torrentStatusList.GetItemData(event.GetItem())
    self.renderFullList()
