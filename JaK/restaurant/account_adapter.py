from allauth.account.adapter import DefaultAccountAdapter

class NoNewUsersAccountsAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        # Prevent new users from signing up
        return False