
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

# PART 3: MODULE 2 (ANATOMY) - Dashboard Layout
part3 = """
    <!-- MODULE 2: ANATOMY DASHBOARD -->
    <section id="anatomy" class="py-20 relative border-t border-white/5 bg-[#050505]">
        <div class="max-w-[1600px] mx-auto px-6 relative z-10">
            <!-- Header -->
            <div class="flex items-center gap-6 mb-12">
                <span class="text-6xl font-cinzel text-white/5 font-bold select-none">02</span>
                <div>
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] font-semibold">Structural Analysis</div>
                    <h2 class="text-4xl font-semibold tracking-tight text-white">Anatomy Dashboard</h2>
                </div>
            </div>

            <!-- 3-Column Dashboard -->
            <div class="dashboard-grid">

                <!-- LEFT COLUMN: PHYSICS DATA -->
                <div class="space-y-6">
                    <div class="glass-card p-6 rounded-xl border-l-2 border-l-blue-500/50">
                        <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-4">Metric Parameters</h4>
                        <div class="space-y-4 font-mono text-xs">
                            <div class="flex justify-between items-center border-b border-white/5 pb-2">
                                <span class="text-zinc-500">Mass (M)</span>
                                <span class="text-white">Variable</span>
                            </div>
                            <div class="flex justify-between items-center border-b border-white/5 pb-2">
                                <span class="text-zinc-500">Spin (J)</span>
                                <span class="text-white">0 ≤ a ≤ 1</span>
                            </div>
                            <div class="flex justify-between items-center border-b border-white/5 pb-2">
                                <span class="text-zinc-500">Charge (Q)</span>
                                <span class="text-white">~ 0 (Neutral)</span>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-4">Critical Radii</h4>
                        <div class="space-y-4">
                            <div>
                                <div class="flex justify-between text-xs text-zinc-400 mb-1">
                                    <span>Singularity</span>
                                    <span class="font-mono text-white">r = 0</span>
                                </div>
                                <div class="h-1 bg-white/10 rounded overflow-hidden"><div class="h-full bg-red-500 w-full"></div></div>
                            </div>
                            <div>
                                <div class="flex justify-between text-xs text-zinc-400 mb-1">
                                    <span>Event Horizon</span>
                                    <span class="font-mono text-white">r = 2M</span>
                                </div>
                                <div class="h-1 bg-white/10 rounded overflow-hidden"><div class="h-full bg-white w-2/3"></div></div>
                            </div>
                            <div>
                                <div class="flex justify-between text-xs text-zinc-400 mb-1">
                                    <span>Photon Sphere</span>
                                    <span class="font-mono text-white">r = 3M</span>
                                </div>
                                <div class="h-1 bg-white/10 rounded overflow-hidden"><div class="h-full bg-yellow-500 w-full"></div></div>
                            </div>
                             <div>
                                <div class="flex justify-between text-xs text-zinc-400 mb-1">
                                    <span>ISCO (Stable Orbit)</span>
                                    <span class="font-mono text-white">r = 6M</span>
                                </div>
                                <div class="h-1 bg-white/10 rounded overflow-hidden"><div class="h-full bg-blue-500 w-full"></div></div>
                            </div>
                        </div>
                    </div>

                    <div class="glass-card p-6 rounded-xl">
                         <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-4">No-Hair Theorem</h4>
                         <p class="text-xs text-zinc-400 leading-relaxed mb-4">
                            "Black holes have no hair." A stationary black hole is completely described by Mass, Spin, and Charge. All other information (baryon number, lepton number, shape) is radiated away during formation.
                         </p>
                         <div class="grid grid-cols-3 gap-2">
                             <div class="bg-white/5 p-2 rounded text-center border border-white/5">
                                 <div class="text-lg font-serif">M</div>
                             </div>
                             <div class="bg-white/5 p-2 rounded text-center border border-white/5">
                                 <div class="text-lg font-serif">J</div>
                             </div>
                             <div class="bg-white/5 p-2 rounded text-center border border-white/5">
                                 <div class="text-lg font-serif">Q</div>
                             </div>
                         </div>
                    </div>
                </div>

                <!-- CENTER COLUMN: VISUAL ENGINE (STICKY) -->
                <div class="relative min-h-[500px] lg:min-h-auto">
                    <div class="sticky-center glass-card rounded-2xl overflow-hidden shadow-2xl shadow-black/50 border border-white/10">
                        <div id="blackhole-wrapper" class="w-full h-full relative bg-radial-gradient">
                            <!-- Canvas injected here -->
                            <canvas id="blackhole-canvas"></canvas>

                            <!-- Overlay UI -->
                            <div class="absolute top-4 left-4 flex gap-2">
                                <span class="px-2 py-1 bg-red-500/20 border border-red-500/30 text-[10px] text-red-200 uppercase tracking-wider rounded">Live Sim</span>
                                <span class="px-2 py-1 bg-white/5 border border-white/10 text-[10px] text-zinc-400 uppercase tracking-wider rounded">Kerr Metric</span>
                            </div>
                            <div class="absolute bottom-6 w-full text-center pointer-events-none">
                                <p class="text-[10px] text-zinc-500 uppercase tracking-[0.3em]">Interactive Model</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- RIGHT COLUMN: EXPLANATIONS -->
                <div class="space-y-6">
                    <!-- Feature 1 -->
                    <div class="glass-card p-6 rounded-xl group hover:bg-white/5 transition-colors cursor-default">
                        <div class="flex items-center justify-between mb-3">
                            <h4 class="font-cinzel text-lg text-white group-hover:text-silver-gradient">The Event Horizon</h4>
                            <i data-lucide="circle" class="w-4 h-4 text-zinc-500"></i>
                        </div>
                        <p class="text-sm text-zinc-400 leading-relaxed mb-4">
                            The point of no return. Here, the escape velocity equals the speed of light. To an outside observer, an object falling in appears to freeze and fade (redshift) forever. To the object, they cross without drama.
                        </p>
                        <div class="h-px w-full bg-white/10 my-4"></div>
                        <div class="flex gap-4">
                            <div class="text-center">
                                <div class="text-[10px] text-zinc-500 uppercase">Temp</div>
                                <div class="text-xs font-mono text-white">~0 K</div>
                            </div>
                            <div class="text-center">
                                <div class="text-[10px] text-zinc-500 uppercase">Time</div>
                                <div class="text-xs font-mono text-white">Frozen</div>
                            </div>
                        </div>
                    </div>

                    <!-- Feature 2 -->
                    <div class="glass-card p-6 rounded-xl group hover:bg-white/5 transition-colors cursor-default">
                         <div class="flex items-center justify-between mb-3">
                            <h4 class="font-cinzel text-lg text-white group-hover:text-silver-gradient">The Photon Sphere</h4>
                            <i data-lucide="orbit" class="w-4 h-4 text-zinc-500"></i>
                        </div>
                        <p class="text-sm text-zinc-400 leading-relaxed mb-4">
                            Located at 1.5Rs (for non-rotating). Here, gravity is so strong that photons are forced into unstable circular orbits. If you stood here, you could see the back of your own head.
                        </p>
                        <div class="h-px w-full bg-white/10 my-4"></div>
                        <div class="text-[10px] text-zinc-500 uppercase mb-1">Orbit Stability</div>
                        <div class="w-full bg-white/10 h-1 rounded overflow-hidden"><div class="w-1/4 bg-red-500 h-full"></div></div>
                        <div class="text-[10px] text-red-400 mt-1">Highly Unstable</div>
                    </div>

                    <!-- Feature 3 -->
                    <div class="glass-card p-6 rounded-xl group hover:bg-white/5 transition-colors cursor-default">
                         <div class="flex items-center justify-between mb-3">
                            <h4 class="font-cinzel text-lg text-white group-hover:text-silver-gradient">The Ergosphere</h4>
                            <i data-lucide="refresh-cw" class="w-4 h-4 text-zinc-500"></i>
                        </div>
                        <p class="text-sm text-zinc-400 leading-relaxed mb-4">
                            Only in rotating (Kerr) black holes. A region outside the horizon where spacetime is dragged along with the rotation (frame-dragging). It is impossible to stand still here.
                        </p>
                        <div class="h-px w-full bg-white/10 my-4"></div>
                         <div class="flex justify-between items-center">
                             <span class="text-[10px] text-zinc-500 uppercase">Penrose Process</span>
                             <span class="text-xs text-green-400">Energy Extraction Possible</span>
                         </div>
                    </div>
                </div>
            </div>

            <!-- SINGULARITIES GRID -->
            <div class="mt-20">
                <h3 class="text-2xl font-cinzel text-white mb-8 border-b border-white/10 pb-4">Types of Singularities</h3>
                <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <!-- Card 1 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Schwarzschild</h4>
                        <p class="text-xs text-zinc-400 mb-4">Point-like singularity. Infinite density, zero volume. The classic result for non-rotating mass.</p>
                        <div class="w-full h-24 bg-black rounded border border-white/5 flex items-center justify-center relative overflow-hidden">
                             <div class="w-1 h-1 bg-white rounded-full shadow-[0_0_20px_white]"></div>
                        </div>
                    </div>
                    <!-- Card 2 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Ring (Kerr)</h4>
                        <p class="text-xs text-zinc-400 mb-4">A one-dimensional ring due to angular momentum. Theoretically traversable in some math models.</p>
                         <div class="w-full h-24 bg-black rounded border border-white/5 flex items-center justify-center relative overflow-hidden">
                             <div class="w-8 h-2 border border-white rounded-full shadow-[0_0_10px_white]"></div>
                        </div>
                    </div>
                    <!-- Card 3 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Naked</h4>
                        <p class="text-xs text-zinc-400 mb-4">A singularity without an event horizon. Prohibited by the Cosmic Censorship Hypothesis.</p>
                         <div class="w-full h-24 bg-black rounded border border-white/5 flex items-center justify-center relative overflow-hidden">
                             <div class="w-1 h-1 bg-red-500 rounded-full shadow-[0_0_20px_red] animate-pulse"></div>
                        </div>
                    </div>
                    <!-- Card 4 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Coordinate</h4>
                        <p class="text-xs text-zinc-400 mb-4">Not a physical singularity, but a flaw in the math (e.g., at the Event Horizon in Schwarzschild coords).</p>
                    </div>
                    <!-- Card 5 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Big Bang</h4>
                        <p class="text-xs text-zinc-400 mb-4">A past singularity. Similar mathematics, but inverted time direction (expansion vs collapse).</p>
                    </div>
                    <!-- Card 6 -->
                    <div class="glass-card p-6 rounded-xl">
                        <h4 class="text-white font-bold mb-2">Big Crunch</h4>
                        <p class="text-xs text-zinc-400 mb-4">A future singularity. The potential end state of a closed universe collapsing.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

append_to_index(part3)
