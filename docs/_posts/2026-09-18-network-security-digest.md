---
layout: post
title: "Network Device Security Digest - 2026-09-18"
date: 2026-09-18 21:08:20 +0000
edition: daily
critical_count: 4
item_count: 17
kev: "CVE-2026-76460"
analysis_mode: "claude-code-action"
categories: digest
---

# Network Device Security Digest — 2026-09-18

*daily edition · window 48h · 18 feeds · 17 items · 4 critical · generated 2026-09-18 21:08 UTC*

> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers, management platforms and SD-WAN edge. Everything else is filtered out.

---

## 📌 Top story — Cisco ISE authentication bypass CVE-2026-76460 (CVSS 10.0) exploited in the wild, KEV due date 19 September 2026

Cisco has disclosed CVE-2026-76460, an authentication bypass in Cisco Identity Services Engine (ISE) and the ISE Passive Identity Connector (ISE-PIC) carrying a CVSS score of 10.0. Cisco attributes it to insufficient authentication control on an API endpoint: an unauthenticated, remote attacker can bypass the web-based management interface and gain unauthorized access to the device. Cisco says the flaw is under active exploitation. CISA added it to the Known Exploited Vulnerabilities catalogue on 16 September 2026 with a remediation due date of 19 September 2026 under BOD 26-04, and the KEV entry carries CISA's forensics triage requirement.

ISE is not a single gateway - it is the policy and identity platform behind RADIUS/TACACS+ authentication, 802.1X on the wired and wireless edge, guest access, posture and device admin for the whole estate. An attacker with administrative reach into ISE can mint access for themselves across every switch, wireless controller and VPN headend that trusts it, and can read the identity data and device-admin credentials it holds. That blast radius is why this outranks the several ASA/FTD gateway issues published in the same cycle.

The same cycle brings a second active-exploitation front at Cisco: the September 2026 Secure Firewall hardening release states that two of the internally discovered flaws are known to be actively exploited, in Secure Firewall Management Center (FMC) Software - a static credential vulnerability and an authentication bypass vulnerability. FMC is the management plane for your ASA/FTD fleet, so treat it with the same urgency as ISE. Independently, ZDI published three further authenticated ISE vulnerabilities this cycle (CVE-2026-20176, CVE-2026-20211, CVE-2026-20235), which raise the value of any foothold on the platform.

None of the collected sources state a fixed release number for any of these. Pull the fixed-version table from Cisco's advisory for your exact train before you open a change window, and treat both ISE and FMC as compromise candidates until you have checked, not just as patch candidates.

**Do this first**

- Inventory every ISE, ISE-PIC and FMC node including standby and lab instances, and check the running version against the fixed-release table in the Cisco advisory - no source here states a fixed build, so take it from the vendor.
- Remove the ISE and FMC administrative/API interfaces from any internet-facing or user-reachable path today; restrict to a dedicated management VLAN or out-of-band network with an explicit source ACL, as an immediate control while the upgrade is scheduled.
- Patch ISE/ISE-PIC first, then FMC, then the ASA/FTD data-plane devices; the KEV due date for CVE-2026-76460 is 19 September 2026.
- Treat pre-patch compromise as possible: after upgrade, rotate ISE and FMC admin credentials, API keys, RADIUS/TACACS+ shared secrets, certificates and any service accounts the platforms hold, and terminate active admin sessions.
- Review ISE and FMC administrator lists, API clients, repositories and audit logs for accounts or policy changes you did not make; capture forensic images before rebuilding if you find any, per the CISA KEV triage requirement.
- Enforce MFA on ISE and FMC admin access and confirm every network device that trusts ISE would fail closed rather than fall back to a local shared credential.

---

> **On the CISA KEV catalog in this edition:** CVE-2026-76460 — treat these as confirmed-exploited and patch on an emergency change.

## Executive summary

- Cisco ISE/ISE-PIC authentication bypass CVE-2026-76460 (CVSS 10.0) is actively exploited and KEV-listed with a 19 September 2026 due date - patch the identity platform before anything else this cycle.
- Cisco's September 2026 Secure Firewall hardening release states two of its flaws are actively exploited, both in FMC: a static credential vulnerability and an authentication bypass. The ASA/FTD management plane is a second live front.
- Check Point Security Management and Log Servers carry a critical unauthenticated remote code execution as root, fixed via the LivePatch channel; Check Point reports no indication of exploitation. Firewall policy control plane - treat as urgent.
- This cycle is a management-plane cycle: ISE, FMC and Check Point Security Management all outrank the individual gateway bugs. If management interfaces are reachable from user or internet networks, fix that first - it is the control that survives the next advisory too.
- Six further Cisco ASA/FTD advisories cover unauthenticated denial of service (IKEv2 certificate handling, DTLS on 3100/4200 Series, EIGRP, syslog rate limiting, TCP DNS) and one access-control bypass in ACL Object Group Search that lets blocked traffic reach protected networks. The ACL bypass is the one that silently undermines a security assumption.
- No source in this window states a fixed release number for any of these issues. Take the fixed-version table from the vendor advisory for your exact train; do not schedule an upgrade against a guessed build.

---

## Items by vendor

## Cisco

*14 item(s) — 3 critical, 6 high, 5 medium*

### Firewalls

#### 🔴 CRITICAL — Cisco Secure Firewall Adaptive Security Appliance, Secure Firewall Threat Defense, and Secure Firewall Management Center Software Hardening Release: September 2026

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-asaftdfmc-uvpPROhN)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software, Secure Firewall Threat Defense (FTD) Software and Secure Firewall Management Center (FMC) Software - affected trains listed in the September 2026 hardening advisories.  

**What happened.** Cisco published a September 2026 hardening release bundling multiple internally discovered vulnerabilities across ASA, FTD and FMC, grouped by CWE class. Cisco states two of them are known to be actively exploited: an FMC static credential vulnerability and an FMC authentication bypass vulnerability.

**Why it matters.** FMC is the management plane for the ASA/FTD fleet. A static credential plus an authentication bypass means an attacker reaching FMC can take over policy for every managed firewall at once, not one gateway. A bundled hardening release also means a long patch list per device, so the upgrade needs planning rather than an ad-hoc reboot.

**Recommended actions**

- Read the linked hardening advisory and the two FMC advisories it references, and confirm your running ASA/FTD/FMC versions against Cisco's fixed-release table - check the vendor advisory for the fixed release, no version is stated in this source.
- Patch FMC before the managed ASA/FTD devices; the actively exploited pair is in FMC.
- Remove FMC HTTPS/SSH/API access from untrusted and internet-facing interfaces; restrict to a dedicated management VLAN or out-of-band network.
- Because a static credential is involved, rotate FMC local admin credentials, API keys, certificates and device-registration keys after upgrade - a pre-patch compromise survives the upgrade.
- Upgrade ASA/FTD in the change window, HA pair secondary first, and verify config sync afterwards.
- Export and review the FMC configuration and managed-device policy for unexpected admin users, new API clients, altered access control rules or modified login pages.

**Legacy / unpatchable gear.** ASA platforms past end of software support will not receive these fixes: isolate them behind a supported inspecting firewall, deny inbound from untrusted zones, remove all direct management access in favour of a dedicated jump host with full session logging, and set a replacement date with a budget owner. Monitor them as high-risk assets with a NetFlow baseline and alerting on new outbound flows.

**Detection.** Alert on FMC administrative logins from sources other than your management jump hosts, on any successful authentication to FMC that did not traverse your MFA path, and on policy/object/deployment changes outside change windows. Compare the FMC device list and audit log against your change record.

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software IKEv2 Certificate Authentication Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-ikev2cert-dos-uWyc2xtv)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software and Secure Firewall Threat Defense (FTD) Software with IKEv2 certificate authentication configured.  

**What happened.** A logic error in the IKEv2 certificate authentication phase lets an unauthenticated, remote attacker crash the IKEv2 process by attempting a VPN connection with a crafted certificate, reloading the device. Cisco has released software updates; the advisory states there are no workarounds.

**Why it matters.** The attacker needs nothing but reachability to the IKEv2 responder, which on a remote-access or site-to-site headend is the internet by design. A repeatable reload of the firewall takes down both VPN and the traffic path behind it, and there is no configuration workaround to buy time.

**Recommended actions**

- Confirm whether IKEv2 with certificate authentication is configured on any internet-facing ASA/FTD - that is the exposure gate.
- Check running versions against Cisco's fixed-release table and schedule the upgrade; check the vendor advisory for the fixed release, none is stated here.
- Upgrade inside the change window, HA pair secondary first, and confirm tunnel re-establishment before failing back.
- Where IKEv2 peers are known and fixed (site-to-site), restrict the IKEv2 responder with a control-plane ACL to peer addresses until patched.
- Verify HA and out-of-band management still give you device access if the data plane reloads under attack.

**Legacy / unpatchable gear.** Unsupported ASA hardware gets no fix for this: terminate remote access on a supported gateway instead, or place the legacy device behind a supported firewall that filters IKEv2 to known peers only. Document the accepted risk and a replacement date.

**Detection.** Alert on unexpected device reloads and on IKEv2 process crashes in syslog, correlated with IKEv2 negotiation failures from unknown source addresses. Baseline reload counts per device so a repeated crash is visible immediately.

#### 🟠 HIGH — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Object Group Access Control List Bypass Vulnerabilities

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ftd-acl-bypass-8p6vFvw)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software and FTD Software with ACL Object Group Search (OGS) configured.  

**What happened.** Multiple logic errors in populating group access control policies when Object Group Search is enabled let an unauthenticated, remote attacker bypass configured access controls by sending traffic that should be blocked. Cisco has released updates; there are no workarounds.

**Why it matters.** This is the quiet one. The firewall reports the policy as configured while traffic reaches protected networks anyway, so segmentation you have documented and audited is not actually being enforced. It fails silently, and there is no workaround - only the upgrade.

**Recommended actions**

- Check whether Object Group Search is enabled on your ASA/FTD devices - that is the exposure condition.
- Check running versions against Cisco's fixed-release table and upgrade; check the vendor advisory for the fixed release, there is no workaround.
- After upgrade, re-test the segmentation assumptions this device enforces: run explicit allow/deny probes from each untrusted zone to a representative protected destination rather than trusting the policy view.
- Review firewall logs retroactively for connections into protected segments that your policy should have denied.
- Where the firewall is the only control between zones, add a compensating control (host firewall, VLAN ACL) so a single policy engine failure is not the whole boundary.

**Legacy / unpatchable gear.** Unsupported ASA units with OGS configured will keep failing open: disable Object Group Search if the platform allows the policy to be expressed without it, otherwise treat that firewall as a non-enforcing boundary, add an inspecting supported firewall behind it, and prioritise replacement.

**Detection.** Compare NetFlow/connection logs against the intended policy matrix: alert on any accepted flow from an untrusted zone to a protected subnet that has no matching permit rule. Periodic active path-testing beats trusting the configuration view.

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA and FTD Software on Secure Firewall 3100 Series and 4200 Series devices.  

**What happened.** Improper resource management when processing certain DTLS messages lets an unauthenticated, remote attacker send a crafted DTLS stream and reload the device, causing a denial of service. Cisco has released updates and states workarounds exist.

**Why it matters.** Limited to the 3100 and 4200 Series, but those are mid-to-high-end perimeter platforms, and DTLS is exposed wherever remote-access VPN is published. A reload is an outage of the whole traffic path, not just the VPN service.

**Recommended actions**

- Identify 3100 and 4200 Series units from the asset inventory, filtered by model and running version.
- Check running versions against Cisco's fixed-release table and schedule the upgrade; check the vendor advisory for the fixed release.
- Apply the workaround documented in the advisory if a maintenance window is not available yet.
- Restrict DTLS-listening interfaces to the addresses that genuinely need them, and confirm management access does not share that interface.
- Record patched/mitigated/accepted-risk against the device group in the change record.

**Legacy / unpatchable gear.** Not applicable to end-of-life hardware, which is not in the affected 3100/4200 range - but any unsupported ASA terminating DTLS should be isolated behind a supported firewall, denied inbound from untrusted zones, and scheduled for replacement.

**Detection.** Alert on unexpected reloads on 3100/4200 Series units and on DTLS traffic volume anomalies toward the VPN interface. Baseline reload counts so a repeat crash is obvious.

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software EIGRP Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-eigrp-dos-GOhNejSj)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software and FTD Software with EIGRP configured.  

**What happened.** Improper resource management when handling EIGRP update messages lets an unauthenticated, adjacent attacker send crafted updates at a high rate, triggering a memory leak that eventually reloads the device. Cisco has released updates; there are no workarounds.

**Why it matters.** Requires adjacency, so this is an insider or post-compromise lateral move rather than an internet-facing risk. The memory leak is slow and cumulative, so the resulting reload can look like an unexplained stability problem rather than an attack.

**Recommended actions**

- Determine which ASA/FTD devices actually run EIGRP - if none, this is an inventory note, not a change.
- Check running versions against Cisco's fixed-release table; check the vendor advisory for the fixed release.
- Enable EIGRP authentication on every EIGRP-speaking interface and disable EIGRP on interfaces that face user, guest or OT segments.
- Segment the routing adjacency: EIGRP neighbours should only be reachable across links you control.
- Upgrade in the change window, HA pair secondary first.

**Legacy / unpatchable gear.** Unsupported ASA units running EIGRP cannot be fixed: move the routing adjacency onto supported hardware, or place the legacy device on a link where no untrusted host can reach the EIGRP multicast group, with strict interface ACLs and full logging.

**Detection.** Trend free memory on ASA/FTD via SNMP and alert on sustained decline; alert on EIGRP neighbour flaps and on EIGRP update rates above baseline from any single neighbour.

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Logging Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asa-ftd-logging-dos-ZXXNesfN)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software and FTD Software - rate limiting for syslog message 419002.  

**What happened.** Improper rate limiting for syslog message 419002 lets an unauthenticated, remote attacker drive high CPU utilisation with a flood of TCP SYN packets, degrading performance. Cisco has released updates and states workarounds exist.

**Why it matters.** Reachable from anywhere the device accepts TCP, and the trigger is ordinary SYN traffic, so it is cheap to attempt. The result is performance degradation rather than a reload, which tends to be diagnosed as a capacity problem and left running for a long time.

**Recommended actions**

- Check running versions against Cisco's fixed-release table and schedule the upgrade; check the vendor advisory for the fixed release.
- Apply the advisory's documented workaround (logging configuration) if the upgrade cannot be scheduled immediately.
- Review the logging configuration for message 419002 and confirm your syslog destination is not itself being overwhelmed.
- Confirm SYN-flood protection and connection limits are configured on internet-facing interfaces.

**Legacy / unpatchable gear.** On unsupported ASA hardware, suppress or rate-limit the affected syslog message locally where the platform allows it, place the device behind a supported firewall that absorbs SYN floods, and plan replacement.

**Detection.** Alert on ASA/FTD CPU above baseline, and on a spike in syslog message 419002 volume - the message rate itself is the indicator.

#### 🟡 MEDIUM — Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software TCP DNS Denial of Service Vulnerability

*Cisco PSIRT · 2026-09-18 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tcpdns-dos-p6dUnjr5)* `vendor-advisory`

**Affected:** Cisco Secure Firewall ASA Software and FTD Software - DNS over TCP implementation.  

**What happened.** A logic error parsing DNS queries and tracking incoming buffer size lets an attacker who can answer the device's own DNS queries - by controlling the DNS service or via machine-in-the-middle - send a crafted reply that restarts the TCP DNS response handler and reloads the device. Cisco has released updates.

**Why it matters.** The attacker must be positioned on the device's DNS path, which raises the bar, but firewalls frequently resolve against upstream or ISP resolvers over untrusted paths. A reload of the perimeter firewall is a full outage.

**Recommended actions**

- Check running versions against Cisco's fixed-release table and schedule the upgrade; check the vendor advisory for the fixed release.
- Point ASA/FTD DNS at internal resolvers you control, reached over trusted paths, rather than at public or ISP resolvers.
- Restrict DNS responses to the configured resolver addresses with an interface ACL so arbitrary hosts cannot answer.
- Review which features cause the device to make DNS queries at all (FQDN objects, update servers) and remove the ones you do not use.

**Legacy / unpatchable gear.** For unsupported ASA hardware, remove the need for the device to resolve names where possible (static objects instead of FQDN objects), force DNS to an internal resolver over a trusted link, and place the device behind a supported firewall. Set a replacement date.

**Detection.** Alert on unexpected device reloads correlated with DNS activity, and on DNS responses to the firewall arriving from addresses other than the configured resolvers.

### Routers

#### 🟠 HIGH — Cisco IOS XR Software Security Hardening Release: September 2026

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)* `vendor-advisory`

**Affected:** Cisco IOS XR Software - affected trains listed in the September 2026 hardening advisory.  

**What happened.** Cisco published a September 2026 IOS XR hardening release addressing multiple internally discovered vulnerabilities, grouped by CWE class with one CVE per grouping. The advisory states these were found during internal testing and are not known to be actively exploited. Software updates are available; there are no workarounds.

**Why it matters.** IOS XR runs service provider and large enterprise core and edge routers, where an unplanned reload or a compromise affects every service riding the platform. No exploitation is reported, so this is scheduled work - but the CWE-grouped bundle means a single upgrade clears a long list, which makes it worth doing properly rather than piecemeal.

**Recommended actions**

- Inventory IOS XR platforms and running trains, and map each against the fixed releases in the hardening advisory; check the vendor advisory for the fixed release.
- Verify image integrity against the Cisco-published hash before loading.
- Plan the upgrade around redundancy: validate the ISSU or hitless path for core and edge routers, and drain traffic before touching a node that carries live services.
- Restrict the management plane while you wait: management ACLs plus control-plane policing, out-of-band management only, no direct operator access from user networks.
- Harden SNMP to v3 with auth and privacy, and disable Telnet, TFTP and any other legacy management services still enabled.

**Legacy / unpatchable gear.** IOS XR platforms past end of software maintenance will not get these fixes: restrict the management plane to an out-of-band network with a dedicated jump host and full session logging, deny management protocols from every other source with infrastructure ACLs, monitor as a high-risk asset, and set a hardware or train-migration date with a budget owner.

**Detection.** Ship IOS XR syslog and AAA accounting to the SIEM and alert on admin logins, configuration commits, and image or package changes. Alert on any management-protocol connection attempt that did not originate from the out-of-band network.

### Management platforms

#### 🔴 CRITICAL — Cisco Zero-Day Highlights API Endpoint Authentication Issues

*Dark Reading · 2026-09-18 · [source](https://www.darkreading.com/vulnerabilities-threats/cisco-zero-day-api-endpoint-authentication-issues)* `KEV`

**Affected:** Cisco Identity Services Engine (ISE) and ISE Passive Identity Connector (ISE-PIC) - CVE-2026-76460.  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** An authentication bypass in an ISE API endpoint, rated CVSS 10.0, lets an unauthenticated remote attacker bypass the web-based management interface and gain unauthorized access. It is listed in the CISA KEV catalogue (added 16 September 2026, due 19 September 2026) and reported as a zero-day.

**Why it matters.** ISE holds identity and access policy for the whole network - 802.1X on wired and wireless, guest, posture, and device administration. Unauthenticated administrative access there converts into access on every switch, controller and VPN headend that trusts it, so the blast radius is the estate rather than one appliance.

**Recommended actions**

- Locate every ISE and ISE-PIC node, including standby, evaluation and lab instances, and check the running version against the Cisco advisory's fixed-release table - check the vendor advisory for the fixed release.
- Restrict the ISE admin and API interfaces to a dedicated management VLAN or out-of-band network with an explicit source ACL; nothing user-facing or internet-facing should reach them.
- Meet the 19 September 2026 KEV due date, and follow CISA's forensics triage requirement before rebuilding or wiping a node you suspect.
- After patching, rotate ISE admin credentials, API keys, certificates and every RADIUS/TACACS+ shared secret distributed to network devices.
- Audit ISE admin accounts, API clients, repositories, endpoint identity groups and authorization policies for changes you did not make.
- Enforce MFA on ISE administrative access and confirm network devices fail closed rather than to a local shared credential if ISE is unavailable.

**Legacy / unpatchable gear.** ISE releases past end of support will not receive the fix - move authentication to a supported release or platform. In the interim, deny all access to the admin and API interfaces except from a single hardened jump host with full session logging, treat the node as an untrusted high-risk asset, and set a replacement date with a budget owner.

**Detection.** Alert on any ISE administrative or API authentication that did not come from your management network, on new admin accounts or API clients, and on authorization policy edits outside change windows. Review web server and admin audit logs for API endpoint calls without a preceding successful login.

#### 🔴 CRITICAL — Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks

*The Hacker News · 2026-09-17 · [source](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)* `KEV`

**Affected:** Cisco Identity Services Engine (ISE) - CVE-2026-76460, CVSS 10.0.  
**CVEs:** [CVE-2026-76460](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) **[KEV]**  

**What happened.** Cisco warned that CVE-2026-76460, caused by insufficient authentication control on an API endpoint, is under active exploitation and allows an unauthenticated remote attacker to bypass authentication. Same vulnerability as item 2, reported independently.

**Why it matters.** Independent confirmation of active exploitation on a maximum-severity flaw in the identity platform. This is the item that sets the priority order for the whole cycle.

**Recommended actions**

- Treat as the same remediation task as item 2 - do not schedule it twice, but do confirm every ISE node is covered.
- Verify patch status against the Cisco advisory's fixed-release table; check the vendor advisory for the fixed release.
- Confirm the ISE API endpoint is not reachable from any user, guest or internet-facing segment.
- Record the patched/mitigated decision against the ISE device group in the change record, with the KEV due date of 19 September 2026.

**Legacy / unpatchable gear.** See item 2: unsupported ISE releases get no fix and must be isolated behind strict ACLs with a dedicated jump host, monitored as high-risk assets, and scheduled for replacement.

**Detection.** Same as item 2: unauthenticated API access attempts against the ISE admin interface, admin logins from outside the management network, and unexplained changes to admin accounts or policy.

#### 🟠 HIGH — ZDI-26-716: Cisco Identity Services Engine createDBLink Command Injection Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-18 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-716/)* 

**Affected:** Cisco Identity Services Engine - CVE-2026-20176, ZDI-26-716, ZDI CVSS 7.2.  
**CVEs:** [CVE-2026-20176](https://nvd.nist.gov/vuln/detail/CVE-2026-20176)  

**What happened.** A command injection in the ISE createDBLink function allows remote attackers to execute arbitrary code on affected installations. Authentication is required to exploit it.

**Why it matters.** Authentication required keeps this below the CVSS 10.0 bypass, but the two chain: CVE-2026-76460 supplies the access this one needs to reach code execution on the identity platform. In a cycle where an unauthenticated bypass in the same product is being exploited, authenticated RCE is not a low-priority finding.

**Recommended actions**

- Patch this alongside CVE-2026-76460 in the same ISE maintenance window; check the vendor advisory for the fixed release, none is stated in this source.
- Restrict ISE administrative and API access to a dedicated management VLAN with an explicit source ACL.
- Audit ISE administrator accounts and API clients, remove stale and shared accounts, and enforce per-admin authentication with MFA.
- Rotate any credential that grants ISE administrative access, including automation and monitoring service accounts.

**Legacy / unpatchable gear.** Unsupported ISE releases get no fix for this either - the isolation and replacement plan from item 2 covers it. Treat administrative access to a legacy ISE as equivalent to root on the platform.

**Detection.** Alert on ISE administrative API calls from unusual source addresses or service accounts, and on any process execution or outbound connection from the ISE node that is not part of its normal profile.

#### 🟠 HIGH — ZDI-26-717: Cisco Identity Services Engine AlarmMessageDiskQueue Deserialization of Untrusted Data Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-18 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-717/)* 

**Affected:** Cisco Identity Services Engine - CVE-2026-20211, ZDI-26-717, ZDI CVSS 7.2.  
**CVEs:** [CVE-2026-20211](https://nvd.nist.gov/vuln/detail/CVE-2026-20211)  

**What happened.** Deserialization of untrusted data in the ISE AlarmMessageDiskQueue component allows remote attackers to execute arbitrary code on affected installations. Authentication is required to exploit it.

**Why it matters.** A second authenticated code-execution path into ISE published the same day as CVE-2026-20176, in a cycle where an unauthenticated bypass in the same product is being actively exploited. Each of these raises the value of the bypass, and all should close in one maintenance window.

**Recommended actions**

- Patch in the same ISE window as CVE-2026-76460 and CVE-2026-20176; check the vendor advisory for the fixed release.
- Restrict ISE administrative and API access to the management VLAN with an explicit source ACL.
- Enforce per-admin accounts with MFA on ISE and remove shared or stale administrative credentials.
- Rotate ISE administrative and service-account credentials after upgrade.

**Legacy / unpatchable gear.** As with the other ISE issues, an unsupported release gets no fix: isolate the admin and API interfaces behind a single jump host, log all sessions, treat the node as high risk, and schedule migration to a supported release.

**Detection.** Alert on unexpected child processes or outbound connections from the ISE node, and on administrative API activity from accounts or addresses outside the normal set.

#### 🟡 MEDIUM — ZDI-26-718: Cisco Identity Services Engine MnTRESTLivelogService XML External Entity Processing Information Disclosure Vulnerability

*Zero Day Initiative · 2026-09-18 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-718/)* 

**Affected:** Cisco Identity Services Engine - CVE-2026-20235, ZDI-26-718, ZDI CVSS 4.9.  
**CVEs:** [CVE-2026-20235](https://nvd.nist.gov/vuln/detail/CVE-2026-20235)  

**What happened.** XML external entity processing in the ISE MnTRESTLivelogService component allows remote attackers to disclose sensitive information on affected installations. Authentication is required to exploit it.

**Why it matters.** Lowest-severity of the four ISE issues this cycle - information disclosure, authenticated. It matters as a reconnaissance step: XXE against the identity platform can surface configuration and file content that makes the other ISE flaws easier to use.

**Recommended actions**

- Include in the same ISE maintenance window as the other ISE fixes; check the vendor advisory for the fixed release.
- Restrict ISE administrative and API access to the management VLAN with an explicit source ACL.
- Review which accounts hold ISE administrative or monitoring API access and remove those that no longer need it.

**Legacy / unpatchable gear.** Unsupported ISE releases get no fix: restrict admin and API access to a single jump host, log all sessions, and schedule migration to a supported release.

**Detection.** Alert on ISE REST API requests carrying XML payloads from unexpected source addresses, and on outbound connections from the ISE node to external hosts during API activity.

### Other

#### 🟠 HIGH — Cisco Secure Email Gateway SQL Injection Vulnerability

*Cisco PSIRT · 2026-09-17 · [source](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-inj-2bLVGmhX)* `vendor-advisory`

**Affected:** Cisco AsyncOS Software for Cisco Secure Email Gateway - email parsing.  

**What happened.** Insufficient validation in the email parsing logic allows an unauthenticated, remote attacker to send a crafted message containing malicious SQL and execute arbitrary SQL statements, leading to command execution with root privileges on the underlying operating system. Cisco has released updates; there are no workarounds.

**Why it matters.** The attack vector is an inbound email - no authentication, no user interaction, and the appliance's entire purpose is to accept messages from strangers. Root on the mail gateway gives an attacker every message transiting it and a foothold inside the perimeter. There is no workaround, so the upgrade is the only control.

**Recommended actions**

- Identify all Secure Email Gateway appliances and virtual instances and check AsyncOS versions against Cisco's fixed-release table; check the vendor advisory for the fixed release.
- Upgrade as a priority - the advisory states there is no workaround.
- After patching, rotate appliance admin credentials, API keys and any directory or LDAP bind accounts stored on it, and review for unexpected admin users.
- Confirm the appliance's management interface is not internet-facing and that it sits in a segment with no unnecessary route to internal servers.
- Restrict outbound connectivity from the appliance to what it actually needs (update servers, mail relays, DNS, SIEM).

**Legacy / unpatchable gear.** An unsupported email security appliance cannot be fixed and accepts untrusted input by design: put it behind a supported filtering layer, restrict its outbound connectivity to an explicit allowlist, deny it lateral access to internal networks, and plan replacement with a dated budget owner.

**Detection.** Alert on any outbound connection from the email gateway to a destination outside its allowlist, on new local accounts, and on shell or database process activity outside normal operating patterns. Review mail logs for parsing errors clustered around a single sender.

---

## Check Point

*3 item(s) — 1 critical, 2 high*

### Management platforms

#### 🔴 CRITICAL — Critical Check Point Management Flaw Lets Unauthenticated Attackers Run Code as Root

*The Hacker News · 2026-09-17 · [source](https://thehackernews.com/2026/09/critical-check-point-management-server.html)* 

**Affected:** Check Point Security Management Server and Log Servers.  

**What happened.** A critical vulnerability lets an attacker without login credentials run code as root on Security Management and Log Servers over the network. Check Point has released a fix through its LivePatch update channel and says it has no indication the flaw has been exploited.

**Why it matters.** The Security Management Server controls firewall policy and administrator access for the whole gateway estate. Unauthenticated root there means an attacker can rewrite policy on every gateway, add administrators, and read the logs that would have shown them doing it. No reported exploitation, but the reachability and the privilege level make this the equal of the Cisco management-plane issues in this cycle.

**Recommended actions**

- Apply the fix via the Check Point LivePatch channel on every Security Management Server and Log Server, including standby and multi-domain servers; check the vendor advisory for the fixed release and the exact LivePatch package.
- Confirm the management and log servers are reachable only from a dedicated management network - no internet exposure, no reachability from user or guest VLANs.
- Rotate management server admin credentials, API keys and SIC certificates after patching, and review the administrator list for accounts you did not create.
- Compare the current policy package and administrator permissions against your change record for unexplained edits.
- Confirm log integrity: if the log server can be rooted, logs from before the patch cannot be treated as authoritative - forward to an external SIEM so there is a copy the attacker cannot edit.

**Legacy / unpatchable gear.** A management or log server on an unsupported version will not receive the LivePatch: isolate it to a management-only segment reachable from a single hardened jump host, deny all other inbound access, forward logs off the box immediately so there is an independent copy, and set a migration date to a supported release with a budget owner.

**Detection.** Alert on administrator logins and policy installs on the management server that fall outside change windows or come from outside the management network, on new SmartConsole administrator accounts, and on gaps or truncation in log server data.

#### 🟠 HIGH — Check Point, Kaspersky, Tanium Patch Product Vulnerabilities

*SecurityWeek · 2026-09-18 · [source](https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/)* 

**Affected:** Check Point Security Management and Log Servers (reported alongside unrelated Kaspersky and Tanium fixes).  

**What happened.** Coverage confirming that Check Point Security Management and Log Servers are affected by a critical vulnerability allowing remote code execution with root privileges. Same issue as items 12 and 17.

**Why it matters.** Corroborates the Check Point management-server flaw from a second source. The Kaspersky and Tanium items in the same article are not network infrastructure and are out of scope here.

**Recommended actions**

- Treat as the same remediation task as item 12 - do not raise a second change.
- Confirm every Security Management and Log Server, including multi-domain and standby, is covered by the LivePatch fix; check the vendor advisory for the fixed release.
- Record the patched/mitigated decision against the management server group in the change record.

**Legacy / unpatchable gear.** See item 12: unsupported management or log servers must be isolated to a management-only segment with a single jump host, with logs forwarded off-box, and migrated to a supported release on a dated plan.

**Detection.** Same as item 12: administrator logins and policy installs outside change windows or from outside the management network.

#### 🟠 HIGH — New Check Point flaw lets hackers execute code with root privileges

*BleepingComputer · 2026-09-18 · [source](https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/)* 

**Affected:** Check Point management systems - Security Management and Log Servers.  

**What happened.** Check Point released security updates for a critical vulnerability that lets attackers execute code with root privileges on management systems. Same issue as items 12 and 13.

**Why it matters.** Third independent report of the same management-server flaw. Confirms the fix is published and available.

**Recommended actions**

- Treat as the same remediation task as item 12 - one change, all management and log servers.
- Verify the update is applied on every management system, including standby and multi-domain servers; check the vendor advisory for the fixed release.
- Confirm management systems are not reachable from user, guest or internet-facing networks.

**Legacy / unpatchable gear.** See item 12: unsupported management systems must be isolated behind a jump host on a management-only segment, with logs forwarded off-box and a dated migration plan.

**Detection.** Same as item 12: administrator logins, policy installs and account changes on the management server outside change windows or from outside the management network.

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
    "firewall",
    "management-platform"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false
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
   "kev": true
  },
  {
   "title": "Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks",
   "link": "https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html",
   "source": "The Hacker News",
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
   "kev": true
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
   "kev": false
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
    "Cisco"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco IOS XR Software Security Hardening Release: September 2026",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM",
   "source": "Cisco PSIRT",
   "relevance": "high",
   "device_types": [
    "router"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false
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
   "kev": false
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
   "kev": false
  },
  {
   "title": "Check Point, Kaspersky, Tanium Patch Product Vulnerabilities",
   "link": "https://www.securityweek.com/check-point-kaspersky-tanium-patch-product-vulnerabilities/",
   "source": "SecurityWeek",
   "relevance": "high",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Check Point"
   ],
   "cves": [],
   "kev": false
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
   "kev": false
  },
  {
   "title": "New Check Point flaw lets hackers execute code with root privileges",
   "link": "https://www.bleepingcomputer.com/news/security/check-point-warns-critical-flaw-lets-hackers-execute-code-as-root/",
   "source": "BleepingComputer",
   "relevance": "high",
   "device_types": [
    "management-platform"
   ],
   "vendors": [
    "Check Point"
   ],
   "cves": [],
   "kev": false
  },
  {
   "title": "Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software for Secure Firewall 3100 and 4200 Series DTLS Denial of Service Vulnerability",
   "link": "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-dtls-dos-Kp57HkyO",
   "source": "Cisco PSIRT",
   "relevance": "medium",
   "device_types": [
    "firewall"
   ],
   "vendors": [
    "Cisco"
   ],
   "cves": [],
   "kev": false
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
   "kev": false
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
   "kev": false
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
   "kev": false
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
   "kev": false
  }
 ]
}
-->

## How this was produced

- Feeds polled: 18 ok, 1 failed
- Raw items: 670 → in window: 94 → network-device relevant: 19 → published: 17
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `claude-code-action`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
