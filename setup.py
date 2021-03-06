#!/usr/bin/env python
import os
import pip


def install(package):
    pip.main(['install', package])

basedir = os.path.abspath(os.path.dirname(__file__))
configFile = open(os.path.join(basedir, 'config.py'), 'w')

# File Imports
configFile.write("import os\nbasedir = os.path.abspath(os.path.dirname(__file__))\n\n")

# BASIC APP CONFIG
WTF_CSRF_ENABLED = "True" if not os.environ.get("WTF_CSRF_ENABLED") else os.environ["WTF_CSRF_ENABLED"]
configFile.write('WTF_CSRF_ENABLED = {0}\n'.format(WTF_CSRF_ENABLED))

SECRET_KEY = "changeme" if not os.environ.get("SECRET_KEY") else os.environ["SECRET_KEY"]
configFile.write("SECRET_KEY = '{0}'\n".format(SECRET_KEY))

BIND_ADDRESS = "0.0.0.0" if not os.environ.get("BIND_ADDRESS") else os.environ["BIND_ADDRESS"]
configFile.write("BIND_ADDRESS = '{0}'\n".format(BIND_ADDRESS))

PORT = "9393" if not os.environ.get("PORT") else os.environ["PORT"]
configFile.write("PORT = {0}\n".format(PORT))

LOGIN_TITLE = "PowerDNS-Admin" if not os.environ.get("LOGIN_TITLE") else os.environ["LOGIN_TITLE"]
configFile.write("LOGIN_TITLE = '{0}'\n".format(LOGIN_TITLE))

# TIMEOUT - for large zones
TIMEOUT = "10" if not os.environ.get("TIMEOUT") else os.environ["TIMEOUT"]
configFile.write("TIMEOUT = {0}\n".format(TIMEOUT))

# LOG CONFIG
LOG_LEVEL = "WARNING" if not os.environ.get("LOG_LEVEL") else os.environ["LOG_LEVEL"]
configFile.write("LOG_LEVEL = '{0}'\n".format(LOG_LEVEL))

configFile.write("LOG_FILE = ''\n")

# UPLOAD
UPLOAD_DIR = "upload" if not os.environ.get("UPLOAD_DIR") else os.environ["UPLOAD_DIR"]
configFile.write("UPLOAD_DIR = os.path.join(basedir, '{0}')\n".format(UPLOAD_DIR))

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = "sqlite://" if not os.environ.get("SQLALCHEMY_DATABASE_URI") else os.environ[
    "SQLALCHEMY_DATABASE_URI"]
configFile.write("SQLALCHEMY_DATABASE_URI = '{0}'\n".format(SQLALCHEMY_DATABASE_URI))

SQLALCHEMY_MIGRATE_REPO = "db_repository" if not os.environ.get("SQLALCHEMY_MIGRATE_REPO") else os.environ[
    "SQLALCHEMY_MIGRATE_REPO"]
configFile.write("SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, '{0}')\n".format(SQLALCHEMY_MIGRATE_REPO))

SQLALCHEMY_TRACK_MODIFICATIONS = "True" if not os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") else os.environ[
    "SQLALCHEMY_TRACK_MODIFICATIONS"]
configFile.write("SQLALCHEMY_TRACK_MODIFICATIONS = {0}\n".format(SQLALCHEMY_TRACK_MODIFICATIONS))

# LDAP CONFIG
LDAP_TYPE = "False" if not os.environ.get("LDAP_TYPE") else os.environ["LDAP_TYPE"]
if LDAP_TYPE != "False":
    configFile.write("LDAP_TYPE = {0}\n".format(LDAP_TYPE))

    LDAP_URI = "" if not os.environ.get("LDAP_URI") else os.environ["LDAP_URI"]
    configFile.write("LDAP_URI = '{0}'\n".format(LDAP_URI))

    LDAP_USERNAME = "" if not os.environ.get("LDAP_USERNAME") else os.environ["LDAP_USERNAME"]
    configFile.write("LDAP_USERNAME = '{0}'\n".format(LDAP_USERNAME))

    LDAP_PASSWORD = "" if not os.environ.get("LDAP_PASSWORD") else os.environ["LDAP_PASSWORD"]
    configFile.write("LDAP_PASSWORD = '{0}'\n".format(LDAP_PASSWORD))

    LDAP_SEARCH_BASE = "" if not os.environ.get("LDAP_SEARCH_BASE") else os.environ["LDAP_SEARCH_BASE"]
    configFile.write("LDAP_SEARCH_BASE = '{0}'\n".format(LDAP_SEARCH_BASE))

    LDAP_USERNAMEFIELD = "" if not os.environ.get("LDAP_USERNAMEFIELD") else os.environ["LDAP_USERNAMEFIELD"]
    configFile.write("LDAP_USERNAMEFIELD = '{0}'\n".format(LDAP_USERNAMEFIELD))

    LDAP_FILTER = "" if not os.environ.get("LDAP_FILTER") else os.environ["LDAP_FILTER"]
    configFile.write("LDAP_FILTER = '{0}'\n".format(LDAP_FILTER))

# Github Oauth
GITHUB_OAUTH_ENABLE = "False" if not os.environ.get("GITHUB_OAUTH_ENABLE") else os.environ["GITHUB_OAUTH_ENABLE"]

if GITHUB_OAUTH_ENABLE != "False":
    configFile.write("GITHUB_OAUTH_ENABLE = {0}\n".format(GITHUB_OAUTH_ENABLE))
    
    GITHUB_OAUTH_KEY = "" if not os.environ.get("GITHUB_OAUTH_KEY") else os.environ["GITHUB_OAUTH_KEY"]
    configFile.write("GITHUB_OAUTH_KEY = '{0}'\n".format(GITHUB_OAUTH_KEY))

    GITHUB_OAUTH_SECRET = "" if not os.environ.get("GITHUB_OAUTH_SECRET") else os.environ["GITHUB_OAUTH_SECRET"]
    configFile.write("GITHUB_OAUTH_SECRET = '{0}'\n".format(GITHUB_OAUTH_SECRET))

    GITHUB_OAUTH_SCOPE = "" if not os.environ.get("GITHUB_OAUTH_SCOPE") else os.environ["GITHUB_OAUTH_SCOPE"]
    configFile.write("GITHUB_OAUTH_SCOPE = '{0}'\n".format(GITHUB_OAUTH_SCOPE))

    GITHUB_OAUTH_URL = "" if not os.environ.get("GITHUB_OAUTH_URL") else os.environ["GITHUB_OAUTH_URL"]
    configFile.write("GITHUB_OAUTH_URL = '{0}'\n".format(GITHUB_OAUTH_URL))

    GITHUB_OAUTH_TOKEN = "" if not os.environ.get("GITHUB_OAUTH_TOKEN") else os.environ["GITHUB_OAUTH_TOKEN"]
    configFile.write("GITHUB_OAUTH_TOKEN = '{0}'\n".format(GITHUB_OAUTH_TOKEN))

    GITHUB_OAUTH_AUTHORIZE = "" if not os.environ.get("GITHUB_OAUTH_AUTHORIZE") else os.environ[
        "GITHUB_OAUTH_AUTHORIZE"]
    configFile.write("GITHUB_OAUTH_AUTHORIZE = '{0}'\n".format(GITHUB_OAUTH_AUTHORIZE))

# Default Auth
BASIC_ENABLED = "True" if not os.environ.get("BASIC_ENABLED") else os.environ["BASIC_ENABLED"]
configFile.write("BASIC_ENABLED = {0}\n".format(BASIC_ENABLED))

SIGNUP_ENABLED = "True" if not os.environ.get("SIGNUP_ENABLED") else os.environ["SIGNUP_ENABLED"]
configFile.write("SIGNUP_ENABLED = {0}\n".format(SIGNUP_ENABLED))

# POWERDNS CONFIG
PDNS_STATS_URL = "http://127.0.0.1:8081/" if not os.environ.get("PDNS_STATS_URL") else os.environ["PDNS_STATS_URL"]
configFile.write("PDNS_STATS_URL = '{0}'\n".format(PDNS_STATS_URL))

PDNS_API_KEY = "changeme" if not os.environ.get("PDNS_API_KEY") else os.environ["PDNS_API_KEY"]
configFile.write("PDNS_API_KEY = '{0}'\n".format(PDNS_API_KEY))

PDNS_VERSION = "3.4.2" if not os.environ.get("PDNS_VERSION") else os.environ["PDNS_VERSION"]
configFile.write("PDNS_VERSION = '{0}'\n".format(PDNS_VERSION))

# RECORDS ALLOWED TO EDIT
RECORDS_ALLOW_EDIT = "'A', 'AAAA', 'CNAME', 'SPF', 'PTR', 'MX', 'TXT'" if not hasattr(os.environ,
                                                                                      "RECORDS_ALLOW_EDIT") else \
    os.environ["RECORDS_ALLOW_EDIT"]
configFile.write("RECORDS_ALLOW_EDIT = [{0}]\n".format(RECORDS_ALLOW_EDIT))

# EXPERIMENTAL FEATURES
PRETTY_IPV6_PTR = "False" if not os.environ.get("PRETTY_IPV6_PTR") else os.environ["PRETTY_IPV6_PTR"]
configFile.write("PRETTY_IPV6_PTR = {0}\n".format(PRETTY_IPV6_PTR))

configFile.close()

PIP_REQUIREMENTS = "" if not os.environ.get("PIP_REQUIREMENTS") else os.environ["PIP_REQUIREMENTS"]
if PIP_REQUIREMENTS != "":
    for req in PIP_REQUIREMENTS.split(","):
        install(req)
