{
  error: bool,
  participationReports: {
    addedAncestor: [
      {
        label: NoneType,
        membersAddingAncestor: int,
        monthEndDate: str,
        monthEndDisplayLabel: str,
        title: str
      }
    ],
    addedMemory: [
      {
        label: NoneType,
        membersAddingMemory: int,
        monthEndDate: str,
        monthEndDisplayLabel: str,
        title: str
      }
    ],
    loggingIn: [
      {
        label: NoneType,
        membersLoggingIn: int,
        monthEndDate: str,
        monthEndDisplayLabel: str,
        title: NoneType
      }
    ],
    membersWhoIndexed: [
      {
        label: NoneType,
        membersIndexing: int,
        monthEndDate: str,
        monthEndDisplayLabel: str,
        title: str
      }
    ],
    percentageFourGen: [
      {
        label: NoneType,
        monthEndDate: str,
        monthEndDisplayLabel: str,
        percent: float,
        title: NoneType
      }
    ],
    yearsInReport: [
      str
    ]
  },
  reportDate: str,
  submitterTrendReport: {
    trendData: [
      {
        label: str,
        months: [
          {
            month: int,
            submitters: int
          }
        ],
        year: int
      }
    ],
    ytdDiffYearOverYear: int
  },
  ytdSubmittersReports: {
    monthEndDate: str,
    summary: {
      adultPercentage: str,
      adultSubmitters: int,
      convertPercentage: str,
      convertSubmitters: int,
      percentSubmitting: float,
      totalAdults: int,
      totalConverts: int,
      totalMembersSubmitting: int,
      totalPercentage: str,
      totalPotentialSubmitters: int,
      totalYouth: int,
      totalYsa: int,
      unitName: str,
      unitNumber: int,
      youthPercentage: str,
      youthSubmitters: int,
      ysaSubmitters: int,
      ysasPercentage: str
    },
    unitTotals: [
      {
        adultPercentage: str,
        adultSubmitters: int,
        convertPercentage: str,
        convertSubmitters: int,
        percentSubmitting: float,
        totalAdults: int,
        totalConverts: int,
        totalMembersSubmitting: int,
        totalPercentage: str,
        totalPotentialSubmitters: int,
        totalYouth: int,
        totalYsa: int,
        unitName: str,
        unitNumber: int,
        youthPercentage: str,
        youthSubmitters: int,
        ysaSubmitters: int,
        ysasPercentage: str
      }
    ]
  }
}