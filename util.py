

def human_byte_quantity(size, suffix):
  for unit in ['','K','M','G','T','P','E','Z']:
    if abs(size) < 1024.0:
      return "%3.1f%s%s" % (size, unit, suffix)
    size /= 1024.0
  return "%.1f%s%s" % (size, 'Y', suffix)
