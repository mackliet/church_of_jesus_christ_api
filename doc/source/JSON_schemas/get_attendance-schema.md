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
          2022-05-29: int,
          2022-06-05: int,
          2022-06-12: int,
          2022-06-19: int,
          2022-06-26: int
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