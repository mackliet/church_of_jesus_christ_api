{
  allAvailableDates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ],
  attendanceData: {
    attendees: [
      {
        cmisId: int,
        displayName: str,
        entries: [
          {
            date: {
              epochSeconds: int,
              isoYearMonthDay: str,
              loaded: bool,
              localeMonthDay: str
            },
            isMarkedAttended: bool,
            markedAttended: bool
          }
        ],
        gender: str,
        sortName: str,
        unitOrgsCombined: [
          str
        ],
        uuid: str
      }
    ],
    visitorCategories: [
      {
        countsByDate: {
          2023-08-20: int,
          2023-08-27: int,
          2023-09-03: int,
          2023-09-10: int,
          2023-09-17: int
        },
        displayName: str,
        name: str
      }
    ]
  },
  dates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ]
}