---
layout: post
title: "Network Device Security Digest - 2026-09-18"
date: 2026-09-18 21:44:24 +0000
edition: daily
critical_count: 3
item_count: 16
kev: "CVE-2026-76460"
analysis_mode: "claude-code-action"
categories: digest
---

# Network Device Security Digest — 2026-09-18

*daily edition · window 36h · 18 feeds · 16 items · 3 critical · generated 2026-09-18 21:44 UTC*

> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers, management platforms and SD-WAN edge. Everything else is filtered out.

---

## 📌 Top story — Cisco Identity Services Engine: maximum-severity authentication bypass in KEV, CISA deadline 19 September 2026

CVE-2026-76460 is an incorrect-use-of-privileged-APIs flaw in Cisco Identity Services Engine (ISE) and the ISE Passive Identity Connector (ISE-PIC) that lets an unauthenticated, remote attacker bypass the web-based management interface and gain unauthorized access to the device. Dark Reading reports a CVSS score of 10 out of 10 and describes it as a zero-day. CISA added it to the Known Exploited Vulnerabilities catalog on 16 September 2026 with a remediation due date of 19 September 2026 under BOD 26-04; the ransomware association is listed as Unknown.

ISE is not a single gateway - it is the policy and identity control plane for the network. It authenticates and authorizes switch ports, wireless clients and VPN sessions, holds RADIUS/TACACS+ secrets and pushes downloadable ACLs and SGT policy to enforcement points. An attacker with administrative access to ISE can author policy that every switch, WLC and firewall in the estate will obey, which is why this outranks the firewall data-plane bugs disclosed in the same window.

The same cycle brings a second management-plane problem from Cisco: the September hardening release for Secure Firewall ASA, FTD and Firewall Management Center states that two of the internally discovered vulnerabilities are known to be actively exploited, specifically an FMC static credential vulnerability and an FMC authentication bypass vulnerability. Treat ISE and FMC as one exposure review, not two.

No fixed version numbers are given in the collected sources for any of these. Pull the fixed-release table from the Cisco advisory for your exact train before scheduling the change, and do not assume the upgrade alone is sufficient - both bugs are authentication bypasses on a box that stores credentials.

**Do this first**

- Inventory every ISE and ISE-PIC node, including PSNs, MnT and PAN, and record the running patch level; check the Cisco advisory for the fixed release that applies to your train.
- Confirm no ISE, ISE-PIC or FMC administrative interface is reachable from the internet or from user VLANs; restrict the admin GUI and API to a dedicated management network and a jump host.
- Apply the Cisco fix for CVE-2026-76460 now - CISA's BOD 26-04 due date for this CVE is 19 September 2026 - and apply the September hardening release covering the actively exploited FMC static credential and authentication bypass issues.
- After patching, rotate ISE administrator passwords, RADIUS/TACACS+ shared secrets, pxGrid and ERS/OpenAPI credentials, and the FMC admin and API accounts; a pre-patch compromise survives the upgrade.
- Review ISE and FMC for unexpected administrator accounts, changed authorization policy, new downloadable ACLs, altered device admin rules and unexplained configuration-change events.
- Alert in the SIEM on ISE and FMC admin logins from outside the management network, on API authentication from unknown sources, and on policy or firewall-rule changes outside change windows.

---

> **On the CISA KEV catalog in this edition:** CVE-2026-76460 — treat these as confirmed-exploited and patch on an emergency change.

## Executive summary

- Cisco ISE/ISE-PIC authentication bypass CVE-2026-76460 (CVSS 10) is in CISA KEV with a 19 September 2026 due date - patch the identity control plane first.
- Cisco's September hardening release for Secure Firewall ASA, FTD and FMC says two of the fixed flaws are actively exploited: an FMC static credential issue and an FMC authentication bypass.
- Six further ASA/FTD advisories landed in the same batch: five denial-of-service paths (IKEv2 certificate auth, DTLS on 3100/4200, EIGRP, syslog rate limiting, TCP DNS) and an Object Group Search ACL bypass that lets blocked traffic reach protected networks.
- Check Point Security Management and Log Servers have a critical unauthenticated remote code execution as root, fixed via LivePatch; Check Point reports no indication of exploitation.
- Zero Day Initiative published three more authenticated Cisco ISE bugs - CVE-2026-20176 and CVE-2026-20211 (RCE, CVSS 7.2) and CVE-2026-20235 (XXE information disclosure, CVSS 4.9).
- No collected source states a fixed version number this cycle. Every upgrade must be sized against the vendor advisory's fixed-release table, not against anything in this digest.
- Nothing in this window genuinely concerns AI and network devices, so no new AI section is written.

---

## Items by vendor

## Cisco

*13 item(s) — 2 critical, 6 high, 5 medium*

### Firewalls

#### 🔴 CRITICAL — Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN) · 2026-09-18* `vendor-advisory`

> Cisco's September hardening release for Secure Firewall ASA, FTD and Firewall Management Center fixes multiple internally found flaws, two of which are already being exploited.

**Affected:** Cisco Secure Firewall Adaptive Security Appliance (ASA) Software, Secure Firewall Threat Defense (FTD) Software and Secure Firewall Management Center (FMC) Software. The advisory does not state fixed release numbers - check the vendor advisory for the fixed release.  

**What happened.** An internal Cisco security review produced hardening releases covering multiple vulnerabilities found in testing, grouped by CWE class. Cisco states that two of them are known to be actively exploited, and points to two FMC advisories: a static credential vulnerability and an authentication bypass vulnerability.

**Why it matters.** FMC is the management platform for an entire ASA/FTD estate: it holds device credentials and pushes access control policy. A static credential plus an authentication bypass, both already exploited, means an attacker who reaches the FMC web interface can own every firewall it manages, and the compromise predates any patch you apply now.

**Recommended actions**

- Identify every FMC instance and the ASA/FTD devices it manages; record running versions and match them against the fixed-release table in the Cisco advisory.
- Remove FMC and ASA/FTD management access (HTTPS, SSH, API) from internet-facing and user-facing interfaces; restrict to a dedicated management VLAN reached through a jump host.
- Apply the hardening release, HA pair secondary first, then fail over and patch the primary; validate policy deployment after the upgrade.
- After patching, rotate FMC local admin passwords, API tokens, device registration keys and ASA/FTD local admin credentials and certificates - static credentials and a pre-patch compromise both survive an upgrade.
- Export the FMC configuration and the ASA/FTD running configs and review for unexpected admin users, new access rules, modified NAT, added static routes or unknown registered devices.
- Enforce MFA on all FMC and firewall administrative accounts and remove shared local admin accounts.

**Legacy / unpatchable gear.** ASA hardware past end of software support will not receive this hardening release. Take its management interface off every routed path, permit administration only from an out-of-band network or dedicated jump host, deny inbound access from untrusted zones through a supported inspecting firewall, and set a replacement date with a budget owner while documenting the accepted risk.

**Detection.** Alert on FMC admin logins from outside the management network and on any FMC API authentication from an unknown source address. Review the FMC audit log for policy deployments, user creation and device registration outside change windows. On ASA/FTD, alert on syslog 605005 and 611101/611102 (admin authentication) from unexpected sources and on configuration-change events without a matching change record.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Object Group Access Control List Bypass Vulnerabilities

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw) · 2026-09-18* `vendor-advisory`

> A logic error in Object Group Search on Cisco ASA and FTD lets an unauthenticated remote attacker push traffic past configured ACLs into protected networks.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software with ACL Object Group Search (OGS) configured. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** Multiple vulnerabilities in the ACL Object Group Search implementation stem from a logic error when populating group access control policies with OGS configured. An unauthenticated remote attacker can send traffic that should be blocked and have it pass through the device. Cisco has released software updates; there are no workarounds.

**Why it matters.** This is not a crash - it is silent policy failure. The firewall reports that it is enforcing the rule base while blocked traffic reaches hosts behind it, which undermines every segmentation boundary built on those ACLs and leaves no obvious symptom to notice.

**Recommended actions**

- Determine which ASA/FTD devices have Object Group Search enabled; those are the ones at risk.
- Confirm the running version against the vendor's fixed-release table and schedule the upgrade in the change window, HA pair secondary first - there is no workaround.
- Until patched, validate critical deny rules by actively testing them from the untrusted side rather than trusting the configuration, prioritising segmentation boundaries to server, OT and management networks.
- Keep management access (HTTPS, SSH, API) off untrusted and internet-facing interfaces and restricted to the management VLAN.
- Review the configuration for unexpected object-group membership changes that would widen an ACL.

**Legacy / unpatchable gear.** Unsupported ASA hardware that cannot take the fixed release should not be relied on for segmentation while OGS is in use. Where possible, disable OGS and accept the ACL scale cost, place a supported inspecting firewall in front of the boundary it protects, and set a replacement date with the accepted risk documented.

**Detection.** Compare NetFlow or firewall connection logs against the intended rule base: look for accepted flows between zone pairs that policy should deny, especially inbound to server and management segments. Alert when a destination that should be unreachable from the untrusted zone records established sessions.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv) · 2026-09-18* `vendor-advisory`

> Cisco ASA and FTD reload when sent a crafted certificate during IKEv2 setup, letting an unauthenticated remote attacker drop the VPN headend.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software using IKEv2 certificate authentication. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** A logic error during the certificate authentication phase of IKEv2 connection setup allows an unauthenticated, remote attacker to crash the IKEv2 process by attempting a VPN connection with a crafted certificate, causing the device to reload. Cisco has released software updates; there are no workarounds.

**Why it matters.** The IKEv2 listener is internet-facing by design on any site-to-site or remote-access VPN headend, and no credentials are needed to reach it. A repeatable reload takes down both the VPN and everything else the firewall is passing, and there is no configuration change that avoids it.

**Recommended actions**

- Identify ASA/FTD devices terminating IKEv2 with certificate authentication and record running versions against the vendor's fixed-release table.
- Schedule the upgrade in the change window, HA pair secondary first, then fail over - there is no workaround, so patching is the only fix.
- Where the VPN peer set is known and static, restrict IKEv2 (UDP 500/4500) to expected peer addresses or ASNs to shrink the attacker population before the patch lands.
- Confirm HA failover is healthy and tested so a single reload does not become an outage.
- Keep management access off the internet-facing interface and enforce MFA on administrative and VPN accounts.

**Legacy / unpatchable gear.** End-of-support ASA hardware terminating IKEv2 cannot be fixed. Front it with a supported device, or restrict UDP 500/4500 upstream to known peers only, monitor for unexplained reloads as a high-risk-asset signal, and set a replacement date with a budget owner.

**Detection.** Alert on unplanned device reloads and on IKEv2 process restarts in syslog, and correlate them with inbound IKEv2 attempts from unfamiliar source addresses. Repeated IKEv2 negotiations that fail at the certificate authentication phase from one source are the pattern to watch.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv)**

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO) · 2026-09-18* `vendor-advisory`

> Crafted DTLS traffic reloads Cisco Secure Firewall 3100 and 4200 Series devices running ASA or FTD, with no authentication required.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software on Secure Firewall 3100 Series and 4200 Series hardware. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** Improper resource management when processing certain DTLS messages lets an unauthenticated, remote attacker reload an affected device by sending a crafted stream of DTLS traffic. Cisco has released software updates, and the advisory states that workarounds exist.

**Why it matters.** DTLS is what remote-access VPN clients use, so the exposed surface faces the internet on exactly the platforms most organisations put at the perimeter. Unlike most of this batch, a workaround is available, which gives teams that cannot patch this week an option.

**Recommended actions**

- Confirm which of your 3100 and 4200 Series units are affected and record running versions against the vendor's fixed-release table.
- Read the workaround in the Cisco advisory and apply it now if the maintenance window is not immediate; do not substitute a guess for the documented one.
- Schedule the upgrade, HA pair secondary first, and verify failover before touching the primary.
- Keep management access (HTTPS, SSH, API) off the internet-facing interface and restricted to the management VLAN.
- Confirm HA and monitoring are in place so a reload is detected immediately rather than reported by users.

**Legacy / unpatchable gear.** Hardware outside this generation is not affected by this specific issue, but any unsupported firewall terminating DTLS should be isolated behind a supported inspecting device, have inbound DTLS restricted to expected sources, and carry a documented replacement date.

**Detection.** Alert on unplanned reloads on 3100 and 4200 Series units and correlate against DTLS (UDP 443) traffic volume. A burst of DTLS from a single source immediately before a reload is the signature to look for in NetFlow.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO)**

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj) · 2026-09-18* `vendor-advisory`

> A memory leak in EIGRP handling on Cisco ASA and FTD lets an unauthenticated adjacent attacker force the device to reload.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software running EIGRP. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** Improper resource management when handling EIGRP update messages allows an unauthenticated, adjacent attacker sending crafted EIGRP updates at a high rate to trigger a memory leak that eventually reloads the device. Cisco has released software updates; there are no workarounds.

**Why it matters.** The attacker must be adjacent, which limits this to someone already on a connected segment, so it is a lateral-movement and insider-risk problem rather than an internet-facing one. The leak is gradual, so the reload can arrive hours after the traffic that caused it and may be misdiagnosed as a hardware fault.

**Recommended actions**

- Determine which ASA/FTD devices actually run EIGRP; devices without it configured are not exposed by this path.
- Confirm running versions against the vendor's fixed-release table and schedule the upgrade - there is no workaround.
- Enforce EIGRP neighbour authentication and configure passive interfaces on every segment that should not carry routing adjacencies.
- Segment so that user, guest and OT VLANs have no routing adjacency with the firewall.
- Monitor memory utilisation on ASA/FTD as a leading indicator rather than waiting for the reload.

**Legacy / unpatchable gear.** On unsupported hardware running EIGRP, restrict adjacencies to authenticated, explicitly configured neighbours, set every other interface passive, deny EIGRP from untrusted segments with an ACL, and track memory utilisation trends as a high-risk-asset signal until the device is replaced.

**Detection.** Trend ASA/FTD memory utilisation and alert on sustained growth with no configuration change. Alert on EIGRP neighbour flaps, on EIGRP packets arriving on interfaces that should be passive, and on unplanned reloads preceded by memory pressure.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj)**

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software TCP DNS Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5) · 2026-09-18* `vendor-advisory`

> A crafted DNS reply can restart the TCP DNS handler on Cisco ASA and FTD and reload the firewall, but the attacker must control or intercept the DNS response.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software using DNS over TCP. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** A logic error parsing DNS queries and tracking incoming buffer sizes lets an attacker who can answer DNS queries sent by the device - by controlling the DNS service or through a machine-in-the-middle position - force the TCP DNS response handler to restart and the device to reload. Cisco has released software updates.

**Why it matters.** The precondition is real: the attacker needs the device's DNS service or a path to intercept it, which is not a drive-by. It does mean the resolver a firewall trusts becomes an availability dependency, and a compromised or spoofed internal resolver can reboot the perimeter.

**Recommended actions**

- Confirm which ASA/FTD devices are configured with DNS servers and record versions against the vendor's fixed-release table.
- Point firewalls at internal, trusted resolvers only, and restrict their DNS traffic to those addresses with an ACL.
- Schedule the upgrade in the normal change window, HA pair secondary first.
- Harden and monitor the resolvers the firewalls use - they are now part of the firewall's availability chain.
- Ensure DNS from network devices cannot be intercepted on a shared or untrusted segment; keep device-originated DNS on the management path.

**Legacy / unpatchable gear.** Unsupported firewalls should have their configured DNS servers pinned to trusted internal resolvers reachable only over the management network, with all other DNS denied by ACL, and should be monitored for unexplained reloads until replaced.

**Detection.** Alert on unplanned reloads correlated with DNS activity, and on DNS responses to the firewall arriving from any address other than the configured resolvers. Monitor for DNS process restarts in syslog.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5)**

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Logging Denial of Service Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN) · 2026-09-18* `vendor-advisory`

> A SYN flood against Cisco ASA or FTD drives CPU to saturation through unrate-limited syslog message 419002, degrading the firewall.

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense Software. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** Improper rate limiting for syslog message 419002 lets an unauthenticated, remote attacker cause high CPU utilisation by sending a flood of TCP SYN packets, resulting in performance degradation. Cisco has released software updates, and the advisory states that workarounds exist.

**Why it matters.** This degrades rather than crashes, which makes it harder to attribute: throughput drops and latency rises while the device stays up. A workaround exists, so it can be contained without an immediate maintenance window.

**Recommended actions**

- Record running versions against the vendor's fixed-release table and read the documented workaround in the Cisco advisory.
- Apply the workaround if the upgrade cannot be scheduled promptly; do not improvise a logging change without checking the advisory first.
- Confirm threat detection and SYN-flood protections (embryonic connection limits) are configured on internet-facing interfaces.
- Schedule the upgrade in the normal change window, HA pair secondary first.
- Baseline normal CPU so degradation is visible in monitoring rather than in user complaints.

**Legacy / unpatchable gear.** On unsupported firewalls, apply embryonic connection limits on internet-facing interfaces, place upstream rate limiting where available, alert on CPU above baseline, and document the accepted risk with a replacement date.

**Detection.** Alert on sustained CPU above baseline on ASA/FTD, and on a spike in the rate of syslog 419002 messages. Correlate with SYN volume in NetFlow from a small number of sources.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN)**

### Routers

#### 🟡 MEDIUM — Cisco IOS XR Software Security Hardening Release: September 2026

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM) · 2026-09-17* `vendor-advisory`

> Cisco shipped a September hardening release for IOS XR fixing multiple internally discovered vulnerabilities, none of them known to be exploited.

**Affected:** Cisco IOS XR Software. The advisory groups issues by CWE class with one CVE per grouping and does not state fixed release numbers here - check the vendor advisory for the fixed release.  

**What happened.** An internal Cisco security review produced hardening releases addressing multiple vulnerabilities found during internal testing. Cisco states that these are not known to be actively exploited. Software updates are available and there are no workarounds.

**Why it matters.** IOS XR runs service provider and large-enterprise core and edge routers, where change windows are long and upgrades are rare. Nothing here is on fire, which makes this the right item to fold into the next planned maintenance rather than an emergency - but the absence of workarounds means the upgrade is the only remediation when one of these is eventually weaponised.

**Recommended actions**

- Inventory IOS XR platforms and running versions and map them against the hardening release train in the Cisco advisory.
- Plan the upgrade into the next scheduled maintenance window; validate the ISSU or hitless upgrade path on core and distribution nodes first.
- Verify image integrity against the vendor hash before loading.
- Restrict the management plane with control-plane policing and management ACLs, and move management to an out-of-band network.
- Harden SNMP to v3 with authentication and privacy only, and disable Telnet, TFTP and other legacy services.

**Legacy / unpatchable gear.** Platforms no longer receiving IOS XR updates should be confined to out-of-band management with strict control-plane policing and management ACLs, given a documented replacement date and budget owner, and monitored with a NetFlow baseline that alerts on new outbound flows.

**Detection.** Ship IOS XR logs to the SIEM and alert on administrative logins, configuration changes and image or package installations outside change windows. Baseline control-plane traffic and alert on deviation.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)**

### Management platforms

#### 🔴 CRITICAL — Cisco Zero-Day Highlights API Endpoint Authentication Issues

*[Dark Reading](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues) · 2026-09-18* `KEV`

> CVE-2026-76460, a CVSS 10 authentication bypass in Cisco Identity Services Engine, is listed in CISA KEV with a remediation due date of 19 September 2026.

**Affected:** Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC). The collected sources do not state a fixed build - check the vendor advisory for the fixed release.  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** An incorrect use of privileged APIs allows an unauthenticated, remote attacker to bypass the ISE web-based management interface and gain unauthorized access to the device. Dark Reading reports a maximum CVSS score of 10 and describes it as a zero-day. CISA added the CVE to the KEV catalog on 16 September 2026 with a due date of 19 September 2026; ransomware use is listed as Unknown.

**Why it matters.** ISE is the identity and policy control plane for switches, wireless controllers and VPN headends. It stores RADIUS and TACACS+ secrets and pushes authorization policy that enforcement points obey without question. Administrative access to ISE is effectively administrative access to network admission control across the estate, and this one needs no credentials.

**Recommended actions**

- List all ISE and ISE-PIC nodes by persona (PAN, MnT, PSN) with running patch level, and match against the fixed release in the Cisco advisory.
- Apply the fix immediately - the CISA BOD 26-04 due date for this CVE is 19 September 2026 - patching secondary nodes first and the primary admin node last.
- Restrict the ISE admin GUI, ERS/OpenAPI and pxGrid interfaces to a dedicated management network; they must not be reachable from the internet or from user or guest VLANs.
- Rotate ISE admin credentials, RADIUS and TACACS+ shared secrets, ERS/OpenAPI accounts, pxGrid certificates and any repository credentials after patching.
- Review authorization policy sets, downloadable ACLs, device admin rules, network device group membership and the internal admin user list for changes you did not make.
- Enforce MFA on ISE administrative access and remove shared local admin accounts.

**Legacy / unpatchable gear.** ISE deployments on an unsupported release train will not get this fix. Isolate the admin interfaces on an out-of-band management network, permit access only from a logged jump host, and if the version cannot be upgraded at all, plan migration now and monitor the nodes as high-risk assets with a NetFlow baseline and alerting on any new outbound flow.

**Detection.** Search ISE operations and audit logs for administrative logins and API calls that did not originate from the management network, for successful access without a preceding authentication event, and for policy or admin-user changes outside change windows. On the network side, alert on new inbound sessions to ISE management ports (TCP 443, 9060, 8910) from outside the management VLAN.

**AI angle.** None reported.

📄 **[Read the full report at Dark Reading →](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)**

#### 🟠 HIGH — ZDI-26-716: Cisco Identity Services Engine createDBLink Command Injection Remote Code Execution Vulnerability

*[Zero Day Initiative](http://www.zerodayinitiative.com/advisories/ZDI-26-716/) · 2026-09-18* 

> ZDI-26-716 reports CVE-2026-20176, a createDBLink command injection in Cisco Identity Services Engine that gives authenticated remote attackers code execution, rated CVSS 7.2.

**Affected:** Cisco Identity Services Engine. No fixed version is stated in the source - check the vendor advisory for the fixed release.  
**CVEs:** [CVE-2026-20176](https://nvd.nist.gov/vuln/detail/CVE-2026-20176)  

**What happened.** Zero Day Initiative published an advisory for a command injection in the createDBLink function of Cisco ISE that allows remote attackers to execute arbitrary code on affected installations. Authentication is required; ZDI assigned a CVSS rating of 7.2 and the CVE CVE-2026-20176.

**Why it matters.** Authentication is required, but ISE holds RADIUS and TACACS+ secrets and defines network access policy, so a low-privileged ISE account turning into code execution is a direct path from a helpdesk-tier login to control of network admission. It compounds the unauthenticated bypass CVE-2026-76460 in the same cycle: chain the two and the authentication requirement disappears.

**Recommended actions**

- Patch ISE to the release identified in the Cisco advisory for CVE-2026-20176, alongside the KEV item CVE-2026-76460.
- Restrict the ISE admin GUI and API to the management network and a jump host; an authenticated bug only matters to someone who can reach the interface.
- Audit ISE internal and external admin accounts, remove stale and shared logins, and enforce least privilege on admin role assignments.
- Enforce MFA on ISE administrative access and rotate any admin or API credentials that have been widely shared.
- Review ISE audit logs for API calls and administrative operations from accounts that should not be performing them.

**Legacy / unpatchable gear.** If the ISE version in use is past support and cannot take the fix, reduce the accessible account set to the minimum, place the admin interfaces behind an out-of-band management network with jump-host-only access and full session logging, and plan the upgrade or migration with a named owner.

**Detection.** Monitor ISE audit logs for unexpected administrative API usage, database link or repository operations, and for admin logins from addresses outside the management network. Alert on new processes or outbound connections from ISE nodes to unfamiliar destinations.

**AI angle.** None reported.

📄 **[Read the full report at Zero Day Initiative →](http://www.zerodayinitiative.com/advisories/ZDI-26-716/)**

#### 🟠 HIGH — ZDI-26-717: Cisco Identity Services Engine AlarmMessageDiskQueue Deserialization of Untrusted Data Remote Code Execution Vulnerability

*[Zero Day Initiative](http://www.zerodayinitiative.com/advisories/ZDI-26-717/) · 2026-09-18* 

> ZDI-26-717 reports CVE-2026-20211, an unsafe deserialization in Cisco ISE AlarmMessageDiskQueue that gives authenticated remote attackers code execution, rated CVSS 7.2.

**Affected:** Cisco Identity Services Engine. No fixed version is stated in the source - check the vendor advisory for the fixed release.  
**CVEs:** [CVE-2026-20211](https://nvd.nist.gov/vuln/detail/CVE-2026-20211)  

**What happened.** Zero Day Initiative published an advisory for deserialization of untrusted data in the AlarmMessageDiskQueue component of Cisco ISE, allowing remote attackers to execute arbitrary code on affected installations. Authentication is required; ZDI assigned a CVSS rating of 7.2 and the CVE CVE-2026-20211.

**Why it matters.** This is the second authenticated ISE code execution path disclosed in the same batch. Together with CVE-2026-20176 and the unauthenticated bypass CVE-2026-76460, it means ISE needs one consolidated patch cycle rather than three separate risk assessments, and any exposed ISE admin interface should be treated as urgent.

**Recommended actions**

- Fold CVE-2026-20211 into the same ISE upgrade as CVE-2026-76460 and CVE-2026-20176 rather than scheduling three windows; take the fixed release from the Cisco advisory.
- Restrict ISE admin GUI, API and pxGrid interfaces to the management network and a jump host.
- Review and reduce the set of ISE administrative accounts; enforce MFA and least privilege on remaining ones.
- Rotate ISE admin and API credentials after patching.
- Ship ISE logs to the SIEM and alert on administrative operations and configuration changes.

**Legacy / unpatchable gear.** An ISE deployment too old to receive the fix should have its administrative surfaces confined to an out-of-band management network with jump-host-only access, a reduced administrator account set, and a documented upgrade or replacement date with a budget owner.

**Detection.** Watch ISE nodes for unexpected child processes, new outbound connections and unexplained service restarts, and review the audit log for administrative sessions that do not correlate with staff activity or a change record.

**AI angle.** None reported.

📄 **[Read the full report at Zero Day Initiative →](http://www.zerodayinitiative.com/advisories/ZDI-26-717/)**

#### 🟡 MEDIUM — ZDI-26-718: Cisco Identity Services Engine MnTRESTLivelogService XML External Entity Processing Information Disclosure Vulnerability

*[Zero Day Initiative](http://www.zerodayinitiative.com/advisories/ZDI-26-718/) · 2026-09-18* 

> ZDI-26-718 reports CVE-2026-20235, an XML external entity flaw in Cisco ISE MnTRESTLivelogService that discloses information to authenticated remote attackers, rated CVSS 4.9.

**Affected:** Cisco Identity Services Engine. No fixed version is stated in the source - check the vendor advisory for the fixed release.  
**CVEs:** [CVE-2026-20235](https://nvd.nist.gov/vuln/detail/CVE-2026-20235)  

**What happened.** Zero Day Initiative published an advisory for XML external entity processing in the MnTRESTLivelogService component of Cisco ISE, allowing remote attackers to disclose sensitive information. Authentication is required; ZDI assigned a CVSS rating of 4.9 and the CVE CVE-2026-20235.

**Why it matters.** The lowest-rated of the three ZDI ISE items, but information disclosure on an identity platform is useful reconnaissance: file contents read from the appliance can feed the two code execution bugs disclosed alongside it. Patch it in the same window, not separately.

**Recommended actions**

- Include CVE-2026-20235 in the consolidated ISE upgrade covering CVE-2026-76460, CVE-2026-20176 and CVE-2026-20211.
- Restrict ISE admin and REST API access to the management network and a jump host.
- Review which accounts hold API access to the monitoring and troubleshooting (MnT) persona and reduce to least privilege.
- Rotate any secrets that could have been read from the appliance if you find evidence of abuse.
- Log and alert on ISE REST API usage from unexpected sources.

**Legacy / unpatchable gear.** An unpatchable ISE deployment should have REST API access restricted to explicitly permitted management hosts only, a minimal administrator account set, and a documented upgrade path with an owner.

**Detection.** Alert on ISE REST API calls to the livelog service from sources outside the management network, and on XML payloads referencing external entities in application logs where visible.

**AI angle.** None reported.

📄 **[Read the full report at Zero Day Initiative →](http://www.zerodayinitiative.com/advisories/ZDI-26-718/)**

### Other

#### 🟠 HIGH — Cisco Secure Email Gateway SQL Injection Vulnerability

*[Cisco PSIRT](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX) · 2026-09-17* `vendor-advisory`

> A crafted email can trigger SQL injection in Cisco Secure Email Gateway and execute commands as root, with no authentication required.

**Affected:** Cisco AsyncOS Software for Cisco Secure Email Gateway. No fixed version is stated in the source - check the vendor advisory for the fixed release.  

**What happened.** Insufficient validation in the email parsing logic allows an unauthenticated, remote attacker to send a crafted message containing malicious SQL statements through an affected device, leading to arbitrary SQL execution and command execution with root privileges on the underlying operating system. Cisco has released software updates; there are no workarounds.

**Why it matters.** The trigger is an inbound email, which is the one input this appliance exists to accept and cannot be firewalled off. Root on a mail gateway gives an attacker the organisation's inbound and outbound mail flow and a trusted position on the perimeter, and there is no workaround short of patching.

**Recommended actions**

- Identify all Secure Email Gateway appliances and virtual instances with their AsyncOS versions and match against the vendor's fixed-release table.
- Schedule the upgrade with priority - the attack vector is ordinary inbound mail and there is no workaround.
- After patching, rotate appliance admin credentials, API keys and any LDAP or service-account bind credentials stored on the device.
- Restrict the appliance management interface to the management network; only SMTP should be reachable from outside.
- Review the appliance for unexpected admin users, new listeners, modified message filters and changed outbound routes.

**Legacy / unpatchable gear.** An email gateway on an unsupported AsyncOS release cannot be fixed and still has to accept internet mail. Put it behind an upstream filtering service so untrusted mail is not parsed by it first, isolate its management and back-end access to an out-of-band network, monitor it as a high-risk asset with a NetFlow baseline, and set a replacement date.

**Detection.** Alert on new outbound connections from the email gateway to destinations other than mail and update infrastructure, on unexpected root-level processes, and on admin account creation or configuration changes in the appliance audit log. Review mail logs for malformed messages immediately preceding any of those events.

**AI angle.** None reported.

📄 **[Read the full report at Cisco PSIRT →](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX)**

---

## Check Point

*3 item(s) — 1 critical, 2 medium*

### Management platforms

#### 🔴 CRITICAL — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root

*[The Hacker News](https://thehackernews.com/2026/09/critical-check-point-management-server.html) · 2026-09-17* 

> A critical flaw in Check Point Security Management and Log Servers lets an unauthenticated attacker run code as root on the system that controls firewall policy.

**Affected:** Check Point Security Management Server and Log Server. Check Point has shipped a fix through its LivePatch update channel; the source does not state version numbers - check the vendor advisory for the fixed release.  

**What happened.** An attacker with no login credentials can execute code as root over the network on Check Point Security Management and Log Servers. Check Point released a fix via LivePatch and says it has no indication that the flaw has been exploited.

**Why it matters.** The Security Management Server defines firewall policy and administrator access for every gateway it manages. Root on that host means the ability to push any rule base to the perimeter and to read the logs that would record it, so a single unauthenticated bug there has a far wider blast radius than a bug on one gateway.

**Recommended actions**

- Confirm LivePatch is enabled and the fix has actually installed on every Security Management Server and Log Server, including standby management and multi-domain servers; verify rather than assume.
- Remove management server access from any untrusted or internet-facing interface; permit SmartConsole, API and SSH only from a dedicated management network and a jump host.
- Verify config sync and policy integrity after the update, then install policy from a known-good revision.
- Rotate management administrator credentials, API keys, SIC certificates where feasible and any service-account secrets stored on the management server.
- Review the audit trail and rule base revisions for administrator accounts, rule changes or policy installations you cannot attribute to a change record.
- Enforce MFA on all SmartConsole and management API administrative accounts.

**Legacy / unpatchable gear.** A management server on a release too old for LivePatch coverage cannot be fixed in place. Put it behind a supported inspecting firewall with inbound access denied from all untrusted zones, allow management only from a dedicated jump host with full session logging, set a replacement or upgrade date with a budget owner, and monitor the host for new outbound flows in the meantime.

**Detection.** Alert on any inbound connection to management server ports from outside the management network, on SmartConsole or management API logins from unknown sources, and on policy installation events without a matching change record. Watch for new processes or listeners on the management server and for gaps or truncation in the log server's own audit trail.

**AI angle.** None reported.

📄 **[Read the full report at The Hacker News →](https://thehackernews.com/2026/09/critical-check-point-management-server.html)**

#### 🟡 MEDIUM — Check Point, Kaspersky, Tanium Patch Product Vulnerabilities

*[SecurityWeek](https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/) · 2026-09-18* 

> SecurityWeek's patch roundup confirms the critical Check Point Security Management and Log Server flaw allowing remote code execution with root privileges.

**Affected:** Check Point Security Management Server and Log Server. Version details are not given in this source - check the vendor advisory for the fixed release.  

**What happened.** A vendor patch roundup covering Check Point, Kaspersky and Tanium reports that Check Point Security Management and Log Servers are affected by a critical vulnerability allowing remote code execution with root privileges. The Kaspersky and Tanium items in the same article are not network infrastructure.

**Why it matters.** Corroborating coverage of the same Check Point management server flaw rather than a new issue. Useful only to confirm severity when building the change case - act on the primary advisory.

**Recommended actions**

- Treat this as confirmation of the Check Point management server issue and act on that item's remediation rather than opening a separate task.
- Verify the LivePatch fix is installed on every management and log server.
- Keep management server access restricted to the management network and a jump host.
- Rotate management administrator credentials and API keys after patching.

**Legacy / unpatchable gear.** As for the primary Check Point item: a management server too old to receive the fix belongs behind a supported inspecting firewall, reachable only from a logged jump host, with a documented replacement date.

**Detection.** Same as the primary Check Point item: alert on management server logins and policy installations from outside the management network and without a matching change record.

**AI angle.** None reported.

📄 **[Read the full report at SecurityWeek →](https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/)**

#### 🟡 MEDIUM — New Check Point flaw lets hackers execute code with root privileges

*[BleepingComputer](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/) · 2026-09-18* 

> BleepingComputer reports Check Point security updates for a critical flaw that lets attackers execute code with root privileges on management systems.

**Affected:** Check Point management systems. Version details are not given in this source - check the vendor advisory for the fixed release.  

**What happened.** Check Point Software released security updates addressing a critical vulnerability that allows attackers to execute code with root privileges on management systems.

**Why it matters.** Third source on the same Check Point management server flaw. The consistency across outlets raises confidence that the fix should be verified as installed rather than assumed, but it adds no new technical detail.

**Recommended actions**

- Confirm the Check Point security update is applied to every management and log server; do not assume LivePatch has completed.
- Restrict management access to the management network and a jump host.
- Review the audit trail for administrator activity and policy installations you cannot attribute.
- Rotate management administrator credentials and API keys after patching.

**Legacy / unpatchable gear.** As for the primary Check Point item: isolate an unpatchable management server behind a supported inspecting firewall with jump-host-only access, full session logging and a documented replacement date.

**Detection.** Same as the primary Check Point item: alert on unexpected management server logins, new listeners or processes, and policy installations outside change windows.

**AI angle.** None reported.

📄 **[Read the full report at BleepingComputer →](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/)**

---

## 🧠 AI & network devices — AI-found bugs land where you cannot patch fast: pre-auth flaws in appliances that parse untrusted traffic

One item this cycle addresses AI directly. Cisco Talos argues that AI-assisted vulnerability discovery will keep surfacing flaws that are difficult or effectively impossible to patch, and that segmentation, visibility and NGFW/IPS inspection have to carry the load as a compensating layer. That is a statement about supply, not about a specific incident: the rate at which bugs are found in appliance code is rising faster than the rate at which network teams can schedule maintenance windows on perimeter gear.

The rest of the cycle shows what that supply looks like when it lands. CVE-2026-76461 in Cisco AsyncOS for Secure Email Gateway is a SQL injection in email parsing logic, CVSS 9.8, unauthenticated, root command execution, exploited in the wild, and triggered by sending a crafted email through the appliance's normal mail flow. There is no administrative interface to firewall off and no login to add MFA to - the attack surface is the data plane doing its job. CISA added it to KEV on 2026-09-14 with a due date of 2026-09-17. ZDI-26-709 (CVE-2026-20242) is the same shape one layer in: unauthenticated deserialization RCE on Cisco Secure Firewall Management Center, the box that owns policy for the firewall estate. Compromise there is compromise of every FTD it manages.

The defensive read for this week: management-plane hardening remains necessary but is no longer sufficient for appliances that accept untrusted input by design. Assume exploit development against internet-facing devices is faster than your historical patch SLA and compress that window to days. Where an AI or AIOps assistant touches network management, treat it as a privileged admin path - device logs, hostnames and ticket text are attacker-influenced content, and an agent that reads them and can write config is a prompt-injection target. Use AI on the defensive side for baselining NetFlow and syslog rather than waiting on signature updates, because the first indicator of a data-plane exploit is usually an anomalous outbound flow from an appliance that should never initiate one.  
*No AI-related network-device news in this window. Carried forward from 2026-09-17.*

**Vendors with an AI angle in this edition:** Check Point, Cisco

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
    "firewall",
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco Zero-Day Highlights API Endpoint Authentication Issues",
   "link": "https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues",
   "source": "Dark Reading",
   "relevance": "critical",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-76460"
   ],
   "kev": true,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root",
   "link": "https://thehackernews.com/2026/09/critical-check-point-management-server.html",
   "source": "The Hacker News",
   "relevance": "critical",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Check Point"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
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
   "ai": true,
   "ai_angle": "None reported."
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
   "ai": true,
   "ai_angle": "None reported."
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
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "ZDI-26-716: Cisco Identity Services Engine createDBLink Command Injection Remote Code Execution Vulnerability",
   "link": "http://www.zerodayinitiative.com/advisories/ZDI-26-716/",
   "source": "Zero Day Initiative",
   "relevance": "high",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-20176"
   ],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "ZDI-26-717: Cisco Identity Services Engine AlarmMessageDiskQueue Deserialization of Untrusted Data Remote Code Execution Vulnerability",
   "link": "http://www.zerodayinitiative.com/advisories/ZDI-26-717/",
   "source": "Zero Day Initiative",
   "relevance": "high",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-20211"
   ],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco Secure Email Gateway SQL Injection Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX",
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
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj",
   "source": "Cisco PSIRT",
   "relevance": "medium",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software TCP DNS Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5",
   "source": "Cisco PSIRT",
   "relevance": "medium",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Logging Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN",
   "source": "Cisco PSIRT",
   "relevance": "medium",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Cisco IOS XR Software Security Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM",
   "source": "Cisco PSIRT",
   "relevance": "medium",
   "device_types": [
    "router"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "ZDI-26-718: Cisco Identity Services Engine MnTRESTLivelogService XML External Entity Processing Information Disclosure Vulnerability",
   "link": "http://www.zerodayinitiative.com/advisories/ZDI-26-718/",
   "source": "Zero Day Initiative",
   "relevance": "medium",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [
    "CVE-2026-20235"
   ],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "Check Point, Kaspersky, Tanium Patch Product Vulnerabilities",
   "link": "https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/",
   "source": "SecurityWeek",
   "relevance": "medium",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Check Point"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  },
  {
   "title": "New Check Point flaw lets hackers execute code with root privileges",
   "link": "https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/",
   "source": "BleepingComputer",
   "relevance": "medium",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Check Point"
   ],
   "cves": [],
   "kev": false,
   "ai": true,
   "ai_angle": "None reported."
  }
 ]
}
-->

## How this was produced

- Feeds polled: 18 ok, 1 failed
- Raw items: 670 → in window: 86 → network-device relevant: 18 → published: 16
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `claude-code-action`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
