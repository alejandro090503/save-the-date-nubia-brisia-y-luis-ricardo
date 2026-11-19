import io, re
SRC = r'C:/Users/aleja/save-the-date-iliana-y-arrigo/index.html'
DST = r'C:/Users/aleja/save-the-date-nubia-brisia-y-luis-ricardo/_espejo/index.html'
s = io.open(SRC, encoding='utf-8').read()
SB = 'https://bsjoelxktbvlavfoozhk.supabase.co/storage/v1/object/public/fotos-clientes/'
for a, b in [
 ('Iliana &amp; Arrigo', 'Nubia Brisia &amp; Luis Ricardo'),
 ('Iliana Sánchez y Arrigo Coen se casan el 17 de abril de 2027', 'Nubia Brisia y Luis Ricardo se casan el 5 de junio de 2027'),
 ('Iliana<span class="amp">&amp;</span>Arrigo', 'Nubia Brisia<span class="amp">&amp;</span>Luis Ricardo'),
 ('17 de abril de 2027', '5 de junio de 2027'),
 ('save-the-date-iliana-y-arrigo.vercel.app', 'save-the-date-nubia-y-luis.vercel.app/_espejo'),
 ('<span class="d-mon">Abril</span>', '<span class="d-mon">Junio</span>'),
 ('17 · 04 · 2027', '05 · 06 · 2027'),
 ('I&amp;A<small>2027</small>', 'B&amp;R<small>2027</small>'),
 ('Sobre con sello de cera I&amp;A', 'Sobre con sello B&amp;R'),
 ("2027-04-17T17:00:00-06:00", "2027-06-05T10:00:00-06:00"),
 ('boda-iliana-y-arrigo/std/sobre.jpg', 'boda-nubia-brisia-luis-ricardo/std/sobre.jpg'),
 ('boda-iliana-y-arrigo/std/sobre-abre.mp4', 'boda-nubia-brisia-luis-ricardo/video/sobre-apertura.mp4'),
 ('boda-iliana-y-arrigo/std/poster.jpg', 'boda-nubia-brisia-luis-ricardo/std/poster.jpg'),
 ('boda-iliana-y-arrigo/std/save-the-date.mp4', 'boda-nubia-brisia-luis-ricardo/std/save-the-date.mp4'),
 ('boda-iliana-y-arrigo/audio/cancion.mp3?v=2', 'audio/boda-nubia-brisia-luis-ricardo/cancion.mp3'),
 ("https://boda-isaac-y-claudia.vercel.app/cancion.mp3", SB + 'audio/boda-nubia-brisia-luis-ricardo/cancion.mp3'),
 ('<span class="d-num">17</span>', '<span class="d-num">5</span>'),
]:
    s = s.replace(a, b)
# el sobre del STD es local (no existe en Supabase std/)
s = s.replace(SB + 'boda-nubia-brisia-luis-ricardo/std/sobre.jpg', 'sobre.jpg')
# paleta: vino -> azul noche, olivo -> oro, tinta -> azul muy oscuro, marfil -> champán
for a, b in [('#f2f2f2', '#F7EBD6'), ('#faf8f4', '#FCF5E6'), ('#fffdf8', '#FFFAEF'), ('#e9e2d6', '#EBDDBF'),
 ('#5a734f', '#A8811C'), ('#3f5237', '#7A5A12'), ('#a9bf9d', '#D8BE7A'), ('#8aa47c', '#C9A24A'),
 ('#701831', '#1E3A8A'), ('#54101f', '#13224A'), ('#3a0c17', '#0A1430'), ('#33282b', '#1B2547'), ('#241a1c', '#0A1430'),
 ('rgba(90,115,79', 'rgba(168,129,28'), ('rgba(112,24,49', 'rgba(30,58,138'), ('rgba(36,26,28', 'rgba(10,20,48'),
 ('WINE=[112,24,49], OLIVE=[90,115,79]', 'WINE=[30,58,138], OLIVE=[168,129,28]'),
 ('rgba(242,242,242', 'rgba(247,235,214'), ('rgba(84,16,31', 'rgba(19,34,74'), ('rgba(250,246,238', 'rgba(255,250,239')]:
    s = s.replace(a, b)
# fondo de respaldo mientras no exista el video del espejo
s = s.replace('#bgwrap{position:fixed;inset:0;z-index:0;overflow:hidden;background:var(--ivory)}',
 '#bgwrap{position:fixed;inset:0;z-index:0;overflow:hidden;background:linear-gradient(170deg,#F7EBD6 0%,#E9D5AE 45%,#B9C7DD 100%)}')
# nombres más largos
s = re.sub(r'(\.hero-names\{[^}]*?)font-size:[^;]+;', r'\1font-size:clamp(34px,10.4vw,52px);', s, count=1)
io.open(DST, 'w', encoding='utf-8', newline='\n').write(s)
print('ok', len(s))
