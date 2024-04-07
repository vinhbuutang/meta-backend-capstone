API paths for testing:

- /restaurant/menu/: get all menu items, post new menu item
- /restaurant/menu/<int:pk>: get, put, delete single menu item
- /restaurant/api-token-auth/: get user's token by providing username & password
- /restaurant/booking/: simple crud for booking a table
- /auth/token/login/: get user's token by providing user & password (via djoser)
- /auth/token/logout/: remove a user's token
- /auth/users/: get list of all users, create new user (via djoser browsable API)

- run `python3 manage.py test` to execute the tests written in /restaurant/tests directory