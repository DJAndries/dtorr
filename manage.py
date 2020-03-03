import dlib
import threading
import tlist
import time
import config

def torrent_lookup(infohash):
  infohash_hexed = bytes(infohash)[:20].hex()
  if infohash_hexed not in tlist.hash_to_torrent:
    return 0

  torrent = tlist.hash_to_torrent[infohash_hexed]

  if not tlist.is_active(None, torrent):
    return 0
  return dlib.addressof(torrent.contents.contents)

class TorrentManageThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.is_running = True

  def run(self):
    config.dtorr_config.torrent_lookup = dlib.CFUNCTYPE(dlib.UNCHECKED(dlib.POINTER(dlib.dtorr_torrent)), dlib.String)(torrent_lookup)

    dlib.peer_server_start(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config))

    while True:
      if not self.is_running:
        return

      tlist.torrents_lock.acquire()

      dlib.peer_server_accept(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config))

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
