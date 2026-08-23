# .github

Organization-level defaults for [**henryj-dev**](https://github.com/henryj-dev).

| Path | What it does |
|---|---|
| [`profile/README.md`](profile/README.md) | Renders as the organization's public profile page at [github.com/henryj-dev](https://github.com/henryj-dev) |
| [`profile/README.ko.md`](profile/README.ko.md) | Korean translation of the profile page |
| `profile/assets/` | Banner artwork, in light and dark variants for each language |

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

## Translations

GitHub has no locale negotiation for READMEs. It renders `profile/README.md` as
the profile page and nothing else, so a translation cannot be served
automatically — the two files are linked to each other by a toggle near the top
of each, and readers switch by hand.

That means the English page is the one visitors land on, and the Korean page is
reached at its file URL. Keep them in sync: a change to one is only half done
until the other matches. Each language has its own banner pair
(`banner-*.svg` for English, `banner-ko-*.svg` for Korean), so a wording change
in the tagline means regenerating two SVGs, not one.

The toggle links must be absolute URLs for the same reason images must be.

## Other things this repository can hold

GitHub also picks up org-wide community health files from here, and any
repository without its own copy falls back to them: `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, plus
`.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`.
