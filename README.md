# OWASP Juice Shop Security Assessment

Author: Thomson Chilomo

## Overview
A practical assessment of my local OWASP Juice Shop lab,
running in Docker on Kali Linux at http://127.0.0.1:3000.

The project covers security testing, evidence collection,
report writing, and a Python demonstration of access controls.

## Scope
Testing was limited to my local lab and accounts I controlled.
Cross-account basket testing used two tester-owned accounts.

## Findings
- Cross-site scripting in search: browser JavaScript execution
  was demonstrated using a test popup.
- Broken basket authorization: an authenticated account could
  read another test account's basket metadata by changing
  the basket ID.

Both tested baskets were empty. Access to populated baskets,
account takeover, data theft, and write access were not demonstrated.

## Tools used
Kali Linux, Docker, Nmap, Nikto, Gobuster, curl,
Burp Suite, Firefox Developer Tools, and Python 3.

## Project folders
- scripts/ - Python utilities and ownership-check demonstration
- reports/ - testing notes, findings, and recommendations
- evidence/ - saved responses and demonstration results

## Python ownership demonstration
Run from the project folder:

    python3 scripts/ownership_check.py

Expected results:
- Own basket: 200
- Another user's basket: 403
- Not logged in: 401
- Missing basket: 404

These are simulated return values from a standalone Python
exercise. Juice Shop itself has not been modified.
Remediation and retesting against Juice Shop remain pending.

## Lessons learned
Authentication verifies who a user is.
Authorization determines which resources that user may access.
A valid login alone does not establish basket ownership.

I also practised validating JSON evidence, documenting
test limitations, and creating verified project backups.
