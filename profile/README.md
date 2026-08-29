<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-light.svg">
  <img alt="henryj-dev — describe it once, apply it safely, roll it back" src="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-light.svg" width="100%">
</picture>

<br>

**Tools for running systems, built so the risky change is the hard one to make by accident.**

<a href="https://github.com/orgs/henryj-dev/repositories"><img alt="Repositories" src="https://img.shields.io/badge/repositories-browse-0969da?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.typescriptlang.org/"><img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178c6?style=flat-square&logo=typescript&logoColor=white"></a>
<img alt="License Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-8250df?style=flat-square">
<a href="#getting-involved"><img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-2da44e?style=flat-square"></a>

<br><br>

<b>English</b> · <a href="https://github.com/henryj-dev/.github/blob/main/profile/README.ko.md">한국어</a>

</div>

---

Most of what we work on starts the same way: something important is configured by
hand, on a box, and the only record of why it looks like that is the person who
did it. These projects turn that into something you can read, review, and undo.

Whatever the subject, they take the same shape — you declare the state you want,
the tool shows you what will change, and it applies that change in a way you can
back out of.

## How things here are built

| | |
|---|---|
| **Desired state, not commands** | You declare what should be true. Reconciliation is the tool's job, and it only ever touches what it manages. |
| **Plan before apply** | Every change is previewable. You see the impact before anything moves. |
| **Safe by construction** | Rollback timers, commit/confirm, verification after the change lands. The move that breaks things is hard to make by accident. |
| **Equal-power surfaces** | GUI, API, and CLI are the same product. Nothing is only clickable, nothing is only scriptable. |
| **Light on dependencies** | Few moving parts, boring stacks, and no runtime you have to adopt to get value. |
| **Open by default** | Apache-2.0, public issue trackers, and READMEs that admit what is not finished yet. |

## Projects

<table>
<tr><td width="290">

**[parallax](https://github.com/henryj-dev/parallax)**

[![build](https://github.com/henryj-dev/parallax/actions/workflows/check.yml/badge.svg)](https://github.com/henryj-dev/parallax/actions/workflows/check.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/parallax?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/parallax?style=flat-square&color=8250df&label=)

</td><td>

Split-horizon DNS control plane — one desired state for internal DNS and Cloudflare

</td></tr>
<tr><td>

**[barycenter](https://github.com/henryj-dev/barycenter)**

[![build](https://github.com/henryj-dev/barycenter/actions/workflows/verify.yml/badge.svg)](https://github.com/henryj-dev/barycenter/actions/workflows/verify.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/barycenter?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/barycenter?style=flat-square&color=8250df&label=)

</td><td>

A control plane for nginx — HTTP, TCP, and UDP reverse proxying and load balancing

</td></tr>
<tr><td>

**[heliopause](https://github.com/henryj-dev/heliopause)**

[![build](https://github.com/henryj-dev/heliopause/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/heliopause/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/heliopause?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/heliopause?style=flat-square&color=8250df&label=)

</td><td>

A host firewall you can't lock yourself out of — declarative nftables with auto-rollback

</td></tr>
<tr><td>

**[lodestar](https://github.com/henryj-dev/lodestar)**

[![build](https://github.com/henryj-dev/lodestar/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/lodestar/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/lodestar?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/lodestar?style=flat-square&color=8250df&label=)

</td><td>

An open-source identity provider on Cloudflare Workers — OIDC, SAML 2.0, WebAuthn/Passkey, TOTP, LDAP

</td></tr>
<tr><td>

**[ionosphere](https://github.com/henryj-dev/ionosphere)**

[![build](https://github.com/henryj-dev/ionosphere/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/ionosphere/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/ionosphere?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/ionosphere?style=flat-square&color=8250df&label=)

</td><td>

A mail server built from scratch — SMTP, IMAP, POP3, JMAP, ManageSieve, LMTP, zero runtime dependencies

</td></tr>
</table>

More are on their way here. Each repository's own README is the source of truth
for what it does and how finished it is.

**[→ Browse all repositories](https://github.com/orgs/henryj-dev/repositories)**

## Also here

Smaller, standalone tools that don't need a control plane of their own:

<table>
<tr><td width="290">

**[d1-jdbc](https://github.com/henryj-dev/d1-jdbc)**

[![build](https://github.com/henryj-dev/d1-jdbc/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/d1-jdbc/actions/workflows/ci.yml)
![Java](https://img.shields.io/github/languages/top/henryj-dev/d1-jdbc?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/d1-jdbc?style=flat-square&color=8250df&label=)

</td><td>

A JDBC driver for Cloudflare D1 — zero-dependency, REST API or self-deployed Worker proxy

</td></tr>
<tr><td>

**[whois2rdap](https://github.com/henryj-dev/whois2rdap)**

[![build](https://github.com/henryj-dev/whois2rdap/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/whois2rdap/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/whois2rdap?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/whois2rdap?style=flat-square&color=8250df&label=)

</td><td>

Converts WHOIS responses into RFC 9083 RDAP-shaped JSON

</td></tr>
</table>

## Upstream contributions

Merged work in other people's projects, kept here as forks:

| | |
|---|---|
| [cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk) | [![merged](https://img.shields.io/badge/PR-merged-2da44e?style=flat-square)](https://github.com/cloudflare/workers-sdk/pull/14712) miniflare: local dev support for remote VPC Network bindings |
| [soulduse/ai-token-monitor](https://github.com/soulduse/ai-token-monitor) | [![merged](https://img.shields.io/badge/6_PRs-merged-2da44e?style=flat-square)](https://github.com/henryj-dev/contribute_soulduse_ai-token-monitor) Kiro provider, credit-based usage tracking, Grok 4.6 pricing, and more |
| [AnimMouse/wgcf-connector](https://github.com/AnimMouse/wgcf-connector) | [![merged](https://img.shields.io/badge/PR-merged-2da44e?style=flat-square)](https://github.com/henryj-dev/contribute_AnimMouse_wgcf-connector) Default IPv4 address prefix fix |
| [dbmail/dbmail](https://github.com/dbmail/dbmail) | [![merged](https://img.shields.io/badge/PR-merged-2da44e?style=flat-square)](https://github.com/henryj-dev/contribute_dbmail_dbmail) RPM spec file updates |

## Getting involved

Issues and pull requests are welcome on any repository. If you are running one of
these in anger and something is missing, an issue describing your setup is more
useful than a feature request in the abstract.

<div align="center">
<sub>Apache-2.0 licensed · <a href="https://github.com/orgs/henryj-dev/repositories">all repositories</a></sub>
</div>
