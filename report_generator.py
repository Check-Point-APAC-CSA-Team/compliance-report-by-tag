from natsort import natsorted
import csv
import sys

import cg_api

CSP_MAPPING = {
    "aws": "CloudAccounts",
    "azure": "AzureCloudAccount",
    "gcp": "GoogleCloudAccount"
}

def main():
    api = cg_api.Session()
    bundle_id = sys.argv[1]

    cloud_account_type = api.get(f"Compliance/Ruleset/{bundle_id}")['cloudVendor']
    cloud_account_ids = [k["id"] for k in api.get(CSP_MAPPING[cloud_account_type])]
    assessments = []
    n = 50

    for sliced_ids in (cloud_account_ids[k:k+n] for k in range(0, len(cloud_account_ids), n)):
        data = api.post(
            "AssessmentHistoryV2/LastAssessmentResults/minimized",
            {
                "cloudAccountBundleFilters": [
                    {
                        "bundleIds": [bundle_id],
                        "cloudAccountIds": sliced_ids,
                        "cloudAccountType": cloud_account_type,
                    }
                ]
            },
        )
        assessments += data

    # A list to hold all rows for CSV
    csv_rows = []

    for assessment in assessments:
        for test in assessment["tests"]:
            # Split the compliance tag into individual principles
            compliance_tags = test['rule']['complianceTag'].split('|')
            for tag in compliance_tags:
                row = {
                    'Compliance Tag': tag,
                    'Severity': test['rule']['severity'],
                    'Rule Name': test['rule']['name'],
                    'Rule Id': test['rule']['ruleId'],
                    'Tested': test['testedCount'],
                    'Relevant': test['relevantCount'],
                    'Non-compliant': test['nonComplyingCount']
                }
                csv_rows.append(row)

    header = ['Compliance Tag', 'Severity', 'Rule Name', 'Rule Id', 'Tested', 'Relevant', 'Non-compliant']
    csv_rows = natsorted(csv_rows, key=lambda k: k['Compliance Tag'])

    with open("output.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(csv_rows)

if __name__ == "__main__":
    main()
