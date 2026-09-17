---
layout: post
title: "Network Device Security Digest - 2026-09-17"
date: 2026-09-17 22:11:22 +0000
edition: daily
critical_count: 7
item_count: 20
kev: "CVE-2026-58704, CVE-2026-76461, CVE-2026-87886"
analysis_mode: "rule-based (agent output unusable)"
categories: digest
---

# Network Device Security Digest — 2026-09-17

*daily edition · window 72h · 18 feeds · 20 items · 7 critical · generated 2026-09-17 22:11 UTC*

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

- 20 network-device items collected in the last 72h from 18 feeds.
- 5 item(s) reference CISA KEV entries.
- Model summarization disabled - rule-based advice shown.

> **On the CISA KEV catalog in this edition:** CVE-2026-58704, CVE-2026-76461, CVE-2026-87886 — treat these as confirmed-exploited and patch on an emergency change.

---

## Items

### 🔴 CRITICAL — CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild

*Rapid7 Blog · 2026-09-15 · [source](https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild)* `KEV`

**Affected:** cisco  
**Device types:** generic  
**CVEs:** [CVE-2026-76461](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) **[KEV]**  

**What happened.** Overview On September 14, 2026, Cisco published a security advisory for CVE-2026-76461 , a critical SQL injection vulnerability affecting Cisco AsyncOS Software for Cisco Secure Email Gateway. The vulnerability has a reported CVSS v3.1 base score of 9.8 and could allow an unauthenticated, remote attacker to execute arbitrary commands with root privileges on an affected appliance. Cisco Secure Emai

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution

*The Hacker News · 2026-09-15 · [source](https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html)* `KEV`

**Affected:** cisco  
**Device types:** generic  
**CVEs:** [CVE-2026-76461](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) **[KEV]**  

**What happened.** Cisco has warned that a new critical vulnerability impacting AsyncOS Software for Cisco Secure Email Gateway has come under active exploitation in the wild. The vulnerability, tracked as CVE-2026-76461, carries a CVSS score of 9.8 out of a maximum of 10.0. It has been described as a case of insufficient validation in the email parsing logic that could allow an unauthenticated, remote attacker

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — CISA KEV addition: Google Pixel - CVE-2026-58704

*CISA KEV catalog · 2026-09-16 · [source](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-58704)* `KEV`

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-58704](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) **[KEV]**  

**What happened.** Google Pixel Improper Authorization Vulnerability. Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges. Required action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see UR

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Google Patches Pixel Modem Flaw Amid Signs of Limited Targeted Exploitation

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/google-patches-pixel-modem-flaw-amid.html)* `KEV`

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-58704](https://nvd.nist.gov/vuln/detail/CVE-2026-58704) **[KEV]**  

**What happened.** Google has disclosed that a high-severity security flaw in its Pixel Cellular Modem has come under exploitation in the wild. The vulnerability, tracked as CVE-2026-58704 (CVSS score: 8.0), is a privilege escalation flaw. "In Cellular Modem, there is a possible permission bypass due to a logic error in the code," according to a description of the bug in the NIST National Vulnerability Database

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Acronis cPanel Backup Plugin Vulnerability Exploited in Targeted Attacks

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/acronis-cpanel-backup-plugin.html)* `KEV`

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-87886](https://nvd.nist.gov/vuln/detail/CVE-2026-87886) **[KEV]**  

**What happened.** Acronis has warned that a high-severity security flaw in its Backup plugin for cPanel and Web Host Manager (WHM) deployments has been exploited in the wild. The vulnerability, tracked as CVE-2026-87886 (CVSS score: 7.8), is described as a case of local privilege escalation due to insecure file permissions. It affects the following versions - Acronis Backup plugin for cPanel & WHM (Linux

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — China-Linked Hackers Exploit Chrome-Windows Zero-Day Chain to Deploy GRIMWEDGE

*The Hacker News · 2026-09-15 · [source](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html)* 

**Affected:** see advisory  
**Device types:** generic  

**What happened.** A Chinese threat actor has been attributed to a spear-phishing campaign that exploits recently patched security flaws in Google Chrome and Microsoft Windows to deliver a malicious JavaScript backdoor called GRIMWEDGE. Volexity, which is tracking the threat cluster under the moniker UTA0560, said the activity targeted multiple non-governmental organizations (NGOs) on September 1, 2026. "The

**Why it matters.** Matched network-device keywords: zero-day, backdoor

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🔴 CRITICAL — Active Exploitation Attempts Target WSO2 API Manager JWT Bypass With Forged Admin Tokens

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/active-exploitation-attempts-target.html)* 

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-5430](https://nvd.nist.gov/vuln/detail/CVE-2026-5430)  

**What happened.** A critical security flaw in WSO2 API Manager has come under active exploitation in the wild, according to findings from watchTowr. The vulnerability, tracked as CVE-2026-5430 (CVSS score: 9.8/10.0), is a case of improper verification of a cryptographic signature that could result in account takeover. Hacktron Team has been credited with discovering and reporting the flaw. "JWT authentication

**Why it matters.** Matched network-device keywords: in the wild

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Attackers Exploit WooCommerce Wholesale Lead Capture Flaw to Plant PHP Web Shells

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/attackers-exploit-woocommerce-wholesale.html)* 

**Affected:** see advisory  
**Device types:** generic  

**What happened.** Threat actors are exploiting a critical security flaw in WooCommerce Wholesale Lead Capture, a premium WordPress plugin that has more than 6,000 active installs. "This vulnerability can be leveraged by unauthenticated attackers to upload arbitrary files, including PHP backdoors, and achieve remote code execution," Wordfence said. The WordPress security company said it has blocked over

**Why it matters.** Matched network-device keywords: unauthenticated, remote code execution, rce, backdoor

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟠 HIGH — Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html)* 

**Affected:** ubiquiti  
**Device types:** generic  
**CVEs:** [CVE-2026-89026](https://nvd.nist.gov/vuln/detail/CVE-2026-89026)  

**What happened.** A critical security flaw in Issabel Framework, a web-based framework for the open-source unified communications PBX software, has come under active exploitation. The vulnerability in question is CVE-2026-89026 (CVSS v3.1 score: 9.8/CVSS v4.0 score: 9.3), which can allow an unauthenticated remote attacker to execute arbitrary operating system (OS) commands by taking advantage of a hard-coded

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — ZDI-26-709: Cisco Secure Firewall Management Center CommandSinkRmi Deserialization of Untrusted Data Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-709/)* 

**Affected:** cisco  
**Device types:** firewall  
**CVEs:** [CVE-2026-20242](https://nvd.nist.gov/vuln/detail/CVE-2026-20242)  

**What happened.** This vulnerability allows remote attackers to execute arbitrary code on affected installations of Cisco Secure Firewall Management Center. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.1. The following CVEs are assigned: CVE-2026-20242.

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — CVE-2026-0307 GlobalProtect App: Local Privilege Escalation Vulnerabilities (Severity: MEDIUM)

*Palo Alto Networks PSIRT · 2026-09-16 · [source](https://security.paloaltonetworks.com/CVE-2026-0307)* `vendor-advisory`

**Affected:** palo alto  
**Device types:** generic  
**CVEs:** [CVE-2026-0307](https://nvd.nist.gov/vuln/detail/CVE-2026-0307)  

**What happened.** CVE-2026-0307 GlobalProtect App: Local Privilege Escalation Vulnerabilities (Severity: MEDIUM)

**Why it matters.** Matched network-device keywords: generic

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — Three Threat Groups Target Russian Enterprises With Backdoors, Ransomware, and Wipers

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html)* 

**Affected:** see advisory  
**Device types:** generic  

**What happened.** Enterprises in Russia have emerged as the target of three threat activity clusters tracked as NightEagle, Hacking Cat, and Toy Ghouls, according to multiple reports from Kaspersky. The cybersecurity vendor said it has identified attacks mounted by NightEagle (aka APT-Q-95), a threat actor known to be active since at least 2023, that involve new techniques for persistence and lateral movement.

**Why it matters.** Matched network-device keywords: backdoor, ransomware

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — Attacker Hijacks AI Coding Assistant Session, Spreads Shai-Hulud Across About 100 Repositories

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/attacker-hijacks-ai-coding-assistant.html)* `AI`

**Affected:** see advisory  
**Device types:** generic  

**What happened.** Mandiant says an attacker hijacked an active AI coding-assistant session at an unnamed software-as-a-service provider and later spread Shai-Hulud across about 100 internal code repositories. Before the repository spread, the assistant recommended software that the attacker had poisoned, and the recommendation was accepted. The worm stole repository secrets and source code for the

**Why it matters.** Matched network-device keywords: rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

**AI angle.** AI/ML mentioned in the source.

---

### 🟡 MEDIUM — Securing the unpatchable in an age of AI-driven vulnerabilities

*Cisco Talos · 2026-09-16 · [source](https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/)* `AI`

**Affected:** see advisory  
**Device types:** firewall  

**What happened.** Advances in AI technology will continue to identify vulnerabilities that in some circumstances are difficult, or effectively impossible, to patch. Appropriate network segmentation, rigorous visibility, and the deployment of NGFW/IPS combinations can provide a powerful compensatory layer.

**Why it matters.** Matched network-device keywords: firewall

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

**AI angle.** AI/ML mentioned in the source.

---

### 🟡 MEDIUM — Human Attacker Exploits Marimo RCE, Reaches SSH Bastion in Eight Seconds

*The Hacker News · 2026-09-15 · [source](https://thehackernews.com/2026/09/human-attacker-exploits-marimo-rce.html)* `AI`

**Affected:** see advisory  
**Device types:** generic  

**What happened.** With artificial intelligence (AI) shrinking the window between vulnerability discovery and exploitation and lowering the barrier to entry for bad actors, new findings from Sysdig show that skilled human operators can move just as swiftly after gaining initial access. In one instance highlighted by the cloud security company, the threat actor pivoted from a vulnerable Marimo notebook to an SSH

**Why it matters.** Matched network-device keywords: rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

**AI angle.** AI/ML mentioned in the source.

---

### 🟡 MEDIUM — ZDI-26-713: GIMP APNG File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-713/)* 

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-92183](https://nvd.nist.gov/vuln/detail/CVE-2026-92183)  

**What happened.** This vulnerability allows remote attackers to execute arbitrary code on affected installations of GIMP. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The ZDI has assigned a CVSS rating of 7.8. The following CVEs are assigned: CVE-2026-92183.

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — ZDI-26-710: NoMachine mDNS Heap-based Buffer Overflow Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-710/)* 

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-92208](https://nvd.nist.gov/vuln/detail/CVE-2026-92208)  

**What happened.** This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of NoMachine. Authentication is not required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-92208.

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — ZDI-26-707: (0Day) MindsDB OpenBBtable Code Injection Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-707/)* 

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-92207](https://nvd.nist.gov/vuln/detail/CVE-2026-92207)  

**What happened.** This vulnerability allows remote attackers to execute arbitrary code on affected installations of MindsDB. Authentication is required to exploit this vulnerability. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-92207.

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — ZDI-26-706: (0Day) CrewAI crewAI Framework Agent Loading Unsafe Reflection Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-706/)* 

**Affected:** see advisory  
**Device types:** generic  
**CVEs:** [CVE-2026-92206](https://nvd.nist.gov/vuln/detail/CVE-2026-92206)  

**What happened.** This vulnerability allows remote attackers to execute arbitrary code on affected installations of CrewAI crewAI. User interaction is required to exploit this vulnerability in that the target must load a malicious agent configuration from the repository. The ZDI has assigned a CVSS rating of 8.8. The following CVEs are assigned: CVE-2026-92206.

**Why it matters.** Matched network-device keywords: remote code execution

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

### 🟡 MEDIUM — Mass-Scanning Campaign Exploits Vite Flaw to Extract Cloud Credentials From Exposed Dev Servers

*The Hacker News · 2026-09-15 · [source](https://thehackernews.com/2026/09/mass-scanning-campaign-exploits-vite.html)* 

**Affected:** f5  
**Device types:** generic  

**What happened.** Cybersecurity researchers have disclosed details of a mass-scanning campaign that has targeted Vite deployments siphon sensitive data. The first is an automated effort aimed at internet-exposed Vite development servers that's designed to steal cloud credentials, configurations from Amazon Web Services (AWS) and Microsoft Azure instances, and infrastructure state files, per F5 Labs. The

**Why it matters.** Matched network-device keywords: generic

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

---

## Watchlist (low confidence, not yet triaged)

- [AI Security Spending Jumps as Fear Outpaces Proof of Value](https://www.darkreading.com/cybersecurity-operations/ai-security-spending-jumps-fear-outpaces-proof-value) — *Dark Reading*
- [Malware bypasses browser checks to force install Chrome, Edge extensions](https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/) — *BleepingComputer*
- [Data Broker Radaris Loses Domains in Privacy Fight](https://krebsonsecurity.com/2026/09/data-broker-radaris-loses-domains-in-privacy-fight/) — *Krebs on Security*
- [Spain's data agency gets first report of AI-powered data breach](https://www.bleepingcomputer.com/news/security/spains-data-agency-gets-first-report-of-ai-powered-data-breach/) — *BleepingComputer*
- [BragJack Attack Can Turn a Browser's Agentic AI Against It](https://www.darkreading.com/endpoint-security/bragjack-browser-agentic-ai) — *Dark Reading*
- [One Extension Could Hijack AI Assistants Across Chrome, Comet, Edge, Opera Neon and Claude](https://thehackernews.com/2026/09/one-extension-could-hijack-ai.html) — *The Hacker News*
- [The true cost of a ransomware attack, with and without BCDR](https://www.bleepingcomputer.com/news/security/the-true-cost-of-a-ransomware-attack-with-and-without-bcdr/) — *BleepingComputer*
- [Cyber Op Targets South Korean Media & Automotive Sectors](https://www.darkreading.com/cyberattacks-data-breaches/cyber-south-korean-media-automotive) — *Dark Reading*
- [Black Hat USA 2026 | OpenAI's Deep Dive Into Hugging Face Incident](https://www.darkreading.com/vulnerabilities-threats/bhusa26huggingfacetalk) — *Dark Reading*

## How this was produced

- Feeds polled: 18 ok, 1 failed
- Raw items: 670 → in window: 72 → network-device relevant: 29 → published: 20
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `rule-based (agent output unusable)`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
