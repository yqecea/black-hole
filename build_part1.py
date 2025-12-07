
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

def write_index(content):
    with open('index.html', 'w') as f:
        f.write(content)

# PART 1: HEAD, STYLES, NAV
part1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zero to Infinity | The Complete Black Hole Guide (Expanded Edition)</title>

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700;800&family=Inter:wght@200;300;400;500;600;700&family=JetBrains+Mono:wght@300;400&display=swap" rel="stylesheet">

    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        serif: ['Cinzel', 'serif'],
                        mono: ['JetBrains Mono', 'monospace'],
                    },
                    colors: {
                        zinc: {
                            850: '#1f1f22',
                            900: '#18181b',
                            950: '#09090b',
                        }
                    },
                    backgroundImage: {
                        'noise': "url('data:image/svg+xml,%3Csvg viewBox=\"0 0 200 200\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cfilter id=\"noiseFilter\"%3E%3CfeTurbulence type=\"fractalNoise\" baseFrequency=\"0.65\" numOctaves=\"3\" stitchTiles=\"stitch\"/%3E%3C/filter%3E%3Crect width=\"100%25\" height=\"100%25\" filter=\"url(%23noiseFilter)\" opacity=\"0.05\"/%3E%3C/svg%3E')",
                    }
                }
            }
        }
    </script>

    <style>
        :root {
            --bg-deep: #050505;
            --accent-silver: #d4d4d8;
            --glass-border: rgba(255, 255, 255, 0.08);
            --glass-bg: rgba(255, 255, 255, 0.02);
        }

        * { box-sizing: border-box; }

        body {
            background: var(--bg-deep);
            color: #fff;
            overflow-x: hidden;
            font-family: 'Inter', sans-serif;
            scroll-behavior: smooth;
        }

        h1, h2, h3, h4, h5, h6, .font-cinzel {
            font-family: 'Cinzel', serif;
        }

        .font-mono {
            font-family: 'JetBrains Mono', monospace;
        }

        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: #050505; }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
        ::-webkit-scrollbar-thumb:hover { background: #555; }

        /* Star Field */
        .star-field {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none; z-index: 0;
        }
        .star {
            position: absolute; background: white; border-radius: 50%;
            animation: twinkle 3s ease-in-out infinite;
        }
        @keyframes twinkle { 0%, 100% { opacity: 0.3; } 50% { opacity: 1; } }

        /* Typography Utilities */
        .text-silver-gradient {
            background: linear-gradient(to right, #ffffff, #e4e4e7, #a1a1aa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .text-justify-academic {
            text-align: justify;
            text-justify: inter-word;
        }

        /* Glass Card Enhanced */
        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border: 1px solid var(--glass-border);
            position: relative;
            overflow: hidden;
            transition: all 0.4s cubic-bezier(0.19, 1, 0.22, 1);
            --mouse-x: 50%; --mouse-y: 50%; --spotlight-size: 500px;
        }
        .glass-card:hover {
            border-color: rgba(255, 255, 255, 0.2);
            transform: translateY(-2px);
            box-shadow: 0 20px 40px -10px rgba(0,0,0,0.5);
        }

        /* Spotlight Effect */
        .glass-card::before {
            content: ""; position: absolute; inset: 0; z-index: 1;
            background: radial-gradient(var(--spotlight-size) circle at var(--mouse-x) var(--mouse-y), rgba(255, 255, 255, 0.06), transparent 40%);
            opacity: 0; transition: opacity 0.5s; pointer-events: none; mix-blend-mode: overlay;
        }
        .glass-card:hover::before { opacity: 1; }
        .glass-card > * { position: relative; z-index: 2; }

        /* Equation Box */
        .equation-box {
            font-family: 'Times New Roman', serif;
            background: rgba(0, 0, 0, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.1);
            position: relative;
        }
        .equation-box::after {
            content: "EQ"; position: absolute; top: 0; right: 0;
            font-size: 0.5rem; padding: 0.2rem 0.4rem;
            background: rgba(255,255,255,0.1); color: #888;
        }

        /* Horizontal Timeline */
        .horizontal-timeline-container {
            width: 100%; overflow-x: auto; padding-bottom: 2rem;
            mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 5%, black 95%, transparent);
        }
        .horizontal-timeline {
            display: flex; gap: 2rem; width: max-content; padding: 0 2rem;
        }
        .timeline-card {
            min-width: 300px; max-width: 300px;
            flex-shrink: 0;
            border-top: 1px solid rgba(255,255,255,0.2);
            padding-top: 1rem; position: relative;
        }
        .timeline-card::before {
            content: ''; position: absolute; top: -3px; left: 0;
            width: 6px; height: 6px; background: white; border-radius: 50%;
            box-shadow: 0 0 10px white;
        }

        /* Dashboard Grid (Anatomy) */
        .dashboard-grid {
            display: grid; grid-template-columns: 1fr; gap: 1.5rem;
        }
        @media (min-width: 1024px) {
            .dashboard-grid { grid-template-columns: 350px 1fr 350px; }
            .sticky-center { position: sticky; top: 6rem; height: calc(100vh - 8rem); }
        }

        /* Deep Dive Accordion */
        details.deep-dive {
            background: rgba(0,0,0,0.2);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 0.75rem; overflow: hidden;
            transition: all 0.3s ease;
        }
        details.deep-dive[open] {
            background: rgba(255,255,255,0.03);
            border-color: rgba(255,255,255,0.1);
        }
        details.deep-dive summary {
            padding: 1rem; cursor: pointer; list-style: none;
            display: flex; align-items: center; justify-content: space-between;
            font-family: 'Cinzel', serif; font-size: 0.9rem; color: #a1a1aa;
        }
        details.deep-dive summary:hover { color: white; }
        details.deep-dive summary::after {
            content: '+'; font-size: 1.2rem; font-weight: 300; transition: transform 0.3s;
        }
        details.deep-dive[open] summary::after { transform: rotate(45deg); }
        .deep-dive-content {
            padding: 1.5rem; border-top: 1px solid rgba(255,255,255,0.05);
            color: #d4d4d8; line-height: 1.8; font-size: 0.95rem;
        }

        /* Data Viz Bars */
        .data-bar-container {
            width: 100%; height: 4px; background: rgba(255,255,255,0.1);
            border-radius: 2px; margin-top: 0.5rem; overflow: hidden;
        }
        .data-bar-fill {
            height: 100%; background: white; border-radius: 2px;
            position: relative;
        }
        .data-bar-fill::after {
            content: ''; position: absolute; top:0; right:0; bottom:0; width: 10px;
            background: linear-gradient(to right, transparent, white);
            filter: blur(2px);
        }

        /* Nav Blur */
        .nav-blur { backdrop-filter: blur(12px); background: rgba(5, 5, 5, 0.6); }

        /* 3D Canvas */
        #blackhole-canvas { width: 100%; height: 100%; }

        /* Animation Classes */
        .reveal-text { clip-path: polygon(0 100%, 100% 100%, 100% 100%, 0% 100%); transform: translateY(100%); }

        /* Custom Grids */
        .key-figures-grid {
            display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.75rem;
        }
        @media (min-width: 640px) { .key-figures-grid { grid-template-columns: repeat(4, 1fr); } }

        /* Watermarks */
        .watermark-huge {
            position: absolute; font-size: 20vw; font-family: 'Cinzel', serif;
            color: rgba(255,255,255,0.01); z-index: 0; pointer-events: none;
            line-height: 1; white-space: nowrap;
        }
    </style>
</head>
<body class="antialiased selection:bg-white/20 selection:text-white">

    <!-- Star Field -->
    <div class="star-field" id="starField"></div>

    <!-- Navigation -->
    <nav class="fixed top-0 left-0 w-full z-50 nav-blur border-b border-white/5 transition-all duration-300" id="navbar">
        <div class="max-w-[1400px] mx-auto px-6 h-20 flex items-center justify-between">
            <a href="#" class="flex items-center gap-3 group">
                <div class="w-8 h-8 rounded-full bg-gradient-to-br from-white to-zinc-600 flex items-center justify-center shadow-[0_0_15px_rgba(255,255,255,0.3)] group-hover:scale-110 transition-transform">
                    <div class="w-2 h-2 bg-black rounded-full"></div>
                </div>
                <div class="flex flex-col">
                    <span class="text-lg font-cinzel font-bold tracking-tight text-white leading-none">ZERO TO INFINITY</span>
                    <span class="text-[0.6rem] font-mono text-zinc-500 tracking-widest uppercase">Expanded Edition</span>
                </div>
            </a>

            <div class="hidden xl:flex items-center gap-8 text-xs font-medium tracking-widest uppercase text-zinc-500">
                <a href="#history" class="hover:text-white transition-colors relative group">History<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#anatomy" class="hover:text-white transition-colors relative group">Anatomy<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#deep-dive" class="hover:text-white transition-colors relative group">Deep Dive<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#formation" class="hover:text-white transition-colors relative group">Formation<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#thermodynamics" class="hover:text-white transition-colors relative group">Thermodynamics<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#evidence" class="hover:text-white transition-colors relative group">Evidence<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
                <a href="#frontier" class="hover:text-white transition-colors relative group">Frontier<span class="absolute -bottom-1 left-0 w-0 h-px bg-white transition-all group-hover:w-full"></span></a>
            </div>

            <button class="xl:hidden text-white p-2">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="relative min-h-screen flex items-center justify-center overflow-hidden">
        <!-- Background Shader/Image -->
        <div class="absolute inset-0 z-0">
             <div class="absolute inset-0 bg-gradient-to-b from-transparent via-[#050505]/50 to-[#050505] z-10"></div>
             <!-- Pollinations BG for Hero -->
             <img src="https://image.pollinations.ai/prompt/black%20hole%20singularity%20event%20horizon%20cinematic%208k%20dark%20void%20interstellar%20photorealistic?width=1920&height=1080&nologo=true"
                  class="w-full h-full object-cover opacity-60 scale-110 animate-pulse-slow" alt="Hero Background">
        </div>

        <div class="absolute inset-0 flex flex-col items-center justify-center text-center z-20 px-6 pt-20">
            <div class="reveal-container mb-6">
                <div class="reveal-text inline-flex items-center gap-3 px-6 py-2 rounded-full border border-white/10 bg-white/5 backdrop-blur-md">
                    <div class="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
                    <span class="text-xs font-bold text-zinc-300 tracking-[0.3em] uppercase font-mono">System Online: v2.0 Expanded</span>
                </div>
            </div>

            <h1 class="text-7xl md:text-[10rem] font-bold tracking-tighter leading-[0.85] mb-8 mix-blend-overlay">
                <div class="reveal-container"><span class="reveal-text block text-white">ZERO</span></div>
                <div class="reveal-container"><span class="reveal-text block text-zinc-600 text-4xl md:text-6xl my-4 font-light tracking-[0.5em] font-sans">TO</span></div>
                <div class="reveal-container"><span class="reveal-text block text-silver-gradient">INFINITY</span></div>
            </h1>

            <div class="reveal-container mb-12">
                <p class="reveal-text text-lg md:text-xl text-zinc-400 max-w-3xl font-light leading-relaxed mx-auto">
                    The ultimate comprehensive treatise on black hole physics. <br class="hidden md:block"/>
                    From Newtonian dark stars to the holographic principle and quantum gravity.
                </p>
            </div>

            <div class="flex flex-col sm:flex-row items-center gap-6 opacity-0" id="hero-buttons">
                <a href="#history" class="group flex items-center gap-3 bg-white text-black px-10 py-5 rounded-full font-bold tracking-wide hover:bg-zinc-200 transition-all shadow-[0_0_30px_-5px_rgba(255,255,255,0.4)]">
                    INITIATE SEQUENCE
                    <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                </a>
            </div>
        </div>
    </section>

    <!-- Infinite Marquee -->
    <div class="w-full overflow-hidden bg-[#050505] border-y border-white/5 py-4 relative z-20">
        <div class="flex w-max animate-[scroll_40s_linear_infinite]">
            <div class="flex gap-12 px-6">
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">EVENT HORIZON</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SINGULARITY</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">ERGOSPHERE</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SPAGHETTIFICATION</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SCHWARZSCHILD METRIC</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">HAWKING RADIATION</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">INFORMATION PARADOX</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">GRAVITATIONAL WAVES</span>
            </div>
            <div class="flex gap-12 px-6">
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">EVENT HORIZON</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SINGULARITY</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">ERGOSPHERE</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SPAGHETTIFICATION</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">SCHWARZSCHILD METRIC</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">HAWKING RADIATION</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">INFORMATION PARADOX</span>
                <span class="text-xs font-cinzel tracking-[0.3em] text-zinc-600">GRAVITATIONAL WAVES</span>
            </div>
        </div>
    </div>
"""

write_index(part1)
