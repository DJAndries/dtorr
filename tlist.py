import dlib
import config
import os

torrent_list = []

download_path = 'D:\\Downloads'

class TorrentInstance:
  def __init__(self, contents, active=True):
    self.active = active
    self.contents = contents


def add_torrent(path):
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
    torrent_list.append(torrent_instance)

    return torrent_instance


def is_active(index):
  return torrent_list[index].active

def change_active(index, active):
  torrent_list[index].active = active
  return torrent_list[index]

def delete_torrent(index):
  torrent_list.pop(index)
