---
layout: default
title: Network Infrastructure Cybersecurity
---

# Network device security digests

Automated daily intelligence on vulnerabilities and attacks affecting **firewalls, VPN
gateways, routers, switches, wireless controllers, load balancers and SD-WAN edge devices** —
with the upgrade and hardening actions to take, for both current and legacy systems.

Every edition leads with **how AI is being used to attack (and defend) network devices**.

Sources: vendor PSIRT advisories, CISA / NCSC, threat-intel research blogs and the security
press, enriched with the **CISA KEV** catalog and **FIRST EPSS** exploit-probability scores.
Full source list: [SOURCES.md](https://github.com/Omidznlp/Network-infrastructures-Cybersecurity-/blob/main/SOURCES.md)

---

## Browse by device type and vendor

Looking for one platform rather than one day? **[Browse the archive]({{ '/browse/' | relative_url }})**
— pick a device class (firewalls, VPN gateways, routers, switches, wireless, load balancers,
SD-WAN) and drill into the vendor, or jump straight to a vendor and see every device class it
appears under.

---

## Editions

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    {% if post.critical_count and post.critical_count > 0 %}
      — <strong>{{ post.critical_count }} critical</strong>
    {% endif %}
    <small>({{ post.item_count }} items{% if post.kev != "none" %}, KEV: {{ post.kev }}{% endif %})</small>
  </li>
{% endfor %}
</ul>

---

*Automated. Always verify version numbers against the vendor advisory before scheduling a change.*
