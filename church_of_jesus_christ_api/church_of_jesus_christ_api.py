"""
The module that implements ChurchOfJesusChristAPI. This module allows the user
to get data from churchofjesuschrist.org.
"""
# This makes JSONType show up as JSONType in the documentation instead of
# showing the aliased type
from __future__ import annotations
import typing
import uuid
from urllib.parse import urlparse, parse_qs
import codecs

typing.get_type_hints = lambda obj, *unused: obj

import datetime
import json
import requests
from typing import List, Dict, Any, Union

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
    + "/services/v2/report/action-interview-list/full?unitNumber={unit}",
    "assigned-missionaries": _host("lcr")
    + "/services/orgs/assigned-missionaries?unitNumber={unit}",
    "attendance": _host("lcr")
    + "/services/umlu/v1/class-and-quorum/attendance/overview/unitNumber/{unit}",
    "authn": _host("id") + "/api/v1/authn",
    "birthdays": _host("lcr")
    + "/services/report/birthday-list/unit/{unit}?month=1&months=12",
    "family-history": _host("lcr")
    + "/services/report/family-history/activity?unitNumber={unit}",
    "full-time-missionaries": _host("lcr")
    + "/services/orgs/full-time-missionaries?unitNumber={unit}",
    "households" : _host("directory")
    + "/api/v4/households?unit={unit}",
    "key-indicators": _host("lcr")
    + "/services/report/key-indicator/unit/{unit}/8?extended=true&unitNumber={unit}",
    "lcr-login": _host("lcr") + "/api/auth/login",
    "member-callings-classes": _host("lcr")
    + "/api/records/member-profile/callings-and-classes/{member_id}",
    "member-list": _host("lcr") + "/services/umlu/report/member-list?unitNumber={unit}",
    "member-service": _host("lcr") + "/api/records/member-profile/service/{member_id}",
    "members-with-callings": _host("lcr")
    + "/services/report/members-with-callings?unitNumber={unit}",
    "members-without-callings": _host("lcr")
    + "/services/orgs/members-without-callings?unitNumber={unit}",
    "ministering": _host("lcr")
    + "/services/umlu/v1/ministering-assignments/ministering-assignments-report?unitNumber={unit}",
    "ministering-full": _host("lcr")
    + "/services/umlu/v1/ministering/data-full?unitNumber={unit}",
    "missionary-progress-record": _host("lcr")
    + "/services/report/progress-record/{unit}/teaching-pool",
    "missionary-indicators": _host("lcr")
    + "/services/report/progress-record/{unit}/key-indicators",
    "mobile-sync": _host("membertools-api")
    + "/api/v4/sync?units={unit}&force=true",
    "moved-in": _host("lcr") + "/services/report/members-moved-in/unit/{unit}/36",
    "moved-out": _host("lcr") + "/services/report/members-moved-out/unit/{unit}/12",
    "new-member": _host("lcr") + "/services/report/new-member/unit/{unit}/12",
    "oauth2-authorize": _host("id") + "/oauth2/default/v1/authorize",
    "oauth2-token": _host("id") + "/oauth2/default/v1/token",
    "out-of-unit-callings": _host("lcr")
    + "/services/orgs/out-of-unit-callings?unitNumber={unit}",
    "quarterly-report": _host("lcr")
    + "/services/report/quarterly-report?populateLabels=true&unitNumber={unit}",
    "quarterly-report-quarters": _host("lcr")
    + "/services/report/quarterly-report/quarters?unitNumber={unit}",
    "seminary-quarters": _host("lcr")
    + "/services/report/si-qr/quarters?unitNumber={unit}",
    "seminary-report": _host("lcr")
    + "/services/report/si-qr/summary?unitNumber={unit}",
    "statistics": _host("lcr") + "/services/report/unit-statistics?unitNumber={unit}",
    "suborganization": _host("lcr")
    + "/services/orgs/sub-orgs-with-callings?unitNumber={unit}&subOrgId={org_id}",
    "unit-organizations": _host("lcr")
    + "/services/orgs/sub-orgs-with-callings?unitNumber={unit}",
    "units": _host("directory")
    + "/api/v4/units/{parent_unit}",
    "user": _host("directory") + "/api/v4/user",
}


class ChurchOfJesusChristAPI(object):
    """
    A class used to interact with features found on churchofjesuschrist.org, such
    as getting member data, calling information, reports, etc.
    """

    def __init__(self, username: str, password: str, proxies: dict[str, str] = None, verify_SSL: bool = None) -> None:
        """
        Parameters:
        username : str
            username for the Church's website
        password : str
            password for the Church's website
        debug_mode : bool
            Disables SSL verification. Useful for debugging HTTPS with a proxy
        """

        self.__session = requests.Session()
        if proxies is not None:
            self.__session.proxies.update(proxies)
        self.__session.verify = verify_SSL if verify_SSL is not None else proxies is None
        self.__user_details = None
        self.__org_id = None

        login_resp = self.__session.post(
            _endpoints["authn"],
            timeout=15,
            headers={"Content-Type": "application/json;charset=UTF-8"},
            data=json.dumps({"username":username, "password": password})
        ).json()

        # Slighly obfuscated, by no means hidden
        client_id = codecs.decode("0bnyu46hlyC0T9DL1357", "rot13")
        client_secret = codecs.decode("9n4ShhBgxm17hz4B8HVT3rSV4hJvnzXH1bjHkMPR", "rot13")

        resp = self.__session.get(
            _endpoints["oauth2-authorize"],
            timeout=15,
            params={"client_id":client_id,
                    "response_type":"code",
                    "scope":"openid profile offline_access cmisid",
                    "redirect_uri": "https://mobileandroid",
                    "state":str(uuid.uuid4()),
                    "sessionToken":login_resp["sessionToken"],
            },
            allow_redirects=False
        )

        code = parse_qs(urlparse(resp.headers["location"]).query)["code"][0]

        token_json = self.__session.post(
            _endpoints["oauth2-token"],
            timeout=15,
            headers={"Content-Type":"application/x-www-form-urlencoded"},
            params={"code":code,
                    "client_id":client_id,
                    "client_secret":client_secret,
                    "grant_type": "authorization_code",
                    "redirect_uri": "https://mobileandroid",
            }
        ).json()

        self.__access_token = token_json["access_token"]

        # Some endpoints require this
        self.__session.cookies.set_cookie(
            requests.cookies.create_cookie(
                name="owp", value=token_json["id_token"]
            ))

        # This is necessary to set appSession cookies for a few endpoints
        self.__session.get(_endpoints["lcr-login"], timeout=15)
        
        self.__user_details = self.__get_JSON(self.__endpoint("user"))

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
            return str(val if val != None else default)

        if self.__user_details:
            endpoint = endpoint.replace(
                "{unit}", default_if_none(unit, self.__user_details["homeUnits"][0])
            )
            endpoint = endpoint.replace(
                "{parent_unit}", default_if_none(parent_unit, self.__user_details["parentUnits"][0])
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

    def __get_JSON(self, endpoint: str) -> JSONType:
        resp = self.__session.get(
            endpoint,
            headers={"Accept": "application/json",
                     "Authorization":f"Bearer {self.__access_token}"},
            timeout=15
        )
        assert resp.ok, resp.content
        return resp.json()

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

    def get_action_and_interviews(self, unit: int = None) -> JSONType:
        """
        Returns the unit action and interview list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_action_and_interviews-schema.md
        """

        return self.__get_JSON(self.__endpoint("action-and-interviews", unit=unit))

    def get_attendance(self, unit: int = None) -> JSONType:
        """
        Returns the attendance list for the last 5 weeks

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_attendance-schema.md
        """

        return self.__get_JSON(self.__endpoint("attendance", unit=unit))

    def get_attendance_date_range(
        self,
        start_date: datetime.date = None,
        end_date: datetime.date = None,
        unit: int = None,
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
            + f"/start/{start_date}/end/{end_date}"
        )

    def get_birthdays(self, unit: int = None) -> JSONType:
        """
        Returns the unit birthday list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_birthdays-schema.md
        """

        return self.__get_JSON(self.__endpoint("birthdays", unit=unit))
    
    def get_mobile_sync_data(self, unit: int = None) -> JSONType:
        """
        Returns data that can be found in the Member Tools app. This is the endpoint
        used by the app when an update is requested.

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_mobile_sync_data-schema.md
        """

        return self.__get_JSON(self.__endpoint("mobile-sync", unit=unit))

    def get_directory(self, unit: int = None) -> JSONType:
        """
        Returns the unit directory of households

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_directory-schema.md
        """

        return self.__get_JSON(self.__endpoint("households", unit=unit))
    
    def get_units(self, parent_unit: int = None) -> JSONType:
        """
        Returns a list of child units for the given parent unit

        Parameters

        parent_unit : int
            Number of the church unit for which to retrieve a list of child units

        Returns

        .. literalinclude:: ../JSON_schemas/get_units-schema.md
        """

        return self.__get_JSON(self.__endpoint("units", parent_unit=parent_unit))

    def get_family_history_report(self, unit: int = None) -> JSONType:
        """
        Returns the unit family history report

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_family_history_report-schema.md
        """

        return self.__get_JSON(self.__endpoint("family-history", unit=unit))

    def get_key_indicators(self, unit: int = None) -> JSONType:
        """
        Returns the unit key indicators

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_key_indicators-schema.md
        """

        return self.__get_JSON(self.__endpoint("key-indicators", unit=unit))

    def get_member_callings_and_classes(self, member_id: int = None) -> JSONType:
        """
        Returns the callings and class assignments for the given member

        Parameters

        member_id : int
            ID of the member for which to retrieve information

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_callings_and_classes-schema.md
        """

        return self.__get_JSON(
            self.__endpoint("member-callings-classes", member_id=member_id)
        )

    def get_member_list(self, unit: int = None) -> JSONType:
        """
        Returns the unit member list

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_list-schema.md
        """

        return self.__get_JSON(self.__endpoint("member-list", unit=unit))

    def get_member_service(self, member_id: int = None) -> JSONType:
        """
        Returns member's service assignments

        Parameters

        member_id : int
            ID of the member for which to retrieve information

        Returns

        .. literalinclude:: ../JSON_schemas/get_member_service-schema.md
        """

        return self.__get_JSON(self.__endpoint("member-service", member_id=member_id))

    def get_members_with_callings(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of members with callings

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_members_with_callings-schema.md
        """

        return self.__get_JSON(self.__endpoint("members-with-callings", unit=unit))

    def get_members_without_callings(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of members without callings

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_members_without_callings-schema.md
        """

        return self.__get_JSON(self.__endpoint("members-without-callings", unit=unit))

    def get_ministering(self, unit: int = None) -> JSONType:
        """
        Returns the unit ministering assignments

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_ministering-schema.md
        """

        return self.__get_JSON(self.__endpoint("ministering", unit=unit))

    def get_ministering_full(self, unit: int = None) -> JSONType:
        """
        Returns the unit ministering assignments as well as interview information

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_ministering_full-schema.md
        """

        return self.__get_JSON(self.__endpoint("ministering-full", unit=unit))

    def get_missionary_indicators(self, unit: int = None) -> JSONType:
        """
        Returns the unit missionary indicators

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_missionary_indicators-schema.md
        """

        return self.__get_JSON(self.__endpoint("missionary-indicators", unit=unit))

    def get_missionary_progress_record(self, unit: int = None) -> JSONType:
        """
        Returns the unit missionary progress record

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_missionary_progress_record-schema.md
        """

        return self.__get_JSON(self.__endpoint("missionary-progress-record", unit=unit))

    def get_moved_in(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of recently moved in members

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_moved_in-schema.md
        """

        return self.__get_JSON(self.__endpoint("moved-in", unit=unit))

    def get_moved_out(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of recently moved out members

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_moved_out-schema.md
        """

        return self.__get_JSON(self.__endpoint("moved-out", unit=unit))

    def get_new_members(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of new members (recent converts)

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_new_members-schema.md
        """

        return self.__get_JSON(self.__endpoint("new-member", unit=unit))

    def get_out_of_unit_callings(self, unit: int = None) -> JSONType:
        """
        Returns the unit list of members with callings out of unit

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_out_of_unit_callings-schema.md
        """

        return self.__get_JSON(self.__endpoint("out-of-unit-callings", unit=unit))

    def get_quarterly_reports(self, unit: int = None) -> JSONType:
        """
        Returns all available unit quarterly reports

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_quarterly_reports-schema.md
        """

        def get_quarters():
            return [
                quarter.split("-")
                for quarter in self.__get_JSON(
                    self.__endpoint("quarterly-report-quarters", unit=unit)
                )
            ]

        def get_report(year, quarter):
            return self.__get_JSON(
                self.__endpoint("quarterly-report", unit=unit)
                + f"&year={year}&quarter={quarter}"
            )

        return {
            year: {quarter: get_report(year, quarter)}
            for year, quarter in get_quarters()
        }

    def get_seminary_and_institute_quarterly_attendance(
        self, unit: int = None
    ) -> JSONType:
        """
        Returns all availabe seminary/institute quarterly attendance reports

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_seminary_and_institute_quarterly_attendance-schema.md
        """

        def get_quarters():
            return [
                quarter.split("-")
                for quarter in self.__get_JSON(
                    self.__endpoint("seminary-quarters", unit=unit)
                )
            ]

        def get_report(year, quarter):
            return self.__get_JSON(
                self.__endpoint("seminary-report", unit=unit)
                + f"&year={year}&quarter={quarter}"
            )

        return {
            year: {quarter: get_report(year, quarter)}
            for year, quarter in get_quarters()
        }

    def get_unit_orginizations(self, unit: int = None) -> JSONType:
        """
        Returns the unit calling/leadership organization structure

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_unit_orginizations-schema.md
        """

        return self.__get_JSON(self.__endpoint("unit-organizations", unit=unit))

    def get_suborganization(self, org_id: int = None, unit: int = None) -> JSONType:
        """
        Returns information for a given suborganization of a unit

        Parameters
        org_id : int
            Number of the suborganization of the unit for which to retrieve the report. Defaults
            to the class assignment for gendered class (Elders' Quorum, Relief Society, etc.).
        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_suborganization-schema.md
        """
        if org_id is None and self.__org_id is None:
            # Set SUNDAY_GENDER class org id
            self.__org_id = next(
                assignment
                for assignment in self.get_member_callings_and_classes()["classAssignments"]
                if assignment["group"] == "SUNDAY_GENDER"
            )["classId"]

        return self.__get_JSON(
            self.__endpoint("suborganization", org_id=org_id, unit=unit)
        )[0]

    def get_full_time_missionaries(self, unit: int = None) -> JSONType:
        """
        Returns a list of the members from the unit currently serving missions

        Parameters
        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_full_time_missionaries-schema.md
        """
        return self.__get_JSON(self.__endpoint("full-time-missionaries", unit=unit))

    def get_assigned_missionaries(self, unit: int = None) -> JSONType:
        """
        Returns a list of the missionaries currently assigned to serve in the unit

        Parameters
        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_assigned_missionaries-schema.md
        """
        return self.__get_JSON(self.__endpoint("assigned-missionaries", unit=unit))

    def get_unit_statistics(self, unit: int = None) -> JSONType:
        """
        Returns the unit statistics

        Parameters

        unit : int
            Number of the church unit for which to retrieve the report

        Returns

        .. literalinclude:: ../JSON_schemas/get_unit_statistics-schema.md
        """

        return self.__get_JSON(self.__endpoint("statistics", unit=unit))
