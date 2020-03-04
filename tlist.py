import dlib
import config
import os
import threading
import enum
import port
import prefs

torrents = {}
hash_to_torrent = {}
next_id = 1
torrents_lock = threading.Lock()

class Status(enum.Enum):
  PAUSED = 1
  DOWNLOADING = 2
  SEEDING = 3
  FAILED = 4

class TorrentInstance:
  def __init__(self, contents, status):
    self.status = status
    self.contents = contents

def add_torrent(path, tid=None, status=Status.DOWNLOADING):
  global next_id
  with open(path, 'rb') as f:
    file_contents = f.read()
    torr_struct = dlib.load_torrent_metadata(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config),
                                    dlib.String(dlib.UserString(file_contents)),
                                    dlib.c_ulong(len(file_contents)))
    if not torr_struct:
      raise Exception('Error loading torrent. See log for details.')

    download_dir = prefs.prefs['download_dir']
    if torr_struct.contents.file_count > 1:
      download_dir = os.path.join(download_dir, str(torr_struct.contents.name))

    torr_struct.contents.download_dir = dlib.String(dlib.UserString(download_dir))

    torr_struct.contents.me.ip = (port.port_info.ip or '0.0.0.0').encode()
    torr_struct.contents.me.port = port.port_info.port
    torr_struct.contents.me.peer_id = os.urandom(20)

    os.makedirs(download_dir, exist_ok=True)

    if dlib.init_torrent_files(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config), torr_struct) != 0:
      raise Exception('Failed to init torrent files. See log for details.')

    torrent_instance = TorrentInstance(torr_struct, status)

    torrents_lock.acquire()
    if not tid:
      tid = next_id

    torrents[tid] = torrent_instance
    hash_to_torrent[bytes(torr_struct.contents.infohash).hex()] = torrent_instance

    if tid >= next_id:
      next_id = tid + 1

    torrents_lock.release()

    return tid, torrent_instance

def get_torrent(tid):
  return torrents.get(tid, None)

def is_active(tid, instance=None):
  if not instance:
    instance = torrents[tid]
  return instance.status in (Status.DOWNLOADING, Status.SEEDING)

def change_status(tid, status):
  torrents_lock.acquire()
  inst = torrents[tid]
  inst.status = status
  torrents_lock.release()
  return inst

def delete_torrent(tid):
  torrents_lock.acquire()
  torrent = torrents[tid]
  hash_to_torrent.pop(bytes(torrent.contents.contents.infohash).hex())
  torrents.pop(tid)
  torrents_lock.release()
