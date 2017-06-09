# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class AddOnResultTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .add_on_results(sid="XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults/XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "reference_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "completed",
                "add_on_sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "add_on_configuration_sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "date_created": "Wed, 01 Sep 2010 15:15:41 +0000",
                "date_updated": "Wed, 01 Sep 2010 15:15:41 +0000",
                "date_completed": "Wed, 01 Sep 2010 15:15:41 +0000",
                "subresource_uris": {
                    "payloads": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults/XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payloads.json"
                }
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .add_on_results(sid="XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .add_on_results.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "count": 1,
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "add_on_results": [
                    {
                        "sid": "XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "reference_sid": "REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "completed",
                        "add_on_sid": "XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "add_on_configuration_sid": "XEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "date_created": "Wed, 01 Sep 2010 15:15:41 +0000",
                        "date_updated": "Wed, 01 Sep 2010 15:15:41 +0000",
                        "date_completed": "Wed, 01 Sep 2010 15:15:41 +0000",
                        "subresource_uris": {
                            "payloads": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults/XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Payloads.json"
                        }
                    }
                ],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .add_on_results.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "count": 0,
                "end": 0,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "add_on_results": [],
                "start": 0,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults.json?PageSize=50&Page=0"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .add_on_results.list()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .add_on_results(sid="XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Recordings/REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AddOnResults/XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .recordings(sid="REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .add_on_results(sid="XRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)
