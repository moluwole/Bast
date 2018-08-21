import shelve
import os


class Session(object):
    flash_session = {}
    session = {}

    def __init__(self, session_object):
        self.session.update(session_object)
        self.client_key = os.getenv('APP_KEY')

    def get_data(self):
        session_ = {}
        if self.client_key in self.session:
            session_.update(self.session[self.client_key])

        if self.client_key in self.flash_session:
            session_.update(self.flash_session[self.client_key])

        if not session_:
            return None

        return session_

    def flush(self):
        self.session = {}

    def get(self, key):
        session = self.get_data()
        if session and key in session:
            return session[key]
        return None

    def put(self, key, value):
        if self.client_key not in self.session:
            self.session[self.client_key] = {}

        self.session[self.client_key][key] = value

    def count(self):
        session = self.get_data()
        return len(session)

    def flash(self, key, value):
        if self.client_key not in self.flash_session:
            self.flash_session[self.client_key] = {}

        self.flash_session[self.client_key][key] = value

    def reset(self, flash_only=False):
        if flash_only:
            if self.client_key in self.flash_session:
                self.flash_session[self.client_key] = {}
            else:
                self.session[self.client_key] = {}

    def flush(self, key):
        session = self.get_data()

        if key in session:
            del session[key]
            return True

        return False

    def has(self, key):
        session = self.get_data()
        if session and key in session:
            return True
        return False


class MemorySession(Session):

    def __init__(self):
        SESSION = {}
        Session.__init__(self, SESSION)


class FileSession(Session):
    SHELVE = None

    def __init__(self):
        """

        """
        self.SHELVE = shelve.open('bast.session', writeback=True)
        Session.__init__(self, self.SHELVE)
        # print(self.SHELVE.)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.SHELVE.close()


class RedisSession(Session):
    pass
