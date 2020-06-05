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
        displayName: str,
        email: str,
        familyName: str,
        givenName: str,
        head: bool,
        householdUuid: str,
        individualId: int,
        permissions: [
          str
        ],
        phone: str,
        preferredName: str,
        uuid: str
      }
    ],
    permissions: [
      str
    ],
    phone: str,
    unitNumber: int,
    uuid: str,
    verified: bool
  }
]