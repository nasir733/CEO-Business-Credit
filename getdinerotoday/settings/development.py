from getdinerotoday.settings.settings import *
from dotenv import dotenv_values
config = dotenv_values(".env")

DEBUG = True

SECRET_KEY = '!nz#yq7*eo@3d*1(=z=f0jd-&uq!2j#ivns(shit7*b0d_h%ki'
STRIPE_PUBLISHABLE_KEY ="pk_test_51GadadExWTjX75uFcS3TQPfUUSt3dkT1Bh92FLcpB3gBUlTI40JU2xp1VPCzktdISjy0dtM14E6WxZP7IoSxlZK100KQEFLvyV"
STRIPE_SECRET_KEY = "sk_test_51GadadExWTjX75uFGi8HJDnVtz1xsoPqSlVu5C1HQNK5DjdN9ANTXlxinjF9hF7UffAcRpwfOcDtXbxw4jTi8jIk00TqleQ5pg"
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    # 'SHOW_TOOLBAR_CALLBACK': True,
}
ALLOWED_HOSTS = ['*']
