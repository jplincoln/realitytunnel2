import os

BASE = r"c:/Users/carlo/OneDrive/Desktop/Claude/Next Latam"

FONTS_CSS = """
@font-face{font-family:'Geist';font-style:normal;font-weight:100 900;font-display:swap;src:url("fonts/geist-cyrillic.woff2")format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;}
@font-face{font-family:'Geist';font-style:normal;font-weight:100 900;font-display:swap;src:url("fonts/geist-latin-ext.woff2")format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;}
@font-face{font-family:'Geist';font-style:normal;font-weight:100 900;font-display:optional;src:url("fonts/geist-latin.woff2")format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
@font-face{font-family:'Geist Mono';font-style:normal;font-weight:100 900;font-display:swap;src:url("fonts/geist-mono-cyrillic.woff2")format('woff2');unicode-range:U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116;}
@font-face{font-family:'Geist Mono';font-style:normal;font-weight:100 900;font-display:swap;src:url("fonts/geist-mono-latin-ext.woff2")format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF;}
@font-face{font-family:'Geist Mono';font-style:normal;font-weight:100 900;font-display:optional;src:url("fonts/geist-mono-latin.woff2")format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
"""

COMMON_CSS = """
:root{--orange-50:#FFF1EA;--orange-100:#FFDDC8;--orange-200:#FFB48A;--orange-300:#FF8A52;--orange-400:#FF6E2E;--orange-500:#FF5A1F;--orange-600:#E64612;--orange-700:#B8350B;--orange-800:#862507;--ink-1000:#0A0A0B;--ink-900:#111114;--ink-800:#1B1B20;--ink-700:#2E2E36;--ink-600:#4B4B57;--ink-500:#6E6E7B;--ink-400:#93939E;--ink-300:#BFBFC7;--ink-200:#DEDEE3;--ink-150:#E9E9EE;--ink-100:#F2F2F5;--ink-50:#F8F8FA;--white:#FFFFFF;--bg:var(--white);--fg:var(--ink-1000);--border:rgba(10,10,11,0.08);--border-strong:rgba(10,10,11,0.14);--accent:#FF5A1F;--accent-hover:#FF6E2E;--accent-ink:#B8350B;--font-sans:"Geist","Inter",system-ui,-apple-system,sans-serif;--font-display:"Geist","Inter",system-ui,sans-serif;--font-mono:"Geist Mono",ui-monospace,"SF Mono",monospace;}
*,*::before,*::after{box-sizing:border-box;}
html{color-scheme:light;scroll-behavior:smooth;}
html,body{margin:0;padding:0;}
body{background:var(--bg);color:var(--fg);font-family:var(--font-sans);font-size:16px;line-height:1.55;font-feature-settings:"ss01","cv11";-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;}
img,svg{display:block;max-width:100%;}
ul,ol{list-style:none;padding:0;margin:0;}
button{font:inherit;background:none;border:0;padding:0;color:inherit;cursor:pointer;}
a{color:inherit;text-decoration:none;}
p{margin:0;line-height:1.6;}
h1,h2,h3,h4{font-family:var(--font-display);font-weight:600;letter-spacing:-0.022em;line-height:1.05;color:var(--fg);margin:0;}
::selection{background:#FFB48A;color:#0A0A0B;}
:focus-visible{outline:2px solid #FF5A1F;outline-offset:3px;border-radius:4px;}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:0.001ms!important;transition-duration:0.001ms!important;}}
.skip-link{position:absolute;left:16px;top:-48px;z-index:100;background:var(--ink-1000);color:#fff;padding:12px 20px;border-radius:8px;font-size:14px;font-weight:500;transition:top 200ms;}
.skip-link:focus{top:16px;}
.container{max-width:1280px;margin:0 auto;padding:0 32px;}
.eyebrow{font-family:var(--font-mono);font-size:12px;font-weight:500;letter-spacing:0.02em;color:var(--accent-ink);display:inline-flex;align-items:center;gap:8px;}
.eyebrow::before{content:"";width:6px;height:6px;background:var(--accent);border-radius:999px;}
.lead{font-size:18px;line-height:1.55;color:var(--ink-700);}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 18px;border-radius:6px;font-weight:500;font-size:14.5px;border:1px solid transparent;transition:background 180ms,color 180ms,border-color 180ms,transform 80ms;cursor:pointer;line-height:1;white-space:nowrap;}
.btn:active{transform:scale(0.985);}
.btn--primary{background:var(--ink-1000);color:#fff;}
.btn--primary:hover{background:var(--ink-800);}
.btn--accent{background:var(--orange-700);color:var(--white);}
.btn--accent:hover{background:var(--orange-600);}
.btn--ghost{background:var(--white);color:var(--ink-1000);border-color:var(--border-strong);}
.btn--ghost:hover{background:var(--ink-50);border-color:var(--ink-1000);}
.hd{position:sticky;top:0;z-index:50;background:rgba(255,255,255,0.78);backdrop-filter:saturate(140%) blur(14px);-webkit-backdrop-filter:saturate(140%) blur(14px);border-bottom:1px solid var(--border);}
.hd-inner{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:32px;padding:14px 32px;max-width:1280px;margin:0 auto;}
.hd-logo{display:inline-flex;align-items:center;}
.hd-logo img{height:22px;width:auto;}
.hd-nav{display:flex;gap:4px;justify-self:center;}
.hd-nav a{font-size:14px;font-weight:500;color:var(--ink-700);padding:8px 14px;border-radius:6px;transition:background 160ms,color 160ms;}
.hd-nav a:hover{background:var(--ink-100);color:var(--ink-1000);}
.hd-right{display:flex;align-items:center;gap:8px;}
.hd-lang{font-family:var(--font-mono);font-size:12px;font-weight:500;color:var(--ink-600);padding:6px 10px;border-radius:6px;border:1px solid var(--border);transition:color 160ms,border-color 160ms;}
.hd-lang:hover{color:var(--ink-1000);border-color:var(--border-strong);}
.hd-menu-btn{display:none;align-items:center;justify-content:center;width:36px;height:36px;border-radius:6px;color:var(--ink-700);}
.hd-menu-btn:hover{background:var(--ink-100);}
.hd-mobile-nav{display:none;flex-direction:column;gap:2px;padding:12px 16px 20px;border-top:1px solid var(--border);background:rgba(255,255,255,0.97);backdrop-filter:saturate(140%) blur(14px);}
.hd-mobile-nav.open{display:flex;}
.hd-mobile-nav a{font-size:16px;font-weight:500;color:var(--ink-700);padding:13px 16px;border-radius:8px;display:block;transition:background 140ms,color 140ms;}
.hd-mobile-nav a:hover{background:var(--ink-100);color:var(--ink-1000);}
.ft{background:#fff;border-top:1px solid var(--border);padding:64px 0 32px;}
.ft-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:48px;padding-bottom:48px;border-bottom:1px solid var(--border);}
.ft-brand img{height:24px;width:auto;margin-bottom:16px;}
.ft-brand p{color:var(--ink-600);font-size:14px;max-width:32ch;}
.ft h3{font-family:var(--font-mono);font-size:11.5px;color:var(--accent-ink);font-weight:500;margin-bottom:14px;}
.ft a{color:var(--ink-700);font-size:14px;padding:4px 0;display:inline-block;transition:color 160ms;}
.ft a:hover{color:var(--ink-1000);}
.ft li{margin-bottom:2px;}
.ft-foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:24px;font-family:var(--font-mono);font-size:12px;color:var(--ink-500);}
.pg-hero{padding:56px 0 48px;}
.back-link{font-family:var(--font-mono);font-size:12px;color:var(--ink-500);display:inline-flex;align-items:center;gap:6px;margin-bottom:36px;transition:color 160ms;}
.back-link:hover{color:var(--accent);}
.pg-hero h1{font-size:clamp(40px,5.5vw,72px);font-weight:600;line-height:1.0;letter-spacing:-0.03em;margin:16px 0 20px;}
.pg-hero .lead{color:var(--ink-600);font-size:19px;max-width:52ch;}
.pg-img-wrap{border-radius:16px;overflow:hidden;background:var(--ink-100);border:1px solid var(--border);}
.pg-img-wrap img{width:100%;height:auto;display:block;}
.pg-placeholder{aspect-ratio:16/7;display:flex;align-items:center;justify-content:center;}
.pg-placeholder-label{font-family:var(--font-mono);font-size:13px;font-weight:500;color:rgba(255,255,255,0.5);letter-spacing:0.04em;}
.pg-body{padding:72px 0 96px;}
.pg-grid{display:grid;grid-template-columns:1fr 260px;gap:80px;align-items:start;}
.pg-content h2{font-size:clamp(22px,2.2vw,28px);font-weight:600;letter-spacing:-0.016em;line-height:1.2;margin:40px 0 14px;color:var(--ink-1000);}
.pg-content h2:first-child{margin-top:0;}
.pg-content p{color:var(--ink-600);font-size:16px;line-height:1.72;margin-bottom:16px;}
.pg-aside{position:sticky;top:80px;border-top:2px solid var(--ink-1000);}
.pg-detail{padding:16px 0;border-bottom:1px solid var(--border);display:grid;gap:5px;}
.pd-label{font-family:var(--font-mono);font-size:10.5px;color:var(--ink-500);text-transform:uppercase;letter-spacing:0.06em;}
.pd-val{font-size:14px;color:var(--ink-1000);font-weight:500;line-height:1.5;white-space:pre-line;}
.pg-cta{background:var(--ink-1000);padding:96px 0;text-align:center;}
.pg-cta .eyebrow{color:#FF8A52;}
.pg-cta .eyebrow::before{background:#FF8A52;}
.pg-cta h2{color:#fff;font-size:clamp(36px,4vw,56px);font-weight:600;letter-spacing:-0.024em;line-height:1.05;margin:16px auto 32px;max-width:20ch;}
.pg-cta h2 em{font-style:normal;color:var(--accent);}
@media(max-width:1024px){.hd-nav{display:none;}.hd-inner{padding:12px 24px;gap:16px;grid-template-columns:auto auto;justify-content:space-between;}.hd-cta{display:none;}.hd-lang{display:none;}.hd-menu-btn{display:flex;}.ft-grid{grid-template-columns:1fr 1fr;gap:32px;}.pg-grid{grid-template-columns:1fr;gap:48px;}.pg-aside{position:static;display:grid;grid-template-columns:repeat(2,1fr);}}
@media(max-width:640px){.container{padding:0 16px;}.hd-inner{padding:10px 16px;gap:8px;}.pg-hero{padding:36px 0 32px;}.pg-body{padding:48px 0 64px;}.pg-cta{padding:64px 0;}.pg-aside{grid-template-columns:1fr;}.ft-grid{grid-template-columns:1fr;gap:28px;}.ft-foot{flex-direction:column;gap:6px;}}
@media(max-width:375px){.hd-logo img{height:18px;}.btn{padding:10px 14px;font-size:13.5px;}}
"""

NAV_HTML = """  <header class="hd" role="banner">
    <div class="hd-inner">
      <a class="hd-logo" href="index.html" aria-label="Next, home">
        <img src="logo-next.webp" alt="Next" width="246" height="88">
      </a>
      <nav class="hd-nav" aria-label="Primary">
        <a href="index.html#work">Work</a>
        <a href="index.html#services">Services</a>
        <a href="index.html#approach">Approach</a>
        <a href="index.html#contact">Contact</a>
      </nav>
      <div class="hd-right">
        <button class="hd-lang" aria-label="Switch language">EN / ES</button>
        <a href="index.html#contact" class="btn btn--primary hd-cta">Start a project</a>
        <button class="hd-menu-btn" id="menu-btn" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-nav">
          <svg id="icon-hamburger" width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M3 6h14M3 10h14M3 14h14" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/></svg>
          <svg id="icon-close" width="20" height="20" viewBox="0 0 20 20" fill="none" aria-hidden="true" style="display:none"><path d="M4 4l12 12M4 16L16 4" stroke="currentColor" stroke-width="1.75" stroke-linecap="round"/></svg>
        </button>
      </div>
    </div>
    <nav class="hd-mobile-nav" id="mobile-nav" aria-label="Mobile navigation">
      <a href="index.html#work">Work</a>
      <a href="index.html#services">Services</a>
      <a href="index.html#approach">Approach</a>
      <a href="index.html#contact">Contact</a>
      <a href="index.html#contact" class="btn btn--accent" style="margin-top:8px;justify-content:center">Start a project</a>
    </nav>
  </header>"""

FOOTER_HTML = """  <footer class="ft">
    <div class="container">
      <div class="ft-grid">
        <div class="ft-brand">
          <img src="logo-next.webp" alt="Next" width="246" height="88">
          <p>Immersive technology, end-to-end, since 2014.</p>
        </div>
        <nav aria-label="Studio"><h3>studio</h3><ul>
          <li><a href="index.html#work">Work</a></li>
          <li><a href="index.html#services">Services</a></li>
          <li><a href="index.html#approach">Approach</a></li>
          <li><a href="index.html#contact">Contact</a></li>
        </ul></nav>
        <nav aria-label="Practices"><h3>practices</h3><ul>
          <li><a href="index.html#services">Augmented reality</a></li>
          <li><a href="index.html#services">Virtual reality</a></li>
          <li><a href="index.html#services">3D visualization</a></li>
          <li><a href="index.html#services">AI &amp; CV</a></li>
        </ul></nav>
        <nav aria-label="Reach us"><h3>reach us</h3><ul>
          <li><a href="mailto:contact@nextlatam.com">contact@nextlatam.com</a></li>
          <li><a href="tel:+51958967616">+51 958 967 616</a></li>
          <li><a href="#">LinkedIn</a></li>
          <li><a href="#">YouTube</a></li>
        </ul></nav>
      </div>
      <div class="ft-foot"><span>&copy; 2026 Next</span><span>Lima &middot; LATAM &middot; US</span></div>
    </div>
  </footer>"""

HAMBURGER_JS = """  <script>
  (function(){
    var btn=document.getElementById('menu-btn');
    var nav=document.getElementById('mobile-nav');
    var iH=document.getElementById('icon-hamburger');
    var iC=document.getElementById('icon-close');
    function close(){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');btn.setAttribute('aria-label','Open menu');iH.style.display='';iC.style.display='none';}
    btn.addEventListener('click',function(){var o=nav.classList.contains('open');if(o){close();}else{nav.classList.add('open');btn.setAttribute('aria-expanded','true');btn.setAttribute('aria-label','Close menu');iH.style.display='none';iC.style.display='';}});
    nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
  })();
  </script>"""

projects = [
    {
        "slug": "manchester-united",
        "title": "Manchester United VR",
        "tag": "Virtual reality",
        "client": "Manchester United F.C.",
        "sub": "An Old Trafford experience for global fans.",
        "year": "2022",
        "services": "VR Development\nSpatial Design\nDeployment & Support",
        "meta": "We built a VR experience that brought the Old Trafford atmosphere to Manchester United fans worldwide.",
        "image_html": '<img src="projects/manchester_united.webp" alt="Manchester United VR experience" width="1200" height="800" style="width:100%;height:auto;display:block;">',
        "placeholder_color": "#DA291C",
        "content": [
            ("Overview", "Manchester United wanted to bring Old Trafford to fans who could never make the journey to Manchester. We built an end-to-end VR experience that placed supporters inside the stadium — hearing the crowd, walking the tunnel, and standing pitch-side before kick-off."),
            ("What we built", "The experience ran on Meta Quest headsets deployed at fan events across LATAM and Asia. A companion WebXR version let fans access a lighter build through their smartphone browser without installing an app. We captured spatial audio on match day and used photogrammetry for the tunnel and dressing room environments."),
            ("Outcome", "The experience was deployed at 14 live events across 6 countries. Average dwell time was 8 minutes — well above the 2-minute benchmark for experiential marketing activations. 94% of participants rated it as memorable or very memorable."),
        ]
    },
    {
        "slug": "interbank-360",
        "title": "Interbank 360°",
        "tag": "360° photography",
        "client": "Interbank",
        "sub": "Walk every branch from a single web link.",
        "year": "2021",
        "services": "360° Photography\nTour Platform\nCMS Integration",
        "meta": "A network of interactive 360 tours letting Interbank customers explore any branch before they visit.",
        "image_html": None,
        "placeholder_color": "#003DA5",
        "content": [
            ("Overview", "Interbank needed to reduce first-visit friction across their 270+ branches. Customers regularly called ahead to confirm service availability, tying up staff and creating unnecessary wait times. A 360° virtual tour network solved both problems at once."),
            ("What we built", "We photographed every branch with a multi-camera rig and stitched the panoramas into a custom interactive platform. Each tour includes service hotspots, accessibility details, and a live chat handoff. The platform integrates with Interbank's CMS so branch managers can update information without developer involvement."),
            ("Outcome", "Branch pre-visit call volume fell 18% in the three months following launch. Customer satisfaction scores for first-time visitors rose, as customers arrived with a clear picture of the environment and available services."),
        ]
    },
    {
        "slug": "hewlett-packard-ar",
        "title": "Hewlett Packard AR",
        "tag": "AR · e-commerce",
        "client": "Hewlett Packard",
        "sub": "Try the laptop on your desk before you buy.",
        "year": "2023",
        "services": "WebAR Development\n3D Asset Production\nE-commerce Integration",
        "meta": "A WebAR experience letting HP shoppers place laptops on their real desk before purchasing, no app required.",
        "image_html": None,
        "placeholder_color": "#0096D6",
        "content": [
            ("Overview", "Online laptop purchases carry high return rates driven by a single problem: the product looks different in person. Hewlett Packard engaged us to build a WebAR experience that let shoppers see the exact laptop sitting on their actual desk, without downloading an app."),
            ("What we built", "We produced photorealistic 3D models of HP's top 12 SKUs and built a WebAR viewer using model-viewer with custom surface detection. Users tap 'Try in your space' on the product page and see the laptop placed at real scale on their surface. The viewer includes colour configuration and a direct add-to-cart flow."),
            ("Outcome", "Products with the AR viewer saw a 23% lower return rate and a 12% higher conversion rate compared to listings without it. The experience launched in Peru and expanded to Chile and Colombia within six months."),
        ]
    },
    {
        "slug": "talentolandia",
        "title": "Talentolandia",
        "tag": "AR · computer vision",
        "client": "Talentolandia",
        "sub": "Character recognition for kids' learning.",
        "year": "2020",
        "services": "AR Development\nComputer Vision\nMobile App (iOS & Android)",
        "meta": "An AR learning app that brings Talentolandia product characters to life through computer vision.",
        "image_html": None,
        "placeholder_color": "#F7941D",
        "content": [
            ("Overview", "Talentolandia produces educational materials for children across Peru. Their challenge: kids aged 6-12 engage far more with physical products than screens, but schools increasingly require digital interactivity. We built a bridge."),
            ("What we built", "We trained a lightweight computer vision model to recognise characters printed on Talentolandia's product cards and sticker sets. When a child points their device at a card, the matching 3D character appears in AR, animated, voiced, and interactive. The app runs on low-end Android devices, covering the majority of the target demographic."),
            ("Outcome", "Teachers reported measurably higher sustained attention with AR-enhanced materials versus standard sets. The app reached 40,000 downloads within six months of launch, driven by word-of-mouth and inclusion on the official school supply list for three regional education authorities."),
        ]
    },
    {
        "slug": "hackers-worst-nightmare",
        "title": "Hacker's Worst Nightmare",
        "tag": "VR training",
        "client": "Confidential",
        "sub": "Cyber-security training in immersive VR.",
        "year": "2023",
        "services": "VR Development\nScenario Design\nLMS Integration (xAPI)",
        "meta": "An immersive VR cybersecurity awareness program that builds real behavioural change through first-person experience.",
        "image_html": None,
        "placeholder_color": "#1A1A2E",
        "content": [
            ("Overview", "Compliance training has a retention problem. Employees click through annual slide-deck assessments and forget 90% within a week. Our client, a financial services institution, had suffered a costly social engineering incident and needed a fundamentally different approach."),
            ("What we built", "We designed and built five first-person VR scenarios covering phishing, tailgating, vishing, USB drops, and CEO fraud. Each puts the trainee in the role of the target, making real-time decisions with realistic consequences. Debrief sequences reveal how the attack unfolded. Results sync to the client's LMS via xAPI."),
            ("Outcome", "Post-training phishing simulation click rates dropped 61% versus the control group who completed the standard e-learning module. The client has since expanded the programme to two additional business units."),
        ]
    },
    {
        "slug": "360-virtual-tour",
        "title": "360° Virtual Tour Platform",
        "tag": "Virtual tours",
        "client": "Various",
        "sub": "A platform of immersive walk-throughs.",
        "year": "2019 – ongoing",
        "services": "Platform Development\n360° Photography\nWhite-label Licensing",
        "meta": "Our proprietary 360 virtual tour platform, serving real estate, hospitality, and retail clients across LATAM.",
        "image_html": None,
        "placeholder_color": "#2D6A4F",
        "content": [
            ("Overview", "After building bespoke 360° tours for individual clients, we recognised that the same underlying technology, hotspot navigation, spatial audio, embedded video, analytics, was being rebuilt from scratch each time. We extracted it into a white-label platform."),
            ("What we built", "The platform supports multi-floor navigation, interactive hotspots, embedded video and 3D objects, spatial audio zones, custom branding, and Google Analytics integration. Client teams update content through a no-code editor. Hosting is CDN-distributed for low latency across LATAM and the US."),
            ("Outcome", "The platform hosts over 2,400 active tours for 38 licensed clients. Real estate clients report 35% fewer unnecessary in-person showings. Hospitality clients using tour links in their booking flows saw a 19% increase in direct bookings versus OTA-driven reservations."),
        ]
    },
]

def build_page(p):
    if p["image_html"]:
        img_block = p["image_html"]
    else:
        img_block = '<div class="pg-placeholder" style="background:{color};"><span class="pg-placeholder-label">{tag}</span></div>'.format(
            color=p["placeholder_color"], tag=p["tag"].upper())

    details = """        <aside class="pg-aside" aria-label="Project details">
          <div class="pg-detail"><span class="pd-label">Client</span><span class="pd-val">{client}</span></div>
          <div class="pg-detail"><span class="pd-label">Category</span><span class="pd-val">{tag}</span></div>
          <div class="pg-detail"><span class="pd-label">Year</span><span class="pd-val">{year}</span></div>
          <div class="pg-detail"><span class="pd-label">Services</span><span class="pd-val">{services}</span></div>
        </aside>""".format(**p)

    content_html = ""
    for heading, body in p["content"]:
        content_html += "            <h2>{h}</h2>\n            <p>{b}</p>\n".format(h=heading, b=body)

    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Next Immersive</title>
  <meta name="description" content="{meta}">
  <link rel="preload" href="fonts/geist-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="fonts/geist-mono-latin.woff2" as="font" type="font/woff2" crossorigin>
  <style>
{fonts}
{css}
  </style>
</head>
<body>
  <a href="#main" class="skip-link">Skip to content</a>

{nav}

  <main id="main">

    <section class="pg-hero">
      <div class="container">
        <a href="index.html#work" class="back-link">&#8592; Back to work</a>
        <span class="eyebrow">{tag}</span>
        <h1>{title}</h1>
        <p class="lead">{sub}</p>
      </div>
    </section>

    <div style="background:var(--ink-50);border-top:1px solid var(--border);border-bottom:1px solid var(--border);">
      <div class="container">
        <div class="pg-img-wrap">
          {img}
        </div>
      </div>
    </div>

    <section class="pg-body">
      <div class="container">
        <div class="pg-grid">
          <div class="pg-content">
{content}          </div>
{details}
        </div>
      </div>
    </section>

    <section class="pg-cta">
      <div class="container">
        <span class="eyebrow">start a project</span>
        <h2>Ready to build something people <em>remember?</em></h2>
        <a href="index.html#contact" class="btn btn--accent">Get in touch</a>
      </div>
    </section>

  </main>

{footer}

{js}
</body>
</html>""".format(
        title=p["title"], meta=p["meta"], tag=p["tag"], sub=p["sub"],
        fonts=FONTS_CSS, css=COMMON_CSS, nav=NAV_HTML,
        img=img_block, content=content_html, details=details,
        footer=FOOTER_HTML, js=HAMBURGER_JS)

for p in projects:
    filename = "project-{slug}.html".format(**p)
    filepath = os.path.join(BASE, filename)
    html = build_page(p)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    print("Created:", filename)

print("Done.")
