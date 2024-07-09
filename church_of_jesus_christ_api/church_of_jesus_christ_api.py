"""
The module that implements ChurchOfJesusChristAPI. This module allows the user
to get data from churchofjesuschrist.org.
"""

# This makes JSONType show up as JSONType in the documentation instead of
# showing the aliased type
from __future__ import annotations
import datetime
import requests
from typing import List, Dict, Any, Union, Optional
import re

JSONType = Union[Dict[str, Any], List[Any]]


def _host(name: str) -> str:
    """
    Takes a subdomain of churchofjesuschrist.org and returns full path to https host

    Parameters

    name : str
        Church website subdomain name
    """

    return f"https://{name}.churchofjesuschrist.org"


_endpoints = {
    "action-and-interviews": _host("lcr")
    + "/api/umlu/report/action-interview-list/full?unitNumber={unit}",
    "assigned-missionaries": _host("lcr")
    + "/api/orgs/assigned-missionaries?unitNumber={unit}",
    "attendance": _host("lcr")
    + "/api/umlu/v1/class-and-quorum/attendance/overview/unitNumber/{unit}",
    "birthdays": _host("lcr")
    + "/api/report/birthday-list/unit/{unit}?month=1&months=12",
    "covenant-path-progress": _host("lcr")
    + "/api/report/one-work/progress-record?unitNumber={unit}",
    "family-history": _host("lcr")
    + "/api/report/family-history/activity?unitNumber={unit}",
    "full-time-missionaries": _host("lcr")
    + "/api/orgs/full-time-missionaries?unitNumber={unit}",
    "group-members": _host("lcr")
    + "/api/leader-messaging/get-group-members/{unit}/{org_id}",
    "households": _host("directory") + "/api/v4/households?unit={unit}",
    "key-indicators": _host("lcr")
    + "/api/report/key-indicator/unit/{unit}/8?extended=true&unitNumber={unit}",
    "member-callings-classes": _host("lcr")
    + "/api/records/member-profile/callings-and-classes/{member_id}",
    "member-list": _host("lcr") + "/api/umlu/report/member-list?unitNumber={unit}",
    "member-photo": _host("directory") + "/api/v4/photos/members/{uuid}",
    "member-service": _host("lcr") + "/api/records/member-profile/service/{member_id}",
    "members-with-callings": _host("lcr")
    + "/api/report/members-with-callings?unitNumber={unit}",
    "members-without-callings": _host("lcr")
    + "/api/orgs/members-without-callings?unitNumber={unit}",
    "ministering": _host("lcr")
    + "/api/umlu/v1/ministering-assignments/ministering-assignments-report?unitNumber={unit}",
    "ministering-full": _host("lcr")
    + "/api/umlu/v1/ministering/data-full?type=ALL&unitNumber={unit}",
    "moved-in": _host("lcr") + "/api/report/members-moved-in/unit/{unit}/36",
    "moved-out": _host("lcr") + "/api/report/members-moved-out/unit/{unit}/12",
    "out-of-unit-callings": _host("lcr")
    + "/api/orgs/out-of-unit-callings?unitNumber={unit}",
    "quarterly-report": _host("lcr")
    + "/api/report/quarterly-report?populateLabels=true&unitNumber={unit}",
    "quarterly-report-quarters": _host("lcr")
    + "/api/report/quarterly-report/quarters?unitNumber={unit}",
    "seminary-quarters": _host("lcr") + "/api/report/si-qr/quarters?unitNumber={unit}",
    "seminary-report": _host("lcr") + "/api/report/si-qr/summary?unitNumber={unit}",
    "statistics": _host("lcr") + "/api/report/unit-statistics?unitNumber={unit}",
    "suborganization": _host("lcr")
    + "/api/orgs/sub-orgs-with-callings?unitNumber={unit}&subOrgId={org_id}",
    "temple-recommend-status": _host("lcr")
    + "/api/temple-recommend/report?unitNumber={unit}",
    "unit-groups": _host("lcr") + "/api/leader-messaging/get-unit-groups",
    "unit-organizations": _host("lcr")
    + "/api/orgs/sub-orgs-with-callings?unitNumber={unit}",
    "units": _host("directory") + "/api/v4/units/{parent_unit}",
    "user": _host("directory") + "/api/v4/user",
}


class ChurchOfJesusChristAPI(object):
    """
    A class used to interact with features found on churchofjesuschrist.org, such
    as getting member data, calling information, reports, etc.
    """

    def __init__(
        self,
        username: str,
        password: str,
        proxies: dict[str, str] = None,
        verify_SSL: bool = None,
        timeout_sec: int = None,
    ) -> None:
        """
        Parameters:
        username : str
            username for the Church's website
        password : str
            password for the Church's website
        verify_SSL : bool
            Enables SSL verification (true by default). Useful for debugging HTTPS with a proxy
        timeout_sec : int
            Number of seconds to wait for a response when making a request
        """

        self.__session = requests.Session()
        if proxies is not None:
            self.__session.proxies.update(proxies)
        self.__session.verify = (
            verify_SSL if verify_SSL is not None else proxies is None
        )
        self.__user_details = None
        self.__org_id = None
        self.__timeout_sec = timeout_sec or 15

        html_resp = self.__session.get(
            f"{_host('www')}/services/platform/v4/login",
            timeout=self.__timeout_sec,
        ).content.decode("unicode_escape")

        # Super hacky, but it works to grab the state token out of the JSON-ish object within the script
        state_token = re.search(r"\"stateToken\":\"([^\"]+)\"", html_resp).groups()[0]
        self.__session.post(
            f"{_host('id')}/idp/idx/introspect",
            json={"stateToken": state_token},
        )
        state_handle = self.__session.post(
            f"{_host('id')}/idp/idx/identify",
            json={"identifier": username, "stateHandle": state_token},
        ).json()["stateHandle"]
        challenge_resp = self.__session.post(
            f"{_host('id')}/idp/idx/challenge/answer",
            json={"credentials": {"passcode": password}, "stateHandle": state_handle},
        ).json()
        self.__session.get(challenge_resp["success"]["href"])
        self.__access_token = self.__session.cookies.get_dict()["oauth_id_token"]
        self.__session.cookies.set("owp", self.__access_token)

        # Does lcr and directory login stuff
        self.__session.get(_host("lcr"))
        self.__session.get(_host("directory"))

        self.__user_details = self.__get_JSON(_endpoints["user"], timeout_sec)

        self.__get_default_org_id()

    def __endpoint(
        self,
        name: str,
        unit: int = None,
        org_id: int = None,
        parent_unit: int = None,
        member_id: int = None,
        uuid: str = None,
    ) -> str:
        endpoint = _endpoints[name]

        def default_if_none(val, default):
            return str(val if val is not None else default)

        if self.__user_details:
            endpoint = endpoint.replace(
                "{unit}", default_if_none(unit, self.__user_details["homeUnits"][0])
            )
            endpoint = endpoint.replace(
                "{parent_unit}",
                default_if_none(parent_unit, self.__user_details["parentUnits"][0]),
            )
            endpoint = endpoint.replace(
                "{member_id}",
                default_if_none(member_id, self.__user_details["individualId"]),
            )
            endpoint = endpoint.replace(
                "{uuid}", default_if_none(uuid, self.__user_details["uuid"])
            )
        if self.__org_id:
            endpoint = endpoint.replace(
                "{org_id}", default_if_none(org_id, self.__org_id)
            )
        return endpoint

    def __get_JPEG(self, endpoint: str, timeout_sec: int) -> Optional[bytes]:
        resp = self.__session.get(
            endpoint,
            headers={
                "Accept": "image/jpeg",
                "Authorization": f"Bearer {self.__access_token}",
            },
            timeout=timeout_sec or self.__timeout_sec,
        )
        assert resp.ok
        return None if not resp.content else resp.content

    def __get_JSON(self, endpoint: str, timeout_sec: int) -> JSONType:
        resp = self.__session.get(
            endpoint,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {self.__access_token}",
            },
            timeout=timeout_sec or self.__timeout_sec,
        )
        assert resp.ok, resp.content
        return resp.json()

    def __get_default_org_id(self):
        if self.__org_id is None:
            # Set SUNDAY_GENDER class org id
            self.__org_id = next(
                assignment
                for assignment in self.get_member_callings_and_classes()[
                    "classAssignments"
                ]
                if assignment["group"] == "SUNDAY_GENDER"
            )["classId"]

    @property
    def session(self):
        """
        Returns the requests session being used by the API.
        """
        return self.__session

    @property
    def user_details(self):
        """
        Returns the details of the user logged into this session

        Returns

        .. literalinclude:: ../JSON_schemas/user_details-schema.md
        """
        return self.__user_details

    @property
    def org_id(self):
        return self.__org_id

    def convert_date_to_string_using_default_date_if_none(self, val, default):
        return (val if val != None else default).strftime("%Y-%m-%d")

    def get_action_and_interviews(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit action and interview list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_action_and_interviews-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("action-and-interviews", unit=unit), timeout_sec
        )

    def get_attendance(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the attendance list for the last 5 weeks

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_attendance-schema.md
        """

        return self.__get_JSON(self.__endpoint("attendance", unit=unit), timeout_sec)

    def get_attendance_date_range(
        self,
        start_date: datetime.date = None,
        end_date: datetime.date = None,
        unit: int = None,
        timeout_sec: int = None,
    ) -> JSONType:
        """
        Returns the attendance list for a given date range (default 1 year ago to today)

        Parameters

        start_date: datetime.date
            The start date after which attendance will be retrieved
        end_date: datetime.date
            The end date after which attendance will no longer be retrieved
        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_attendance_date_range-schema.md
        """

        start_date = self.convert_date_to_string_using_default_date_if_none(
            start_date, datetime.datetime.now() - datetime.timedelta(days=365)
        )
        end_date = self.convert_date_to_string_using_default_date_if_none(
            end_date, datetime.date.today()
        )

        return self.__get_JSON(
            self.__endpoint("attendance", unit=unit)
            + f"/start/{start_date}/end/{end_date}",
            timeout_sec,
        )

    def get_birthdays(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit birthday list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_birthdays-schema.md
        """

        return self.__get_JSON(self.__endpoint("birthdays", unit=unit), timeout_sec)

    def get_directory(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit directory of households

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_directory-schema.md
        """

        return self.__get_JSON(self.__endpoint("households", unit=unit), timeout_sec)

    def get_units(self, parent_unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns a list of child units for the given parent unit

        Parameters

        parent_unit : int
            Number of the church unit for which to retrieve a list of child units
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_units-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("units", parent_unit=parent_unit), timeout_sec
        )

    def get_family_history_report(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit family history report

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_family_history_report-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("family-history", unit=unit), timeout_sec
        )

    def get_key_indicators(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit key indicators

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_key_indicators-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("key-indicators", unit=unit), timeout_sec
        )

    def get_member_callings_and_classes(
        self, member_id: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the callings and class assignments for the given member

        Parameters

        member_id : int
            ID of the member for which to retrieve information
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_callings_and_classes-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("member-callings-classes", member_id=member_id), timeout_sec
        )

    def get_member_list(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit member list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_list-schema.md
        """

        return self.__get_JSON(self.__endpoint("member-list", unit=unit), timeout_sec)

    def download_member_photo(
        self, uuid: str = None, timeout_sec: int = None
    ) -> Optional[bytes]:
        """
        Returns the raw bytes for a member's photo in JPEG format

        Parameters

        uuid: str
            The given member's uuid
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        The raw bytes for the member's photo, if available. None if no photo is available,
        throws an exception if an error occurs
        """

        return self.__get_JPEG(self.__endpoint("member-photo", uuid=uuid), timeout_sec)

    def get_member_service(
        self, member_id: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns member's service assignments

        Parameters

        member_id : int
            ID of the member for which to retrieve information
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_service-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("member-service", member_id=member_id), timeout_sec
        )

    def get_members_with_callings(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit list of members with callings

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_members_with_callings-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("members-with-callings", unit=unit), timeout_sec
        )

    def get_members_without_callings(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit list of members without callings

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_members_without_callings-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("members-without-callings", unit=unit), timeout_sec
        )

    def get_ministering(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit ministering assignments

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_ministering-schema.md
        """

        return self.__get_JSON(self.__endpoint("ministering", unit=unit), timeout_sec)

    def get_ministering_full(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit ministering assignments as well as interview information

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_ministering_full-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("ministering-full", unit=unit), timeout_sec
        )

    def get_covenant_path_progress(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit covenant path progress record. Includes information about new members
        and non-members being taught by the missionaries

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_covenant_path_progress-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("covenant-path-progress", unit=unit), timeout_sec
        )

    def get_moved_in(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit list of recently moved in members

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_moved_in-schema.md
        """

        return self.__get_JSON(self.__endpoint("moved-in", unit=unit), timeout_sec)

    def get_moved_out(self, unit: int = None, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit list of recently moved out members

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_moved_out-schema.md
        """

        return self.__get_JSON(self.__endpoint("moved-out", unit=unit), timeout_sec)

    def get_out_of_unit_callings(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit list of members with callings out of unit

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_out_of_unit_callings-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("out-of-unit-callings", unit=unit), timeout_sec
        )

    def get_quarterly_reports(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns all available unit quarterly reports

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_quarterly_reports-schema.md
        """

        def get_quarters():
            return [
                quarter.split("-")
                for quarter in self.__get_JSON(
                    self.__endpoint("quarterly-report-quarters", unit=unit), timeout_sec
                )
            ]

        def get_report(year, quarter):
            return self.__get_JSON(
                self.__endpoint("quarterly-report", unit=unit)
                + f"&year={year}&quarter={quarter}",
                timeout_sec,
            )

        return {
            year: {quarter: get_report(year, quarter)}
            for year, quarter in get_quarters()
        }

    def get_seminary_and_institute_quarterly_attendance(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns all availabe seminary/institute quarterly attendance reports

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_seminary_and_institute_quarterly_attendance-schema.md
        """

        def get_quarters():
            return [
                quarter.split("-")
                for quarter in self.__get_JSON(
                    self.__endpoint("seminary-quarters", unit=unit), timeout_sec
                )
            ]

        def get_report(year, quarter):
            return self.__get_JSON(
                self.__endpoint("seminary-report", unit=unit)
                + f"&year={year}&quarter={quarter}",
                timeout_sec,
            )

        return {
            year: {quarter: get_report(year, quarter)}
            for year, quarter in get_quarters()
        }

    def get_temple_recommend_status(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the temple recommend status

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_temple_recommend_status-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("temple-recommend-status", unit=unit), timeout_sec
        )

    def get_unit_organizations(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit calling/leadership organization structure

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_unit_organizations-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("unit-organizations", unit=unit), timeout_sec
        )

    def get_suborganization(
        self, org_id: int = None, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns information for a given suborganization of a unit

        Parameters
        org_id : int
            Number of the suborganization of the unit for which to retrieve the report. Defaults
            to the class assignment for gendered class (Elders' Quorum, Relief Society, etc.).
        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_suborganization-schema.md
        """
        return self.__get_JSON(
            self.__endpoint("suborganization", org_id=org_id, unit=unit), timeout_sec
        )[0]

    def get_full_time_missionaries(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns a list of the members from the unit currently serving missions

        Parameters
        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_full_time_missionaries-schema.md
        """
        return self.__get_JSON(
            self.__endpoint("full-time-missionaries", unit=unit), timeout_sec
        )

    def get_assigned_missionaries(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns a list of the missionaries currently assigned to serve in the unit

        Parameters
        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_assigned_missionaries-schema.md
        """
        return self.__get_JSON(
            self.__endpoint("assigned-missionaries", unit=unit), timeout_sec
        )

    def get_unit_statistics(
        self, unit: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the unit statistics

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_unit_statistics-schema.md
        """

        return self.__get_JSON(self.__endpoint("statistics", unit=unit), timeout_sec)

    def get_unit_groups(self, timeout_sec: int = None) -> JSONType:
        """
        Returns the unit groups, as used by the email/message application

        Parameters

        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_unit_groups-schema.md
        """

        return self.__get_JSON(self.__endpoint("unit-groups"), timeout_sec)

    def get_group_members(
        self, unit: int = None, org_id: int = None, timeout_sec: int = None
    ) -> JSONType:
        """
        Returns the members of a given group, as used by the LCR
        message/email application

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report
        org_id : int
            Number of the suborganization of the unit for which to retrieve
            the members list.
        timeout_sec : int
            Number of seconds to wait for a response when making a request

        Returns

        .. literalinclude:: ../JSON_schemas/get_group_members-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("group-members", unit=unit, org_id=org_id), timeout_sec
        )
