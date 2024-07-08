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
      formatted5: NoneType,
      formatted6: NoneType,
      formattedAll: list,
      formattedLine1: str,
      formattedLine2: str,
      formattedLine3: NoneType,
      formattedLine4: NoneType,
      useType: NoneType
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
          formatted5: NoneType,
          formatted6: NoneType,
          formattedAll: list,
          formattedLine1: str,
          formattedLine2: str,
          formattedLine3: NoneType,
          formattedLine4: NoneType,
          useType: NoneType
        },
        anchorPerson: {
          legacyCmisId: int,
          uuid: str
        },
        directoryPreferredLocal: str,
        emails: NoneType,
        familyNameLocal: str,
        phones: NoneType,
        unit: {
          addressUnknown: NoneType,
          adminUnit: NoneType,
          cdolLink: NoneType,
          children: NoneType,
          nameLatin: NoneType,
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
    householdRole: str,
    householdUuid: str,
    households: NoneType,
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
    mrn: NoneType,
    nameFamilyPreferredLocal: str,
    nameFormats: {
      certificateChurchOfficerLocal: NoneType,
      certificateOfficialLocal: NoneType,
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
        internationalFormat: NoneType,
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
    wamPolicy: NoneType,
    youthBasedOnAge: bool
  }
]