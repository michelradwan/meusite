import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index_safe.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Hero HTML to be a Sticky Wrapper and add scrub-item classes
hero_html_new = '''<div class="hero-sticky-wrap" style="position:sticky; top:0; height:100vh; width:100%; display:flex; flex-direction:column; align-items:center; justify-content:center; overflow:hidden;">
    <div class="hero-text-content" style="display:flex;flex-direction:column;align-items:center;z-index:2;position:relative;">
      <div class="hero-badge scrub-item">Sites Profissionais · 2026</div>
      <h1 class="scrub-item">Seu negócio existe.<br>Mas o Google <em class="typewriter-text">sabe disso?</em></h1>
      <p class="hero-sub scrub-item">Enquanto você serve seus clientes com todo o cuidado do mundo, seus concorrentes estão sendo encontrados por centenas de pessoas prontas para comprar. E você não aparece em lugar nenhum.</p>
      <div class="hero-actions scrub-item">
        <a href="https://wa.me/5511932609424" target="_blank" class="btn-blue">Quero meu site agora</a>
        <a href="#por-que" class="btn-ghost">
          Ver como funciona
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
      </div>
      <p class="hero-note scrub-item">Entrega em até 7 dias &nbsp;·&nbsp; Sem mensalidade oculta &nbsp;·&nbsp; Suporte incluído</p>
    </div>
    
    <!-- BROWSER MOCKUP -->
    <div class="hero-visual scrub-visual" style="position:absolute; bottom: 5%; width: 100%; max-width: 1200px; transform-origin: top center;">
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
    </div>
  </div>'''

hero_full_regex = re.compile(r'<div class="hero-text-content"(.*?)</div>\s*</div>\s*</div>\s*</div>\s*</section>', re.DOTALL)

def replace_hero(match):
    return hero_html_new + '\n</section>'

content = hero_full_regex.sub(replace_hero, content)

# 2. Update .hero CSS to have 250vh height and remove flex layout so sticky works
content = content.replace('.hero{\n  min-height:100vh;\n  display:flex;flex-direction:column;\n  align-items:center;justify-content:center;\n  text-align:center;\n  padding:120px 5% 80px;', '.hero{\n  min-height:250vh;\n  display:block;\n  text-align:center;\n  padding:0;')

# 3. Remove default animations from CSS
content = content.replace('animation:fadeUp 0.7s 0.2s forwards;', '')
content = content.replace('animation:fadeUp 0.8s 0.4s forwards;', '')
content = content.replace('.hero-sub{\n  font-size:1.05rem;\n  color:var(--text-mid);\n  line-height:1.7;\n  max-width:680px;\n  margin-bottom:2.5rem;\n  opacity:0;\n  animation:fadeUp 0.8s 0.5s forwards;', '.hero-sub{\n  font-size:1.05rem;\n  color:var(--text-mid);\n  line-height:1.7;\n  max-width:680px;\n  margin-bottom:2.5rem;')

# 4. Inject the Scrub JS
scrub_js = '''// =====================
// HERO SCROLL SCRUBBING
// =====================
const heroSection = document.querySelector('.hero');
const scrubItems = document.querySelectorAll('.scrub-item');
const scrubVisual = document.querySelector('.scrub-visual');

// Initialize opacity to 0
scrubItems.forEach(item => {
  item.style.opacity = '0';
  item.style.transform = 'translate3d(0, -48px, 0)';
  item.style.willChange = 'opacity, transform';
});
if(scrubVisual){
  scrubVisual.style.opacity = '0';
  scrubVisual.style.transform = 'translate3d(0, 80px, 0) scale(0.95)';
  scrubVisual.style.willChange = 'opacity, transform';
}

function updateScrub() {
  if(!heroSection) return;
  const rect = heroSection.getBoundingClientRect();
  
  const scrollDistance = heroSection.offsetHeight - window.innerHeight;
  let progress = -rect.top / scrollDistance;
  
  if (progress < 0) progress = 0;
  if (progress > 1) progress = 1;

  const totalItems = scrubItems.length;
  // Let text animate between 0 and 0.5 progress
  scrubItems.forEach((item, index) => {
    const startP = index * (0.5 / totalItems);
    const endP = startP + 0.15;
    
    let ip = (progress - startP) / (endP - startP);
    if(ip < 0) ip = 0;
    if(ip > 1) ip = 1;
    
    const easeOut = 1 - Math.pow(1 - ip, 3);
    
    item.style.opacity = easeOut;
    item.style.transform = `translate3d(0, ${-48 * (1 - easeOut)}px, 0)`;
  });

  // Let visual (mockup) animate between 0.3 and 0.8 progress
  if(scrubVisual) {
    let vp = (progress - 0.3) / 0.5;
    if(vp < 0) vp = 0;
    if(vp > 1) vp = 1;
    const vEaseOut = 1 - Math.pow(1 - vp, 3);
    
    scrubVisual.style.opacity = vEaseOut;
    scrubVisual.style.transform = `translate3d(0, ${80 * (1 - vEaseOut)}px, 0) scale(${0.95 + 0.05 * vEaseOut})`;
  }
}

window.addEventListener('scroll', () => {
  requestAnimationFrame(updateScrub);
}, {passive: true});

updateScrub();
'''

content = content.replace('// SCROLL REVEAL', scrub_js + '\n// SCROLL REVEAL')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Script applied!')
