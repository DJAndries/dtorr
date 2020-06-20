import dlib
import threading
import store
import time
import config

def torrent_lookup(infohash):
  infohash_hexed = bytes(infohash)[:20].hex()
  if infohash_hexed not in store.hash_to_torrent:
    return 0

  torrent = store.hash_to_torrent[infohash_hexed]

  if not store.is_active(None, torrent):
    return 0
  return dlib.addressof(torrent.contents.contents)

class TorrentManageThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.is_running = True

  def run(self):
    config.dtorr_config.torrent_lookup = dlib.CFUNCTYPE(dlib.UNCHECKED(dlib.POINTER(dlib.dtorr_torrent)), dlib.String)(torrent_lookup)

    dlib.peer_server_start(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config))

    while self.is_running:
      store.torrents_lock.acquire()

      dlib.peer_server_accept(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config))

      for torrent_instance in store.torrents.values():
        if not store.is_active(None, torrent_instance):
          continue

        if dlib.manage_torrent(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config),
                            torrent_instance.contents) != 0:
          torrent_instance.status = store.Status.FAILED

        if (torrent_instance.status == store.Status.DOWNLOADING and
            torrent_instance.contents.contents.length == torrent_instance.contents.contents.downloaded):
          torrent_instance.status = store.Status.SEEDING


      store.torrents_lock.release()
      time.sleep(0.001)

  def stop(self):
    self.is_running = False

class TorrentAllocateThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.is_running = True

  def run(self):

    while self.is_running:
      to_alloc = []

      store.torrents_lock.acquire()
      for torrent_instance in store.torrents.values():
        if torrent_instance.status != store.Status.ALLOCATING:
          continue
        to_alloc.append({ 'inst': torrent_instance, 'success': False })
      store.torrents_lock.release()

      for alloc_inst in to_alloc:
        torrent_instance = alloc_inst['inst']
        if dlib.init_torrent_files(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config), torrent_instance.contents) == 0:
          alloc_inst['success'] = True

      store.torrents_lock.acquire()
      for alloc_inst in to_alloc:
        alloc_inst['inst'].status = store.Status.DOWNLOADING if alloc_inst['success'] else store.Status.FAILED
      store.torrents_lock.release()

      time.sleep(2.5)

  def stop(self):
    self.is_running = False
