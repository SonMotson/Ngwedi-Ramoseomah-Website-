#!/usr/bin/env python3
"""Fetch public GDELT article metadata for discovery. No page HTML is executed or embedded."""
import json, urllib.parse, urllib.request, datetime, re, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/"data"/"affairs.json"
QUERIES=[
 ("africa",'(Botswana OR SADC OR AfCFTA OR "Southern Africa") (trade OR economy OR investment OR tariff)'),
 ("trade",'(global trade OR WTO OR UNCTAD OR tariffs OR shipping OR commodities)'),
 ("geopolitics",'(geopolitics OR elections OR sanctions OR conflict OR diplomacy)')]
def get_json(url):
 req=urllib.request.Request(url,headers={"User-Agent":"HouseOfNgwediResearchBot/1.0 (+https://github.com/SonMotson/Ngwedi-Ramoseomah-Website-)"})
 with urllib.request.urlopen(req,timeout=25) as response:
  if response.status!=200: raise RuntimeError("feed request failed")
  return json.loads(response.read().decode("utf-8"))
def safe_item(raw,topic):
 url=raw.get("url","")
 if not url.startswith("https://"): return None
 title=re.sub(r"\s+"," ",raw.get("title","")).strip()
 if not title or len(title)>300: return None
 domain=raw.get("domain") or urllib.parse.urlparse(url).netloc
 date=raw.get("seendate","")
 published=None
 if re.fullmatch(r"\d{14}",date):
  try: published=datetime.datetime.strptime(date,"%Y%m%d%H%M%S").replace(tzinfo=datetime.timezone.utc).isoformat()
  except ValueError: pass
 return {"topic":topic,"source":domain,"published":published,"title":title,"summary":"Automated discovery result. Open the publisher's original report and corroborate important claims with primary sources.","url":url}
def main():
 merged={}
 errors=[]
 for topic,query in QUERIES:
  params=urllib.parse.urlencode({"query":query,"mode":"ArtList","format":"json","maxrecords":"30","sort":"DateDesc"})
  try:
   payload=get_json("https://api.gdeltproject.org/api/v2/doc/doc?"+params)
   for raw in payload.get("articles",[]):
    item=safe_item(raw,topic)
    if item: merged[item["url"]]=item
  except Exception as exc:
   errors.append(topic+": "+str(exc))
 old={}
 if OUT.exists():
  try: old=json.loads(OUT.read_text(encoding="utf-8"))
  except Exception: old={}
 curated=[x for x in old.get("items",[]) if x.get("source","").split(" ")[0] in {"UNCTAD","WTO","SADC","Bank","Reuters","World"}]
 # Prefer latest discovery metadata, retain curated institutional leads.
 combined={x["url"]:x for x in curated}
 combined.update(merged)
 items=sorted(combined.values(),key=lambda x:x.get("published") or "",reverse=True)[:90]
 result={"updated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"mode":"scheduled-public-source-discovery","items":items,"collection_notes":errors}
 OUT.parent.mkdir(parents=True,exist_ok=True)
 OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print("Wrote",len(items),"items; feed warnings:",len(errors))
if __name__=="__main__": main()
