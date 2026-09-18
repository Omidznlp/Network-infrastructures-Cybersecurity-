---
layout: post
title: "Network Device Security Digest - 2026-09-17"
date: 2026-09-17 22:35:51 +0000
edition: daily
critical_count: 2
item_count: 6
kev: "CVE-2026-76461"
analysis_mode: "claude-code-action"
categories: digest
---

# Network Device Security Digest — 2026-09-17

*daily edition · window 72h · 18 feeds · 6 items · 2 critical · generated 2026-09-17 22:35 UTC*

> Scope: firewalls, VPN gateways, routers, switches, wireless controllers, load balancers and SD-WAN edge. Everything else is filtered out.

---

## 🧠 Headline — AI-found bugs land where you cannot patch fast: pre-auth flaws in appliances that parse untrusted traffic

One item this cycle addresses AI directly. Cisco Talos argues that AI-assisted vulnerability discovery will keep surfacing flaws that are difficult or effectively impossible to patch, and that segmentation, visibility and NGFW/IPS inspection have to carry the load as a compensating layer. That is a statement about supply, not about a specific incident: the rate at which bugs are found in appliance code is rising faster than the rate at which network teams can schedule maintenance windows on perimeter gear.

The rest of the cycle shows what that supply looks like when it lands. CVE-2026-76461 in Cisco AsyncOS for Secure Email Gateway is a SQL injection in email parsing logic, CVSS 9.8, unauthenticated, root command execution, exploited in the wild, and triggered by sending a crafted email through the appliance's normal mail flow. There is no administrative interface to firewall off and no login to add MFA to - the attack surface is the data plane doing its job. CISA added it to KEV on 2026-09-14 with a due date of 2026-09-17. ZDI-26-709 (CVE-2026-20242) is the same shape one layer in: unauthenticated deserialization RCE on Cisco Secure Firewall Management Center, the box that owns policy for the firewall estate. Compromise there is compromise of every FTD it manages.

The defensive read for this week: management-plane hardening remains necessary but is no longer sufficient for appliances that accept untrusted input by design. Assume exploit development against internet-facing devices is faster than your historical patch SLA and compress that window to days. Where an AI or AIOps assistant touches network management, treat it as a privileged admin path - device logs, hostnames and ticket text are attacker-influenced content, and an agent that reads them and can write config is a prompt-injection target. Use AI on the defensive side for baselining NetFlow and syslog rather than waiting on signature updates, because the first indicator of a data-plane exploit is usually an anomalous outbound flow from an appliance that should never initiate one.

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

## Executive summary

- CVE-2026-76461 (Cisco AsyncOS / Secure Email Gateway, CVSS 9.8) is exploited in the wild and on KEV with a due date of 2026-09-17 - unauthenticated root command execution triggered by a crafted email, no admin interface involved. Treat as the emergency of the cycle.
- ZDI-26-709 / CVE-2026-20242: unauthenticated deserialization RCE on Cisco Secure Firewall Management Center (CVSS 8.1). The management plane of the firewall estate; restrict reachability to a jump host now and patch on vendor release.
- Neither Cisco item ships a fixed release in the collected sources - pull the version table directly from the vendor advisory before you build the change record.
- Cisco Talos frames the structural issue: AI-driven vulnerability discovery produces flaws that cannot be patched in time or at all, so segmentation, visibility and NGFW/IPS inspection become the compensating control rather than the backstop.
- Lower priority: Palo Alto GlobalProtect App local privilege escalation (CVE-2026-0307, MEDIUM) folds into the normal client push cycle; Issabel PBX CVE-2026-89026 is a hard-coded-credential unauth RCE under active exploitation - relevant if your voice platform sits in your estate, and note the feed mis-tagged it as Ubiquiti.
- One item dropped as out of scope (Vite dev-server mass scanning - F5 is the researcher, not the affected product).

> **On the CISA KEV catalog in this edition:** CVE-2026-76461 — treat these as confirmed-exploited and patch on an emergency change.

---

## Items

### 🔴 CRITICAL — CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild

*Rapid7 Blog · 2026-09-15 · [source](https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild)* `KEV`

**Affected:** Cisco AsyncOS Software for Cisco Secure Email Gateway (formerly IronPort Email Security Appliance). CVE-2026-76461, reported CVSS v3.1 base score 9.8. No fixed release is stated in the source.  
**Device types:** email security gateway, perimeter appliance  
**CVEs:** [CVE-2026-76461](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) **[KEV]**  

**What happened.** Cisco published an advisory on 2026-09-14 for a SQL injection vulnerability in Cisco AsyncOS for Secure Email Gateway allowing an unauthenticated remote attacker to execute arbitrary commands with root privileges on the appliance. Exploitation reportedly requires only sending a specially crafted email through the gateway - no authentication and no access to the administrative interface. CISA added it to KEV on 2026-09-14 with a remediation due date of 2026-09-17.

**Why it matters.** The vulnerable path is the appliance's normal mail-processing function, so management-plane ACLs and admin MFA provide no protection. A rooted email gateway sits inline on all inbound and outbound mail, holds mail-flow credentials and LDAP/AD bind accounts, and is typically trusted by internal mail infrastructure. It is being exploited now and the KEV due date has already arrived.

**Recommended actions**

- Inventory every Secure Email Gateway / ESA appliance and record its running AsyncOS version; check each against the vendor's fixed-release table - check the vendor advisory for the fixed release, it is not stated in the reporting.
- Upgrade immediately as an emergency change; where appliances are clustered, upgrade the secondary or non-active unit first and validate mail flow before failing over.
- If a maintenance window cannot be secured today, apply the vendor's documented mitigation and treat the appliance as suspect - exploitation needs only inbound mail, so there is no exposure reduction available short of taking it out of the mail path.
- After patching, rotate everything the appliance holds: local admin credentials, API keys, LDAP/AD bind accounts, SMTP relay credentials, certificates and any cloud-console tokens.
- Export and diff the appliance configuration against a known-good copy: unexpected admin users, message filters, content filters, listener changes, SSH keys or altered routing entries.
- Restrict management access (HTTPS/SSH/API) to a dedicated management VLAN or out-of-band network and enforce MFA on all administrative accounts, to limit the attacker's next hop even though it does not block this bug.
- Record the outcome (patched / mitigated / accepted risk) per appliance against the KEV due date of 2026-09-17.

**Legacy / unpatchable gear.** IronPort-generation hardware or an AsyncOS train past end of support will not receive a fix. Take it out of the inbound mail path - route mail through a supported gateway or a cloud mail-security service - rather than leaving an unpatchable appliance parsing internet email. If it must stay inline temporarily, place it in its own segment behind an inspecting firewall, deny it any outbound connectivity except the specific mail and update destinations it needs, remove all direct management access in favour of a jump host with full session logging, and monitor it as a high-risk asset. Set a replacement date and a budget owner.

**Detection.** Hunt for outbound connections from the gateway to anything other than known mail peers, DNS, NTP and Cisco update endpoints - a mail appliance initiating arbitrary egress is the strongest signal. Review AsyncOS mail logs and system logs for malformed or unusually structured inbound messages preceding process restarts or errors in the email parsing path, new or modified CLI/admin accounts, new SSH authorized keys, unexpected message/content filter changes, and shell command execution by root outside of maintenance. In NetFlow, alert on any new destination ASN or port from the appliance's IP.

**AI angle.** No AI involvement is reported for this vulnerability. It is the archetype Talos describes in the same cycle: a pre-auth flaw in code that parses attacker-supplied data, where the only durable controls are segmentation, egress control and behavioural detection rather than the patch window.

---

### 🔴 CRITICAL — Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution

*The Hacker News · 2026-09-15 · [source](https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html)* `KEV`

**Affected:** Cisco AsyncOS Software for Cisco Secure Email Gateway. CVE-2026-76461, CVSS 9.8, described as insufficient validation in the email parsing logic. No fixed release is stated in the source.  
**Device types:** email security gateway, perimeter appliance  
**CVEs:** [CVE-2026-76461](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) **[KEV]**  

**What happened.** Second-source confirmation of item 0. Cisco warned that CVE-2026-76461 in AsyncOS for Secure Email Gateway is under active exploitation in the wild; the root cause is described as insufficient validation in the email parsing logic permitting an unauthenticated remote attacker to execute commands.

**Why it matters.** Independent reporting of active exploitation raises confidence that this is a live campaign rather than a theoretical CVSS 9.8. The 'insufficient validation in email parsing' framing confirms the trigger is inbound mail, which rules out exposure reduction as a mitigation.

**Recommended actions**

- Treat as the same change record as item 0 - do not open a second workstream.
- Confirm the running AsyncOS version on every appliance against the vendor advisory and upgrade as an emergency change; check the vendor advisory for the fixed release.
- Escalate the assumption from 'vulnerable' to 'potentially compromised' for any appliance that processed internet mail while unpatched, and run the credential rotation and configuration diff from item 0 regardless of whether IOCs are found.
- Ask the mail team to preserve AsyncOS logs beyond the default retention before upgrading, so forensic triage is still possible afterwards.

**Legacy / unpatchable gear.** Same as item 0: an unsupported AsyncOS train or IronPort-era appliance cannot be fixed. Remove it from the inbound mail path, front it with a supported gateway or cloud mail security, isolate it behind an inspecting firewall with strict egress ACLs and jump-host-only management, monitor it as a high-risk asset, and set a replacement date with a named owner.

**Detection.** As item 0. Additionally, correlate inbound message metadata (sender, source IP, message ID) around the time of any anomalous appliance egress or process behaviour, so the triggering message can be recovered for analysis and the sending infrastructure blocked at the perimeter.

---

### 🟠 HIGH — ZDI-26-709: Cisco Secure Firewall Management Center CommandSinkRmi Deserialization of Untrusted Data Remote Code Execution Vulnerability

*Zero Day Initiative · 2026-09-16 · [source](http://www.zerodayinitiative.com/advisories/ZDI-26-709/)* 

**Affected:** Cisco Secure Firewall Management Center. CVE-2026-20242, deserialization of untrusted data in CommandSinkRmi, ZDI-assigned CVSS 8.1, authentication not required. Affected and fixed versions are not stated in the advisory text.  
**Device types:** firewall, firewall management platform  
**CVEs:** [CVE-2026-20242](https://nvd.nist.gov/vuln/detail/CVE-2026-20242)  

**What happened.** ZDI published advisory ZDI-26-709 describing an unauthenticated remote code execution vulnerability in Cisco Secure Firewall Management Center caused by deserialization of untrusted data in the CommandSinkRmi component.

**Why it matters.** FMC is the policy and management plane for the FTD estate. Code execution on FMC means the ability to push arbitrary policy, read the full firewall configuration set, harvest device credentials and certificates, and reach every managed firewall from a trusted source. No authentication is required, so a single reachable FMC instance is a full-estate compromise path. RMI listeners are frequently left reachable from broader internal networks than intended.

**Recommended actions**

- Locate every FMC instance (physical, virtual and cloud-delivered) and determine which networks can currently reach its RMI and management ports.
- Restrict FMC reachability immediately to a dedicated management network and a named jump host; deny access from user, guest, server and OT VLANs and confirm it is not reachable from the internet or from any VPN pool.
- Check the vendor advisory for the fixed release and schedule the FMC upgrade ahead of any managed-device upgrades - patch the management plane before the data plane.
- Enforce MFA on all FMC administrative accounts and remove shared local admin accounts; move admin authentication to TACACS+/RADIUS with per-admin identities.
- After patching, rotate FMC admin credentials, API tokens, the FMC-to-FTD registration keys and device certificates, and re-verify device registration health.
- Audit the FMC policy set and audit log for unauthorised access-control rule changes, new policy objects, new admin users, scheduled tasks and unexpected policy deployments.

**Legacy / unpatchable gear.** An FMC running on an unsupported hardware generation or an EOL software train will not get this fix. Do not leave it as the live management plane for production firewalls - plan migration to a supported FMC (virtual FMC is the usual bridge) and set a date. Until then, reduce it to a single reachable source: a hardened jump host on an out-of-band management network, with all other paths denied at the firewall in front of it, full session recording on the jump host, and alerting on every authentication attempt. Managed FTDs that survive an FMC compromise still need their registration keys and certificates rotated after migration.

**Detection.** Alert on connections to the FMC RMI/management ports from any source outside the management network. On the FMC itself, hunt for unexpected child processes spawned by the Java management process, new files written outside normal update paths, outbound connections from FMC to non-Cisco destinations, and audit-log entries for policy deployments, new admin users or object changes with no matching change record. On managed FTDs, alert on policy deployments arriving outside the change window.

**AI angle.** None reported. Deserialization sinks in management daemons are a prime target for automated and AI-assisted code analysis, which is an argument for treating the management plane as internet-equivalent hostile territory rather than a trusted internal service.

---

### 🟠 HIGH — Securing the unpatchable in an age of AI-driven vulnerabilities

*Cisco Talos · 2026-09-16 · [source](https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/)* `AI`

**Affected:** No specific product. Cisco Talos guidance on devices where a patch is difficult or effectively unavailable.  
**Device types:** firewall, ips, network infrastructure generally  

**What happened.** Cisco Talos published guidance arguing that advances in AI will keep identifying vulnerabilities that are in some circumstances difficult or effectively impossible to patch, and that network segmentation, rigorous visibility and NGFW/IPS deployment provide a compensatory layer.

**Why it matters.** This is the strategic frame for the rest of the cycle, and it changes how a network team should budget its attention. If discovery outpaces the ability to patch, the controls that carry risk are the ones that work without a fix: segmentation that limits what a compromised appliance can reach, egress control that blocks the attacker's callback, inspection that catches exploitation in traffic, and visibility that detects deviation. The two Cisco vulnerabilities this cycle are both pre-auth flaws in code that processes untrusted input - exactly the class where a fast patch is the only traditional control and it frequently arrives too late.

**Recommended actions**

- Produce a list of devices in the estate that cannot be patched quickly or at all - end-of-life models, appliances with no maintenance window, OT and voice gear, anything running a train past end of support - and treat that list as a standing risk register rather than a one-off audit.
- For each device on that list, define the blast radius: what it can reach, what can reach it, and what credentials it holds. Reduce each of the three with ACLs, segmentation and credential scoping.
- Enforce egress control on network appliances themselves - a firewall, mail gateway or controller should reach a short, named list of destinations and nothing else. This is the control that survives an unpatchable pre-auth RCE.
- Deploy NGFW/IPS inspection in front of appliances that must accept untrusted input, so exploitation attempts are visible and blockable even before a vendor fix exists.
- Baseline NetFlow and syslog per device class and alert on deviation rather than relying on signature updates alone; a new outbound flow from an appliance is a higher-fidelity signal than any single IOC.
- Scope any AI, AIOps or MCP/agent integration touching network management to read-only credentials with no unattended config write and a full audit trail, and test it for prompt injection from attacker-influenced text such as device logs, hostnames and ticket contents.
- Shorten the patch SLA for internet-facing network devices to days and require callback verification for out-of-band requests to change firewall or VPN configuration.

**Legacy / unpatchable gear.** This item is about legacy gear by definition. For anything that will never receive a fix: isolate it behind a supported inspecting firewall, deny inbound access from untrusted zones, permit only the specific flows the device needs in either direction, remove direct management access in favour of a dedicated jump host with full session logging, and monitor it as a high-risk asset with a NetFlow baseline and alerting on any new flow. Then set a replacement date and a named budget owner, and record the accepted risk against the device group until the replacement lands. Compensating controls are a bridge, not a destination.

**Detection.** Not an incident, so no IOCs. The detection work it implies: per-device egress baselines with alerting on any new destination, syslog alerting on admin logins, configuration changes and firmware changes outside change windows, and periodic reconciliation of running versions against the asset inventory so unpatchable devices cannot quietly accumulate.

**AI angle.** This is the AI item of the cycle. Talos's claim is about the supply side - AI-assisted discovery raises the rate at which appliance vulnerabilities are found, including flaws in code paths that cannot be safely changed. The operational consequence is that patch velocity alone stops being a viable strategy and compensating architecture becomes the primary control. The same logic applies to AI on the management side: an LLM assistant or agent with write access to network configuration is a new privileged path that needs scoping, auditing and prompt-injection testing before it is trusted with anything beyond read.

---

### 🟡 MEDIUM — CVE-2026-0307 GlobalProtect App: Local Privilege Escalation Vulnerabilities (Severity: MEDIUM)

*Palo Alto Networks PSIRT · 2026-09-16 · [source](https://security.paloaltonetworks.com/CVE-2026-0307)* `vendor-advisory`

**Affected:** Palo Alto Networks GlobalProtect App. CVE-2026-0307, local privilege escalation, vendor severity MEDIUM. No affected or fixed version numbers appear in the PSIRT feed entry.  
**Device types:** vpn, vpn client endpoint software  
**CVEs:** [CVE-2026-0307](https://nvd.nist.gov/vuln/detail/CVE-2026-0307)  

**What happened.** Palo Alto Networks PSIRT published an advisory for local privilege escalation vulnerabilities in the GlobalProtect App.

**Why it matters.** This is the VPN client on managed endpoints, not the gateway, and exploitation requires local access - so it is not a perimeter emergency. It still belongs to the network team because GlobalProtect runs with high privilege on every remote-access endpoint and a local-privilege-escalation chain there gives an attacker SYSTEM/root on machines that hold VPN certificates and tunnel into the corporate network. Firewall and Panorama availability are unaffected.

**Recommended actions**

- Read the PSIRT advisory for the affected client version ranges and the fixed build - check the vendor advisory for the fixed release, the PSIRT feed entry does not list versions.
- Determine the deployed GlobalProtect App versions from your endpoint management platform, and publish the fixed client through the normal software-distribution cycle rather than as an emergency change.
- Where the gateway is configured to push client upgrades, set the client-upgrade policy so endpoints pick up the fixed build on next connection, and set a date after which non-compliant client versions are refused or quarantined by HIP policy.
- Confirm end users cannot disable or downgrade the GlobalProtect client, and that the installation directory and service configuration are not writable by unprivileged users.
- Continue to enforce phishing-resistant MFA on the remote-access portal, so that a compromised endpoint does not directly yield reusable gateway access.

**Legacy / unpatchable gear.** Endpoints on an operating system too old to run a fixed GlobalProtect build cannot be remediated by upgrading the client. Move them off direct VPN access: terminate their sessions on a jump host or virtual desktop in a restricted segment instead of granting a full tunnel, restrict what that segment can reach to the specific applications they need, and set a replacement date for the machines. Do not leave unpatchable endpoints holding a full-tunnel VPN certificate.

**Detection.** On endpoints, alert on privilege escalation patterns around the GlobalProtect service - service binary or configuration modification, unexpected child processes spawned by the GlobalProtect service account, and writes to the installation directory outside of a signed update. On the gateway, report on connecting client versions so stale builds are visible.

---

### ⚪ WATCH — Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution

*The Hacker News · 2026-09-16 · [source](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html)* 

**Affected:** Issabel Framework, the web-based framework for the open-source unified communications PBX software. CVE-2026-89026, CVSS v3.1 9.8 / CVSS v4.0 9.3, hard-coded credential leading to unauthenticated OS command execution. No fixed release is stated in the source.  
**Device types:** unified communications / PBX server, voice infrastructure  
**CVEs:** [CVE-2026-89026](https://nvd.nist.gov/vuln/detail/CVE-2026-89026)  

**What happened.** A critical flaw in Issabel Framework is under active exploitation. A hard-coded credential allows an unauthenticated remote attacker to execute arbitrary operating system commands.

**Why it matters.** This is a UC/PBX application server, not a firewall, router or switch - hence 'watch' rather than a higher rating. It matters to the network team anyway because voice platforms are commonly internet-exposed for SIP trunking and remote extensions, sit in a VLAN that is often over-trusted, and hold SIP trunk credentials whose theft produces direct toll fraud. Note that the collection feed tagged this item 'ubiquiti'; that is a mis-tag - Issabel is unrelated to Ubiquiti, so do not scope a Ubiquiti estate against this CVE.

**Recommended actions**

- Ask whoever owns voice whether any Issabel (or Issabel-derived FreePBX-family) system exists in the estate; if not, close this out.
- If one exists, confirm from the firewall whether its web interface is reachable from the internet and remove that exposure now - restrict the admin web UI to an internal management network or VPN.
- Check the vendor/project advisory for the fixed release and apply it; a hard-coded credential cannot be mitigated by changing a password.
- Rotate SIP trunk credentials, extension secrets and any AMI/API credentials on the platform, and ask the carrier to apply a spend cap and destination restrictions on the trunk.
- Segment the voice VLAN: deny it any route to management or server networks it does not need, and restrict outbound SIP to the carrier's IP ranges only.

**Legacy / unpatchable gear.** Unmaintained Issabel or Elastix-era installations are common and will not be fixed. Take the web interface off the internet entirely, place the server behind an inspecting firewall that permits only carrier SIP/RTP ranges inbound and nothing else, deny outbound except to the carrier and NTP/DNS, and manage it only from a jump host. Enforce a carrier-side spend cap and international-destination block so that a compromise is bounded by cost. Plan migration to a supported platform with a named owner and date.

**Detection.** Alert on inbound HTTP/HTTPS to the PBX from external addresses, on outbound connections from the PBX to anything other than the carrier, NTP and DNS, and on shell processes spawned by the web server user. In call detail records, watch for spikes in international or premium-rate destinations, out-of-hours call volume, and new extensions or trunk definitions with no change record.

---

<!--index
{
 "url": "/2026/09/17/network-security-digest/",
 "date": "2026-09-17",
 "entries": [
  {
   "title": "CVE-2026-76461: Critical Cisco Secure Email Gateway Vulnerability Exploited in the Wild",
   "link": "https://www.rapid7.com/blog/post/etr-cve-2026-76461-critical-cisco-secure-email-gateway-vulnerability-exploited-in-the-wild",
   "source": "Rapid7 Blog",
   "relevance": "critical",
   "device_types": [
    "email security gateway",
    "perimeter appliance"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-76461"
   ],
   "kev": true
  },
  {
   "title": "Cisco Secure Email Gateway Flaw Exploited in the Wild, Enables Root Command Execution",
   "link": "https://thehackernews.com/2026/09/cisco-secure-email-gateway-flaw.html",
   "source": "The Hacker News",
   "relevance": "critical",
   "device_types": [
    "email security gateway",
    "perimeter appliance"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-76461"
   ],
   "kev": true
  },
  {
   "title": "ZDI-26-709: Cisco Secure Firewall Management Center CommandSinkRmi Deserialization of Untrusted Data Remote Code Execution Vulnerability",
   "link": "http://www.zerodayinitiative.com/advisories/ZDI-26-709/",
   "source": "Zero Day Initiative",
   "relevance": "high",
   "device_types": [
    "firewall",
    "firewall management platform"
   ],
   "vendors": [
    "cisco"
   ],
   "cves": [
    "CVE-2026-20242"
   ],
   "kev": false
  },
  {
   "title": "Securing the unpatchable in an age of AI-driven vulnerabilities",
   "link": "https://blog.talosintelligence.com/securing-the-unpatchable-in-an-age-of-ai-driven-vulnerabilities/",
   "source": "Cisco Talos",
   "relevance": "high",
   "device_types": [
    "firewall",
    "ips",
    "network infrastructure generally"
   ],
   "vendors": [],
   "cves": [],
   "kev": false
  },
  {
   "title": "CVE-2026-0307 GlobalProtect App: Local Privilege Escalation Vulnerabilities (Severity: MEDIUM)",
   "link": "https://security.paloaltonetworks.com/CVE-2026-0307",
   "source": "Palo Alto Networks PSIRT",
   "relevance": "medium",
   "device_types": [
    "vpn",
    "vpn client endpoint software"
   ],
   "vendors": [
    "palo alto"
   ],
   "cves": [
    "CVE-2026-0307"
   ],
   "kev": false
  },
  {
   "title": "Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Command Execution",
   "link": "https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html",
   "source": "The Hacker News",
   "relevance": "watch",
   "device_types": [
    "unified communications / PBX server",
    "voice infrastructure"
   ],
   "vendors": [
    "ubiquiti"
   ],
   "cves": [
    "CVE-2026-89026"
   ],
   "kev": false
  }
 ]
}
-->

## How this was produced

- Feeds polled: 18 ok, 1 failed
- Raw items: 670 → in window: 100 → network-device relevant: 8 → published: 6
- Enrichment: CISA KEV, FIRST EPSS
- Analysis: `claude-code-action`

_Automated digest. Verify every version number against the vendor advisory before you schedule a change._
