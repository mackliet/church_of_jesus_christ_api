[
  {
    address: str,
    age: str,
    assignedMissionaries: [
      {
        accountable: bool,
        actualAge: NoneType,
        actualAgeInMonths: NoneType,
        age: NoneType,
        birthDate: NoneType,
        birthDateFormatted: str,
        birthDateSort: NoneType,
        birthDayFormatted: NoneType,
        birthDaySort: NoneType,
        email: str,
        formattedMrn: NoneType,
        gender: str,
        genderCode: int,
        genderLabelShort: str,
        householdEmail: NoneType,
        householdPhone: str,
        id: int,
        mrn: NoneType,
        name: str,
        nameOrder: NoneType,
        nonMember: bool,
        notAccountable: bool,
        outOfUnitMember: bool,
        phone: str,
        priesthood: NoneType,
        priesthoodCode: NoneType,
        priesthoodType: NoneType,
        setApart: bool,
        spokenName: NoneType,
        sustainedDate: NoneType,
        unitName: NoneType,
        unitNumber: NoneType,
        visible: NoneType
      }
    ],
    baptism_date: int,
    baptism_goal_date: NoneType,
    cmis_id: NoneType,
    confirmation_date: NoneType,
    email: {
      family: NoneType,
      home: NoneType,
      other: NoneType,
      work: NoneType
    },
    fellowshippers: list,
    first_name: str,
    formattedBaptismDate: NoneType,
    formattedLastSacramentAttendance: NoneType,
    formattedLastVisit: NoneType,
    fullName: str,
    gender: NoneType,
    last6Sundays: [
      {
        attended: bool,
        date: int,
        formattedDate: str
      }
    ],
    lastSacramentAttendance: int,
    lastVisit: int,
    last_name: NoneType,
    mem_taught: NoneType,
    member: NoneType,
    memberFellowshippers: list,
    missionaries: {
      area_id: str,
      names: [
        str
      ]
    },
    needs: NoneType,
    otherFellowshippers: list,
    person_id: int,
    phone: {
      home: NoneType,
      mobile: NoneType,
      other: NoneType,
      work: NoneType
    },
    sacramentAttendanceFilters: list,
    sacrament_attendance: list,
    status: int,
    statusFilters: [
      str
    ],
    statusName: str,
    teachingRecord: NoneType,
    visitFilters: list,
    visits: list
  }
]