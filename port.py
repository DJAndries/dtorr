import miniupnpc
import socket
import random

u = None
port_info = None

class PortInfo:
  def __init__(self):
    self.ip = None
    self.port = None
    self.mapped_port = False
    self.upnp_avail = False

def init_upnp():
  global u

  if u != None:
    return True

  try:
    new_u = miniupnpc.UPnP()
    new_u.discoverdelay = 200

    if new_u.discover() == 0:
      raise Exception('No IGD detected')

    new_u.selectigd()

    u = new_u

    return True
  except:
    return False

def is_port_used(port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)
    return s.connect_ex(('127.0.0.1', port)) == 0

def find_random_unused_port():

  max_tries = 4000
  for i in range(max_tries):
    port = random.randint(10000, 60000)

    if u != None and u.getspecificportmapping(port, 'TCP') != None:
      continue

    if not is_port_used(port):
      return port
  return None

def upnp_add_mapping(port_info):
  try:
    port_info.ip = u.externalipaddress()
    port_info.mapped_port = u.addportmapping(port_info.port, 'TCP', u.lanaddr, port_info.port,
                                             'dtorr port {}'.format(port_info.port), '')
  except:
    pass

def upnp_del_mapping(port_info):
  try:
    u.deleteportmapping(port_info.port, 'TCP')
  except:
    pass

def prep_port():
  global port_info
  port_info = PortInfo()
  port_info.upnp_avail = init_upnp()

  port_info.port = find_random_unused_port()
  if port_info.port == None:
    return port_info

  if port_info.upnp_avail:
    upnp_add_mapping(port_info)

  return port_info

def clean_port():
  try:
    if u != None and port_info.mapped_port:
      upnp_del_mapping(port_info)
  except:
    pass
