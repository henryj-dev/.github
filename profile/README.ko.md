<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-ko-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-ko-light.svg">
  <img alt="henryj-dev — 한 번 기술하고, 안전하게 적용하고, 되돌립니다" src="https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/banner-ko-light.svg" width="100%">
</picture>

<br>

**시스템을 운영하는 도구를 만듭니다. 위험한 변경일수록 실수로 만들기 어렵도록.**

<a href="https://github.com/orgs/henryj-dev/repositories"><img alt="Repositories" src="https://img.shields.io/badge/repositories-browse-0969da?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.typescriptlang.org/"><img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-3178c6?style=flat-square&logo=typescript&logoColor=white"></a>
<img alt="License Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-8250df?style=flat-square">
<a href="#참여하기"><img alt="PRs Welcome" src="https://img.shields.io/badge/PR-환영-2da44e?style=flat-square"></a>

<br>

<sub>
<a href="#여기서-만드는-방식">철학</a> ·
<a href="#소개">소개</a> ·
<a href="#프로젝트">프로젝트</a> ·
<a href="#그-외-도구">그 외 도구</a> ·
<a href="#오픈소스-기여">기여</a> ·
<a href="#참여하기">참여하기</a>
</sub>

<br><br>

<a href="https://github.com/henryj-dev">English</a> · <b>한국어</b>

</div>

---

> 여기서 다루는 일은 대개 비슷하게 시작합니다. 중요한 무언가가 서버 어딘가에서 손으로 설정되어 있고, 왜 그렇게 되어 있는지는 그 작업을 한 사람만 알고 있는 상태. 이 프로젝트들은 그것을 읽고, 검토하고, 되돌릴 수 있는 형태로 바꿉니다.
>
> 주제가 무엇이든 같은 형태를 따릅니다. 원하는 상태를 선언하면, 도구가 무엇이 바뀔지 먼저 보여주고, 물러설 수 있는 방식으로 적용합니다.

## 소개

<table>
<tr>
<td width="88" align="center"><img src="https://avatars.githubusercontent.com/u/9063075?v=4" width="72" height="72" alt="mack-erel"></td>
<td>

**장효찬 (Henry Jang)** · [@mack-erel](https://github.com/mack-erel)

백엔드 / 인프라 엔지니어. 이 조직은 위 도구들이 README, 라이선스, 빌드 배지까지
갖춰졌을 때 올라오는 자리입니다. 자잘한 스크립트나 그날그날의 실험은 개인
계정에 남아있다가, 그중 하나가 여기 올 만큼 다듬어지면 옮겨옵니다.

[![Email](https://img.shields.io/badge/email-jang%40hyochan.site-24292f?style=flat-square&logo=gmail&logoColor=white)](mailto:jang@hyochan.site)
[![Blog](https://img.shields.io/badge/blog-hyochan.site-8250df?style=flat-square&logo=rss&logoColor=white)](https://hyochan.site)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-yrneh--jang-0a66c2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yrneh-jang/)
[![GitHub](https://img.shields.io/badge/personal-@mack--erel-0969da?style=flat-square&logo=github&logoColor=white)](https://github.com/mack-erel?tab=repositories)

</td>
</tr>
</table>

## 여기서 만드는 방식

| 원칙 | 의미 |
|---|---|
| **명령이 아닌 desired state** | 무엇이 참이어야 하는지를 선언합니다. 조정은 도구의 몫이며, 자신이 관리하는 대상 외에는 건드리지 않습니다. |
| **적용 전 계획** | 모든 변경은 미리 볼 수 있습니다. 무언가 움직이기 전에 영향 범위를 확인합니다. |
| **구조적으로 안전하게** | 롤백 타이머, commit/confirm, 적용 후 검증. 사고를 내는 변경을 실수로 만들기 어렵게 설계합니다. |
| **동등한 인터페이스** | GUI, API, CLI가 같은 제품입니다. 클릭으로만 되는 것도, 스크립트로만 되는 것도 없습니다. |
| **가벼운 의존성** | 움직이는 부품을 줄이고, 익숙한 스택을 쓰며, 도입해야만 쓸 수 있는 런타임을 만들지 않습니다. |
| **기본은 공개** | Apache-2.0, 공개 이슈 트래커, 그리고 아직 끝나지 않은 부분을 숨기지 않는 README. |

## 프로젝트

<table>
<tr><td width="290">

**[parallax](https://github.com/henryj-dev/parallax)**  
[![build](https://github.com/henryj-dev/parallax/actions/workflows/check.yml/badge.svg)](https://github.com/henryj-dev/parallax/actions/workflows/check.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/parallax?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/parallax?style=flat-square&color=8250df&label=)

</td><td>

스플릿 호라이즌 DNS 컨트롤 플레인 — 내부 DNS와 Cloudflare를 하나의 desired state로

</td></tr>
<tr><td>

**[barycenter](https://github.com/henryj-dev/barycenter)**  
[![build](https://github.com/henryj-dev/barycenter/actions/workflows/verify.yml/badge.svg)](https://github.com/henryj-dev/barycenter/actions/workflows/verify.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/barycenter?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/barycenter?style=flat-square&color=8250df&label=)

</td><td>

nginx를 위한 컨트롤 플레인 — HTTP, TCP, UDP 리버스 프록시와 로드 밸런싱

</td></tr>
<tr><td>

**[heliopause](https://github.com/henryj-dev/heliopause)**  
[![build](https://github.com/henryj-dev/heliopause/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/heliopause/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/heliopause?style=flat-square&color=0969da&label=)
![Apache-2.0](https://img.shields.io/github/license/henryj-dev/heliopause?style=flat-square&color=8250df&label=)

</td><td>

스스로를 잠가버릴 수 없는 호스트 방화벽 — 자동 롤백을 갖춘 선언형 nftables

</td></tr>
<tr><td>

**[lodestar](https://github.com/henryj-dev/lodestar)**  
[![build](https://github.com/henryj-dev/lodestar/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/lodestar/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/lodestar?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/lodestar?style=flat-square&color=8250df&label=)

</td><td>

오픈소스 아이덴티티 프로바이더 — 하나의 SvelteKit 앱으로 Cloudflare Workers와 Node에 모두 배포 가능; OIDC, SAML 2.0, WebAuthn/Passkey, TOTP, LDAP

</td></tr>
<tr><td>

**[ionosphere](https://github.com/henryj-dev/ionosphere)**  
[![build](https://github.com/henryj-dev/ionosphere/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/ionosphere/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/ionosphere?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/ionosphere?style=flat-square&color=8250df&label=)

</td><td>

처음부터 직접 만든 메일 서버 — SMTP·IMAP·POP3·JMAP·ManageSieve·LMTP, 런타임 의존성 0

</td></tr>
</table>

앞으로 더 추가될 예정입니다. 각 프로젝트가 무엇을 하고 어느 단계인지는 해당 저장소의 README가 기준입니다.

**[→ 전체 저장소 보기](https://github.com/orgs/henryj-dev/repositories)**

## 그 외 도구

컨트롤 플레인까지는 필요 없는 작은 독립 도구들:

<table>
<tr><td width="290">

**[d1-jdbc](https://github.com/henryj-dev/d1-jdbc)**  
[![build](https://github.com/henryj-dev/d1-jdbc/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/d1-jdbc/actions/workflows/ci.yml)
![Java](https://img.shields.io/github/languages/top/henryj-dev/d1-jdbc?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/d1-jdbc?style=flat-square&color=8250df&label=)

</td><td>

Cloudflare D1용 JDBC 드라이버 — 의존성 0, REST API 또는 자체 배포 Worker 프록시

</td></tr>
<tr><td>

**[whois2rdap](https://github.com/henryj-dev/whois2rdap)**  
[![build](https://github.com/henryj-dev/whois2rdap/actions/workflows/ci.yml/badge.svg)](https://github.com/henryj-dev/whois2rdap/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/github/languages/top/henryj-dev/whois2rdap?style=flat-square&color=0969da&label=)
![MIT](https://img.shields.io/github/license/henryj-dev/whois2rdap?style=flat-square&color=8250df&label=)

</td><td>

WHOIS 응답을 RFC 9083 RDAP 형식 JSON으로 변환

</td></tr>
</table>

## 오픈소스 기여

다른 프로젝트에 남긴 작업, fork 형태로 남겨둠 (별도 표시 없으면 머지됨):

<table>
<tr><th width="230">저장소</th><th>PR</th></tr>
<tr><td>

**[cloudflare/workers-sdk](https://github.com/cloudflare/workers-sdk)**  
[![fork](https://img.shields.io/badge/fork-here-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/mack-erel/workers-sdk)

</td><td>

- [#14712](https://github.com/cloudflare/workers-sdk/pull/14712): miniflare — 원격 VPC Network 바인딩에서 로컬 개발 시 `connect()` 지원
- [#14900](https://github.com/cloudflare/workers-sdk/pull/14900): miniflare — 원격 Hyperdrive 바인딩 로컬 개발 지원 *(진행 중)*

</td></tr>
<tr><td>

**[soulduse/ai-token-monitor](https://github.com/soulduse/ai-token-monitor)**  
[![fork](https://img.shields.io/badge/fork-here-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/henryj-dev/contribute_soulduse_ai-token-monitor)

</td><td>

- [#189](https://github.com/soulduse/ai-token-monitor/pull/189): Grok 4.6 가격, SuperGrok 크레딧, Linux/Windows 지원
- [#181](https://github.com/soulduse/ai-token-monitor/pull/181): 게이트웨이가 재작성한 모델 ID의 가격·집계를 올바르게 처리
- [#180](https://github.com/soulduse/ai-token-monitor/pull/180): 크레딧 기반 사용량 추적을 갖춘 Kiro provider 추가
- [#179](https://github.com/soulduse/ai-token-monitor/pull/179): kiro-cli를 셸아웃하는 대신 Kiro API 직접 호출
- [#154](https://github.com/soulduse/ai-token-monitor/pull/154): OAuth 사용량 응답의 null `resets_at` 허용 처리
- [#143](https://github.com/soulduse/ai-token-monitor/pull/143): Kiro CLI를 API 키 기반 번역 프로바이더로 추가

</td></tr>
<tr><td>

**[AnimMouse/wgcf-connector](https://github.com/AnimMouse/wgcf-connector)**  
[![fork](https://img.shields.io/badge/fork-here-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/henryj-dev/contribute_AnimMouse_wgcf-connector)

</td><td>

- [#10](https://github.com/AnimMouse/wgcf-connector/pull/10): 기본 IPv4 주소 프리픽스 `/12` → `/32` 변경 (라우팅은 `AllowedIPs`에 위임)

</td></tr>
<tr><td>

**[dbmail/dbmail](https://github.com/dbmail/dbmail)**  
[![fork](https://img.shields.io/badge/fork-here-24292f?style=flat-square&logo=github&logoColor=white)](https://github.com/henryj-dev/contribute_dbmail_dbmail)

</td><td>

- [#348](https://github.com/dbmail/dbmail/pull/348): dbmail·libsieve·libzdb용 RPM spec 파일 업데이트

</td></tr>
</table>

<div align="center">
<sub>· · ·</sub>
</div>

## 참여하기

모든 저장소에서 이슈와 풀 리퀘스트를 환영합니다. 실제 운영 중에 부족한 점을 발견하셨다면, 추상적인 기능 요청보다 사용 환경을 설명한 이슈가 훨씬 도움이 됩니다.

<div align="center">
<sub>Apache-2.0 라이선스 · <a href="https://github.com/orgs/henryj-dev/repositories">전체 저장소</a></sub>
</div>
