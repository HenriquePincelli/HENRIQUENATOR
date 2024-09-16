"""DEFAULT VARIABLES"""
from robocorp import vault, storage


secrets = vault.get_secret("HENRIQUENATOR")
locators = storage.get_json("HENRIQUENATOR EXTRACTION")


# EMAIL to send RPA's results
EMAIL = locators["email"]

# >>>>>>>>>EMAIL CONFIGS>>>>>>>>>
SMTP_HOST = secrets["smtp_host"]
SMTP_PORT = secrets["smtp_port"]
SMTP_USER = secrets["smtp_user"]
SMTP_PASSWORD = secrets["smtp_password"]
# <<<<<<<<<EMAIL CONFIGS<<<<<<<<<

# >>>>>>>>>ALJAZEERA'S RPA CONFIGS>>>>>>>>>
ALJAZEERA_SEARCH_PHRASE = locators["aljazeera_search_phrase"]
ALJAZEERA_SHOW_MORE = locators["aljazeera_show_more"]
# <<<<<<<<<ALJAZEERA'S RPA CONFIGS<<<<<<<<<
