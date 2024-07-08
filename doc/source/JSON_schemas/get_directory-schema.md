[
  {
    address: str,
    coordinates: {
      latitude: float,
      longitude: float
    },
    editable: bool,
    members: [
      {
        countryId: int,
        displayName: str,
        editable: bool,
        email: {
          email: str
        },
        givenName: str,
        head: bool,
        householdUuid: str,
        name: str,
        phone: {
          country: int,
          e164: str,
          number: str
        },
        privacy: {
          birthDate: str,
          email: str,
          phone: str,
          photo: str
        },
        surname: str,
        unitNumber: int,
        uuid: str
      }
    ],
    movable: bool,
    name: str,
    privacy: {
      address: str,
      coordinates: str,
      photo: str
    },
    surname: str,
    unitNumber: int,
    uuid: str,
    verified: bool
  }
]