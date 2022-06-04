{
  households: [
    {
      hasReliefSocietyMember: bool,
      headOfHouseholdCmisId: int,
      headOfHouseholdUuid: str,
      householdName: str,
      householdSortOrder: int,
      ministeringBrothers: [
        {
          age: int,
          legacyCmisId: int,
          name: str,
          nameOrder: int,
          personUuid: str,
          youthBasedOnAge: bool
        }
      ],
      ministeringSisters: list,
      unitName: str,
      unitNumber: int
    }
  ],
  individuals: [
    {
      assignments: [
        {
          age: int,
          legacyCmisId: int,
          name: str,
          nameOrder: int,
          personUuid: str,
          youthBasedOnAge: bool
        }
      ],
      companions: [
        {
          age: int,
          legacyCmisId: int,
          name: str,
          nameOrder: int,
          personUuid: str,
          youthBasedOnAge: bool
        }
      ],
      legacyCmisId: int,
      name: str,
      nameOrder: int,
      personUuid: str,
      unitOrgTypeId: int,
      youthBasedOnAge: bool
    }
  ]
}