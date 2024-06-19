import pytest
from GoogleSheets.ServiceStaffContactInfoConnector import ServiceStaffContactInfoConnector
from GoogleSheets.SundayServiceSermonScriptureConnector import SundayServiceSermonScriptureConnector
from GoogleSheets.SundayServiceStaffConnector import SundayServiceStaffConnector
from GoogleSheets.DateHelper import get_upcoming_sunday


def test_sunday_service_staff_connector():
    sundayServiceStaffConnector = SundayServiceStaffConnector('../Security/church-service-automation-2bbbc534b2e3.json')
    upcoming_sunday_date = get_upcoming_sunday()
    resultDto = sundayServiceStaffConnector.get_sunday_service_staff_data(upcoming_sunday_date)


def test_service_staff_contact_info_connector():
    serviceStaffContactInfoConnector = ServiceStaffContactInfoConnector('../Security/church-service-automation-2bbbc534b2e3.json')
    resultDto = serviceStaffContactInfoConnector.get_contact_info_data()


def test_sunday_service_sermon_scripture_connector():
    sundayServiceSermonScriptureConnector = SundayServiceSermonScriptureConnector('../Security/church-service-automation-2bbbc534b2e3.json')
    upcoming_sunday_date = get_upcoming_sunday()
    resultDto = sundayServiceSermonScriptureConnector.get_sermon_scripture_data(upcoming_sunday_date)


if __name__ == '__main__':
    pytest.main()
