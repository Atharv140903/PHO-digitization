AUTHORIZATION_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/authorize/'

REDIRECT_URI = 'http://127.0.0.1:8000/oauth/callback/'

CLIENT_ID = 'Ji3kYtUkmDY2TSQx2AbFY7M5rqFrMuu5kiSUEFXm'

CLIENT_SECRET = 'xPUfWFRM8Zm40izx6DLee21FPihIaKZHeDeKo7yMSTabIFH9anbTGcwzyY9LOoFP0gz6Af6PL4lD22sLE5NfggzHODtgb2TsgKjFGabr4sD7IG2QgXA3lI7Lez6y4ARJ'

SCOPE = '%20'.join([
    'profile', 'ldap', 'program'
])

SSO_TOKEN_URL = "https://gymkhana.iitb.ac.in/sso/oauth/token/"

SSO_PROFILE_URL = "https://gymkhana.iitb.ac.in/sso/user/api/user/" \
                  "?fields=first_name,last_name,roll_number,email,insti_address"
