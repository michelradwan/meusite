import re

def update_file(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    proof_html = '''<!-- PROOF -->
<section class="proof-section">
  <div class="proof-header reveal">
    <h2>O <em>impacto</em> de um site profissional</h2>
    <p>Histórias reais de negócios que deixaram de ser invisíveis e começaram a dominar suas regiões no digital.</p>
  </div>

  <div class="human-proof-slider-container reveal">
    <div class="human-proof-slider-wrapper">
      <div class="human-proof-slider-track" id="proofSliderTrack">
        
        <!-- Card 1: Fisioterapeuta -->
        <div class="human-proof-card">
          <div class="human-proof-badge">Fisioterapia Local</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            Eu achava que ter uma conta no Instagram era suficiente. Mas os pacientes que vinham de lá sempre choravam preço. Quando o Michel estruturou o meu site com foco no Google local, tudo mudou. Na primeira semana com o site no ar, fechei 4 tratamentos completos com pessoas que me acharam no Google pesquisando por 'fisioterapia especializada'. O site se pagou em 10 dias.
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar">LH</div>
              <div class="human-proof-meta">
                <h4>Dr. Lucas Henrique</h4>
                <p>Clínica de Fisioterapia</p>
              </div>
            </div>
            <div class="human-proof-metric">
              <span class="human-proof-metric-val">ROI em 10 dias</span>
              <span class="human-proof-metric-lbl">+22 novos pacientes no 1º mês</span>
            </div>
          </div>
        </div>
        
        <!-- Card 2: Boutique Bella -->
        <div class="human-proof-card">
          <div class="human-proof-badge">Loja Física &amp; Condicional</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            O meu maior erro era vender apenas pelo direct do Instagram. Dava um trabalho gigante responder todo mundo e muitos desistiam. Com o site de alta conversão que o Michel criou, apresentando a loja de forma profissional e com botão direto de agendamento de condicional, as clientes agora chegam prontas para comprar. A credibilidade da minha loja física triplicou.
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar" style="background: rgba(236, 72, 153, 0.08); color: #ec4899;">MS</div>
              <div class="human-proof-meta">
                <h4>Mariana Souza</h4>
                <p>Boutique Bella Moda</p>
              </div>
            </div>
            <div class="human-proof-metric">
              <span class="human-proof-metric-val">+35% no Ticket Médio</span>
              <span class="human-proof-metric-lbl">Redução de 70% no tempo de atendimento</span>
            </div>
          </div>
        </div>
        
        <!-- Card 3: Advocacia -->
        <div class="human-proof-card">
          <div class="human-proof-badge">Serviço Premium</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            Advogado depende de indicação, certo? Eu também achava isso. Mas quando decidi focar em direito societário para startups, percebi que precisava de uma presença séria. O site feito pelo Michel passa exatamente a autoridade que um fundador de startup procura antes de nos contratar. Já fechamos dois contratos de assessoria mensal recorrente vindos diretamente do formulário do site.
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar" style="background: rgba(217, 119, 6, 0.08); color: #d97706;">RA</div>
              <div class="human-proof-meta">
                <h4>Dr. Roberto Alves</h4>
                <p>Alves &amp; Associados</p>
              </div>
            </div>
            <div class="human-proof-metric">
              <span class="human-proof-metric-val">Recorrência Mensal</span>
              <span class="human-proof-metric-lbl">2 contratos de assessoria fechados</span>
            </div>
          </div>
        </div>

        <!-- Card 4: Consultoria (Human) -->
        <div class="human-proof-card">
          <div class="human-proof-badge" style="background: rgba(34,197,94,0.1); color: #22c55e;">Gratidão</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            Passando aqui só pra te agradecer, Michel. O site ficou simplesmente perfeito. Meus clientes não param de elogiar o profissionalismo e a rapidez. Foi a melhor decisão que tomei pro meu negócio esse ano.
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar" style="background: rgba(34,197,94,0.1); color: #22c55e;">CE</div>
              <div class="human-proof-meta">
                <h4>Carlos Eduardo</h4>
                <p>Consultoria Empresarial</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 5: Agência (Human) -->
        <div class="human-proof-card">
          <div class="human-proof-badge" style="background: rgba(168,85,247,0.1); color: #a855f7;">Feedback Real</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            Cara, surreal. O pessoal tá achando que a minha agência tem 50 funcionários só pelo nível de sofisticação do site. Trabalho de mestre, entregue antes do prazo. Só tenho a agradecer pela parceria.
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar" style="background: rgba(168,85,247,0.1); color: #a855f7;">FR</div>
              <div class="human-proof-meta">
                <h4>Felipe Ramos</h4>
                <p>Agência de Marketing</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Card 6: Nutricionista (Human) -->
        <div class="human-proof-card">
          <div class="human-proof-badge" style="background: rgba(245,158,11,0.1); color: #f59e0b;">Agradecimento</div>
          <div class="human-proof-quote-icon">“</div>
          <p class="human-proof-quote-text">
            Muito obrigada pela paciência e pelo carinho com o projeto. Eu não entendia nada de site e você deixou tudo tão fácil, claro e tão lindo. Me sinto muito mais segura para captar pacientes agora!
          </p>
          <div class="human-proof-footer">
            <div class="human-proof-author">
              <div class="human-proof-avatar" style="background: rgba(245,158,11,0.1); color: #f59e0b;">AC</div>
              <div class="human-proof-meta">
                <h4>Ana Clara</h4>
                <p>Nutricionista Esportiva</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
    
    <!-- Slider Controls -->
    <div class="human-slider-controls">
      <button class="human-slider-btn prev" id="proofPrevBtn" aria-label="Anterior">
        <svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg>
      </button>
      <div class="human-slider-dots" id="proofSliderDots"></div>
      <button class="human-slider-btn next" id="proofNextBtn" aria-label="Próximo">
        <svg viewBox="0 0 24 24"><polyline points="9 18 15 12 9 6"/></svg>
      </button>
    </div>
  </div>
</section>'''

    content = re.sub(r'<!-- PROOF -->.*?</div>\s*</section>', proof_html, content, flags=re.DOTALL)

    proof_js = '''// =====================
  // HUMAN TESTIMONIALS SLIDER JS
  // =====================
  const track = document.getElementById('proofSliderTrack');
  const prevBtn = document.getElementById('proofPrevBtn');
  const nextBtn = document.getElementById('proofNextBtn');
  const dotsContainer = document.getElementById('proofSliderDots');
  
  if (track && track.children.length > 0) {
    let isTransitioning = false;
    let autoPlayInterval;
    
    if (dotsContainer) dotsContainer.style.display = 'none';

    function getCardWidth() {
      const card = track.children[0];
      const style = window.getComputedStyle(track);
      const gap = parseFloat(style.gap) || 24;
      return card.getBoundingClientRect().width + gap;
    }
    
    function moveNext() {
      if (isTransitioning) return;
      isTransitioning = true;
      const moveDistance = getCardWidth();
      
      track.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      track.style.transform = `translate3d(-${moveDistance}px, 0, 0)`;
      
      const onTransitionEnd = () => {
        track.removeEventListener('transitionend', onTransitionEnd);
        track.style.transition = 'none';
        track.appendChild(track.firstElementChild);
        track.style.transform = 'translate3d(0, 0, 0)';
        track.offsetHeight;
        isTransitioning = false;
      };
      track.addEventListener('transitionend', onTransitionEnd);
    }
    
    function movePrev() {
      if (isTransitioning) return;
      isTransitioning = true;
      const moveDistance = getCardWidth();
      
      track.style.transition = 'none';
      track.insertBefore(track.lastElementChild, track.firstElementChild);
      track.style.transform = `translate3d(-${moveDistance}px, 0, 0)`;
      track.offsetHeight;
      
      requestAnimationFrame(() => {
        track.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        track.style.transform = 'translate3d(0, 0, 0)';
        
        const onTransitionEnd = () => {
          track.removeEventListener('transitionend', onTransitionEnd);
          isTransitioning = false;
        };
        track.addEventListener('transitionend', onTransitionEnd);
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        clearInterval(autoPlayInterval);
        moveNext();
        startAutoPlay();
      });
    }
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        clearInterval(autoPlayInterval);
        movePrev();
        startAutoPlay();
      });
    }
    
    function startAutoPlay() {
      autoPlayInterval = setInterval(moveNext, 4500);
    }
    startAutoPlay();
    
    track.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
    track.addEventListener('mouseleave', startAutoPlay);
  }'''

    # For index.html, replace existing script
    if 'HUMAN TESTIMONIALS SLIDER JS' in content:
        content = re.sub(r'// =====================\s*// HUMAN TESTIMONIALS SLIDER JS.*?}(?=\n\n|\n  // =====================)', proof_js, content, flags=re.DOTALL)
    else:
        # For index_safe.html, inject script at end of DOMContentLoaded
        content = content.replace('});\n</script>\n</body>', proof_js + '\n});\n</script>\n</body>')

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {html_file}')

update_file(r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index.html')
update_file(r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index_safe.html')
