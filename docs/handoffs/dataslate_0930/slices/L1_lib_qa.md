PASS

# L1 — Librarian QA

- New source frontmatter contains `title`, `type`, `system`, `created`, `updated`, `version`, `sources`, `confidence`, and `tags`; `confidence` is `draft`.
- Index rows agree with their pages: Necron 1000 V1 is 935 on MFM v1.5; Cryptek Conclave remains 2DP and its active 1000 list is 935; Space Marines were reviewed and the 1000 list was not recosted.
- Bidirectional links exist between `[[mfm_v1_5_2026_09_30]]` and each of `[[necrons]]`, `[[cryptek_conclave]]`, and `[[space_marines]]`.
- Updates are teaching paraphrase and points/list commentary only; no datasheet stat block was added.
- Working-tree inspection shows no `raw/` path changed. The latest commit remains `bf66c076031b71368e814b902d8694d36b8b1865` from 2026-09-25, so the L1 work was not committed or pushed.
