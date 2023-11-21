{
  authorized: bool,
  countries: [
    {
      addressFields: [
        [
          str
        ]
      ],
      dialingCode: int,
      id: int,
      iso: str,
      iso3: str,
      name: str,
      states: [
        {
          id: int,
          name: str
        }
      ]
    }
  ],
  finances: [
    {
      accounts: [
        {
          categories: [
            {
              id: int,
              name: str,
              permissions: [
                str
              ],
              type: str
            }
          ],
          countryIso: str,
          currencyIso: str,
          id: int,
          name: str,
          permissions: [
            str
          ]
        }
      ],
      unitNumber: int
    }
  ],
  households: [
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
          patriarchalBlessing: bool,
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
  ],
  lists: [
    {
      members: [
        str
      ],
      name: str,
      sort: int,
      uuid: str
    }
  ],
  ministering: [
    {
      assignments: [
        {
          companions: [
            str
          ],
          households: [
            str
          ]
        }
      ],
      brothers: [
        str
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
    cdolAccess: bool,
    units: [
      {
        reports: [
          str
        ],
        unitNumber: int
      }
    ]
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
    leaderParentUnits: [
      int
    ],
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