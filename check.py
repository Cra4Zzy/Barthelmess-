from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json
ROOT=Path(__file__).resolve().parent
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.tags=[]
 def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
errors=[];pages=list(ROOT.glob('**/*.html'))
for file in pages:
 parser=Parser();parser.feed(file.read_text())
 if sum(t=='h1' for t,a in parser.tags)!=1:errors.append(str(file)+': expected one H1')
 for tag,attrs in parser.tags:
  if tag=='img' and not attrs.get('alt'):errors.append(str(file)+': missing image description')
  for attr in ('href','src','data-enlarge'):
   value=attrs.get(attr,'');url=urlsplit(value)
   if not value or url.scheme or url.netloc or not url.path:continue
   target=((ROOT/url.path.lstrip('/')) if url.path.startswith('/') else (file.parent/unquote(url.path))).resolve()
   if target.is_dir():target=target/'index.html'
   if not target.exists():errors.append(str(file.relative_to(ROOT))+': missing '+value)
for image in (ROOT/'assets').glob('*.webp'):
 data=image.read_bytes()
 if data[:4]!=b'RIFF' or data[8:12]!=b'WEBP':errors.append(str(image)+': invalid WebP header')
catalog=json.loads((ROOT/'assets/catalog.json').read_text())
for item in catalog:
 if not (ROOT/'maschinen'/item['id']/'index.html').exists():errors.append('Missing detail for '+item['id'])
 if not (ROOT/'assets'/(item['image']+'.webp')).exists():errors.append('Missing image for '+item['id'])
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages, relative paths, image descriptions and {len(catalog)} complete catalog entries')
