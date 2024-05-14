# Press the green button in the gutter to run the script.
import Service
from GoogleSheets.DateHelper import get_upcoming_sunday

if __name__ == '__main__':

    serviceAndStaffService = Service.SundayServiceStaffAndContactGoogleSheets('../Security/church-service-automation-2bbbc534b2e3.json', 'https://docs.google.com/spreadsheets/d/1mF3DKEHQXaNPNYvc4_oqOtTL7xCw-TpwQaCTNYO5NA0/edit?usp=sharing')
    upcoming_sunday_date = get_upcoming_sunday()
    result = serviceAndStaffService.get_sunday_service_staff_data(upcoming_sunday_date)
