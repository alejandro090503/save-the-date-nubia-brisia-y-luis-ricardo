import io, re, sys
P='index.html'; s=io.open(P,encoding='utf-8').read()
def rep(o,n,c=1):
    global s
    if s.count(o)!=c: sys.exit('ERR %d %r'%(s.count(o),o[:70]))
    s=s.replace(o,n)
def drop(i):
    global s
    a=s.find('<section id="%s"'%i); assert a>0,i
    b=s.find('</section>',a)+10
    # secciones con <section> anidado no hay; dresscode/sobres/hosp son planas
    s=s[:a]+s[b:]
for i in ['location','itinerary','sobres','album','dresscode','hospedaje','family','padrinos','gallery','weather','faq','rsvp']:
    drop(i)
U='https://save-the-date-nubia-brisia-y-luis-ricardo.vercel.app'
rep('https://boda-nubia-brisia-y-luis-ricardo.vercel.app/og-image.jpg', U+'/og-image.jpg')
rep('<title>Nubia Brisia &amp; Luis Ricardo · 05 · VI · 2027</title>','<title>Save the Date · Nubia Brisia &amp; Luis Ricardo · 05 · VI · 2027</title>')
rep('content="Boda Nubia Brisia & Luis Ricardo · 5 jun 2027"','content="Save the Date · Nubia Brisia & Luis Ricardo · 5 jun 2027"')
rep('content="Nos casamos — Ciudad de México · 5 de junio de 2027"','content="Guarda la fecha — Ciudad de México · 5 de junio de 2027 · Invitación formal próximamente"')
rep('<p class="h-we" id="hWe">Nos casamos</p>','<p class="h-we" id="hWe">Save the Date</p>')
rep('<p class="sub rvc" style="margin-top:8px">los invitamos a<br>nuestra boda</p>','<p class="sub rvc" style="margin-top:8px">nos casamos y queremos<br>que guardes la fecha</p>')
# bloque "próximamente" después del calendario
a=s.find('<section id="calendar"'); b=s.find('</section>',a)+10
s=s[:b]+'''

<!-- PRÓXIMAMENTE -->
<section id="pronto" class="has-ink" style="text-align:center">
  <div class="ink-bg oval" aria-hidden="true"><i style="background-image:url('ink/ink-oval.webp')"></i></div>
  <span class="lbl">Muy pronto</span>
  <h2 class="ttl">Invitación Formal</h2>
  <div class="gline"></div>
  <p class="pronto-txt">Ceremonia religiosa en el Templo de la Ciudad de México y recepción en Ciudad de México.</p>
  <p class="pronto-big">Invitación formal próximamente</p>
  <p class="pronto-txt">Te enviaremos todos los detalles: lugares, itinerario y confirmación de asistencia.</p>
</section>
'''+s[b:]
rep('  </style>','''#pronto{padding-bottom:clamp(70px,18vw,110px)}
.pronto-txt{font-family:'Jost',sans-serif;font-weight:500;font-size:17px;line-height:1.6;color:rgba(247,231,206,.92);max-width:330px;margin:20px auto 0}
.pronto-big{font-family:'Cinzel',serif;font-weight:600;font-size:clamp(17px,4.8vw,20px);letter-spacing:.14em;text-transform:uppercase;color:#F1DC8A;margin:30px auto 0;max-width:330px;line-height:1.5}
.nav-btn,#nav-panel{display:none!important}
  </style>''')
# JS que apunta a secciones quitadas: protegido con guardas en los init; quitar lifeLayer de padrinos ya no existe
io.open(P,'w',encoding='utf-8',newline='\n').write(s); print('ok', len(s))
