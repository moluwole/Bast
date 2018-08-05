import os

import shelve



class Session(object):

    @property
    def __getitem__(self, *args):
        """

      :return:
      :type args: key


      """
        return self.data.__getitem__(*args)

    @property
    def __setitem__(self,*args, **kwargs):
        """

    :rtype: dict
    """
        return self.data.__setitem__(*args, **kwargs)

    @property
    def __len__(self):
        """

        :return: int
        """
        return self.data.__len__
    @property
    def __delitem__(self, *args):
        return self.data.__delitem__(*args)




class MemorySession(Session):

    def __init__(self):
        self.SESSION = dict()
        Session.__init__(self)

    def get(self, key):
        return self.SESSION.__getitem__(key)

    def put(self, key, value):
        return self.SESSION.__setitem__(key, value)

    def count(self):
        return self.SESSION.__len__()

    def flush(self, key):
        return self.SESSION.__delitem__(key)


class FileSession(Session):
    def __init__(self):
        """

        """
        self.SHELVE = shelve.open('session.shelve')
        Session.__init__(self)

    def get(self, key):
        return self.SHELVE.__getitem__(key)

    def put(self, key, value):
        return self.SHELVE.__setitem__(key, value)

    def count(self):
        return self.SHELVE.__len__()

    def flush(self, key):
        return self.SHELVE.__delitem__(key)


class RedisSession(Session):
    pass
