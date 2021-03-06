import os
import store
import yaml
import dlib
import config
import util

app_path = util.get_app_path()
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
      store.add_torrent(os.path.join(app_path, 'torrents', '{}.torrent'.format(tid)), tid,
                        store.Status[torrent['status']])
    except:
      pass

def save_state():
  state = { 'torrents': {} }

  store.torrents_lock.acquire()

  for tid, torrent in store.torrents.items():
    result_len = dlib.c_ulonglong(0)
    torr_enc = dlib.save_state(dlib.POINTER(dlib.dtorr_config)(config.dtorr_config), torrent.contents,
                               dlib.POINTER(dlib.c_ulonglong)(result_len))
    if result_len.value == 0:
      continue

    with open(os.path.join(app_path, 'torrents', '{}.torrent'.format(tid)), 'wb') as f:
      f.write(torr_enc.raw[:result_len.value])

    dlib.mfree(torr_enc.raw)

    state['torrents'][tid] = { 'status': torrent.status.name }

  with open(state_path, 'w') as f:
    yaml.dump(state, f)

  store.torrents_lock.release()
