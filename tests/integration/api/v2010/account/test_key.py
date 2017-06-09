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


class KeyTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys/SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "foo",
                "date_created": "Mon, 13 Jun 2016 22:50:08 +0000",
                "date_updated": "Mon, 13 Jun 2016 22:50:08 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys/SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "friendly_name": "foo",
                "date_created": "Mon, 13 Jun 2016 22:50:08 +0000",
                "date_updated": "Mon, 13 Jun 2016 22:50:08 +0000"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys/SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.json',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .keys(sid="SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").delete()

        self.assertTrue(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .keys.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "keys": [
                    {
                        "sid": "SKaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "friendly_name": "foo",
                        "date_created": "Mon, 13 Jun 2016 22:50:08 +0000",
                        "date_updated": "Mon, 13 Jun 2016 22:50:08 +0000"
                    }
                ],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys.json?PageSize=50&Page=0",
                "end": 3,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys.json?PageSize=50&Page=0",
                "page_size": 50,
                "start": 0,
                "next_page_uri": null,
                "page": 0,
                "count": 1
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .keys.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "keys": [],
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys.json?PageSize=50&Page=0",
                "end": 3,
                "previous_page_uri": null,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Keys.json?PageSize=50&Page=0",
                "page_size": 50,
                "start": 0,
                "next_page_uri": null,
                "page": 0,
                "count": 0
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .keys.list()

        self.assertIsNotNone(actual)
