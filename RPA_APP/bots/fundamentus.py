from RPA_APP.rpa.procedures import RPAFundamentus
from RPA_APP.config import EMAIL
from robocorp.tasks import task
import sys
import json


@task
def bot_fundamentus():
    try:
        # >>>>>>>>>Fundamentus RPA>>>>>>>>>
        # >>>>>>>>>Parameters from robocorp storage>>>>>>>>>
        email = EMAIL
        # <<<<<<<<<Parameters from robocorp storage<<<<<<<<<

        # >>>>>>>>>RPA's Procedure>>>>>>>>>
        print("=-=" * 24)
        print("Initiating Fundamentus RPA")
        result_fundamentus = RPAFundamentus.fundamentus_extraction(email=email)
        print(">" * 45)
        print(result_fundamentus)
        print("<" * 45)
        print("=-=" * 24)
        # <<<<<<<<<RPA's Procedure<<<<<<<<<
        # <<<<<<<<<Fundamentus RPA<<<<<<<<<
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
