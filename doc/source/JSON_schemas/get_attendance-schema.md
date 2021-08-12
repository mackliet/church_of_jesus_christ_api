{
  allAvailableDates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ],
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
  dates: [
    {
      epochSeconds: int,
      isoYearMonthDay: str,
      loaded: bool,
      localeMonthDay: str
    }
  ]
}