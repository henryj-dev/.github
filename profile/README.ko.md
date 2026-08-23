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

<br><br>

<a href="https://github.com/henryj-dev">English</a> · <b>한국어</b>

</div>

---

여기서 다루는 일은 대개 비슷하게 시작합니다. 중요한 무언가가 서버 어딘가에서 손으로 설정되어 있고, 왜 그렇게 되어 있는지는 그 작업을 한 사람만 알고 있는 상태. 이 프로젝트들은 그것을 읽고, 검토하고, 되돌릴 수 있는 형태로 바꿉니다.

주제가 무엇이든 같은 형태를 따릅니다. 원하는 상태를 선언하면, 도구가 무엇이 바뀔지 먼저 보여주고, 물러설 수 있는 방식으로 적용합니다.

## 여기서 만드는 방식

| | |
|---|---|
| **명령이 아닌 desired state** | 무엇이 참이어야 하는지를 선언합니다. 조정은 도구의 몫이며, 자신이 관리하는 대상 외에는 건드리지 않습니다. |
| **적용 전 계획** | 모든 변경은 미리 볼 수 있습니다. 무언가 움직이기 전에 영향 범위를 확인합니다. |
| **구조적으로 안전하게** | 롤백 타이머, commit/confirm, 적용 후 검증. 사고를 내는 변경을 실수로 만들기 어렵게 설계합니다. |
| **동등한 인터페이스** | GUI, API, CLI가 같은 제품입니다. 클릭으로만 되는 것도, 스크립트로만 되는 것도 없습니다. |
| **가벼운 의존성** | 움직이는 부품을 줄이고, 익숙한 스택을 쓰며, 도입해야만 쓸 수 있는 런타임을 만들지 않습니다. |
| **기본은 공개** | Apache-2.0, 공개 이슈 트래커, 그리고 아직 끝나지 않은 부분을 숨기지 않는 README. |

## 프로젝트

| | |
|---|---|
| [**parallax**](https://github.com/henryj-dev/parallax) | 스플릿 호라이즌 DNS 컨트롤 플레인 — 내부 DNS와 Cloudflare를 하나의 desired state로 |
| [**barycenter**](https://github.com/henryj-dev/barycenter) | nginx를 위한 컨트롤 플레인 — HTTP, TCP, UDP 리버스 프록시와 로드 밸런싱 |
| [**heliopause**](https://github.com/henryj-dev/heliopause) | 스스로를 잠가버릴 수 없는 호스트 방화벽 — 자동 롤백을 갖춘 선언형 nftables |

앞으로 더 추가될 예정입니다. 각 프로젝트가 무엇을 하고 어느 단계인지는 해당 저장소의 README가 기준입니다.

**[→ 전체 저장소 보기](https://github.com/orgs/henryj-dev/repositories)**

## 참여하기

모든 저장소에서 이슈와 풀 리퀘스트를 환영합니다. 실제 운영 중에 부족한 점을 발견하셨다면, 추상적인 기능 요청보다 사용 환경을 설명한 이슈가 훨씬 도움이 됩니다.

<div align="center">
<sub>Apache-2.0 라이선스 · <a href="https://github.com/orgs/henryj-dev/repositories">전체 저장소</a></sub>
</div>
