import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index_safe.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Restore original Hero HTML
hero_html_original = '''<div class="hero-text-content" style="display:flex;flex-direction:column;align-items:center;z-index:2;position:relative;">
    <div class="hero-badge">Sites Profissionais · 2026</div>
    <h1>Seu negócio existe.<br>Mas o Google <em class="typewriter-text">sabe disso?</em></h1>
    <p class="hero-sub">Enquanto você serve seus clientes com todo o cuidado do mundo, seus concorrentes estão sendo encontrados por centenas de pessoas prontas para comprar. E você não aparece em lugar nenhum.</p>
    <div class="hero-actions">
      <a href="https://wa.me/5511932609424" target="_blank" class="btn-blue">Quero meu site agora</a>
      <a href="#por-que" class="btn-ghost">
        Ver como funciona
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>
    <p class="hero-note">Entrega em até 7 dias &nbsp;·&nbsp; Sem mensalidade oculta &nbsp;·&nbsp; Suporte incluído</p>
  </div>
  
  <!-- BROWSER MOCKUP -->
  <div class="hero-visual">
    <div class="hero-parallax-inner" style="transform-origin: top center; transition: transform 0.1s ease-out, opacity 0.1s ease-out; position:relative; z-index:1;">
      <div class="browser-wrap">
        <div class="browser-head">
          <div class="browser-dots"><span></span><span></span><span></span></div>
          <div class="browser-url"><svg viewBox="0 0 24 24"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg> seu-negocio.com.br</div>
        </div>
        <div class="browser-body">
          <div class="site-hero-mock">
            <div class="mock-eyebrow">Qualidade Superior</div>
            <h2 class="mock-h1">A melhor massa da cidade<br><em>pede aqui!</em></h2>
            <p class="mock-sub">Ingredientes frescos, receita de família e entrega em 30 minutos.</p>
            <div class="mock-btn">Fazer Pedido Agora</div>
          </div>
          <div class="mock-stats">
            <div class="mock-stat-item"><span class="mock-stat-n">4.9</span><span class="mock-stat-l">Avaliações</span></div>
            <div class="mock-stat-item"><span class="mock-stat-n">+12k</span><span class="mock-stat-l">Pedidos</span></div>
            <div class="mock-stat-item"><span class="mock-stat-n">30m</span><span class="mock-stat-l">Entrega</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>'''

# Replace the sticky wrap back to normal
hero_full_regex = re.compile(r'<div class="hero-sticky-wrap".*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)
def restore_hero(match):
    return hero_html_original + '\n</section>'
content = hero_full_regex.sub(restore_hero, content)

# 2. Restore .hero CSS
content = content.replace('.hero{\n  min-height:250vh;\n  display:block;\n  text-align:center;\n  padding:0;', '.hero{\n  min-height:100vh;\n  display:flex;flex-direction:column;\n  align-items:center;justify-content:center;\n  text-align:center;\n  padding:120px 5% 80px;')

# 3. Restore animations to CSS
content = content.replace('margin-bottom:2.5rem;\n  opacity:0;\n}', 'margin-bottom:2.5rem;\n  opacity:0;\n  animation:fadeUp 0.7s 0.2s forwards;\n}')
content = content.replace('margin-bottom:1.6rem;\n  opacity:0;\n}', 'margin-bottom:1.6rem;\n  opacity:0;\n  animation:fadeUp 0.8s 0.4s forwards;\n}')
content = content.replace('.hero-sub{\n  font-size:1.05rem;\n  color:var(--text-mid);\n  line-height:1.7;\n  max-width:680px;\n  margin-bottom:2.5rem;', '.hero-sub{\n  font-size:1.05rem;\n  color:var(--text-mid);\n  line-height:1.7;\n  max-width:680px;\n  margin-bottom:2.5rem;\n  opacity:0;\n  animation:fadeUp 0.8s 0.5s forwards;')

# 4. Remove the Scrub JS
scrub_js_regex = re.compile(r'// =====================\n// HERO SCROLL SCRUBBING\n// =====================.*?updateScrub\(\);\n', re.DOTALL)
content = scrub_js_regex.sub('', content)

# 5. Remove reveal-top from JS (if any left)
content = content.replace("querySelectorAll('.reveal,.reveal-left,.reveal-right,.reveal-top')", "querySelectorAll('.reveal,.reveal-left,.reveal-right')")

# 6. Remove reveal-top CSS
reveal_top_regex = re.compile(r'\.reveal-top\{\n  opacity:0;\n  transform:translateY\(-48px\);\n  transition:\n    opacity 1\.3s cubic-bezier\(0\.22,1,0\.36,1\),\n    transform 1\.3s cubic-bezier\(0\.22,1,0\.36,1\);\n  will-change: opacity, transform;\n\}\n\.reveal-top\.visible\{opacity:1;transform:translateY\(0\);\}\n\n', re.DOTALL)
content = reveal_top_regex.sub('', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted!')
