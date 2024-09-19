from RPA_APP.rpa.services import Service
from RPA_APP.rpa.procedures import RPAAljazeera
from RPA_APP.config import EMAIL, ALJAZEERA_SEARCH_PHRASE, ALJAZEERA_SHOW_MORE
from robocorp.tasks import task


service_rpa = Service()


@task
def bot_aljazeera():
    try:
        # >>>>>>>>>Aljazeera's RPA>>>>>>>>>
        # >>>>>>>>>Parameters from robocorp storage>>>>>>>>>
        email = EMAIL
        search_phrase = ALJAZEERA_SEARCH_PHRASE
        show_more = ALJAZEERA_SHOW_MORE
        # <<<<<<<<<Parameters from robocorp storage<<<<<<<<<

        # >>>>>>>>>RPA's Procedure>>>>>>>>>
        print("=-=" * 24)
        print("Initiating Aljazeera's RPA")
        result_aljazeera = RPAAljazeera.aljazeera_news(email=email, search_phrase=search_phrase, show_more=show_more)
        print(">" * 45)
        print(result_aljazeera)
        print("<" * 45)
        print("=-=" * 24)
        # <<<<<<<<<RPA's Procedure<<<<<<<<<
        # <<<<<<<<<Aljazeera's RPA<<<<<<<<<
    except Exception as e:
        # Tracing the Error
        return service_rpa.trace_error(e)
    finally:
        print("BOT-Aljazeera finished!!!")
