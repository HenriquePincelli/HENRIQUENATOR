from RPA_APP.rpa.services import Service, FundamentusService
import json
import sys


service = FundamentusService()


class FundamentusScreensService(Service):

    # >>>>>>>>>Fundamentus RPA logic>>>>>>>>>
    def rpa_fundamentus(self, payload):
        try:
            # >>>>>>>>>OPEN ALJAZEERA WEBSITE>>>>>>>>>
            bot = self.start_bot("https://www.fundamentus.com.br/buscaavancada.php")
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"]}
            # <<<<<<<<<OPEN ALJAZEERA WEBSITE<<<<<<<<<

            # >>>>>>>>>EXTRACT ALJAZEERA DATA>>>>>>>>>
            bot = self.extract_data(bot["bot"], payload)
            if not bot["status"]:
                # Kill bot
                bot["bot"]["bot"].stop_browser()
                return {"status": False, "msg": bot["msg"]}
            # <<<<<<<<<EXTRACT ALJAZEERA DATA<<<<<<<<<

            # >>>>>>>>>Close bot process and return success>>>>>>>>>
            bot["bot"].stop_browser()
            return {"status": True, "data": bot["data"]}
            # <<<<<<<<<Close bot process and return success<<<<<<<<<
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
    # <<<<<<<<<Fundamentus RPA logic<<<<<<<<<

    # >>>>>>>>>Extract newest data from "https://www.fundamentus.com.br/buscaavancada.php">>>>>>>>>
    def extract_data(self, bot, payload):
        try:
            # >>>>>>>>>Filter data to be extracted>>>>>>>>>
            bot = self.xpath_elements_click(bot=bot, father_name="input", son_name="class", son_content="buscar")
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Filter data to be extracted<<<<<<<<<

            # >>>>>>>>>Extract data>>>>>>>>>
            bot = service.extract_fundamentus_data(bot["bot"])
            if not bot["status"]:
                return {"status": False, "msg": bot["msg"], "bot": bot["bot"]}
            # <<<<<<<<<Extract data<<<<<<<<<

            return {"status": True, "bot": bot["bot"], "data": bot["data"]}
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
            return {"status": False, "msg": json.dumps(traceback_details), "bot": bot}
    # <<<<<<<<<Extract newest data from "https://www.fundamentus.com.br/buscaavancada.php"<<<<<<<<<
