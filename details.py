import util
import store
from forms import SummaryPanel

summary = None

def populate_notebook(notebook):
  global summary
  summary = SummaryPanel(notebook)
  notebook.AddPage(summary, "Summary", True, 0)

def update_summary_info(torr_instance):
  name = ''
  size = ''
  infohash = ''
  piece_size = ''
  file_count = ''
  download_path = ''
  announce_url = ''

  if torr_instance:
    name = str(torr_instance.contents.contents.name)
    size = util.human_byte_quantity(int(torr_instance.contents.contents.length), 'B')
    infohash = bytes(torr_instance.contents.contents.infohash).hex()
    piece_len = util.human_byte_quantity(int(torr_instance.contents.contents.piece_length), 'B')
    piece_size = '{} ({} pieces)'.format(piece_len, torr_instance.contents.contents.piece_count)
    file_count = str(torr_instance.contents.contents.file_count)
    download_path = str(torr_instance.contents.contents.download_dir)
    announce_url = str(torr_instance.contents.contents.announce)

  summary.nameText.SetValue(name)
  summary.sizeText.SetValue(size)
  summary.infohashText.SetValue(infohash)
  summary.pieceText.SetValue(piece_size)
  summary.fileCountText.SetValue(file_count)
  summary.downloadPathText.SetValue(download_path)
  summary.announceUrlText.SetValue(announce_url)

def update_summary_stats(torr_instance):
  progress_val = 0
  progress_text = '0%'
  dl_rate = ''
  ul_rate = ''
  data_dl = ''
  data_ul = ''
  peers = ''
  eta = ''

  if torr_instance:
    progress_val = round(float(torr_instance.contents.contents.downloaded) / \
                         float(torr_instance.contents.contents.length) * 100, 2)
    progress_text = '{}%'.format(progress_val)

    if store.is_active(None, torr_instance):
      dl_rate = util.human_byte_quantity(int(torr_instance.contents.contents.download_rate), 'B/s')
      ul_rate = util.human_byte_quantity(int(torr_instance.contents.contents.upload_rate), 'B/s')
      data_dl = util.human_byte_quantity(torr_instance.contents.contents.downloaded, 'B')
      data_ul = util.human_byte_quantity(torr_instance.contents.contents.uploaded, 'B')
      peers = str(torr_instance.contents.contents.active_peer_count)
      eta = util.eta(int(torr_instance.contents.contents.downloaded),
                    int(torr_instance.contents.contents.length),
                    int(torr_instance.contents.contents.download_rate))

  summary.progressText.SetLabel(progress_text)
  summary.progressBar.SetValue(int(progress_val))
  summary.dlRateText.SetLabel(dl_rate)
  summary.ulRateText.SetLabel(ul_rate)
  summary.dataDlText.SetLabel(data_dl)
  summary.dataUlText.SetLabel(data_ul)
  summary.peerCountText.SetLabel(peers)
  summary.etaText.SetLabel(eta)

def update_summary(torr_instance, full_update=False):
  if full_update:
    update_summary_info(torr_instance)
  update_summary_stats(torr_instance)

