users: dict[int, dict[str, str]] = {
    1: {
        'username': 'lxsz LA',
        'password': '123'
    },
    2: {
        'username': 'johnny.reis',
        'password': '123'
    },
    3: {
        'username': 'erivelter_82407',
        'password': '123'
    }
}

def get_users_by_username(username: str)-> dict | None:
   id = user = None
   for current_id, current_user in users.items():
      if current_user.get('username') == username:
         id, user = current_id, current_user
         break
   return id, user