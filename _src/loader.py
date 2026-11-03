# STD: loader propio (constelación + monograma), sin sobre que se abre
import io, sys
P = r'C:/Users/aleja/save-the-date-nubia-brisia-y-luis-ricardo/index.html'
s = io.open(P, encoding='utf-8').read()
def rep(o, n):
    global s
    c = s.count(o)
    if c != 1: sys.exit('ERR %d %r' % (c, o[:80]))
    s = s.replace(o, n)

rep('''<div id="envelope-screen" role="button" aria-label="Toca para abrir tu invitación">
  <img id="env-image" src="sobre.jpg" alt="Sobre de la invitación de Nubia Brisia y Luis Ricardo" />
  <video id="env-video" src="https://bsjoelxktbvlavfoozhk.supabase.co/storage/v1/object/public/fotos-clientes/audio/boda-metzli-y-rodolfo/sobre-apertura.mp4" playsinline webkit-playsinline muted preload="auto"></video>
  <p class="envelope-hint" id="env-hint">Toca para abrir</p>
</div>''', '''<div id="envelope-screen" role="button" aria-label="Toca para entrar al Save the Date">
  <img id="env-image" alt="" hidden>
  <video id="env-video" muted playsinline hidden></video>
  <div class="ld-sky" id="ldSky" aria-hidden="true"></div>
  <svg class="ld-const" viewBox="0 0 375 812" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
    <path d="M40 120 L96 168 L150 140 L196 196 M250 96 L300 150 L338 128 M300 150 L286 214" />
    <path d="M30 660 L84 620 L132 676 L188 640 M250 700 L304 664 L346 716 M304 664 L322 604" />
  </svg>
  <div class="ld-center">
    <div class="ld-ring">
      <svg viewBox="0 0 220 220" aria-hidden="true">
        <defs><linearGradient id="ldFoil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9C7A1E"/><stop offset=".35" stop-color="#D4AF37"/><stop offset=".5" stop-color="#FFF4CC"/><stop offset=".65" stop-color="#D4AF37"/><stop offset="1" stop-color="#9C7A1E"/></linearGradient></defs>
        <circle class="ld-c1" cx="110" cy="110" r="100"/>
        <circle class="ld-c2" cx="110" cy="110" r="90"/>
        <g class="ld-orbit"><circle cx="110" cy="10" r="3.2" fill="#FFFBEA"/></g>
      </svg>
      <span class="ld-mono foil-text">B<i>&amp;</i>R</span>
    </div>
    <p class="ld-std">Save the Date</p>
    <p class="ld-date">05 · 06 · 2027</p>
    <span class="ld-btn" id="env-hint">Toca para entrar</span>
  </div>
</div>''')

rep('  </style>', r'''/* ═══ LOADER del Save the Date (constelación + monograma) ═══ */
#envelope-screen{background:radial-gradient(ellipse 90% 60% at 50% 45%,#13224A 0%,#0A1430 62%,#060D22 100%)!important;display:flex;align-items:center;justify-content:center}
.ld-sky{position:absolute;inset:0;pointer-events:none}
.ld-sky i{position:absolute;border-radius:50%;background:#FFF4CC;box-shadow:0 0 6px rgba(241,220,138,.9);animation:ldTw 3s ease-in-out infinite}
@keyframes ldTw{0%,100%{opacity:.25;transform:scale(.7)}50%{opacity:1;transform:scale(1.15)}}
.ld-const{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.ld-const path{fill:none;stroke:rgba(212,175,55,.45);stroke-width:.8;stroke-dasharray:600;stroke-dashoffset:600;animation:ldDraw 3.2s ease-out .4s forwards}
.ld-center{position:relative;z-index:2;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 24px}
.ld-ring{position:relative;width:min(58vw,230px);aspect-ratio:1;display:flex;align-items:center;justify-content:center;opacity:0;animation:ldIn 1.4s cubic-bezier(.22,1,.36,1) .2s forwards}
.ld-ring svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.ld-c1{fill:none;stroke:url(#ldFoil);stroke-width:1.6;stroke-dasharray:630;stroke-dashoffset:630;animation:ldDraw 2.4s ease-out .3s forwards}
.ld-c2{fill:none;stroke:rgba(212,175,55,.4);stroke-width:.7;stroke-dasharray:2 6}
.ld-orbit{transform-origin:110px 110px;animation:ldSpin 9s linear infinite}
.ld-mono{font-family:'Great Vibes',cursive;font-size:min(19vw,76px);line-height:1.25;display:inline-block}
.ld-mono i{font-style:normal;font-size:.6em;margin:0 .08em}
.ld-std{font-family:'Cinzel',serif;font-weight:600;font-size:clamp(14px,4vw,17px);letter-spacing:.42em;text-transform:uppercase;color:#F7E7CE;margin-top:30px;opacity:0;animation:ldUp 1s ease-out 1.1s forwards}
.ld-date{font-family:'Cinzel',serif;font-weight:500;font-size:clamp(15px,4.3vw,18px);letter-spacing:.3em;color:#F1DC8A;margin-top:12px;opacity:0;animation:ldUp 1s ease-out 1.35s forwards}
.ld-btn{margin-top:38px;display:inline-flex;align-items:center;min-height:46px;padding:0 26px;border-radius:999px;border:1px solid rgba(212,175,55,.65);
  font-family:'Jost',sans-serif;font-weight:500;font-size:13px;letter-spacing:.28em;text-transform:uppercase;color:#F7E7CE;background:rgba(19,34,74,.45);
  opacity:0;animation:ldUp 1s ease-out 1.7s forwards,ldBreath 3s ease-in-out 2.7s infinite}
@keyframes ldDraw{to{stroke-dashoffset:0}}
@keyframes ldIn{from{opacity:0;transform:scale(.86)}to{opacity:1;transform:scale(1)}}
@keyframes ldUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes ldSpin{to{transform:rotate(360deg)}}
@keyframes ldBreath{0%,100%{box-shadow:0 0 0 0 rgba(212,175,55,0)}50%{box-shadow:0 0 22px 2px rgba(212,175,55,.35)}}
@media(prefers-reduced-motion:reduce){.ld-sky i,.ld-orbit,.ld-btn{animation:none}.ld-ring,.ld-std,.ld-date,.ld-btn{opacity:1;animation:none}.ld-const path,.ld-c1{stroke-dashoffset:0;animation:none}}
  </style>''')

# JS: estrellas del loader + abrir sin video de sobre
rep('''  function openEnvelope() {
    if (opened) return;
    opened = true;
    unlockSong();
    gsap.killTweensOf(envImage);
    gsap.to(hint, { opacity: 0, duration: 0.2 });
    var p = envVideo.play();
    gsap.to(envImage, { opacity: 0, duration: 0.55, ease: 'power2.inOut', onComplete: function () { envImage.style.display = 'none'; } });
    gsap.to(envVideo, { opacity: 1, duration: 0.55, ease: 'power2.inOut' });
    if (p !== undefined) p.catch(function () { revealInvitation(); });
    startMusicOnOpen();
  }''', '''  (function(){
    var sky = document.getElementById('ldSky'); if (!sky) return;
    for (var i = 0; i < 46; i++) {
      var st = document.createElement('i'), z = 1 + Math.random() * 2.4;
      st.style.cssText = 'left:' + (Math.random() * 100) + '%;top:' + (Math.random() * 100) + '%;width:' + z + 'px;height:' + z + 'px;animation-delay:' + (-Math.random() * 3).toFixed(2) + 's;animation-duration:' + (2.4 + Math.random() * 2.6).toFixed(2) + 's';
      sky.appendChild(st);
    }
  })();

  function openEnvelope() {
    if (opened) return;
    opened = true;
    unlockSong();
    gsap.to('.ld-center', { scale: 1.12, opacity: 0, duration: .9, ease: 'power2.in' });
    gsap.to(envScreen, { opacity: 0, duration: 1.1, delay: .35, ease: 'power2.inOut', onComplete: revealInvitation });
    /* el intro (video) aparece debajo mientras el loader se desvanece */
    var scr = document.getElementById('intro-screen'); if (scr) scr.classList.add('on');
  }''')
io.open(P, 'w', encoding='utf-8', newline='\n').write(s)
print('ok')
