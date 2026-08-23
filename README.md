# .github

Organization-level defaults for [**henryj-dev**](https://github.com/henryj-dev).

| Path | What it does |
|---|---|
| [`profile/README.md`](profile/README.md) | Renders as the organization's public profile page at [github.com/henryj-dev](https://github.com/henryj-dev) |
| `profile/assets/` | Banner artwork for the profile, in light and dark variants |

## Editing the profile page

`profile/README.md` is the org landing page. It goes live the moment it lands on
the default branch — there is no build step. Notes for editing it:

- **Images must be absolute URLs.** Relative paths break, because the file is
  rendered outside this repository. Use
  `https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/...`.
- **Light and dark** are handled by a `<picture>` element with
  `prefers-color-scheme` sources. Update both SVGs together.
- **Markdown inside block HTML does not render** on GitHub. Inside `<table>`,
  write plain HTML.
- Mermaid code fences render natively and follow the reader's GitHub theme.

## Other things this repository can hold

GitHub also picks up org-wide community health files from here, and any
repository without its own copy falls back to them: `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, plus
`.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`.
