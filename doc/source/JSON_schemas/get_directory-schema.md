[
  {
    address: str,
    coordinates: {
      lat: float,
      long: float
    },
    displayName: str,
    email: str,
    familyName: str,
    members: [
      {
        ageGroup: str,
        bic: bool,
        birthCountry: str,
        birthDate: str,
        birthPlace: str,
        classes: [
          str
        ],
        displayName: str,
        email: str,
        familyName: str,
        father: {
          birthDate: str,
          displayName: str,
          uuid: str
        },
        givenName: str,
        head: bool,
        householdUuid: str,
        individualId: int,
        marriage: {
          country: str,
          date: str,
          place: str,
          sealingDate: str,
          spouse: {
            birthDate: str,
            displayName: str,
            uuid: str
          },
          temple: str
        },
        member: bool,
        missionCountry: str,
        missionLanguage: str,
        mother: {
          birthDate: str,
          displayName: str,
          uuid: str
        },
        mrn: str,
        officialName: str,
        ordinances: [
          {
            date: str,
            type: str
          }
        ],
        permissions: [
          str
        ],
        positions: [
          {
            activeDate: str,
            name: str,
            setApart: bool,
            type: str,
            unitName: str,
            unitNumber: int,
            uuid: str
          }
        ],
        preferredName: str,
        priesthood: str,
        priorUnit: {
          name: str,
          unitNumber: int,
          unitType: str
        },
        priorUnitMoveOutDate: str,
        privacy: {
          email: str,
          master: str,
          photo: str
        },
        sex: str,
        templeRecommendExpiration: str,
        templeRecommendStatus: str,
        templeRecommendType: str,
        unitMoveInDate: str,
        uuid: str
      }
    ],
    permissions: [
      str
    ],
    phone: str,
    privacy: {
      address: str,
      coordinates: str,
      email: str,
      master: str,
      phone: str,
      photo: str
    },
    unitNumber: int,
    uuid: str,
    verified: bool
  }
]