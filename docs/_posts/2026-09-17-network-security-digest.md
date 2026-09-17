---
layout: post
title: "Network Device Security Digest - 2026-09-17"
date: 2026-09-17 22:16:05 +0000
edition: daily
critical_count: 4
item_count: 25
kev: "CVE-2026-76460"
analysis_mode: "rule-based"
categories: digest
---

# Network Device Security Digest — 2026-09-17

*daily edition · window 24h · 19 feeds · 25 items · 4 critical · generated 2026-09-17 22:16 UTC*

> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers and SD-WAN edge. Everything else is filtered out.

---

## 🧠 Headline — AI and network devices: standing guidance

No model summary was generated for this edition (ANTHROPIC_API_KEY not set), so this section carries the standing guidance. AI shortens the gap between a public advisory and mass exploitation of internet-facing network devices, and it adds a new privileged surface wherever an assistant or agent can read device state or push configuration.

**Preventing it on current systems**

- Assume exploit development and mass scanning are faster than your historical patch SLA - shorten the window for internet-facing network devices to days, not months.
- Treat any AI/LLM integration on network devices (assistants, AIOps, MCP or agent connectors) as a privileged admin path: scoped read-only credentials, no unattended config write, full audit trail.
- Test AI-facing management surfaces for prompt injection from attacker-controlled data (device logs, hostnames, ticket text) before letting an agent act on them.
- Use AI-assisted detection on your side too: baseline NetFlow/syslog and alert on deviation rather than relying on signature updates alone.
- Harden against AI-enabled social engineering of the network team - callback verification for any out-of-band request to change firewall or VPN configuration.

**Preventing it on legacy / end-of-life systems**

- Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.
- Put compensating controls in place - strict ACLs, no direct management access, dedicated jump host, full session logging.
- Set a replacement date and a budget owner; document the accepted risk until then.
- Where the device cannot be replaced soon, monitor it as a high-risk asset (NetFlow baseline, alert on new outbound flows).

---

## Executive summary

- 56 network-device items collected in the last 24h from 19 feeds.
- 2 item(s) reference CISA KEV entries.
- Model summarization disabled - rule-based advice shown.

> **On the CISA KEV catalog in this edition:** CVE-2026-76460 — treat these as confirmed-exploited and patch on an emergency change.

---

## Items

### 🔴 CRITICAL — Unauthenticated attackers are bypassing Cisco ISE’s management interface (CVE-2026-76460)

*Help Net Security · 2026-09-17 · [source](https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/)* `KEV`

**Affected:** cisco  
**Device types:** generic  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** Two days after it warned customers about an actively exploited email gateway zero-day, Cisco confirmed one more flaw is being targeted: CVE-2026-76460, an authentication bypass bug in an API of Cisco Identity Services Engine (ISE). About CVE-2026-76460 Cisco ISE is an identity-based network access control and policy platform. It checks connecting users&#8217; identity, profiles devices and checks 

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Firewall Adaptive Security Appliance (ASA) Software, Cisco Secure Firewall Threat Defense (FTD) Software and Cisco Secure Firewall Management Center (FMC) Software engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address 

**Why it matters.** Matched network-device keywords: actively exploited, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks

*The Hacker News · 2026-09-17 · [source](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)* `KEV`

**Affected:** cisco  
**Device types:** generic  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** Cisco has warned of a fresh maximum-severity security flaw impacting Identity Services Engine (ISE) that has come under active exploitation. The vulnerability, tracked as CVE-2026-76460 (CVSS score: 10.0), could allow an unauthenticated, remote attacker to bypass authentication. "This vulnerability is due to insufficient authentication control on an API endpoint," Cisco said. "An attacker

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Cisco Identity Services Engine Hardening Release: September 2026

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T)* `vendor-advisory`

**Affected:** cisco  
**Device types:** generic  

**What happened.** As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) engineering teams have conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. These vulnerabilities were found during

**Why it matters.** Matched network-device keywords: actively exploited, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Nexus 9000 Series Switches Silicon One Remote Code Execution Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr)* `vendor-advisory`

**Affected:** cisco  
**Device types:** switch  

**What happened.** A vulnerability in the Silicon One integration for Cisco Nexus 9000 Series Switches could allow an unauthenticated, remote attacker to execute code with root privileges. This vulnerability exists because TCP ports 43210 and 43211 are accessible in the default Layer 3 (L3) virtual routing and forwarding (VRF). A successful exploit could allow the attacker to connect to an affected device and send c

**Why it matters.** Matched network-device keywords: unauthenticated, remote code execution, rce

**Recommended actions**

- Upgrade NOS to the fixed release; validate ISSU/hitless upgrade path for core and distribution switches first.
- Restrict management plane with control-plane policing and management ACLs; move to out-of-band management.
- Disable unused ports, set unused ports to an unrouted VLAN, and enforce 802.1X or MAC authentication on access ports.
- Harden SNMP (v3 with auth+priv only, no public/private community strings) and disable legacy protocols.
- Segment management, user, guest and OT traffic; verify VLAN ACLs and private VLAN enforcement.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall, vpn  

**What happened.** A vulnerability in the certification authentication feature of Internet Key Exchange version 2 (IKEv2) for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause an affected device to reload unexpectedly. This vulnerability is due to a logic error during the certificate authen

**Why it matters.** Matched network-device keywords: kev, unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Management Center Software Java Deserialization Remote Code Execution Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in the External Database Access feature of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to execute arbitrary commands as root on an affected device. This vulnerability is due to insecure deserialization of a user-supplied Java byte stream from a host that is configured in the external database access list. An attacker could 

**Why it matters.** Matched network-device keywords: unauthenticated, remote code execution

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Management Center Software Authentication Bypass Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system. This vulnerability is due to an improper system process that is created at boot time. An attacker could exploit this vulnerabil

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Management Center and Secure Firewall Threat Defense Software sftunnel Vulnerabilities

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** Multiple vulnerabilities in Cisco Secure Firewall Management Center (FMC) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated attacker to perform an sftunnel authentication bypass or sftunnel denial of service (DoS) attack. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released software updates that

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in the EIGRP implementation in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, adjacent attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition. This vulnerability is due to improper resource management when handling EIGRP update mes

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in Datagram TLS (DTLS) message handling of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software for Cisco Secure Firewall 3100 Series and 4200 Series devices could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device. This vulnerability is due to improper reso

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall, vpn  

**What happened.** A vulnerability in the Remote Access SSL VPN service for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition. This vulnerability is due to insufficient error checking when processing HTTP re

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software SSL VPN Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftdvirtual-dos-MuenGnYR)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall, vpn  

**What happened.** Update for September 16, 2026: The original 1.0 version of this advisory was specific to the Cisco Adaptive Security Virtual Appliance (ASAv) and Cisco Secure Firewall Threat Defense Virtual (FTDv) models. However, it was later found that this vulnerability affects all Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software platforms

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Identity Services Engine Authentication Bypass Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5)* `vendor-advisory`

**Affected:** cisco  
**Device types:** generic  

**What happened.** A vulnerability in an API of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote attacker to bypass authentication. This vulnerability is due to insufficient authentication control on an API endpoint. An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint. A successful exploit could allow the attacker to gain unauthorized acces

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Advance Notification for Publication of August 19, 2026, Security Advisories

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d)* `vendor-advisory`

**Affected:** cisco, ubiquiti  
**Device types:** switch  
**CVEs:** [CVE-2026-20030](https://nvd.nist.gov/vuln/detail/CVE-2026-20030), [CVE-2026-20231](https://nvd.nist.gov/vuln/detail/CVE-2026-20231), [CVE-2026-20232](https://nvd.nist.gov/vuln/detail/CVE-2026-20232), [CVE-2026-20302](https://nvd.nist.gov/vuln/detail/CVE-2026-20302), [CVE-2026-20315](https://nvd.nist.gov/vuln/detail/CVE-2026-20315), [CVE-2026-20317](https://nvd.nist.gov/vuln/detail/CVE-2026-20317), [CVE-2026-20318](https://nvd.nist.gov/vuln/detail/CVE-2026-20318), [CVE-2026-20319](https://nvd.nist.gov/vuln/detail/CVE-2026-20319), [CVE-2026-20320](https://nvd.nist.gov/vuln/detail/CVE-2026-20320), [CVE-2026-20327](https://nvd.nist.gov/vuln/detail/CVE-2026-20327), [CVE-2026-20357](https://nvd.nist.gov/vuln/detail/CVE-2026-20357), [CVE-2026-20358](https://nvd.nist.gov/vuln/detail/CVE-2026-20358), [CVE-2026-20359](https://nvd.nist.gov/vuln/detail/CVE-2026-20359)  

**What happened.** On August 19, 2026, the Cisco Product Security Incident Response Team (PSIRT) published the following advisories: Cisco Security Advisory CVE ID Security Impact Rating CVSS Base Score Cisco Crosswork Security Hardening Release: August 2026 CVE-2026-20030 CVE-2026-20357 CVE-2026-20358 CVE-2026-20359 Critical 10.0 Cisco Secure Workload Software Security Hardening Release: August 2026 CVE-2026-20231 

**Why it matters.** Matched network-device keywords: switch

**Recommended actions**

- Upgrade NOS to the fixed release; validate ISSU/hitless upgrade path for core and distribution switches first.
- Restrict management plane with control-plane policing and management ACLs; move to out-of-band management.
- Disable unused ports, set unused ports to an unrouted VLAN, and enforce 802.1X or MAC authentication on access ports.
- Harden SNMP (v3 with auth+priv only, no public/private community strings) and disable legacy protocols.
- Segment management, user, guest and OT traffic; verify VLAN ACLs and private VLAN enforcement.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Desk Phone 9800 Series, IP Phone 7800 and 8800 Series, and Video Phone 8875 with SIP Software Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phone-dos-txMYNRzv)* `vendor-advisory`

**Affected:** cisco, ubiquiti  
**Device types:** generic  

**What happened.** A vulnerability in Cisco Desk Phone 9800 Series, Cisco IP Phone 7800 and 8800 Series, and Cisco Video Phone 8875 that are running Cisco Session Initiation Protocol (SIP) Software could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device. This vulnerability is due to improper memory management when an affected device processes HTTP packets. A

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Advance Notification for Publication of September 2, 2026, Security Advisories

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-f2SiMFxl)* `vendor-advisory`

**Affected:** cisco  
**Device types:** switch  
**CVEs:** [CVE-2026-20212](https://nvd.nist.gov/vuln/detail/CVE-2026-20212), [CVE-2026-20274](https://nvd.nist.gov/vuln/detail/CVE-2026-20274), [CVE-2026-20275](https://nvd.nist.gov/vuln/detail/CVE-2026-20275), [CVE-2026-20276](https://nvd.nist.gov/vuln/detail/CVE-2026-20276), [CVE-2026-20277](https://nvd.nist.gov/vuln/detail/CVE-2026-20277), [CVE-2026-20278](https://nvd.nist.gov/vuln/detail/CVE-2026-20278), [CVE-2026-20279](https://nvd.nist.gov/vuln/detail/CVE-2026-20279), [CVE-2026-20280](https://nvd.nist.gov/vuln/detail/CVE-2026-20280), [CVE-2026-20281](https://nvd.nist.gov/vuln/detail/CVE-2026-20281), [CVE-2026-20354](https://nvd.nist.gov/vuln/detail/CVE-2026-20354), [CVE-2026-20355](https://nvd.nist.gov/vuln/detail/CVE-2026-20355)  

**What happened.** On September 2, 2026, the Cisco Product Security Incident Response Team (PSIRT) published the following advisories: Cisco Security Advisory CVE ID Security Impact Rating CVSS Base Score Cisco IOS XR Software Security Hardening Release: September 2026 CVE-2026-20277 CVE-2026-20278 CVE-2026-20280 CVE-2026-20279 CVE-2026-20276 CVE-2026-20275 CVE-2026-20274 Critical 9.8 Cisco Nexus 9000 Series Switche

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Upgrade NOS to the fixed release; validate ISSU/hitless upgrade path for core and distribution switches first.
- Restrict management plane with control-plane policing and management ACLs; move to out-of-band management.
- Disable unused ports, set unused ports to an unrouted VLAN, and enforce 802.1X or MAC authentication on access ports.
- Harden SNMP (v3 with auth+priv only, no public/private community strings) and disable legacy protocols.
- Segment management, user, guest and OT traffic; verify VLAN ACLs and private VLAN enforcement.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco UCS and UCS-Based Appliances UEFI Shell Secure Boot Bypass Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW)* `vendor-advisory`

**Affected:** cisco, ubiquiti  
**Device types:** generic  

**What happened.** A vulnerability in the Unified Extensible Firmware Interface (UEFI) Shell implementation of Cisco UCS Servers and UCS-based appliances could allow an authenticated attacker with valid credentials for a user account with the role of user or admin or an unauthenticated attacker with physical access to an affected device to bypass UEFI Secure Boot validation checks and execute unauthorized software. 

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Identity Services Engine 802.1X Session Hijack and Information Disclosure Vulnerabilities

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-vuln-kWLeNnRD)* `vendor-advisory`

**Affected:** cisco  
**Device types:** generic  

**What happened.** Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an unauthenticated, local attacker to either conduct an authentication bypass or disclose sensitive information. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released software updates that address these vulnerabilities. There are no workarounds that address these vu

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Identity Services Engine Remote Code Execution Vulnerabilities

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57)* `vendor-advisory`

**Affected:** cisco  
**Device types:** generic  

**What happened.** Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an affected device. To exploit these vulnerabilities, the attacker must have valid administrative credentials. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released

**Why it matters.** Matched network-device keywords: remote code execution, rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Management Center Software Static Credential Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to log in to an affected device using a low-privileged account to access sensitive data within the impacted systems. This vulnerability is due to the presence of static user credentials for a low-privileged account. An attacker could exploit this vulnerabil

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Email Secure/Multipurpose Internet Mail Extensions Ciphertext Decryption Vulnerabilities

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY)* `vendor-advisory`

**Affected:** cisco  
**Device types:** generic  
**CVEs:** [CVE-2026-20354](https://nvd.nist.gov/vuln/detail/CVE-2026-20354), [CVE-2026-20355](https://nvd.nist.gov/vuln/detail/CVE-2026-20355)  

**What happened.** Multiple vulnerabilities in the Secure/Multipurpose Internet Mail Extensions (S/MIME) decryption functionality of Cisco Secure Email could allow an unauthenticated, remote attacker to recover plain text from encrypted email messages. These vulnerabilities are due to insufficient validation of message integrity. An attacker could exploit these vulnerabilities by using a machine-in-the-middle techni

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Logging Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in the system rate-limiting process for syslog message 419002 of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause high CPU utilization on an affected device, resulting in a denial of service (DoS) condition. This vulnerability is due to improper rate limi

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Object Group Access Control List Bypass Vulnerabilities

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** Multiple vulnerabilities in the access control list (ACL) Object Group Search (OGS) implementation of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to bypass configured access controls. These vulnerabilities are due to a logic error in populating group access control policies 

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Cisco Secure Firewall Threat Defense Software Snort 2 SSL/TLS Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-snort2-ssldos-Mw7WYX9c)* `vendor-advisory`

**Affected:** cisco  
**Device types:** firewall  

**What happened.** A vulnerability in SSL/TLS certificate parsing in the Snort 2 Detection Engine of Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause the Snort 2 Detection Engine to restart. This vulnerability is due to incomplete validation of the SSL certificate. An attacker could exploit this vulnerability by sending a crafted SSL connection setup reques

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

<!--index
{
 "url": "/2026/09/17/network-security-digest/",
 "date": "2026-09-17",
 "entries": [
  {
   "title": "Unauthenticated attackers are bypassing Cisco ISE\u2019s management interface (CVE-2026-76460)",
   "link": "https://www.helpnetsecurity.com/2026/09/17/cisco-ise-vulnerability-exploited-cve-2026-76460/",
   "source": "Help Net Security",
   "relevance": "critical",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-76460"
   ],
   "kev": true
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN",
   "source": "Cisco PSIRT",
   "relevance": "critical",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks",
   "link": "https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html",
   "source": "The Hacker News",
   "relevance": "critical",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-76460"
   ],
   "kev": true
  },
  {
   "title": "Cisco Identity Services Engine Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T",
   "source": "Cisco PSIRT",
   "relevance": "critical",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Nexus 9000 Series Switches Silicon One Remote Code Execution Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "switch"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Management Center Software Java Deserialization Remote Code Execution Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Management Center Software Authentication Bypass Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Management Center and Secure Firewall Threat Defense Software sftunnel Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software SSL VPN Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftdvirtual-dos-MuenGnYR",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Identity Services Engine Authentication Bypass Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Advance Notification for Publication of August 19, 2026, Security Advisories",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "switch"
   ],
   "vendors": [
    "cisco",
    "ubiquiti"
   ],
   "cves": [
    "CVE-2026-20030",
    "CVE-2026-20231",
    "CVE-2026-20232",
    "CVE-2026-20302",
    "CVE-2026-20315",
    "CVE-2026-20317",
    "CVE-2026-20318",
    "CVE-2026-20319",
    "CVE-2026-20320",
    "CVE-2026-20327",
    "CVE-2026-20357",
    "CVE-2026-20358",
    "CVE-2026-20359"
   ],
   "kev": false
  },
  {
   "title": "Cisco Desk Phone 9800 Series, IP Phone 7800 and 8800 Series, and Video Phone 8875 with SIP Software Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phone-dos-txMYNRzv",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco",
    "ubiquiti"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Advance Notification for Publication of September 2, 2026, Security Advisories",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-f2SiMFxl",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "switch"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-20212",
    "CVE-2026-20274",
    "CVE-2026-20275",
    "CVE-2026-20276",
    "CVE-2026-20277",
    "CVE-2026-20278",
    "CVE-2026-20279",
    "CVE-2026-20280",
    "CVE-2026-20281",
    "CVE-2026-20354",
    "CVE-2026-20355"
   ],
   "kev": false
  },
  {
   "title": "Cisco UCS and UCS-Based Appliances UEFI Shell Secure Boot Bypass Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco",
    "ubiquiti"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Identity Services Engine 802.1X Session Hijack and Information Disclosure Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-vuln-kWLeNnRD",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Identity Services Engine Remote Code Execution Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Management Center Software Static Credential Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Email Secure/Multipurpose Internet Mail Extensions Ciphertext Decryption Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "generic"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-20354",
    "CVE-2026-20355"
   ],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Logging Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Object Group Access Control List Bypass Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Threat Defense Software Snort 2 SSL/TLS Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-snort2-ssldos-Mw7WYX9c",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [],
   "kev": false
  }
 ]
}
-->

## How this was produced

- Feeds polled: 19 ok, 0 failed
- Raw items: 700 → in window: 111 → network-device relevant: 56 → published: 25
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `rule-based`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
