import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add CSS
arch_css = '''
/* BROWSER REVEAL ARCH EFFECT */
.browser-reveal-section {
  position: relative;
  height: 350vh;
  width: 100%;
  background: transparent;
  z-index: 10;
  margin-top: -100px;
}
.arch-container {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}
.arch-bg {
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%) translateY(50%);
  width: 150vw;
  height: 150vh;
  background: radial-gradient(circle at bottom, #111B29 0%, #080D14 100%);
  border-radius: 50% 50% 0 0;
  will-change: transform, border-radius, width, height;
}
.arch-content {
  position: relative;
  z-index: 2;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: translateY(10vh) scale(0.85);
  opacity: 0;
  will-change: transform, opacity;
}
'''
content = content.replace('/* HERO */', arch_css + '\n/* HERO */')

# 2. Split Hero HTML
split_target = '  <!-- BROWSER MOCKUP -->\n  <div class="hero-visual">'
split_replacement = '''</section>

<!-- BROWSER REVEAL (APPLE-STYLE ARCH) -->
<section class="browser-reveal-section">
  <div class="arch-container">
    <div class="arch-bg"></div>
    <div class="arch-content">
      <!-- BROWSER MOCKUP -->
      <div class="hero-visual">'''
content = content.replace(split_target, split_replacement)

# 3. Close the new tags
end_target = '''    <div class="badge-row">
      <div class="browser-badge">
        <div class="badge-icon green">🎬</div>
        <div class="badge-content">
          <p>Animações que prendem atenção</p>
          <span>sem travamentos ou poluição visual</span>
        </div>
      </div>
      <div class="browser-badge">
        <div class="badge-icon blue">🚀</div>
        <div class="badge-content">
          <p>Sites feitos para impressionar</p>
          <span>e converter visitantes em clientes</span>
        </div>
      </div>
    </div>

    </div>
  </div>
</section>'''

end_replacement = '''    <div class="badge-row">
      <div class="browser-badge">
        <div class="badge-icon green">🎬</div>
        <div class="badge-content">
          <p>Animações que prendem atenção</p>
          <span>sem travamentos ou poluição visual</span>
        </div>
      </div>
      <div class="browser-badge">
        <div class="badge-icon blue">🚀</div>
        <div class="badge-content">
          <p>Sites feitos para impressionar</p>
          <span>e converter visitantes em clientes</span>
        </div>
      </div>
    </div>

        </div>
      </div>
    </div>
  </div>
</section>'''
content = content.replace(end_target, end_replacement)

# 4. Inject JS
arch_js = '''// =====================
// APPLE-STYLE ARCH REVEAL
// =====================
document.addEventListener('DOMContentLoaded', () => {
  const revealSection = document.querySelector('.browser-reveal-section');
  const archBg = document.querySelector('.arch-bg');
  const archContent = document.querySelector('.arch-content');

  if (revealSection && archBg && archContent) {
    function updateArch() {
      const rect = revealSection.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      
      const scrollDistance = revealSection.offsetHeight - windowHeight;
      let progress = -rect.top / scrollDistance;
      
      if (progress < 0) progress = 0;
      if (progress > 1) progress = 1;

      const easeOut = 1 - Math.pow(1 - progress, 3);

      const br = 50 * (1 - easeOut);
      const bgScale = 1 + (0.5 * easeOut);
      const ty = 50 * (1 - easeOut);
      
      archBg.style.borderRadius = `${br}% ${br}% 0 0`;
      archBg.style.transform = `translateX(-50%) translateY(${ty}%) scale(${bgScale}, ${1 + (0.2 * easeOut)})`;

      let opacityProgress = (progress - 0.1) / 0.4;
      if (opacityProgress < 0) opacityProgress = 0;
      if (opacityProgress > 1) opacityProgress = 1;
      
      const contentScale = 0.85 + (0.15 * easeOut);
      const contentTy = 10 * (1 - easeOut);
      
      archContent.style.opacity = opacityProgress;
      archContent.style.transform = `translateY(${contentTy}vh) scale(${contentScale})`;
    }

    window.addEventListener('scroll', () => {
      requestAnimationFrame(updateArch);
    }, {passive: true});

    updateArch();
  }
});
'''
content = content.replace('// SCROLL REVEAL', arch_js + '\n// SCROLL REVEAL')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied!')
