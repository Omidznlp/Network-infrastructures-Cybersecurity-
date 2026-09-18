---
layout: post
title: "Network Device Security Digest - 2026-09-18"
date: 2026-09-18 21:46:19 +0000
edition: daily
critical_count: 3
item_count: 25
kev: "CVE-2026-76460"
analysis_mode: "rule-based"
categories: digest
---

# Network Device Security Digest — 2026-09-18

*daily edition · window 24h · 19 feeds · 25 items · 3 critical · generated 2026-09-18 21:46 UTC*

> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers, management platforms and SD-WAN edge. Everything else is filtered out.

---

## 📌 Top story — Cisco Nexus 9000 Series Switches Silicon One Remote Code Execution Vulnerability

A vulnerability in the Silicon One integration for Cisco Nexus 9000 Series Switches could allow an unauthenticated, remote attacker to execute code with root privileges. This vulnerability exists because TCP ports 43210 and 43211 are accessible in the default Layer 3 (L3) virtual routing and forwarding (VRF). A successful exploit could allow the attacker to connect to an affected device and send c

**Do this first**

- Upgrade NOS to the fixed release; validate ISSU/hitless upgrade path for core and distribution switches first.
- Restrict management plane with control-plane policing and management ACLs; move to out-of-band management.
- Disable unused ports, set unused ports to an unrouted VLAN, and enforce 802.1X or MAC authentication on access ports.
- Harden SNMP (v3 with auth+priv only, no public/private community strings) and disable legacy protocols.
- Segment management, user, guest and OT traffic; verify VLAN ACLs and private VLAN enforcement.

---

> **On the CISA KEV catalog in this edition:** CVE-2026-76460 — treat these as confirmed-exploited and patch on an emergency change.

## Executive summary

- 57 network-device items collected in the last 24h from 19 feeds.
- 1 item(s) reference CISA KEV entries.
- Model summarization unavailable - rule-based advice shown.

---

## Items by vendor

## Cisco

*25 item(s) — 3 critical, 22 high*

### Firewalls

#### 🔴 CRITICAL — Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN) · 2026-09-18* `vendor-advisory`

> As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Firewall Adaptive Security Appliance (ASA) Software, Cisco Secure Firewall Threat Defense…

**Affected:** Cisco  

**What happened.** As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Firewall Adaptive Security Appliance (ASA) Software, Cisco Secure Firewall Threat Defense (FTD) Software and Cisco Secure Firewall Management Center (FMC) Software engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address 

**Why it matters.** Matched network-device keywords: actively exploited, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv) · 2026-09-18* `vendor-advisory`

> A vulnerability in the certification authentication feature of Internet Key Exchange version 2 (IKEv2) for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure…

**Affected:** Cisco  

**What happened.** A vulnerability in the certification authentication feature of Internet Key Exchange version 2 (IKEv2) for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause an affected device to reload unexpectedly. This vulnerability is due to a logic error during the certificate authen

**Why it matters.** Matched network-device keywords: kev, unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv)**

#### 🟠 HIGH — Cisco Secure Firewall Management Center Software Java Deserialization Remote Code Execution Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk) · 2026-09-18* `vendor-advisory`

> A vulnerability in the External Database Access feature of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to execute arbitrary…

**Affected:** Cisco  

**What happened.** A vulnerability in the External Database Access feature of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to execute arbitrary commands as root on an affected device. This vulnerability is due to insecure deserialization of a user-supplied Java byte stream from a host that is configured in the external database access list. An attacker could 

**Why it matters.** Matched network-device keywords: unauthenticated, remote code execution

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-javarce-y2NypXwk)**

#### 🟠 HIGH — Cisco Secure Firewall Management Center Software Authentication Bypass Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2) · 2026-09-18* `vendor-advisory`

> A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to bypass authentication and execute script…

**Affected:** Cisco  

**What happened.** A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to bypass authentication and execute script files on an affected device to obtain root access to the underlying operating system. This vulnerability is due to an improper system process that is created at boot time. An attacker could exploit this vulnerabil

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2)**

#### 🟠 HIGH — Cisco Secure Firewall Management Center and Secure Firewall Threat Defense Software sftunnel Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3) · 2026-09-18* `vendor-advisory`

> Multiple vulnerabilities in Cisco Secure Firewall Management Center (FMC) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated attacker to perform…

**Affected:** Cisco  

**What happened.** Multiple vulnerabilities in Cisco Secure Firewall Management Center (FMC) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated attacker to perform an sftunnel authentication bypass or sftunnel denial of service (DoS) attack. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released software updates that

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmcftd-sftun-multivulns-WGVHOrN3)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF) · 2026-09-18* `vendor-advisory`

> A vulnerability in the Remote Access SSL VPN service for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow…

**Affected:** Cisco  

**What happened.** A vulnerability in the Remote Access SSL VPN service for Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition. This vulnerability is due to insufficient error checking when processing HTTP re

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software SSL VPN Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftdvirtual-dos-MuenGnYR) · 2026-09-18* `vendor-advisory`

> Update for September 16, 2026: The original 1.0 version of this advisory was specific to the Cisco Adaptive Security Virtual Appliance (ASAv) and Cisco Secure Firewall Threat Defense…

**Affected:** Cisco  

**What happened.** Update for September 16, 2026: The original 1.0 version of this advisory was specific to the Cisco Adaptive Security Virtual Appliance (ASAv) and Cisco Secure Firewall Threat Defense Virtual (FTDv) models. However, it was later found that this vulnerability affects all Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software platforms

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftdvirtual-dos-MuenGnYR)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj) · 2026-09-18* `vendor-advisory`

> A vulnerability in the EIGRP implementation in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an…

**Affected:** Cisco  

**What happened.** A vulnerability in the EIGRP implementation in Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, adjacent attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition. This vulnerability is due to improper resource management when handling EIGRP update mes

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO) · 2026-09-18* `vendor-advisory`

> A vulnerability in Datagram TLS (DTLS) message handling of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software for Cisco…

**Affected:** Cisco  

**What happened.** A vulnerability in Datagram TLS (DTLS) message handling of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software for Cisco Secure Firewall 3100 Series and 4200 Series devices could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device. This vulnerability is due to improper reso

**Why it matters.** Matched network-device keywords: unauthenticated, rce

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO)**

#### 🟠 HIGH — Cisco Secure Firewall Management Center Software Static Credential Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh) · 2026-09-18* `vendor-advisory`

> A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to log in to an affected device using a…

**Affected:** Cisco  

**What happened.** A vulnerability in the web interface of Cisco Secure Firewall Management Center (FMC) Software could allow an unauthenticated, remote attacker to log in to an affected device using a low-privileged account to access sensitive data within the impacted systems. This vulnerability is due to the presence of static user credentials for a low-privileged account. An attacker could exploit this vulnerabil

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh)**

#### 🟠 HIGH — Cisco Secure Firewall Threat Defense Software Snort 2 SSL/TLS Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-snort2-ssldos-Mw7WYX9c) · 2026-09-18* `vendor-advisory`

> A vulnerability in SSL/TLS certificate parsing in the Snort 2 Detection Engine of Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to…

**Affected:** Cisco  

**What happened.** A vulnerability in SSL/TLS certificate parsing in the Snort 2 Detection Engine of Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause the Snort 2 Detection Engine to restart. This vulnerability is due to incomplete validation of the SSL certificate. An attacker could exploit this vulnerability by sending a crafted SSL connection setup reques

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-snort2-ssldos-Mw7WYX9c)**

#### 🟠 HIGH — Cisco Secure Firewall Threat Defense Software TLS 1.3 Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-tls1.3-dos-dLxwFWgF) · 2026-09-18* `vendor-advisory`

> A vulnerability in the TLS 1.3 implementation in Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause an affected device to reload…

**Affected:** Cisco  

**What happened.** A vulnerability in the TLS 1.3 implementation in Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause an affected device to reload unexpectedly, resulting in a denial of service (DoS) condition. This vulnerability is due to improper buffer management during the TLS 1.3 connection. An attacker could exploit this vulnerability by sending a craf

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-tls1.3-dos-dLxwFWgF)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software TCP DNS Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5) · 2026-09-18* `vendor-advisory`

> A vulnerability in the DNS over TCP implementation of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an…

**Affected:** Cisco  

**What happened.** A vulnerability in the DNS over TCP implementation of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to cause the TCP DNS response handler to unexpectedly restart, causing the device to reload. This vulnerability is due to a logic error when parsing a DNS query and tracking the

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Object Group Access Control List Bypass Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw) · 2026-09-18* `vendor-advisory`

> Multiple vulnerabilities in the access control list (ACL) Object Group Search (OGS) implementation of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure…

**Affected:** Cisco  

**What happened.** Multiple vulnerabilities in the access control list (ACL) Object Group Search (OGS) implementation of Cisco Secure Firewall Adaptive Security Appliance (ASA) Software and Cisco Secure Firewall Threat Defense (FTD) Software could allow an unauthenticated, remote attacker to bypass configured access controls. These vulnerabilities are due to a logic error in populating group access control policies 

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Confirm the running version against the vendor's fixed-release table; schedule the upgrade inside the change window, HA pair secondary first.
- Remove management access (HTTPS/SSH/API) from any untrusted or internet-facing interface; restrict to a dedicated management VLAN or out-of-band network.
- Enforce MFA on all administrative and VPN accounts; remove shared local admin accounts.
- After patching, rotate local admin credentials, API keys, certificates and VPN pre-shared keys - a pre-patch compromise survives the upgrade.
- Export and review the configuration for unexpected admin users, scripts, static routes or modified login pages.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw)**

### Switches

#### 🟠 HIGH — Cisco Nexus 9000 Series Switches Silicon One Remote Code Execution Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr) · 2026-09-18* `vendor-advisory`

> A vulnerability in the Silicon One integration for Cisco Nexus 9000 Series Switches could allow an unauthenticated, remote attacker to execute code with root privileges.

**Affected:** Cisco  

**What happened.** A vulnerability in the Silicon One integration for Cisco Nexus 9000 Series Switches could allow an unauthenticated, remote attacker to execute code with root privileges. This vulnerability exists because TCP ports 43210 and 43211 are accessible in the default Layer 3 (L3) virtual routing and forwarding (VRF). A successful exploit could allow the attacker to connect to an affected device and send c

**Why it matters.** Matched network-device keywords: unauthenticated, remote code execution, rce

**Recommended actions**

- Upgrade NOS to the fixed release; validate ISSU/hitless upgrade path for core and distribution switches first.
- Restrict management plane with control-plane policing and management ACLs; move to out-of-band management.
- Disable unused ports, set unused ports to an unrouted VLAN, and enforce 802.1X or MAC authentication on access ports.
- Harden SNMP (v3 with auth+priv only, no public/private community strings) and disable legacy protocols.
- Segment management, user, guest and OT traffic; verify VLAN ACLs and private VLAN enforcement.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr)**

#### 🟠 HIGH — Cisco Advance Notification for Publication of August 19, 2026, Security Advisories

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d) · 2026-09-18* `vendor-advisory`

> On August 19, 2026, the Cisco Product Security Incident Response Team (PSIRT) published the following advisories: Cisco Security Advisory CVE ID Security Impact Rating CVSS Base Score Cisco…

**Affected:** Cisco, Ubiquiti  
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

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-LDquvx5d)**

#### 🟠 HIGH — Cisco Advance Notification for Publication of September 2, 2026, Security Advisories

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-f2SiMFxl) · 2026-09-18* `vendor-advisory`

> On September 2, 2026, the Cisco Product Security Incident Response Team (PSIRT) published the following advisories: Cisco Security Advisory CVE ID Security Impact Rating CVSS Base Score…

**Affected:** Cisco  
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

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-notice-f2SiMFxl)**

### Other

#### 🔴 CRITICAL — Cisco Zero-Day Highlights API Endpoint Authentication Issues

*[Dark Reading](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues) · 2026-09-18* `KEV`

> The authentication bypass flaw CVE-2026-76460 impacts Cisco's Identity Services Engine (ISE) and received a maximum 10 out of 10 CVSS score.

**Affected:** Cisco  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** The authentication bypass flaw CVE-2026-76460 impacts Cisco's Identity Services Engine (ISE) and received a maximum 10 out of 10 CVSS score.

**Why it matters.** Listed on the CISA KEV catalog - exploitation is confirmed.

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Dark Reading →](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)**

#### 🔴 CRITICAL — Cisco Identity Services Engine Hardening Release: September 2026

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T) · 2026-09-18* `vendor-advisory`

> As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) engineering…

**Affected:** Cisco  

**What happened.** As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) engineering teams have conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered vulnerabilities. These vulnerabilities were found during

**Why it matters.** Matched network-device keywords: actively exploited, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T)**

#### 🟠 HIGH — Cisco Identity Services Engine Authentication Bypass Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5) · 2026-09-18* `vendor-advisory`

> A vulnerability in an API of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote attacker to bypass authentication.

**Affected:** Cisco  

**What happened.** A vulnerability in an API of Cisco Identity Services Engine (ISE) could allow an unauthenticated, remote attacker to bypass authentication. This vulnerability is due to insufficient authentication control on an API endpoint. An attacker could exploit this vulnerability by sending a crafted request to an affected API endpoint. A successful exploit could allow the attacker to gain unauthorized acces

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5)**

#### 🟠 HIGH — Cisco Desk Phone 9800 Series, IP Phone 7800 and 8800 Series, and Video Phone 8875 with SIP Software Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phone-dos-txMYNRzv) · 2026-09-18* `vendor-advisory`

> A vulnerability in Cisco Desk Phone 9800 Series, Cisco IP Phone 7800 and 8800 Series, and Cisco Video Phone 8875 that are running Cisco Session Initiation Protocol (SIP) Software could…

**Affected:** Cisco, Ubiquiti  

**What happened.** A vulnerability in Cisco Desk Phone 9800 Series, Cisco IP Phone 7800 and 8800 Series, and Cisco Video Phone 8875 that are running Cisco Session Initiation Protocol (SIP) Software could allow an unauthenticated, remote attacker to cause a denial of service (DoS) condition on an affected device. This vulnerability is due to improper memory management when an affected device processes HTTP packets. A

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phone-dos-txMYNRzv)**

#### 🟠 HIGH — Cisco UCS and UCS-Based Appliances UEFI Shell Secure Boot Bypass Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW) · 2026-09-18* `vendor-advisory`

> A vulnerability in the Unified Extensible Firmware Interface (UEFI) Shell implementation of Cisco UCS Servers and UCS-based appliances could allow an authenticated attacker with valid…

**Affected:** Cisco, Ubiquiti  

**What happened.** A vulnerability in the Unified Extensible Firmware Interface (UEFI) Shell implementation of Cisco UCS Servers and UCS-based appliances could allow an authenticated attacker with valid credentials for a user account with the role of user or admin or an unauthenticated attacker with physical access to an affected device to bypass UEFI Secure Boot validation checks and execute unauthorized software. 

**Why it matters.** Matched network-device keywords: unauthenticated

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW)**

#### 🟠 HIGH — Cisco Identity Services Engine 802.1X Session Hijack and Information Disclosure Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-vuln-kWLeNnRD) · 2026-09-18* `vendor-advisory`

> Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an unauthenticated, local attacker to either conduct an authentication bypass or disclose sensitive information.

**Affected:** Cisco  

**What happened.** Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an unauthenticated, local attacker to either conduct an authentication bypass or disclose sensitive information. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released software updates that address these vulnerabilities. There are no workarounds that address these vu

**Why it matters.** Matched network-device keywords: unauthenticated, authentication bypass

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-vuln-kWLeNnRD)**

#### 🟠 HIGH — Cisco Identity Services Engine Remote Code Execution Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57) · 2026-09-18* `vendor-advisory`

> Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an…

**Affected:** Cisco  

**What happened.** Multiple vulnerabilities in Cisco Identity Services Engine (ISE) could allow an authenticated, remote attacker to execute arbitrary commands on the underlying operating system of an affected device. To exploit these vulnerabilities, the attacker must have valid administrative credentials. For more information about these vulnerabilities, see the Details section of this advisory. Cisco has released

**Why it matters.** Matched network-device keywords: remote code execution, rce

**Recommended actions**

- Identify affected devices from your asset inventory, filtered by model and running version.
- Apply the vendor fixed release, or the documented workaround if a maintenance window is not available yet.
- Reduce exposure now: management interfaces off the internet, ACLs on the management plane, MFA on all admin access.
- Ship device logs to the SIEM and alert on admin logins, config changes and firmware changes.
- Record the decision (patched / mitigated / accepted risk) against the device group in the change record.

**Legacy / unpatchable gear.** Legacy or end-of-life gear will not receive a fix: isolate it behind a supported inspecting firewall and deny inbound access from untrusted zones.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57)**

#### 🟠 HIGH — Cisco Secure Email Secure/Multipurpose Internet Mail Extensions Ciphertext Decryption Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY) · 2026-09-18* `vendor-advisory`

> Multiple vulnerabilities in the Secure/Multipurpose Internet Mail Extensions (S/MIME) decryption functionality of Cisco Secure Email could allow an unauthenticated, remote attacker to…

**Affected:** Cisco  
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

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY)**

---

## 🧠 AI & network devices — AI-found bugs land where you cannot patch fast: pre-auth flaws in appliances that parse untrusted traffic

One item this cycle addresses AI directly. Cisco Talos argues that AI-assisted vulnerability discovery will keep surfacing flaws that are difficult or effectively impossible to patch, and that segmentation, visibility and NGFW/IPS inspection have to carry the load as a compensating layer. That is a statement about supply, not about a specific incident: the rate at which bugs are found in appliance code is rising faster than the rate at which network teams can schedule maintenance windows on perimeter gear.

The rest of the cycle shows what that supply looks like when it lands. CVE-2026-76461 in Cisco AsyncOS for Secure Email Gateway is a SQL injection in email parsing logic, CVSS 9.8, unauthenticated, root command execution, exploited in the wild, and triggered by sending a crafted email through the appliance's normal mail flow. There is no administrative interface to firewall off and no login to add MFA to - the attack surface is the data plane doing its job. CISA added it to KEV on 2026-09-14 with a due date of 2026-09-17. ZDI-26-709 (CVE-2026-20242) is the same shape one layer in: unauthenticated deserialization RCE on Cisco Secure Firewall Management Center, the box that owns policy for the firewall estate. Compromise there is compromise of every FTD it manages.

The defensive read for this week: management-plane hardening remains necessary but is no longer sufficient for appliances that accept untrusted input by design. Assume exploit development against internet-facing devices is faster than your historical patch SLA and compress that window to days. Where an AI or AIOps assistant touches network management, treat it as a privileged admin path - device logs, hostnames and ticket text are attacker-influenced content, and an agent that reads them and can write config is a prompt-injection target. Use AI on the defensive side for baselining NetFlow and syslog rather than waiting on signature updates, because the first indicator of a data-plane exploit is usually an anomalous outbound flow from an appliance that should never initiate one.  
*No AI-related network-device news in this window. Carried forward from 2026-09-17.*

**Preventing it on current systems**

- Compress the patch SLA for internet-facing appliances to days. Track KEV due dates as hard change-freeze exceptions - CVE-2026-76461 was added 2026-09-14 with a 2026-09-17 due date.
- Separate the two attack surfaces: management plane off the internet behind a dedicated management VLAN or out-of-band network with MFA, and data-plane appliances (mail gateways, VPN portals, load balancers) explicitly baselined for outbound behaviour because you cannot ACL away their inbound exposure.
- Put management systems - firewall management centres, controllers, orchestrators - on their own segment reachable only from a jump host, and patch them before the devices they manage.
- Baseline NetFlow and syslog per appliance and alert on deviation: any new outbound connection, any new local account, any config or firmware change outside a change record.
- Scope any AI/LLM/AIOps integration on network gear to read-only credentials with no unattended config write and a full audit trail; test it for prompt injection from device logs, hostnames and ticket text before letting it act.
- Rotate admin credentials, API keys, certificates and VPN pre-shared keys after patching any appliance that was internet-reachable while vulnerable - the upgrade does not evict an attacker who was already in.
- Require callback verification for any out-of-band request to change firewall or VPN configuration; AI-generated voice and text make the pretext cheap.

**Preventing it on legacy / end-of-life systems**

- Accept that end-of-life gear will never receive a fix for an AI-discovered flaw. Isolate it behind a supported inspecting firewall with IPS and deny inbound access from untrusted zones.
- Deny the legacy device any direct management access: strict ACLs, dedicated jump host, full session logging, no direct admin path from user VLANs.
- Where an unsupported appliance must keep processing untrusted input, front it with a supported device that terminates and inspects the protocol first, rather than passing traffic straight through.
- Monitor unsupported devices as high-risk assets: NetFlow baseline, alert on any new outbound flow or any inbound connection from outside the expected source set.
- Set a replacement date and a named budget owner, and record the accepted risk against the device group until the swap is done.
- Disable every service on the legacy device that is not load-bearing - Telnet, TFTP, HTTP admin, UPnP, WAN-side management, SNMP v1/v2c community strings.

---

<!--index
{
 "url": "/2026/09/18/network-security-digest/",
 "date": "2026-09-18",
 "entries": [
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN",
   "source": "Cisco PSIRT",
   "relevance": "critical",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Zero-Day Highlights API Endpoint Authentication Issues",
   "link": "https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues",
   "source": "Dark Reading",
   "relevance": "critical",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-76460"
   ],
   "kev": true,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Identity Services Engine Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ise-XU5EwX5T",
   "source": "Cisco PSIRT",
   "relevance": "critical",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn-gateway"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn-gateway"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software SSL VPN Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftdvirtual-dos-MuenGnYR",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall",
    "vpn-gateway"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Identity Services Engine Authentication Bypass Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
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
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Desk Phone 9800 Series, IP Phone 7800 and 8800 Series, and Video Phone 8875 with SIP Software Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-phone-dos-txMYNRzv",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
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
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco UCS and UCS-Based Appliances UEFI Shell Secure Boot Bypass Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ucs-uefi-sb-bypass-eb6xC5GW",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Identity Services Engine 802.1X Session Hijack and Information Disclosure Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-vuln-kWLeNnRD",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Identity Services Engine Remote Code Execution Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-rce-se7bYU57",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Email Secure/Multipurpose Internet Mail Extensions Ciphertext Decryption Vulnerabilities",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-smime-disc-dzw4rEdY",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "other"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-20354",
    "CVE-2026-20355"
   ],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Firewall Threat Defense Software TLS 1.3 Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-tls1.3-dos-dLxwFWgF",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software TCP DNS Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
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
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": false,
   "ai_angle": ""
  }
 ]
}
-->

## How this was produced

- Feeds polled: 19 ok, 0 failed
- Raw items: 700 → in window: 106 → network-device relevant: 57 → published: 25
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `rule-based`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
