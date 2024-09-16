from RPA_APP.rpa.screens import Screens, FundamentusScreensService
from RPA_APP.rpa.services import FundamentusService
import json
import sys


# >>>>>>>>>INITIALIZE SERVICES>>>>>>>>>
service = Screens()
service_screen = FundamentusScreensService()
service_fundamentus = FundamentusService()
# <<<<<<<<<INITIALIZE SERVICES<<<<<<<<<

# >>>>>>>>>Destiny directory for news images>>>>>>>>>
directory = "output/"
excel_filename = "fundamentus.xlsx"
# <<<<<<<<<Destiny directory for news images<<<<<<<<<


class RPAFundamentus:

    def fundamentus_extraction(email):
        try:
            # >>>>>>>>>RPA Payload>>>>>>>>>
            payload = {
                "email": email
            }
            # <<<<<<<<<RPA Payload<<<<<<<<<

            # >>>>>>>>>Start RPA process>>>>>>>>>
            print("Starting RPA process.........")
            return_rpa = service_screen.rpa_fundamentus(payload)
            if not return_rpa["status"]:
                return {"status": False, "msg": return_rpa["msg"]}
            # <<<<<<<<<Start RPA process<<<<<<<<<

            # >>>>>>>>>Save Fundamentus data in 'output/fundamentus.xlsx'>>>>>>>>>
            print("Saving Aljazeera data in 'output/fundamentus.xlsx'.........")
            print(return_rpa["data"])
            return_excel = service_fundamentus.make_fundamentus_excel_file(return_rpa["data"], directory, excel_filename)
            if not return_excel["status"]:
                return {"status": False, "msg": return_excel["msg"]}
            # <<<<<<<<<Save Fundamentus data in 'output/fundamentus.xlsx'<<<<<<<<<

            # >>>>>>>>>Send excel file by email>>>>>>>>>
            if payload["email"] is not None:
                print("Sending excel file by email.........")
                return_email = service.send_excel_email(payload["email"], "Fundamentus Excel", directory, excel_filename)
                if not return_email["status"]:
                    return {"status": False, "msg": return_email["msg"]}
                return {"status": True, "msg": f"News extracted and sent to email: {payload['email']}"}
            # <<<<<<<<<Send excel file by email<<<<<<<<<

            return {"status": True, "msg": f"Data extracted and sent to email."}
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
            return {"status": False, "msg": json.dumps(traceback_details)}
