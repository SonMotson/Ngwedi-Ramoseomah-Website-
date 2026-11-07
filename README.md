# House of Ngwedi Ramoseomah I

Independent Botswana-rooted website for consciousness, Ngwao and ancestral knowledge, cosmology, holistic wellbeing, retreats, creative arts and booking enquiries.

## Current build
- `index.html`: responsive public website with all core sections.
- `privacy.html`: early-stage privacy notice.
- `sentinel.html` and `sentinel.js`: Ngwedi Sentinel local browser posture console.
- `booking.js`: local enquiry-file generator. It does not transmit or store personal information.
- `house-of-ngwedi-crest.svg`: lightweight repository emblem.
- `_headers` and `vercel.json`: security response-header configurations for supported static hosts.
- `SECURITY.md`: security design, limitations and production launch checklist.

## Important status
This is a working source build, not a deployed production service. Cloudflare account access is connected, but no domain/zone is currently attached to the account. No WAF rules, server-side API, administrator identity, live security telemetry, database or payment integration is active. Sentinel clearly labels these gaps and must not be treated as a live SOC.

The proposed WOKE three-day off-grid camp for April 2027 is shown as proposed only. Dates, venue, fees and registration are unconfirmed.

## Hosting
Cloudflare Workers with Static Assets is the preferred new-project hosting direction. Vercel configuration is included as an alternative. Connect the repository only after confirming the final domain and hosting account.
