{
  elders: [
    {
      companionships: [
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
          id: str,
          ministers: [
            {
              assignType: str,
              email: str,
              interviews: [
                {
                  date: str,
                  id: str,
                  timestamp: str
                }
              ],
              legacyCmisId: int,
              name: str,
              nameOrder: int,
              personUuid: str,
              unitOrgId: str,
              youthBasedOnAge: bool
            }
          ],
          recentlyChangedDate: str,
          recentlyChangedDateInMilliseconds: int
        }
      ],
      districtName: str,
      districtUuid: str,
      supervisorLegacyCmisId: int,
      supervisorName: str,
      supervisorPersonUuid: str
    }
  ],
  eldersQuorumSupervisors: [
    {
      legacyCmisId: int,
      name: str,
      nameOrder: int,
      personUuid: str,
      youthBasedOnAge: bool
    }
  ],
  error: bool,
  interviewViewAccess: bool,
  reliefSociety: [
    {
      companionships: [
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
          id: str,
          ministers: [
            {
              assignType: str,
              email: str,
              interviews: [
                {
                  date: str,
                  id: str,
                  timestamp: str
                }
              ],
              legacyCmisId: int,
              name: str,
              nameOrder: int,
              personUuid: str,
              unitOrgId: str,
              youthBasedOnAge: bool
            }
          ],
          recentlyChangedDate: str,
          recentlyChangedDateInMilliseconds: int
        }
      ],
      districtName: str,
      districtUuid: str,
      supervisorLegacyCmisId: int,
      supervisorName: str,
      supervisorPersonUuid: str
    }
  ],
  reliefSocietySupervisors: [
    {
      legacyCmisId: int,
      name: str,
      nameOrder: int,
      personUuid: str,
      youthBasedOnAge: bool
    }
  ],
  unitOrgs: [
    {
      children: [
        {
          children: NoneType,
          isClass: bool,
          unitNumber: int,
          unitOrgName: str,
          unitOrgTypeIds: [
            int
          ],
          unitOrgUuid: str,
          unitUuid: str
        }
      ],
      isClass: bool,
      unitNumber: int,
      unitOrgName: str,
      unitOrgTypeIds: [
        int
      ],
      unitOrgUuid: str,
      unitUuid: str
    }
  ]
}