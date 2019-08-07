class Error(Exception):
    """"""
    pass


class ResponseError(Error):
    """Exception raised for errors in response.

        Attributes:
              code -- response code that was returned.
              message -- explanation of the response code as per the Cylance API documentation.
        """

    def __init__(self, code):
        self.code = code
        self.message = str(self.code) + ' -- Unknown --'


class Response400Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 400
        self.message = str(self.code) + ' -- BadRequest --'


class Response401Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 401
        self.message = str(self.code) + ' -- Unauthorized --'


class Response403Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 403
        self.message = str(self.code) + ' -- Forbidden --'


class Response404Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 404
        self.message = str(self.code) + ' -- NotFound --'


class Response409Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 409
        self.message = str(self.code) + ' -- Conflict --'


class Response429Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 429
        self.message = str(self.code) + ' -- TooManyRequests --'


class Response500Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 500
        self.message = str(self.code) + ' -- InternalServerError --'


class Response501Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.code = 501
        self.message = str(self.code) + ' -- Not Implemented --'


class InvalidSHA256Error(Error):
    """Exception raised for errors in response.

    Attributes:
          code -- response code that was returned.
          message -- explanation of the response code as per the Cylance API documentation.
    """

    def __init__(self):

        self.message = 'Invalid SHA256 -- This hash does not meet the length requirements for SHA256'


class InvalidBaseEndpoint(Error):
    """Exception raised for when an invalid base endpoint is selected.

    Attributes:
           code --
           message --
    """

    def __init__(self):

        self.message = 'Invalid Base Endpoint'


class InvalidListType(Error):
    """Exception raised for when an invalid base endpoint is selected.

    Attributes:
           code --
           message --
    """

    def __init__(self):

        self.message = 'Invalid List Type. List range is 0 (GlobalQuarantine or 1 (GlobalSafe)'
