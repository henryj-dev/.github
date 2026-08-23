# .github

Organization-level defaults for [**henryj-dev**](https://github.com/henryj-dev).

| Path | What it does |
|---|---|
| [`profile/README.md`](profile/README.md) | Renders as the organization's public profile page at [github.com/henryj-dev](https://github.com/henryj-dev) |
| [`profile/README.ko.md`](profile/README.ko.md) | Korean translation of the profile page |
| `profile/assets/` | Generated banner artwork — do not hand-edit |
| [`scripts/build-banners.py`](scripts/build-banners.py) | Renders every banner from one template |

## The profile page is deliberately generic

It describes how things here are built, not what each project does in detail.
That is on purpose: per-project feature lists and architecture diagrams go stale
the moment a repository is added or changes shape, and the profile page is the
worst place to find that out. Each repository's own README is the source of truth
for its scope and status.

The practical rule: if a sentence on the profile page would need editing because
a new repository showed up, it does not belong there.

## Adding a repository

Append one row to the `Projects` table in **both** `profile/README.md` and
`profile/README.ko.md` — name, one line, nothing more. That is the only routine
edit this repository needs.

You can skip even that. GitHub shows an organization's **pinned repositories**
underneath the profile README, so pinning from the organization's landing page
gets new work in front of visitors with no commit at all. The table is here
because it lets you say a sentence about each project in the reader's language;
if that stops being worth the upkeep, delete it and lean on pinning.

## Editing the profile page

`profile/README.md` goes live the moment it lands on the default branch — there
is no build step. Things that will bite you:

- **Images must be absolute URLs.** Relative paths break, because the file is
  rendered outside this repository. Use
  `https://raw.githubusercontent.com/henryj-dev/.github/main/profile/assets/...`.
  The same applies to the language toggle links.
- **Markdown inside block HTML does not render** on GitHub. Inside `<table>`,
  write plain HTML.
- **Light and dark** are handled by a `<picture>` element with
  `prefers-color-scheme` sources.
- Mermaid code fences render natively and follow the reader's GitHub theme.

## Banners

Wording and palette live in `scripts/build-banners.py`. Edit it and run:

```sh
python3 scripts/build-banners.py
```

That rewrites all four SVGs — two languages by two themes. Editing the SVGs
directly means the next run silently discards your change.

The Korean banner needs CJK glyphs, so the font stack names Korean faces ahead of
the Latin ones. It falls back cleanly on systems with no Korean font installed.

## Translations

GitHub has no locale negotiation for READMEs. It renders `profile/README.md` as
the profile page and nothing else, so a translation cannot be served
automatically — the two files link to each other by a toggle near the top of
each, and readers switch by hand. English is what visitors land on; Korean is
reached at its file URL.

Keep them in sync. A change to one is only half done until the other matches.

## Other things this repository can hold

GitHub also picks up org-wide community health files from here, and any
repository without its own copy falls back to them: `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md`, `SECURITY.md`, `SUPPORT.md`, plus
`.github/ISSUE_TEMPLATE/` and `.github/PULL_REQUEST_TEMPLATE.md`.
