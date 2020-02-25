from sys import platform
import os
import tlist
import yaml
import dlib
import config

app_path = os.path.expanduser('~/AppData/Roaming/dtorr' if platform in ('win32', 'cygwin') else '~/.dtorr')
os.makedirs(app_path, exist_ok=True)
os.makedirs(os.path.join(app_path, 'torrents'), exist_ok=True)

state_path = os.path.join(app_path, 'state.yml')

def load_state():
  if not os.path.isfile(state_path):
    return

  with open(state_path) as f:
    state = yaml.load(f, yaml.FullLoader)

  if 'torrents' not in state:
    return

  torrents = state['torrents']

  for tid, torrent in torrents.items():
    try:
      tlist.add_torrent(os.path.join(app_path, 'torrents/{}.torrent'.format(tid)), tid,
                        tlist.Status[torrent['status']])
    except:
      pass

def save_state():
  state = { 'torrents': {} }

  tlist.torrents_lock.acquire()

  for tid, torrent in tlist.torrents.items():
    result_len = dlib.c_ulong(0)
    torr_enc = dlib.save_state(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config), torrent.contents,
                               dlib.POINTER(dlib.c_ulong)(result_len))
    if result_len.value == 0:
      continue

    with open(os.path.join(app_path, 'torrents/{}.torrent'.format(tid)), 'wb') as f:
      f.write(torr_enc.raw[:result_len.value])

    dlib.mfree(torr_enc.raw)

    state['torrents'][tid] = { 'status': torrent.status.name }

  with open(state_path, 'w') as f:
    yaml.dump(state, f)

  tlist.torrents_lock.release()
