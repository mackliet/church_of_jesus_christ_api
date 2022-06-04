[
  {
    address: str,
    coordinates: {
      lat: float,
      long: float
    },
    displayName: str,
    familyName: str,
    members: [
      {
        ageGroup: str,
        birthDate: str,
        classes: [
          str
        ],
        displayName: str,
        email: str,
        familyName: str,
        givenName: str,
        head: bool,
        householdUuid: str,
        individualId: int,
        member: bool,
        ordinances: [
          {
            type: str
          }
        ],
        permissions: [
          str
        ],
        phone: str,
        preferredName: str,
        priesthood: str,
        priorUnitMoveOutDate: str,
        privacy: {
          email: str,
          master: str,
          phone: str,
          photo: str
        },
        sex: str,
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
      master: str,
      phone: str,
      photo: str
    },
    unitNumber: int,
    uuid: str,
    verified: bool
  }
]