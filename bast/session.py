import shelve
from datetime import datetime, timedelta
import os


class SessionManager(object):
    SESSION_ID = "id_"
    DEFAULT_SESSION_LIFETIME = 1200

    def __init__(self, handler):
        self.handler = handler
        self.settings = {}
        self._default_session_lifetime = datetime.utcnow() + timedelta(seconds=self.settings.get('session_lifetime', self.DEFAULT_SESSION_LIFETIME))
        self._expires = self._default_session_lifetime
        self._is_dirty = True
        self.__init_session_driver()
        self.__init_session_object()

    def __init_session_driver(self):
        session_name = self.settings.get('sid_name', self.SESSION_ID)

class Session(object):
    flash_session = {}
    session = {}

    def __init__(self, session_object, client_ip):
        self.session = session_object
        self.client_ip = client_ip

    def get_data(self):
        session = {}
        if self.client_ip in self.session:
            session = self.session

        if self.client_ip in self.flash_session:
            session.update(self.flash_session[self.client_ip])

        if not session:
            return None

        return session

    def get(self, key):
        session = self.get_data()
        if session and key in session:
            return session[key]
        return None

    def put(self, key, value):
        if self.client_ip not in self.session:
            self.session[self.client_ip] = {}

        self.session[self.client_ip][key] = value

    def count(self):
        session = self.get_data()
        return len(session)

    def flash(self, key, value):
        if self.client_ip not in self.flash_session:
            self.flash_session[self.client_ip] = {}

        self.flash_session[self.client_ip][key] = value

    def reset(self, flash_only=False):
        if flash_only:
            if self.client_ip in self.flash_session:
                self.flash_session[self.client_ip] = {}
            else:
                self.session[self.client_ip] = {}

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

    def __init__(self, client_ip):
        SESSION = {}
        Session.__init__(self, SESSION, client_ip)


class FileSession(Session):
    SHELVE = None

    def __init__(self, client_ip):
        """

        """
        self.SHELVE = shelve.open('bast.session', writeback=True)
        Session.__init__(self, self.SHELVE, client_ip)
        # print(self.SHELVE.)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.SHELVE.close()


class RedisSession(Session):
    pass
