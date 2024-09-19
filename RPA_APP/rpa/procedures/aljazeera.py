from RPA_APP.rpa.services import Service
from RPA_APP.rpa.screens import Screens, AljazeeraScreensService


# >>>>>>>>>INITIALIZE SERVICES>>>>>>>>>
service_rpa = Service()
service = Screens()
service_screen = AljazeeraScreensService()
#  <<<<<<<<<INITIALIZE SERVICES<<<<<<<<<

# >>>>>>>>>Destiny directory for news images>>>>>>>>>
directory = "output/"
excel_filename = "aljazeera_news.xlsx"
# <<<<<<<<<Destiny directory for news images<<<<<<<<<


class RPAAljazeera:

    def aljazeera_news(email, search_phrase, show_more):
        try:
            # >>>>>>>>>RPA Payload>>>>>>>>>
            payload = {
                "email": email,
                "search_phrase": search_phrase,
                "show_more": show_more
            }
            # <<<<<<<<<RPA Payload<<<<<<<<<

            # >>>>>>>>>Start RPA process>>>>>>>>>
            print("Starting RPA process.........")
            return_rpa = service_screen.rpa_aljazeera(payload)
            if not return_rpa["status"]:
                return {"status": False, "msg": return_rpa["msg"]}
            # <<<<<<<<<Start RPA process<<<<<<<<<

            # >>>>>>>>>Save Aljazeera data in 'output/aljazeera_news.xlsx'>>>>>>>>>
            print("Saving Aljazeera data in 'output/aljazeera_news.xlsx'.........")
            return_excel = service.make_excel_file(payload, return_rpa["data"], directory, excel_filename)
            if not return_excel["status"]:
                return {"status": False, "msg": return_excel["msg"]}
            # <<<<<<<<<Save Aljazeera data in 'output/aljazeera_news.xlsx'<<<<<<<<<

            # >>>>>>>>>Send excel file by email>>>>>>>>>
            if payload["email"] is not None:
                print("Sending excel file by email.........")
                return_email = service.send_excel_email(payload["email"], "Aljazeera Excel", directory, excel_filename)
                if not return_email["status"]:
                    return {"status": False, "msg": return_email["msg"]}
                return {"status": True, "msg": f"News extracted and sent to email: {payload['email']}"}
            # <<<<<<<<<Send excel file by email<<<<<<<<<

            return {"status": True, "msg": f"News extracted and sent to email."}
        except Exception as e:
            # Tracing the Error
            return service_rpa.trace_error(e)
