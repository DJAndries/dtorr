
log_labels = [
  'ERROR',
  'WARN',
  'INFO',
  'DEBUG'
]

log_buf = ''
log_len = 0
log_new = False
def handle_log(log_level, content):
  global log_buf, log_new, log_len

  entry = '[{}] {}\n'.format(log_labels[int(log_level) - 1], content)
  log_buf += entry

  log_len += len(entry)

  if log_len > 400000:
    log_buf = log_buf[-200000:]
    log_len = 200000

  log_new = True
