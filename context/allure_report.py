import allure

class AllureReport:
    
    def allureLogs(self,text):
        with allure.step(text):
            pass