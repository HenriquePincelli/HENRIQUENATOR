from RPA_APP.rpa.procedures import RPAAljazeera
from RPA_APP.config import EMAIL, ALJAZEERA_SEARCH_PHRASE, ALJAZEERA_SHOW_MORE
from robocorp.tasks import task
import sys
import json


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
            # >>>>>>>>>Tracing the Error>>>>>>>>>
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback_details = {
                'filename': exc_traceback.tb_frame.f_code.co_filename,
                'line_number': exc_traceback.tb_lineno,
                'function_name': exc_traceback.tb_frame.f_code.co_name,
                'exception_type': exc_type.__name__,
                'exception_message': str(exc_value)
            }
            print("=-==-==-=ERROR=-==-==-=")
            print(traceback_details)
            print("=-==-==-=ERROR=-==-==-=")
            # <<<<<<<<<Tracing the Error<<<<<<<<<
            print({"status": False, "msg": json.dumps(traceback_details)})
    finally:
        print("BOT-Aljazeera finished!!!")
