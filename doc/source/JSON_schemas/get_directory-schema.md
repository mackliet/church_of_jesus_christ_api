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
        displayName: str,
        editable: bool,
        email: str,
        givenName: str,
        head: bool,
        householdUuid: str,
        name: str,
        phone: str,
        positions: [
          {
            positionTypeId: int,
            positionTypeName: str,
            unitName: str,
            unitNumber: int,
            uuid: str
          }
        ],
        privacy: {
          email: str,
          master: str,
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
    phone: str,
    privacy: {
      address: str,
      coordinates: str,
      master: str,
      phone: str,
      photo: str
    },
    surname: str,
    unitNumber: int,
    uuid: str,
    verified: bool
  }
]