# Compliance Report Generator

This tool generates a comprehensive Compliance Report focusing on Compliance Tags. It represents the compliance status according to specific compliance principles, which allows for an in-depth analysis of adherence to compliance frameworks. Thanks to Jonas Rosenboom for providing the first version.

## Description

The Compliance Report Generator reformats compliance data into a report where each compliance principle is listed in its own row. This structure ensures that data is presented in a principle-centric manner, allowing for a clearer understanding of compliance across multiple frameworks.

## Prerequisites

Before using this Reporting Engine, users must install and configure the `cg-api` Python package. This package facilitates the interaction with the compliance data source. Detailed installation instructions can be found at the [`cg-api` GitHub repository](https://github.com/jzr/cg-api).

## Installation

To set up the Compliance Report Generator, ensure you have Python and `pip` installed on your system. Then proceed with the following steps:

1. Install the `cg-api` package from the [cg-api GitHub repository](https://github.com/jzr/cg-api) as it is crucial for the Reporting Engine's data retrieval process.

2. Clone this repository to your machine using:

    ```bash
    git clone https://github.com/Check-Point-APAC-CSA-Team/compliance-report-by-tag.git
    ```

3. Change to the repository directory:

    ```bash
    cd compliance-report-generator
    ```

4. Install any additional dependencies if specified.

## Usage

To generate the compliance report, execute the script with the bundle ID as a command-line argument:

```bash
python compliance_report_generator.py <bundle_id>
