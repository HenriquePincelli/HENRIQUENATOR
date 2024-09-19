from RPA_APP.rpa.services import Service
from RPA_APP.rpa.procedures import RPAFundamentus
from RPA_APP.config import EMAIL
from robocorp.tasks import task


service_rpa = Service()


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
        # Tracing the Error
        return service_rpa.trace_error(e)
    finally:
        print("BOT-Fundamentus finished!!!")
