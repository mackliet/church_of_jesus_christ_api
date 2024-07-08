{
  elders: [
    {
      companionships: [
        {
          assignmentErrors: list,
          assignmentWarnings: list,
          assignments: [
            {
              age: int,
              assignType: str,
              legacyCmisId: int,
              name: str,
              nameSort: str,
              personUuid: str,
              youthBasedOnAge: bool
            }
          ],
          id: str,
          ministerErrors: list,
          ministerWarnings: list,
          ministers: [
            {
              age: int,
              assignType: str,
              email: str,
              interviews: [
                {
                  date: str,
                  id: str,
                  month: int,
                  timestamp: str,
                  year: int
                }
              ],
              legacyCmisId: int,
              name: str,
              nameSort: str,
              personUuid: str,
              priesthoodOffice: str,
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
      name: str,
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
          assignmentErrors: list,
          assignmentWarnings: list,
          assignments: [
            {
              age: int,
              assignType: str,
              legacyCmisId: int,
              name: str,
              nameSort: str,
              personUuid: str,
              youthBasedOnAge: bool
            }
          ],
          id: str,
          ministerErrors: list,
          ministerWarnings: list,
          ministers: [
            {
              age: int,
              assignType: str,
              email: str,
              interviews: [
                {
                  date: str,
                  id: str,
                  month: int,
                  timestamp: str,
                  year: int
                }
              ],
              legacyCmisId: int,
              name: str,
              nameSort: str,
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
      name: str,
      personUuid: str,
      youthBasedOnAge: bool
    }
  ],
  unitOrgs: [
    {
      children: NoneType,
      isClass: bool,
      unitNumber: NoneType,
      unitOrgName: str,
      unitOrgTypeIds: [
        int
      ],
      unitOrgUuid: str,
      unitUuid: NoneType
    }
  ]
}