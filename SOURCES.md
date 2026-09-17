# Sources

Two kinds of source: **machine-readable feeds** (what the pipeline actually ingests) and
**LinkedIn pages** (for humans to follow — LinkedIn has no RSS and its public API does not
expose company posts, so these are not automated; see the note at the bottom).

---

## 1. Automated feeds (in `config/sources.json`)

### Vendor PSIRT — network device advisories (highest signal)

| Vendor | Feed / advisory page |
|---|---|
| Cisco | `https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml` |
| Palo Alto Networks | `https://security.paloaltonetworks.com/rss.xml` |
| Fortinet | `https://filestore.fortinet.com/fortiguard/rss/ir.xml` · https://fortiguard.fortinet.com/psirt |
| Juniper | https://supportportal.juniper.net/JSA (JSA advisories) |
| F5 | https://my.f5.com/manage/s/security-advisories |
| Citrix / NetScaler | https://support.citrix.com/securitybulletins |
| Ivanti | https://forums.ivanti.com/s/security-advisories |
| SonicWall | https://psirt.global.sonicwall.com/vuln-list |
| Check Point | https://support.checkpoint.com/results/sk/sk181639 |
| Sophos | https://www.sophos.com/en-us/security-advisories |
| HPE Aruba Networking | https://www.arubanetworks.com/support-services/security-bulletins/ |
| Arista | https://www.arista.com/en/support/advisories-notices |
| Zyxel | https://www.zyxel.com/global/en/support/security-advisories |
| MikroTik | https://mikrotik.com/download/changelogs |
| NETGEAR | https://kb.netgear.com/000065984/Security-Advisories |
| TP-Link | https://www.tp-link.com/us/press/security-advisory/ |
| D-Link | https://supportannouncement.us.dlink.com/ |
| Ubiquiti | https://community.ui.com/releases |
| WatchGuard | https://www.watchguard.com/wgrd-psirt |
| Barracuda | https://www.barracuda.com/company/legal/trust-center/advisories |

> Feeds marked `enabled: false` in `config/sources.json` are vendors whose RSS endpoint is
> unstable or login-gated — the page is listed here so you can add a working feed URL later.
> A failing feed never breaks a run; it is logged and skipped.

### Government / CERT

| Source | Feed |
|---|---|
| CISA advisories (incl. ICS) | `https://www.cisa.gov/cybersecurity-advisories/all.xml` |
| CISA KEV catalog (enrichment) | `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` |
| NCSC UK | `https://www.ncsc.gov.uk/api/1/services/v1/report-rss-feed.xml` |
| FIRST EPSS (enrichment) | `https://api.first.org/data/v1/epss?cve=` |
| NVD (CVE detail links) | https://nvd.nist.gov/vuln/detail/CVE-… |

### Research / threat intel

Zero Day Initiative · Cisco Talos · Unit 42 · Rapid7 · watchTowr Labs · GreyNoise ·
SANS Internet Storm Center · Shadowserver

### Security press

BleepingComputer · The Hacker News · SecurityWeek · The Record · Dark Reading ·
Help Net Security · Krebs on Security

---

## 2. LinkedIn pages to follow

Grouped by how useful they are for **network-device** security specifically. Slugs are the
common ones; confirm each by opening it once — LinkedIn occasionally changes a company slug.

### Vendor security / PSIRT-adjacent pages

| Page | URL |
|---|---|
| Cisco Security | `linkedin.com/company/cisco-security` |
| Cisco Talos Intelligence Group | `linkedin.com/company/cisco-talos-intelligence-group` |
| Fortinet | `linkedin.com/company/fortinet` |
| FortiGuard Labs | `linkedin.com/showcase/fortiguard-labs` |
| Palo Alto Networks | `linkedin.com/company/palo-alto-networks` |
| Unit 42 | `linkedin.com/showcase/unit42` |
| Juniper Networks | `linkedin.com/company/juniper-networks` |
| F5 | `linkedin.com/company/f5` |
| Check Point Software | `linkedin.com/company/check-point-software-technologies` |
| Sophos | `linkedin.com/company/sophos` |
| SonicWall | `linkedin.com/company/sonicwall` |
| Ivanti | `linkedin.com/company/ivanti` |
| Citrix | `linkedin.com/company/citrix` |
| HPE Aruba Networking | `linkedin.com/company/hpe-aruba-networking` |
| Arista Networks | `linkedin.com/company/arista-networks-inc` |
| Extreme Networks | `linkedin.com/company/extreme-networks` |
| Ubiquiti | `linkedin.com/company/ubiquiti-inc` |
| MikroTik | `linkedin.com/company/mikrotik` |
| Netgear | `linkedin.com/company/netgear` |
| WatchGuard Technologies | `linkedin.com/company/watchguard-technologies` |
| Barracuda | `linkedin.com/company/barracuda-networks` |

### Government / national bodies

| Page | URL |
|---|---|
| CISA | `linkedin.com/company/cisa` |
| NSA | `linkedin.com/company/national-security-agency` |
| UK NCSC | `linkedin.com/company/national-cyber-security-centre` |
| ENISA | `linkedin.com/company/european-union-agency-for-cybersecurity` |
| FIRST.org | `linkedin.com/company/first-org` |
| NIST | `linkedin.com/company/nist` |

### News outlets and research labs

| Page | URL |
|---|---|
| BleepingComputer | `linkedin.com/company/bleepingcomputer` |
| The Hacker News | `linkedin.com/company/thehackernews` |
| SecurityWeek | `linkedin.com/company/securityweek` |
| Dark Reading | `linkedin.com/company/dark-reading` |
| The Record from Recorded Future | `linkedin.com/company/therecordmedia` |
| Help Net Security | `linkedin.com/company/help-net-security` |
| SANS Institute | `linkedin.com/company/sans-institute` |
| Zero Day Initiative | `linkedin.com/company/zero-day-initiative` |
| GreyNoise Intelligence | `linkedin.com/company/greynoise-intelligence` |
| Censys | `linkedin.com/company/censys` |
| Shodan | `linkedin.com/company/shodan` |
| Rapid7 | `linkedin.com/company/rapid7` |
| watchTowr | `linkedin.com/company/watchtowr` |
| Recorded Future | `linkedin.com/company/recorded-future` |
| Shadowserver Foundation | `linkedin.com/company/the-shadowserver-foundation` |

### Communities, hashtags and search feeds

- Hashtags worth following: `#networksecurity` `#firewall` `#ciscosecurity` `#fortinet`
  `#paloaltonetworks` `#zerotrust` `#CVE` `#KEV` `#ThreatIntel` `#OTsecurity` `#AIsecurity`
- LinkedIn Groups: *Network Security*, *Cyber Security Forum Initiative (CSFI)*,
  *Information Security Community*, *ISACA*, *(ISC)² members*
- Saved LinkedIn searches (content search, sorted by latest) for terms like
  `FortiOS CVE`, `PAN-OS advisory`, `IOS XE exploited`, `NetScaler`, `Ivanti Connect Secure`

> **Why LinkedIn is not automated here.** LinkedIn dropped public RSS years ago, and its
> Marketing/Community APIs only return posts for pages *you administer* (or via a Partner
> Program). Scraping it breaks the User Agreement and will get the account restricted. So:
> follow these pages personally, and let the pipeline ingest the same organizations through
> their RSS/advisory feeds, which are faster and more complete anyway. If you later want
> LinkedIn output, the supported direction is the reverse — **posting** your published digest
> to a LinkedIn page you own via the Community Management API.
