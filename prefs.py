import wx
import os
import util
import yaml
from forms import PrefDialog

app_path = util.get_app_path()

prefs = None

fields = {
  'random_port': (True, 'randomPortCheckBox'),
  'port': (None, 'listeningPortText'),
  'upnp': (True, 'upnpCheckBox'),
  'download_dir': (os.path.join(os.path.expanduser('~'), 'Downloads'), 'downloadDirCtrl')
}

class FullPrefDialog(PrefDialog):
  def __init__(self, parent):
    PrefDialog.__init__(self, parent)
    self.prefs = dict(prefs)

    for key, info in fields.items():
      ctrl = getattr(self, info[1])
      value = self.prefs[key]
      if isinstance(ctrl, wx.TextCtrl):
        ctrl.SetValue(value or '')
      elif isinstance(ctrl, wx.DirPickerCtrl):
        ctrl.SetPath(value or '')
      else:
        ctrl.SetValue(value)

    if not self.prefs['random_port']:
      self.listeningPortText.Enable()

  def randomPortChanged(self, event):
    random_port = event.IsChecked()
    self.prefs['random_port'] = random_port
    if random_port:
      self.listeningPortText.SetValue('')
      self.listeningPortText.Disable()
      self.prefs['port'] = None
    else:
      self.listeningPortText.Enable()

  def cancel(self, event):
    self.Close()

  def report_error(self, msg):
    wx.MessageDialog(self, msg, style=wx.OK | wx.ICON_ERROR).ShowModal()

  def save(self, event):
    global prefs

    for key, info in fields.items():
      ctrl = getattr(self, info[1])
      if isinstance(ctrl, wx.DirPickerCtrl):
        self.prefs[key] = ctrl.GetPath()
      else:
        self.prefs[key] = ctrl.GetValue()

    if self.prefs['port'] != None and not self.prefs['random_port']:
      try:
        port = int(self.prefs['port'])
        if port < 1 or port > 65535:
          raise Exception()
      except:
        self.report_error('Invalid port number')
        return

    if not os.path.exists(self.prefs['download_dir']):
      self.report_error('Download path does not exist')
      return

    prefs = self.prefs

    with open(os.path.join(app_path, 'prefs.yml'), 'w') as f:
      yaml.dump(prefs, f)

    self.Close()

def show_editor(parent):
  FullPrefDialog(parent).ShowModal()

def update_default_prefs():
  global prefs
  if not prefs:
    prefs = dict()
  for key, info in fields.items():
    if key not in prefs:
      prefs[key] = info[0]
  os.makedirs(prefs['download_dir'], exist_ok=True)

def load():
  global prefs
  try:
    prefs_path = os.path.join(app_path, 'prefs.yml')
    if os.path.isfile(prefs_path):
      with open(prefs_path) as f:
        prefs = yaml.load(f, yaml.FullLoader)
  except:
    pass
  update_default_prefs()

load()
