{
  authorized: bool,
  households: [
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
          permissions: [
            str
          ],
          phone: str,
          positions: [
            {
              name: str,
              setApart: bool,
              type: str,
              unitName: str,
              unitNumber: int,
              uuid: str
            }
          ],
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
  ],
  ministering: [
    {
      assignments: [
        {
          companions: [
            str
          ],
          members: [
            str
          ]
        }
      ],
      uuid: str
    }
  ],
  missionLeaders: [
    {
      leader: {
        optedIn: bool,
        preferredName: str,
        uuid: str
      },
      mission: {
        name: str,
        unitNumber: int,
        unitType: str
      },
      optedIn: bool,
      serviceEnded: str,
      serviceStarted: str,
      spouse: {
        optedIn: bool,
        preferredName: str,
        uuid: str
      },
      uuid: str
    }
  ],
  missionariesAssigned: [
    {
      areaId: int,
      email: str,
      mission: {
        address: str,
        email: str,
        name: str,
        phone: str,
        unitNumber: int
      },
      missionaries: [
        {
          displayName: str,
          email: str,
          preferredName: str,
          sex: str,
          type: str,
          uuid: str
        }
      ],
      phone: str,
      unitNumbers: [
        int
      ]
    }
  ],
  missionariesServing: [
    {
      displayName: str,
      email: str,
      mission: {
        address: str,
        email: str,
        name: str,
        phone: str,
        unitNumber: int
      },
      preferredName: str,
      sex: str,
      type: str,
      unitNumber: int,
      uuid: str
    }
  ],
  organizations: [
    {
      name: str,
      orgTypes: [
        str
      ],
      positions: [
        str
      ],
      unitNumber: int,
      uuid: str
    }
  ],
  reportsAccess: {
    cdolAccess: bool
  },
  toEpoch: int,
  unitSubscriptions: [
    int
  ],
  units: [
    {
      childUnits: [
        {
          name: str,
          unitNumber: int,
          unitType: str
        }
      ],
      name: str,
      unitNumber: int,
      unitType: str
    }
  ],
  user: {
    authorized: bool,
    country: str,
    developer: bool,
    homeUnits: [
      int
    ],
    individualId: int,
    ldsAccountId: int,
    member: bool,
    mrn: str,
    parentUnits: [
      int
    ],
    preferredLanguage: str,
    preferredName: str,
    proxyEdit: bool,
    proxyUnit: bool,
    proxyUser: bool,
    templeNearest: [
      int
    ],
    templeUnits: [
      int
    ],
    username: str,
    uuid: str
  },
  uuid: str
}