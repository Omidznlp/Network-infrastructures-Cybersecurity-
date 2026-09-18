---
layout: default
title: Network Infrastructure Cybersecurity
---

# Network device security digests

Daily intelligence on vulnerabilities and attacks affecting **firewalls, VPN gateways, routers,
switches, wireless controllers, load balancers and SD-WAN edge** — with the upgrade and hardening
actions to take, for current *and* legacy systems. Unrelated security news is filtered out.

**[📡 Subscribe by RSS]({{ '/feed.xml' | relative_url }})** ·
**[🏢 Browse by vendor]({{ '/browse/' | relative_url }})** ·
**[🧠 AI & network devices]({{ '/browse/ai/' | relative_url }})**

{% assign L = site.data.latest %}
{% if L %}
---

## 📋 Latest edition — {{ L.date }}

**{{ L.item_count }} items · {{ L.critical_count }} critical{% if L.kev.size > 0 %} · KEV: {{ L.kev | join: ", " }}{% endif %}**

### {{ L.top_story_title }}

{{ L.top_story_summary }}

{% if L.top_actions.size > 0 %}
**Do this first**

{% for a in L.top_actions %}- {{ a }}
{% endfor %}{% endif %}

{% if L.executive_summary.size > 0 %}
**In summary**

{% for s in L.executive_summary %}- {{ s }}
{% endfor %}{% endif %}

{% if L.key_actions.size > 0 %}
### 🛠️ Solutions this edition

{% for a in L.key_actions %}- {{ a }}
{% endfor %}{% endif %}

{% if L.headlines.size > 0 %}
### Today's items

{% for h in L.headlines %}- **{{ h.relevance | upcase }}** — [{{ h.title }}]({{ h.link }}){% if h.summary %}  
  <small>{{ h.summary }}</small>{% endif %}
{% endfor %}

**[Read the full edition →]({{ L.url | relative_url }})**
{% endif %}
{% endif %}

---

## Browse

**[By vendor and device type]({{ '/browse/' | relative_url }})** — pick a vendor (Cisco, Fortinet,
Palo Alto, Check Point…) and drill into firewalls, VPN gateways, routers or switches.

**[By week, month and year]({{ '/browse/archive/' | relative_url }})** — everything published in a
given period, grouped by vendor.

**[AI & network devices]({{ '/browse/ai/' | relative_url }})** — AI-assisted attacks, AI on network
gear, prompt injection against network management.

---

## All editions

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

*Automated, reviewed before publication. Always verify version numbers against the vendor advisory
before scheduling a change.*
