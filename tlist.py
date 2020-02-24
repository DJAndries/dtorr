import dlib
import config
import os
import threading
import enum

torrents = {}
next_id = 1
torrents_lock = threading.Lock()

download_path = 'D:\\Downloads\\dtorr_test'

class Status(enum.Enum):
  PAUSED = 1
  DOWNLOADING = 2
  SEEDING = 3
  FAILED = 4

class TorrentInstance:
  def __init__(self, contents, status=Status.DOWNLOADING):
    self.status = Status.DOWNLOADING
    self.contents = contents

def add_torrent(path):
  global next_id
  with open(path, 'rb') as f:
    file_contents = f.read()
    torr_struct = dlib.load_torrent_metadata(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config),
                                    dlib.String(dlib.UserString(file_contents)),
                                    dlib.c_ulong(len(file_contents)))
    if not torr_struct:
      raise Exception('Error loading torrent. See log for details.')

    download_dir = download_path
    if torr_struct.contents.file_count > 1:
      download_dir = os.path.join(download_dir, str(torr_struct.contents.name))

    torr_struct.contents.download_dir = dlib.String(dlib.UserString(download_dir))

    os.makedirs(download_dir, exist_ok=True)

    if dlib.init_torrent_files(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config), torr_struct) != 0:
      raise Exception('Failed to init torrent files. See log for details.')

    torrent_instance = TorrentInstance(torr_struct)

    torrents_lock.acquire()
    tid = next_id
    torrents[tid] = torrent_instance
    next_id += 1
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
  torrents.pop(tid)
  torrents_lock.release()
