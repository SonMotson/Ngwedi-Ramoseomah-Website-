#!/usr/bin/env python3
"""Static-site integrity checks. No network requests or third-party dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, sys, xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; ERRORS=[]
class Scan(HTMLParser):
 def __init__(self): super().__init__(); self.ids=set(); self.dupes=[]; self.refs=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if a.get("id"):
   if a["id"] in self.ids:self.dupes.append(a["id"])
   self.ids.add(a["id"])
  for k in ("href","src"):
   if a.get(k):self.refs.append((k,a[k]))
def fail(s):ERRORS.append(s)
pages=sorted(ROOT.glob("*.html")); scans={}
for p in pages:
 try:
  x=Scan();x.feed(p.read_text(encoding="utf-8"));scans[p.name]=x
  for d in x.dupes:fail(f"{p.name}: duplicate id {d}")
 except Exception as e:fail(f"{p.name}: parse error {e}")
for name,x in scans.items():
 for kind,ref in x.refs:
  if ref.startswith(("https://","http://","mailto:","tel:","data:","javascript:")):continue
  if ref.startswith("#"):
   if unquote(ref[1:]) not in x.ids:fail(f"{name}: missing fragment {ref}")
   continue
  u=urlsplit(ref); target=(ROOT/unquote(u.path)).resolve() if u.path else ROOT/name
  if not str(target).startswith(str(ROOT.resolve())):fail(f"{name}: path escapes root {ref}");continue
  if u.path and not target.exists():fail(f"{name}: missing local {kind} {ref}")
  if u.fragment and target.name in scans and unquote(u.fragment) not in scans[target.name].ids:fail(f"{name}: missing target {ref}")
for p in (ROOT/"data").glob("*.json"):
 try:json.loads(p.read_text(encoding="utf-8"))
 except Exception as e:fail(f"{p.relative_to(ROOT)}: invalid JSON {e}")
try:
 tree=ET.parse(ROOT/"sitemap.xml"); locs=[e.text or "" for e in tree.findall(".//{*}loc")]
 if not locs:fail("sitemap.xml: no locations")
 for loc in locs:
  if "example.invalid" in loc or "github.io/Ngwedi-Ramoseomah-Website-" not in loc:fail(f"sitemap.xml: unexpected location {loc}")
except Exception as e:fail(f"sitemap.xml: invalid XML {e}")
for p in pages:
 if "example.invalid" in p.read_text(encoding="utf-8"):fail(f"{p.name}: placeholder domain remains")
if ERRORS:print("\n".join("FAIL: "+e for e in ERRORS));sys.exit(1)
print(f"PASS: {len(pages)} HTML pages, local references, fragments, JSON and sitemap checked.")
