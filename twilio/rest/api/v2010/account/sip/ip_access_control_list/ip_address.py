# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio import deserialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page


class IpAddressList(ListResource):

    def __init__(self, version, account_sid, ip_access_control_list_sid):
        """
        Initialize the IpAddressList

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param ip_access_control_list_sid: The ip_access_control_list_sid

        :returns: IpAddressList
        :rtype: IpAddressList
        """
        super(IpAddressList, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses.json'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams IpAddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists IpAddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of IpAddressInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of IpAddressInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return IpAddressPage(self._version, response, self._solution)

    def create(self, friendly_name, ip_address):
        """
        Create a new IpAddressInstance

        :param unicode friendly_name: The friendly_name
        :param unicode ip_address: The ip_address

        :returns: Newly created IpAddressInstance
        :rtype: IpAddressInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'IpAddress': ip_address,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
        )

    def get(self, sid):
        """
        Constructs a IpAddressContext

        :param sid: The sid

        :returns: IpAddressContext
        :rtype: IpAddressContext
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a IpAddressContext

        :param sid: The sid

        :returns: IpAddressContext
        :rtype: IpAddressContext
        """
        return IpAddressContext(
            self._version,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressList>'


class IpAddressPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the IpAddressPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The account_sid
        :param ip_access_control_list_sid: The ip_access_control_list_sid

        :returns: IpAddressPage
        :rtype: IpAddressPage
        """
        super(IpAddressPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of IpAddressInstance

        :param dict payload: Payload response from the API

        :returns: IpAddressInstance
        :rtype: IpAddressInstance
        """
        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.IpAddressPage>'


class IpAddressContext(InstanceContext):

    def __init__(self, version, account_sid, ip_access_control_list_sid, sid):
        """
        Initialize the IpAddressContext

        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param ip_access_control_list_sid: The ip_access_control_list_sid
        :param sid: The sid

        :returns: IpAddressContext
        :rtype: IpAddressContext
        """
        super(IpAddressContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/SIP/IpAccessControlLists/{ip_access_control_list_sid}/IpAddresses/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a IpAddressInstance

        :returns: Fetched IpAddressInstance
        :rtype: IpAddressInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid'],
        )

    def update(self, ip_address=values.unset, friendly_name=values.unset):
        """
        Update the IpAddressInstance

        :param unicode ip_address: The ip_address
        :param unicode friendly_name: The friendly_name

        :returns: Updated IpAddressInstance
        :rtype: IpAddressInstance
        """
        data = values.of({
            'IpAddress': ip_address,
            'FriendlyName': friendly_name,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return IpAddressInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressContext {}>'.format(context)


class IpAddressInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, ip_access_control_list_sid,
                 sid=None):
        """
        Initialize the IpAddressInstance

        :returns: IpAddressInstance
        :rtype: IpAddressInstance
        """
        super(IpAddressInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'ip_address': payload['ip_address'],
            'ip_access_control_list_sid': payload['ip_access_control_list_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {
            'account_sid': account_sid,
            'ip_access_control_list_sid': ip_access_control_list_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: IpAddressContext for this IpAddressInstance
        :rtype: IpAddressContext
        """
        if self._context is None:
            self._context = IpAddressContext(
                self._version,
                account_sid=self._solution['account_sid'],
                ip_access_control_list_sid=self._solution['ip_access_control_list_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: The friendly_name
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def ip_address(self):
        """
        :returns: The ip_address
        :rtype: unicode
        """
        return self._properties['ip_address']

    @property
    def ip_access_control_list_sid(self):
        """
        :returns: The ip_access_control_list_sid
        :rtype: unicode
        """
        return self._properties['ip_access_control_list_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def uri(self):
        """
        :returns: The uri
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a IpAddressInstance

        :returns: Fetched IpAddressInstance
        :rtype: IpAddressInstance
        """
        return self._proxy.fetch()

    def update(self, ip_address=values.unset, friendly_name=values.unset):
        """
        Update the IpAddressInstance

        :param unicode ip_address: The ip_address
        :param unicode friendly_name: The friendly_name

        :returns: Updated IpAddressInstance
        :rtype: IpAddressInstance
        """
        return self._proxy.update(
            ip_address=ip_address,
            friendly_name=friendly_name,
        )

    def delete(self):
        """
        Deletes the IpAddressInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.IpAddressInstance {}>'.format(context)
