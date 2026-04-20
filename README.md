# wazuh-alert-reporter
# Wazuh Automated Security Alert Reporter

A Python script that connects to a Wazuh SIEM deployment, pulls real-time security alerts from the OpenSearch indexer, and generates a formatted HTML report — built as part of a home lab project to demonstrate security operations and automation skills.

## Overview

This tool was developed on top of a Wazuh SIEM home lab running on Ubuntu 24.04 in VirtualBox, with a live Windows 11 endpoint enrolled as a monitored agent. The script authenticates against the Wazuh REST API, queries the OpenSearch indexer for the 50 most recent alerts, and outputs a structured HTML report with timestamp, agent, rule ID, description, and severity level for each event.

## Features

- Authenticates to the Wazuh API using JWT token-based authentication
- Queries the OpenSearch indexer directly for real-time alert data
- Generates a timestamped HTML report with a sortable alert table
- Captures alerts from multiple agents (supports both Linux and Windows endpoints)
- Lightweight — built with Python standard library plus `requests`

## Tech Stack

- Python 3
- Wazuh SIEM (Manager + Indexer + Dashboard)
- OpenSearch REST API
- Ubuntu 24.04 (VirtualBox)
- Windows 11 (monitored endpoint agent)

## Prerequisites

- A running Wazuh deployment (manager, indexer, and dashboard)
- Python 3 installed on the Wazuh server
- `requests` library (`pip install requests`)
- Wazuh API credentials and OpenSearch admin credentials

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/murphys611/wazuh-alert-reporter.git
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Open `wazuh_report.py` and update the credentials:
   ```python
   USERNAME = "wazuh"
   PASSWORD = "your_wazuh_api_password_here"
   ```
   And in the `get_alerts` function:
   ```python
   auth=("admin", "your_opensearch_admin_password_here")
   ```

4. Update the output path in `generate_report` to match your system:
   ```python
   with open("/your/desired/output/path/report.html", "w") as f:
   ```

## Usage

Run the script from the Wazuh server:

```bash
python3 wazuh_report.py
```

The report will be saved as `report.html` at the configured output path. Open it in any browser to view the alert table.

## Sample Output

The generated report includes:

| Time | Agent | Rule | Description | Level |
|------|-------|------|-------------|-------|
| 2026-04-20T17:57:36 | Sean_Murphy-PC | 60106 | Windows logon success | 3 |
| 2026-04-20T18:00:42 | seanmurphy-VirtualBox | 52002 | Apparmor DENIED | 3 |

## Project Context

This project was built as an extension of a Wazuh SIEM home lab, which included:
- Deploying a full Wazuh stack (manager, indexer, dashboard) on Ubuntu 24.04 in VirtualBox
- Enrolling a live Windows 11 endpoint as a monitored agent via NAT port forwarding
- Analyzing real-time security events including authentication monitoring, file integrity alerts, and MITRE ATT&CK technique detections

## Author

Sean Murphy — [LinkedIn](https://www.linkedin.com/in/sean-murphy-psu/) | [GitHub](https://github.com/murphys611)
