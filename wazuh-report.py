import requests
import json
from datetime import datetime

#Wazuh API config

WAZUH_URL = "https://localhost:55000"
USERNAME = "wazuh"
PASSWORD = "YOUR WAZUH API PASSWORD HERE"

def get_token():
url = f"{WAZUH_URL}/security/user/authenticate"
response = requests.post(url, auth=(USERNAME, PASSWORD), verify=False)
token = response.json()["data"]["token"]
return token

def get_alerts(token):
url = "https://localhost:9200/wazuh-alerts-*/_search"
headers = {"Content-Type": "application/json"}
response = requests.post(
url, headers=headers,
json={"size": 50, "sort": [{"timestamp": "desc"}]},
auth=("admin", "e2f.p?Q3LHt0S52PQjgPVJsXlNy0vcA8"),
verify=False)
hits = response.json()["hits"]["hits"]
alerts = [hit["_source"] for hit in hits]
return alerts

def generate_report(alerts):
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = f"<html><body>"
report += f"<h1>Wazuh Security Report Alert</h1>"
report += f"<p>Generated: {now}</p>"
report += f"<p> Total Alerts: {len(alerts)}</p>"
report += f"<table border ='1'><tr><th>Time</th><th>Agent</th><th>Rule</th><th>Description</th><th>Level</th></tr>"
for alert in alerts:
timestamp = alert.get("timestamp", "N/A")
agent_info = alert.get("agent", {})
agent = agent_info.get("name", "N/A")
rule_info = alert.get("rule", {})
rule_id = rule_info.get("id", "N/A")
description = rule_info.get("description", "N/A")
level = str(rule_info.get("level", "N/A"))
report += f"<tr><td>{timestamp}</td><td>{agent}</td><td>{rule_id}</td><td>{description}</td><td>{level}</td></tr>"
report += f"</table></body></html>"
with open("/home/seanmurphy/Desktop/report.html", "w") as f:
f.write(report)
print("Report saved to desktop as report.html")

token = get_token()
alerts = get_alerts(token)
generate_report(alerts)
