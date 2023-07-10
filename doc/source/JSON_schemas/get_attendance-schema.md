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
          2023-06-18: int,
          2023-06-25: int,
          2023-07-02: int,
          2023-07-09: int,
          2023-07-16: int
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