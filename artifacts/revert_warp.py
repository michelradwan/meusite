import re

file_path = r'c:\Users\miche\OneDrive\Desktop\michel-radwan-site\index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Revert .browser-reveal-section CSS
reveal_bg_replacement = '''.browser-reveal-section {
  position: relative;
  height: 350vh;
  width: 100%;
  background: transparent;
  z-index: 10;
  margin-top: -100px;
}'''
reveal_bg_target = '''.browser-reveal-section {
  position: relative;
  height: 350vh;
  width: 100%;
  background: linear-gradient(135deg, #FFF0E6 0%, #FFFBF5 100%);
  z-index: 10;
  margin-top: -100px;
}
[data-theme="dark"] .browser-reveal-section {
  background: transparent;
}'''

content = content.replace(reveal_bg_target, reveal_bg_replacement)

# 2. Revert updateArch JS to remove window.scrubProgress
scrub_replacement = 'const easeOut = 1 - Math.pow(1 - progress, 3);'
scrub_target = '''window.scrubProgress = progress; // Expose for particles warp speed
      const easeOut = 1 - Math.pow(1 - progress, 3);'''
content = content.replace(scrub_target, scrub_replacement)

# 3. Revert Particles Canvas logic
particle_draw_replacement = '''      p.update();
      ctx.beginPath();
      ctx.arc(p.x,p.y,p.r,0,Math.PI*2);
      ctx.fillStyle=`rgba(${p.color},${p.alpha})`;
      ctx.fill();
    });
    // connections
    for(let i=0;i<particles.length;i++){
      for(let j=i+1;j<particles.length;j++){
        const dx=particles[i].x-particles[j].x;
        const dy=particles[i].y-particles[j].y;
        const dist=Math.sqrt(dx*dx+dy*dy);
        if(dist<140){
          ctx.beginPath();
          ctx.strokeStyle=`rgba(59,130,246,${0.15 - dist/140*0.15})`;
          ctx.lineWidth=0.6;
          ctx.moveTo(particles[i].x,particles[i].y);
          ctx.lineTo(particles[j].x,particles[j].y);
          ctx.stroke();
        }
      }
    }'''

particle_draw_target = '''      p.update();
      ctx.beginPath();
      
      // Warp Speed Calculation
      const scrub = window.scrubProgress || 0;
      const scaleMultiplier = 1 + (scrub * 15); // Grow up to 16x
      
      ctx.arc(p.x, p.y, p.r * scaleMultiplier, 0, Math.PI*2);
      ctx.fillStyle=`rgba(${p.color},${p.alpha})`;
      ctx.fill();
    });
    // connections
    const scrub = window.scrubProgress || 0;
    const connectionDist = 140 * (1 + (scrub * 1.5));
    const lineThick = 0.6 + (scrub * 3);
    
    for(let i=0;i<particles.length;i++){
      for(let j=i+1;j<particles.length;j++){
        const dx=particles[i].x-particles[j].x;
        const dy=particles[i].y-particles[j].y;
        const dist=Math.sqrt(dx*dx+dy*dy);
        if(dist<connectionDist){
          ctx.beginPath();
          ctx.strokeStyle=`rgba(59,130,246,${0.15 - dist/connectionDist*0.15})`;
          ctx.lineWidth=lineThick;
          ctx.moveTo(particles[i].x,particles[i].y);
          ctx.lineTo(particles[j].x,particles[j].y);
          ctx.stroke();
        }
      }
    }'''

content = content.replace(particle_draw_target, particle_draw_replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Reverted warp speed particles!')
