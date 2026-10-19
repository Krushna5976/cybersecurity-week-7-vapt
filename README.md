# Week 7 — Web Application VAPT with Burp Suite

A learning project documenting authorized, local web application security testing performed against **Damn Vulnerable Web Application (DVWA)** on `127.0.0.1:8081` using Burp Suite Community Edition. This repository is for educational demonstration only; it does not document testing of a real third-party target.

## Objectives

- Configure and verify Burp Suite proxy interception.
- Map application routes and identify request parameters.
- Perform manual testing with Burp Proxy and Repeater, and a small controlled Intruder run.
- Conduct limited local directory/endpoint discovery.
- Document observed behavior, evidence, impact, and remediation.

## Deliverables

- `Deliverables/Week7_VAPT_Vulnerability_Report.pdf` — final report.
- `Deliverables/Week7_VAPT_Presentation.pptx` — presentation.

## Findings documented

1. **SQL injection in DVWA's SQL injection module** — input handling allows SQL syntax manipulation and a Boolean-based test changes the returned records under the configured training security level.
2. **Reflected cross-site scripting (XSS)** — a test payload is reflected into the response and was demonstrated executing in the local training application.
3. **Stored cross-site scripting (XSS)** — a test payload submitted through the local stored-XSS module persists and is rendered when the affected page is revisited.

These results apply to the deliberately vulnerable local training app and its current configuration; they must not be generalized to other applications.

## Additional observations (not counted as confirmed vulnerabilities)

- Changing the IP parameter in DVWA's command-execution training module changed the ping target. This alone is not treated as proof of arbitrary command execution.
- The local DVWA `admin/password` credentials were accepted. This is a training-app default-credential observation, not evidence of an authentication bypass in a production system.
- The directory scan found several expected routes and responses. `robots.txt` directives are crawler guidance, not access control; a 403/404 response alone does not establish a vulnerability.

## Repository structure

- `Evidence/Burp/` — proxy, SQL injection, Intruder and parameter-tampering evidence.
- `Evidence/Reflected-XSS/` — reflected-XSS request/response and browser proof.
- `Evidence/Stored-XSS/` — stored-XSS request/response and persistence proof.
- `Evidence/Directory-Discovery/` — local discovery results and supporting screenshots.
- `Scripts/directory_scan.py` — limited path-checking helper used for the local lab.

## Scope and safety

- Target: local DVWA only (`127.0.0.1:8081`).
- Proxy used: `127.0.0.1:8080`.
- No third-party systems were in scope.
- Review screenshots before publishing publicly. Redact session cookies, PHPSESSID values, user tokens, credentials, and other session data if visible. Login/authentication and weak-session screenshots were intentionally excluded from this curated bundle.
- Use the script only against systems you own or are explicitly authorized to test.

## Remediation themes

- Use parameterized queries and server-side input handling for database operations.
- Contextually encode output and apply safe templating practices to prevent reflected and stored XSS.
- Avoid exposing diagnostic interfaces; enforce authentication and authorization server-side.
- Validate inputs against expected formats and restrict command execution through safer APIs and allowlists.
- Keep security testing within a documented, authorized scope.

## Limitations

This is a training exercise, not a comprehensive professional penetration test. Findings are based on the screenshots and observations gathered during the exercise; no claim is made that all endpoints or vulnerabilities have been discovered.
