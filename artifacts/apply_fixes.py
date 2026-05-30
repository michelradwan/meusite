import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the bottom scroll indicator
scroll_bottom_target = '''    <!-- SCROLL INDICATOR -->
    <div class="scroll-indicator">
      <div class="mouse"></div>
      <span>Role para baixo</span>
    </div>'''
content = content.replace(scroll_bottom_target, '')

# 2. Update hero-badge
hero_badge_target = '<div class="hero-badge">Sites Profissionais · 2026</div>'
hero_badge_replacement = '''<div class="hero-badge">
      <div class="mouse-icon"></div>
      Role para baixo
    </div>'''
content = content.replace(hero_badge_target, hero_badge_replacement)

# 3. Add mouse-icon CSS and remove scroll-indicator CSS
css_target = re.compile(r'/\* SCROLL INDICATOR \*/.*?@keyframes bounce \{.*?\n\}\n', re.DOTALL)
css_replacement = '''/* SCROLL INDICATOR MOUSE ICON */
.mouse-icon {
  width: 12px;
  height: 18px;
  border: 1.5px solid var(--blue);
  border-radius: 8px;
  position: relative;
  display: inline-block;
  margin-right: 2px;
}
.mouse-icon::before {
  content: '';
  position: absolute;
  top: 3px;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 4px;
  background: var(--blue);
  border-radius: 2px;
  animation: scrollWheelMini 1.5s infinite;
}
@keyframes scrollWheelMini {
  0% { top: 3px; opacity: 1; }
  100% { top: 8px; opacity: 0; }
}
'''
content = css_target.sub(css_replacement, content)

# 4. Move MAC TOOLTIP
# Find tooltip
tooltip_regex = re.compile(r'(\s*<!-- MAC TOOLTIP -->\s*<div class="mac-tooltip">.*?</div>)', re.DOTALL)
match = tooltip_regex.search(content)
if match:
    tooltip_html = match.group(1)
    content = content.replace(tooltip_html, '') # Remove from current location
    
    # New copy
    new_tooltip = '''
      <!-- MAC TOOLTIP -->
      <div class="mac-tooltip">
        <span class="tooltip-badge">Demonstração</span>
        <p><strong>Sua Nova Máquina de Vendas</strong></p>
        <p>O layout perfeito não é apenas bonito. Ele guia a atenção do cliente e transforma visitantes casuais em pedidos instantâneos e lucro real.</p>
      </div>'''
    
    # Insert it right after <div class="arch-content">
    content = content.replace('<div class="arch-content">', '<div class="arch-content">' + new_tooltip)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
