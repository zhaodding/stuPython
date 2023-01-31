SELECT
        a.iCaseId, cas.sName sCaseName, ISNULL(a.iDepartmentId, ISNULL(cas.iDepartmentId, 0)) iDeptId, a.iPersonId, per.sName sPersonName, a.iEmployeeId, a.dScore, ISNULL(pt.sName, '') sScoreType, a.dtAttribution dtTime
FROM
        dbo.tblScoreAdjustment a
        LEFT JOIN dbo.tblCase cas ON cas.iCaseId = a.iCaseId AND cas.cFlag = 0
        LEFT JOIN dbo.tblPerson per ON per.iPersonId = a.iPersonId AND per.cFlag = 0
        LEFT JOIN dbo.tblPeopleTag pt ON pt.iId = a.iType AND pt.cFlag = 0
WHERE
        a.cFlag = 0 AND a.iEmployeeId IN (217) AND a.dtAttribution >= '2022-11-01' AND a.dtAttribution < '2023-01-01' AND a.isOperating = 1
ORDER BY
        a.dtAttribution DESC
OFFSET 0 ROWS FETCH NEXT 50 ROWS ONLY;

