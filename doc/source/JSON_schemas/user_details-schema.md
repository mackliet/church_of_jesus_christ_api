{
  emails: [
    {
      email: str,
      privacy: str,
      useType: str
    }
  ],
  households: [
    {
      household: {
        addresses: [
          {
            postalCode: str
          }
        ]
      }
    }
  ],
  legacyCmisId: str,
  membershipUnit: {
    areaUnit: [
      {
        unitNumber: str
      }
    ],
    country: {
      name: str,
      nameLatin: str,
      nameLocal: str
    },
    nameLocal: str,
    parentUnit: {
      nameLocal: str,
      unitNumber: str,
      unitType: {
        id: str,
        name: str
      }
    },
    templeUnit: [
      {
        nameLatin: str,
        nameLocal: str,
        unitNumber: str,
        uuid: str
      }
    ],
    unitNumber: str,
    unitType: {
      id: str,
      name: str
    },
    wardClerk: [
      {
        person: {
          emails: [
            {
              email: str,
              privacy: str,
              useType: str
            }
          ]
        }
      }
    ]
  },
  nameFormats: {
    familyPreferred: str,
    givenPreferred: str,
    listPreferred: str,
    mailPreferred: str,
    spokenPreferred: str
  },
  positions: [
    {
      positionType: {
        id: str,
        name: str
      }
    }
  ],
  uuid: str
}