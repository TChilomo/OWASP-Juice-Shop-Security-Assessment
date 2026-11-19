from pathlib import Path

# Find the evidence file inside our project.
project = Path(__file__).resolve().parent.parent
evidence = project / "evidence" / "response-headers.txt"

if not evidence.exists():
    raise SystemExit(f"Evidence file not found: {evidence}")

# Read header names and values.
headers = {}
for line in evidence.read_text().splitlines():
    if ":" in line:
        name, value = line.split(":", 1)
        headers[name.strip().lower()] = value.strip()

# Check for selected browser security controls.
checks = [
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

results = ["Juice Shop: HTTP Header Review", ""]

for name in checks:
    value = headers.get(name.lower())
    if value is None:
        results.append(f"ABSENT: {name}")
    else:
        results.append(f"PRESENT: {name}: {value}")

cors = headers.get("access-control-allow-origin", "Not present")
results.append(f"\nAccess-Control-Allow-Origin: {cors}")
results.append(
    "\nThese are observations, not confirmed vulnerabilities."
)
results.append(
    "Header presence alone does not prove correct configuration."
)

# Display and save the review.
report = "\n".join(results)
print(report)

output = project / "reports" / "header-review.txt"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(report + "\n")
print(f"\nReport saved to: {output}")
