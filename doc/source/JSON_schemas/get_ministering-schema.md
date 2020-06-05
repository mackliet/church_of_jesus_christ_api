{
  households: [
    {
      hasReliefSocietyMember: bool,
      headOfHouseholdCmisId: int,
      headOfHouseholdUuid: str,
      householdName: str,
      householdSortOrder: int,
      ministeringBrothers: list,
      ministeringSisters: list,
      unitName: str,
      unitNumber: int
    }
  ],
  individuals: [
    {
      assignments: [
        {
          legacyCmisId: int,
          name: str,
          nameOrder: int,
          personUuid: str,
          youthBasedOnAge: bool
        }
      ],
      companions: [
        {
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