import dlib
import threading
import tlist
import time
import config

class TorrentManageThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.is_running = True

  def run(self):
    while True:
      if not self.is_running:
        return

      tlist.torrents_lock.acquire()
      for torrent_instance in tlist.torrents.values():
        if not tlist.is_active(None, torrent_instance):
          continue

        if dlib.manage_torrent(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config),
                            torrent_instance.contents) != 0:
          torrent_instance.status = tlist.Status.FAILED

        if (torrent_instance.status == tlist.Status.DOWNLOADING and
            torrent_instance.contents.contents.length == torrent_instance.contents.contents.downloaded):
          torrent_instance.status = tlist.Status.SEEDING


      tlist.torrents_lock.release()
      time.sleep(0.001)

  def stop(self):
    self.is_running = False
