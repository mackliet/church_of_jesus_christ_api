[
  {
    address: {
      addressLines: [
        str
      ],
      formatted1: NoneType,
      formatted2: NoneType,
      formatted3: NoneType,
      formatted4: NoneType,
      formattedAll: list,
      formattedLine1: str,
      formattedLine2: str,
      formattedLine3: NoneType,
      formattedLine4: NoneType
    },
    age: int,
    birth: {
      country: NoneType,
      date: {
        calc: str,
        date: str,
        display: str
      },
      monthDay: {
        calc: str,
        date: str,
        display: str
      },
      place: NoneType
    },
    convert: bool,
    email: str,
    emails: [
      {
        email: str,
        ownerType: NoneType,
        useType: NoneType
      }
    ],
    formattedAddress: str,
    houseHoldMemberNameForList: str,
    householdAnchorPersonUuid: str,
    householdEmail: NoneType,
    householdMember: {
      household: {
        address: {
          addressLines: [
            str
          ],
          formatted1: NoneType,
          formatted2: NoneType,
          formatted3: NoneType,
          formatted4: NoneType,
          formattedAll: list,
          formattedLine1: str,
          formattedLine2: str,
          formattedLine3: NoneType,
          formattedLine4: NoneType
        },
        anchorPerson: {
          legacyCmisId: int,
          uuid: str
        },
        directoryPreferredLocal: str,
        emails: NoneType,
        familyNameLocal: str,
        phones: [
          {
            number: str,
            ownerType: NoneType,
            useType: NoneType
          }
        ],
        unit: {
          addressUnknown: NoneType,
          adminUnit: NoneType,
          cdolLink: NoneType,
          children: NoneType,
          nameLocal: str,
          parentUnit: NoneType,
          positions: NoneType,
          unitNumber: int,
          unitType: NoneType,
          uuid: NoneType
        },
        uuid: str
      },
      householdRole: str,
      membershipUnitFlag: bool
    },
    householdNameDirectoryLocal: str,
    householdNameFamilyLocal: str,
    householdPhoneNumber: str,
    householdRole: str,
    householdUuid: str,
    isAdult: bool,
    isHead: bool,
    isMember: bool,
    isOutOfUnitMember: bool,
    isProspectiveElder: bool,
    isSingleAdult: bool,
    isSpouse: bool,
    isYoungSingleAdult: bool,
    legacyCmisId: int,
    member: bool,
    membershipUnit: NoneType,
    nameFamilyPreferredLocal: str,
    nameFormats: {
      familyPreferredLocal: str,
      givenPreferredLocal: str,
      listOfficial: NoneType,
      listPreferred: NoneType,
      listPreferredLocal: str,
      spokenPreferredLocal: NoneType
    },
    nameGivenPreferredLocal: str,
    nameListPreferredLocal: str,
    nameOrder: int,
    outOfUnitMember: bool,
    personStatusFlags: {
      adult: bool,
      convert: bool,
      deceased: bool,
      hasPatriarchalBlessing: bool,
      member: bool,
      prospectiveElder: bool,
      singleAdult: bool,
      youngSingleAdult: bool
    },
    personUuid: str,
    phoneNumber: str,
    phones: [
      {
        number: str,
        ownerType: NoneType,
        useType: NoneType
      }
    ],
    positions: NoneType,
    priesthoodOffice: str,
    priesthoodTeacherOrAbove: bool,
    sex: str,
    unitName: str,
    unitNumber: int,
    unitOrgsCombined: [
      str
    ],
    uuid: str,
    youthBasedOnAge: bool
  }
]