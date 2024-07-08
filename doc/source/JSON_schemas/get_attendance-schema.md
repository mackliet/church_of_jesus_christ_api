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
          2024-06-16: int,
          2024-06-23: int,
          2024-06-30: int,
          2024-07-07: int,
          2024-07-14: int
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