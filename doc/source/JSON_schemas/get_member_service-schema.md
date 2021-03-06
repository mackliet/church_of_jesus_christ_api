{
  authorizedToAddEndowment: bool,
  authorizedToEditMelchizedekPriesthood: bool,
  authorizedToPrintCertificates: bool,
  authorizedToPrintMelchizedekPriesthood: bool,
  authorizedToUpdateContactInfo: bool,
  authorizedToUpdateRecord: bool,
  authorizedToViewHTVT: bool,
  authorizedToViewRecord: bool,
  authorizedToViewReportBasic: bool,
  canChangeMoveRestriction: bool,
  consentFormId: NoneType,
  consentFormMediaType: NoneType,
  family: {
    children: list,
    hohMrn: NoneType,
    marriage: {
      authorizedToViewNonMemberSpouse: bool,
      country: NoneType,
      countryId: NoneType,
      date: NoneType,
      errors: {},
      individualId: int,
      legalNameGroup: NoneType,
      madeHeadOfHousehold: bool,
      marriageId: str,
      marriageTerminated: bool,
      marriageTerminationCause: NoneType,
      memberStatus: NoneType,
      memberType: NoneType,
      mrn: str,
      nonMemberSpouseNameBirthdateNotEditable: bool,
      place: NoneType,
      preferredNameGroup: NoneType,
      restorationOfBlessingsRequired: bool,
      sealedToPriorSpouse: bool,
      sealingDate: NoneType,
      sealingTemple: NoneType,
      showTempleInfo: bool,
      spouse: {
        age: NoneType,
        allPriesthoodOrdinations: NoneType,
        birthDate: str,
        deathDate: NoneType,
        deceased: bool,
        displayBirthDate: str,
        gender: str,
        headOfHousehold: bool,
        id: int,
        inAuthorizedUnit: bool,
        inHousehold: bool,
        linkedRecord: bool,
        listName: str,
        maidenName: str,
        maidenOrLegalName: str,
        member: bool,
        mrn: NoneType,
        name: str,
        nameGroup: NoneType,
        noMrnInitiated: bool,
        pendingId: NoneType,
        preferredOrLegalName: str,
        priesthood: NoneType,
        priesthoodCode: NoneType,
        priesthoodType: NoneType,
        relationship: str,
        relationshipDisplay: str,
        spokenName: NoneType,
        unitNumber: int,
        unknown: bool
      },
      spouseDeceased: bool,
      spouseEditable: bool,
      spouseId: int,
      spouseInDifferentWardBranch: bool,
      spouseMember: bool,
      spouseMrn: NoneType,
      spouseUnitNumber: int,
      templeId: NoneType,
      terminationDate: NoneType,
      updateName: NoneType,
      warnings: {}
    },
    parents: NoneType
  },
  household: {
    errors: {},
    familyNameGroup: {
      autoRomanize: bool,
      formattedLatin: str,
      formattedLocal: str,
      name1: {
        family: str,
        given: NoneType,
        label: str,
        labelKey: NoneType,
        suffix: NoneType,
        translitSource: bool,
        writingSystem: str
      },
      name2: NoneType,
      name3: NoneType
    },
    hohMrn: NoneType,
    members: [
      {
        age: NoneType,
        allPriesthoodOrdinations: NoneType,
        birthDate: str,
        deathDate: NoneType,
        deceased: bool,
        displayBirthDate: str,
        gender: str,
        headOfHousehold: bool,
        id: int,
        inAuthorizedUnit: bool,
        inHousehold: bool,
        linkedRecord: bool,
        listName: str,
        maidenName: NoneType,
        maidenOrLegalName: str,
        member: bool,
        mrn: NoneType,
        name: str,
        nameGroup: NoneType,
        noMrnInitiated: bool,
        pendingId: NoneType,
        preferredOrLegalName: str,
        priesthood: NoneType,
        priesthoodCode: NoneType,
        priesthoodType: NoneType,
        relationship: str,
        relationshipDisplay: str,
        spokenName: NoneType,
        unitNumber: int,
        unknown: bool
      }
    ]
  },
  individual: {
    actualAge: NoneType,
    actualAgeInMonths: NoneType,
    adultAgeOrMarried: bool,
    age: NoneType,
    ageAsOfDec31: NoneType,
    ageAsOfDec31NextYear: NoneType,
    birthCountry: NoneType,
    birthCountryId: NoneType,
    birthDate: str,
    birthDateDisplay: str,
    birthPlace: NoneType,
    canHaveCalling: NoneType,
    canHaveHTAssignment: bool,
    canHaveMaidenName: bool,
    canHaveVTAssignment: bool,
    confidentialEvents: NoneType,
    email: str,
    endowed: NoneType,
    errors: {},
    formattedHouseholdCoupleName: str,
    formattedMrn: NoneType,
    gender: str,
    hasOutOfUnitRecord: bool,
    head: bool,
    headInUnit: bool,
    hohId: int,
    hohName: str,
    householdEmail: str,
    householdPhone: str,
    hqMoveRestriction: bool,
    id: int,
    legalNameGroup: {
      autoRomanize: bool,
      formattedLatin: str,
      formattedLocal: str,
      name1: {
        family: str,
        given: str,
        label: str,
        labelKey: NoneType,
        suffix: NoneType,
        translitSource: bool,
        writingSystem: str
      },
      name2: NoneType,
      name3: NoneType
    },
    maidenNameGroup: {
      autoRomanize: bool,
      formattedLatin: NoneType,
      formattedLocal: NoneType,
      name1: {
        family: NoneType,
        given: NoneType,
        label: str,
        labelKey: NoneType,
        suffix: NoneType,
        translitSource: bool,
        writingSystem: str
      },
      name2: NoneType,
      name3: NoneType
    },
    mailingAddress: {
      city: NoneType,
      country: NoneType,
      district: NoneType,
      formattedLines: NoneType,
      geocodeToUnits: bool,
      postalCode: NoneType,
      standardized: NoneType,
      state: NoneType,
      street1: NoneType,
      street2: NoneType,
      units: NoneType
    },
    mailingSameAsResidential: bool,
    missionCountry: NoneType,
    missionCountryId: NoneType,
    missionLanguage: NoneType,
    missionLanguageId: NoneType,
    moveDate: NoneType,
    moveDateDuration: NoneType,
    moveRestriction: bool,
    moveRestrictionDate: NoneType,
    mrn: NoneType,
    name: str,
    nameUpdateReason: NoneType,
    notAccountable: bool,
    outOfUnit: bool,
    phone: str,
    preferredNameGroup: {
      autoRomanize: bool,
      formattedLatin: str,
      formattedLocal: str,
      name1: {
        family: str,
        given: str,
        label: str,
        labelKey: NoneType,
        suffix: NoneType,
        translitSource: bool,
        writingSystem: str
      },
      name2: NoneType,
      name3: NoneType
    },
    priesthood: NoneType,
    priesthoodCode: NoneType,
    primaryUnitName: str,
    primaryUnitNumber: NoneType,
    priorUnitName: NoneType,
    priorUnitNumber: NoneType,
    priorUnits: NoneType,
    recommendStatus: NoneType,
    residentialAddress: {
      city: str,
      country: int,
      district: NoneType,
      formattedLines: [
        str
      ],
      geocodeToUnits: bool,
      postalCode: str,
      standardized: NoneType,
      state: int,
      street1: str,
      street2: NoneType,
      units: NoneType
    },
    restorationOfBlessingsRequired: bool,
    sealedToSpouse: NoneType,
    spouseId: int,
    spouseInUnit: bool,
    spouseName: str,
    unitName: str,
    unitNumber: str,
    warnings: {}
  },
  individualName: str,
  ordinances: NoneType,
  outOfUnitMember: bool,
  recommend: NoneType,
  showNotEditEnabledMessage: bool,
  stakeOrDistrictUser: bool,
  unitLocaleData: {
    addressFields: [
      str
    ],
    hasLatinWritingSystem: bool,
    name1WritingSystem: str,
    name2WritingSystem: NoneType
  },
  withinStewardship: bool
}