# House of Ngwedi security baseline

## Included
- Cloudflare _headers and Vercel vercel.json security response headers.
- CSP: same-origin executable scripts, no objects, no framing, same-origin forms. Inline styles remain allowed because the site currently embeds CSS.
- HSTS, MIME sniffing protection, referrer policy, restrictive permissions policy and cross-origin isolation headers. Enable HSTS only after the domain and every subdomain are HTTPS-capable.
- Booking enquiry is a local text export only. It does not send or store submissions.
- Ngwedi Sentinel runs browser-side posture checks only. It is not a live SOC, threat feed, penetration test or security certification.

## Before production
1. Connect the final domain to Cloudflare. Enable managed WAF rules and DDoS protection; review rules in log mode before blocking.
2. Add rate limits and Turnstile server-side validation only when a real API/form endpoint is deployed.
3. Require admin MFA, least privilege and private admin access. Do not rely on an unlisted URL or front-end password.
4. Add server-side validation, CSRF controls for cookie auth, secure cookies, audit logging and alert delivery before accepting accounts or bookings.
5. Use hosted payment checkout and verify signed webhooks server-side. Never store card data, CVV, wallet PINs or passwords.
6. Protect main, review code, scan dependencies and secrets, and verify response headers after deployment.

## Limitations
No backend, database, admin identity, payment integration, live threat telemetry or Cloudflare WAF rules are connected yet. Do not present the console as live monitoring until trusted server-side telemetry is integrated.
