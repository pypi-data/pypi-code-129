class AfxException(Exception):
  pass

class InvalidVersion(AfxException, TypeError):
  pass

class StatusError(AfxException, TypeError):
  pass

class NotFound(AfxException):
  pass

class UploadError(AfxException):
  pass