import mock_demo
from mock import Mock, patch


@patch('mock_demo.requests')  # patch as decorator
def test_get_holidays(mock_requests):
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independence Day',
    }

    mock_requests.get.return_value = response_mock

    assert mock_demo.get_holidays()['12/25'] == 'Christmas'


def test_get_holidays_02():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = {
        '12/25': 'Christmas',
        '7/4': 'Independence Day',
    }

    # patch as context manager
    with patch('mock_demo.requests') as mock_requests:
        mock_requests.get.return_value = response_mock

        assert mock_demo.get_holidays()['7/4'] == 'Independence Day'
