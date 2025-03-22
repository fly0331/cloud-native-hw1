# user_repository.py
class UserRepository:
    
    def __init__(self):
        self._users = set()
    
    def save(self, username):
        self._users.add(username)

    
    def exists(self, username):
        return username in self._users
    
    def delete(self, username):
        if username in self._users:
            self._users.remove(username)
    
    def get_all(self):
        return list(self._users)