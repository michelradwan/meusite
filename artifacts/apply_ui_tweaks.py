import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Disable noise overlay in dark mode
noise_target = '[data-theme="dark"] .noise-overlay {\n  opacity: 0.15;\n}'
noise_replacement = '[data-theme="dark"] .noise-overlay {\n  opacity: 0;\n}'
content = content.replace(noise_target, noise_replacement)

# 2. Add Scroll Down indicator
# Hero ends at <p class="hero-note">...</p>\n    </div>\n\n</section>
# Let's find exactly the end of the text content inside the hero section
hero_text_content_regex = re.compile(r'(<p class="hero-note">.*?</p>\s*</div>)', re.DOTALL)
scroll_html = '''
    <!-- SCROLL INDICATOR -->
    <div class="scroll-indicator">
      <div class="mouse"></div>
      <span>Role para baixo</span>
    </div>
'''
def inject_scroll(match):
    return match.group(1) + '\n' + scroll_html
content = hero_text_content_regex.sub(inject_scroll, content, count=1)

scroll_css = '''
/* SCROLL INDICATOR */
.scroll-indicator {
  position: absolute;
  bottom: 8vh;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  opacity: 0.7;
  animation: bounce 2s infinite;
  z-index: 5;
}
.scroll-indicator .mouse {
  width: 24px;
  height: 38px;
  border: 2px solid var(--text-mid);
  border-radius: 12px;
  position: relative;
}
.scroll-indicator .mouse::before {
  content: '';
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 8px;
  background: var(--blue);
  border-radius: 2px;
  animation: scrollWheel 2s infinite;
}
.scroll-indicator span {
  font-size: 0.65rem;
  color: var(--text-mid);
  text-transform: uppercase;
  letter-spacing: 1px;
}
@keyframes scrollWheel {
  0% { top: 6px; opacity: 1; }
  100% { top: 18px; opacity: 0; }
}
@keyframes bounce {
  0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
  40% { transform: translateY(-10px); }
  60% { transform: translateY(-5px); }
}
'''
content = content.replace('/* HERO */', scroll_css + '\n/* HERO */')

# 3. Mac Tooltip
tooltip_html = '''    <div class="browser-wrap">
      
      <!-- MAC TOOLTIP -->
      <div class="mac-tooltip">
        <span class="tooltip-badge">Demonstração</span>
        <p><strong>A vitrine perfeita para o seu negócio</strong></p>
        <p>Veja como um design imersivo e de alta conversão transforma cliques em clientes instantâneos.</p>
      </div>
'''
content = content.replace('    <div class="browser-wrap">', tooltip_html)

tooltip_css = '''
/* MAC TOOLTIP */
.mac-tooltip {
  position: absolute;
  right: -290px;
  top: 40%;
  width: 260px;
  background: rgba(255,255,255,0.92);
  backdrop-filter: blur(10px);
  padding: 16px;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0,0,0,0.1);
  border: 1px solid rgba(255,255,255,0.8);
  opacity: 0;
  transform: translateX(-20px);
  transition: all 0.6s cubic-bezier(0.22, 1, 0.36, 1);
  pointer-events: none;
  z-index: 100;
  text-align: left;
}
[data-theme="dark"] .mac-tooltip {
  background: rgba(13, 21, 37, 0.85);
  border-color: rgba(255,255,255,0.08);
  box-shadow: 0 10px 40px rgba(0,0,0,0.6);
}
.mac-tooltip.show {
  opacity: 1;
  transform: translateX(0);
}
.tooltip-badge {
  display: inline-block;
  background: var(--blue);
  color: white;
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 3px 8px;
  border-radius: 4px;
  margin-bottom: 8px;
}
.mac-tooltip p {
  font-size: 0.85rem;
  color: var(--text-mid);
  line-height: 1.45;
  margin: 0;
}
.mac-tooltip p strong {
  color: var(--dark);
  font-size: 0.95rem;
  display: block;
  margin-bottom: 4px;
}
@media (max-width: 1100px) {
  .mac-tooltip {
    right: auto;
    left: 50%;
    top: -120px;
    transform: translateX(-50%) translateY(20px);
    width: 90%;
    max-width: 320px;
  }
  .mac-tooltip.show {
    transform: translateX(-50%) translateY(0);
  }
}
'''
content = content.replace('/* HERO */', tooltip_css + '\n/* HERO */')

# JS for tooltip
js_tooltip_target = '''if(pCanvas) {
         pCanvas.style.opacity = Math.max(0, 0.85 - (progress * 2));
      }'''
js_tooltip_replacement = '''if(pCanvas) {
         pCanvas.style.opacity = Math.max(0, 0.85 - (progress * 2));
      }
      
      const tooltip = document.querySelector('.mac-tooltip');
      if(tooltip) {
        if(progress > 0.9) tooltip.classList.add('show');
        else tooltip.classList.remove('show');
      }'''
content = content.replace(js_tooltip_target, js_tooltip_replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Applied UI tweaks!')
