import mock
import pytest
import requests

from bitcoin.source.btc import Bitcoin


class TestBitcoin:
    @mock.patch("bitcoin.source.btc.requests.get")
    def test_get_btc_current_price_success(self, mocked_requests_get):
        mocked_response = mock.MagicMock(
            name="btc_api",
            **{"status_code": 200,
               "json.return_value": {
                   "bpi": {
                       "USD": {
                           "rate_float": 60000
                       }
                   }
               }
               }
        )
        mocked_requests_get.return_value = mocked_response

        assert Bitcoin.get_btc_current_price(self) == 60000
        mocked_requests_get.assert_called_once()

    @mock.patch("bitcoin.source.btc.requests.get")
    def test_get_btc_current_price_exception(self, mocked_requests_get):
        failed_response = mock.MagicMock(requests.Response)
        failed_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        mocked_requests_get.return_value = failed_response

        with pytest.raises(requests.exceptions.HTTPError) as err:
            Bitcoin.get_btc_current_price(self)
