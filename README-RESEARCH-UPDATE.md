# Research Library and Global Affairs Update

Added:
- `library.html`: contextual guide to Gilgamesh, Adamic writings, 1/2/3 Enoch, the Book of Giants, Mesopotamian literature, Second Temple writings, Nag Hammadi texts and African manuscript traditions.
- `affairs.html`: global affairs and trade briefing page.
- `data/affairs.json`: curated initial source-linked briefing.
- `scripts/update_affairs.py`: safe metadata-only public article discovery from GDELT. It stores title, source, date and canonical HTTPS URL; it does not execute or embed publisher HTML.
- `.github/workflows/refresh-affairs.yml`: scheduled refresh every six hours and manual dispatch.
- `RESEARCH-EDITORIAL-POLICY.md`: editorial standards and correction principles.

The term "elluminash" is recorded as unverified because no recognized ancient text or scholarly term could be identified under that spelling. The site invites the original spelling/source rather than inventing an attribution.

Automation status: the workflow is committed but its first run and subsequent GitHub Actions execution have not yet been observed. GitHub Actions must be enabled in repository settings. The page displays the last committed dataset; the browser does not scrape third-party sites directly.
