import shelve
import os


class Session(object):
    flash_session = {}

    def __init__(self, session_object, client_ip):
        self.session = session_object
        self.client_ip = client_ip

    def get_data(self):
        session = dict()
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

    flash_session = {}

    def __init__(self, client_ip):
        self.SESSION = {}
        Session.__init__(self, self.SESSION, client_ip)


class FileSession(Session):
    def __init__(self, client_ip):
        """

        """
        self.SHELVE = shelve.open('bast.session', writeback=True)
        Session.__init__(self, self.SHELVE.dict, client_ip)
        # print(self.SHELVE.)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.SHELVE.close()


class RedisSession(Session):
    pass
