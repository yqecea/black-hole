
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

# PART 2: MODULE 1 (HISTORY) - Expanded
# Features: Horizontal Timeline, Vertical Expansion (Michell, Einstein, Schwarzschild)
# Molecular Rule: Intro + Deep Dive + 4 Cards + Data Viz

part2 = """
    <!-- MODULE 1: HISTORICAL FOUNDATION -->
    <section id="history" class="py-32 relative border-t border-white/5 overflow-hidden">
        <!-- Background -->
        <div class="absolute inset-0 w-full h-full z-0 opacity-20 pointer-events-none">
             <img src="https://image.pollinations.ai/prompt/vintage%20astronomy%20diagrams%20parchment%20black%20hole%20history%20cinematic%208k?width=1920&height=1080&nologo=true" class="w-full h-full object-cover mix-blend-screen" alt="History BG">
             <div class="absolute inset-0 bg-gradient-to-b from-[#050505] via-transparent to-[#050505]"></div>
        </div>

        <div class="max-w-[1400px] mx-auto px-6 relative z-10">
            <!-- Header -->
            <div class="flex items-end justify-between mb-16 border-b border-white/10 pb-8">
                <div>
                    <div class="text-xs font-mono text-zinc-500 mb-4 tracking-widest">MODULE 01</div>
                    <h2 class="text-5xl md:text-7xl font-semibold tracking-tight text-white mb-2">Historical Foundation</h2>
                    <p class="text-zinc-400 max-w-xl text-lg font-light">The evolution of an impossible idea: from "Dark Stars" to Physical Reality.</p>
                </div>
                <div class="hidden md:block text-right">
                    <div class="text-6xl font-cinzel text-white/5 font-bold">1783—2019</div>
                </div>
            </div>

            <!-- NEW: Horizontal Scroll Timeline -->
            <div class="mb-32">
                <h3 class="text-sm font-mono text-zinc-400 mb-6 uppercase tracking-widest flex items-center gap-2">
                    <i data-lucide="clock" class="w-4 h-4"></i> Chronological Overview
                </h3>
                <div class="horizontal-timeline-container">
                    <div class="horizontal-timeline">
                        <!-- 1783 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">1783</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">John Michell</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">First proposes "dark stars" where escape velocity exceeds the speed of light using Newtonian physics.</p>
                        </div>
                        <!-- 1915 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">1915</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">General Relativity</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">Einstein publishes the field equations, linking gravity to spacetime curvature.</p>
                        </div>
                        <!-- 1916 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">1916</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">Schwarzschild</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">First exact solution derived. Discovers the "Magic Circle" (Event Horizon) radius.</p>
                        </div>
                         <!-- 1939 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">1939</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">Oppenheimer-Snyder</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">Calculates that massive stars can indeed collapse indefinitely into a singularity.</p>
                        </div>
                        <!-- 1974 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">1974</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">Hawking Radiation</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">Hawking applies quantum field theory, proving black holes emit radiation and evaporate.</p>
                        </div>
                        <!-- 2015 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">2015</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">LIGO Detection</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">First direct detection of gravitational waves from a binary black hole merger.</p>
                        </div>
                        <!-- 2019 -->
                        <div class="timeline-card group">
                            <div class="text-3xl font-cinzel text-white mb-2 group-hover:text-silver-gradient transition-colors">2019</div>
                            <h4 class="text-sm font-bold text-zinc-300 uppercase tracking-wider mb-2">EHT Image</h4>
                            <p class="text-xs text-zinc-500 leading-relaxed">Humanity captures the first radio image of M87*'s shadow.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Vertical Deep Dives -->
            <div class="space-y-32">

                <!-- 1. John Michell -->
                <div class="grid lg:grid-cols-2 gap-16 items-start">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-zinc-300 mb-6">
                            <span class="w-2 h-2 rounded-full bg-zinc-500"></span> 1783: The Corpuscular Theory
                        </div>
                        <h3 class="text-4xl font-cinzel text-white mb-6">Michell's Dark Stars</h3>

                        <!-- Intro -->
                        <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                            Long before Einstein, the Reverend John Michell conceived of a body so massive that its escape velocity would exceed the speed of light. Writing to the Royal Society in 1783, he used Newton's corpuscular theory of light—which treated photons as having mass—to argue that light emitted from such a star would be dragged back by its own gravity.
                        </p>

                        <!-- Deep Dive Accordion -->
                        <details class="deep-dive mb-8">
                            <summary>DEEP DIVE: The Newtonian Calculation</summary>
                            <div class="deep-dive-content">
                                <p class="mb-4">
                                    Michell's calculation was surprisingly accurate despite the incorrect physical premise (light does not have mass in the Newtonian sense). He equated kinetic energy with gravitational potential energy:
                                </p>
                                <div class="bg-black/30 p-4 rounded border border-white/10 font-mono text-sm text-center mb-4 text-zinc-300">
                                    ½mv² = GMm/r  →  v = √(2GM/r)
                                </div>
                                <p>
                                    Setting v = c (speed of light), he found that a star with the same density as the Sun but 500 times the diameter would be invisible. The "corpuscles" of light would shoot up, slow down, stop, and fall back to the surface like a thrown stone. While General Relativity would later discard the idea of light slowing down (c is constant), the radius he calculated is exactly the Schwarzschild radius derived 133 years later.
                                </p>
                            </div>
                        </details>

                        <!-- Data Viz -->
                        <div class="mb-8">
                            <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                                <span>CONCEPTUAL ACCURACY</span>
                                <span>45%</span>
                            </div>
                            <div class="data-bar-container">
                                <div class="data-bar-fill" style="width: 45%"></div>
                            </div>
                        </div>

                        <!-- Key Figures Grid -->
                        <div class="key-figures-grid">
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Peer</div>
                                <div class="font-bold text-white text-sm">Cavendish</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Concept</div>
                                <div class="font-bold text-white text-sm">Escape Velocity</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Paper</div>
                                <div class="font-bold text-white text-sm">Phil. Trans.</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Successor</div>
                                <div class="font-bold text-white text-sm">Laplace</div>
                            </div>
                        </div>
                    </div>

                    <div class="relative">
                        <div class="glass-card p-2 rounded-2xl border-white/10">
                             <img src="https://image.pollinations.ai/prompt/18th%20century%20diagram%20of%20a%20dark%20star%20newtonian%20physics%20parchment%20vintage%20science%20cinematic?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover opacity-80" alt="Michell Diagram">
                             <div class="absolute bottom-6 left-6 right-6 p-6 glass-card bg-black/80 rounded-xl border border-white/10">
                                <div class="font-serif italic text-zinc-300">"Light attracted by gravity... made to return towards it."</div>
                             </div>
                        </div>
                    </div>
                </div>

                <!-- 2. Einstein -->
                <div class="grid lg:grid-cols-2 gap-16 items-start">
                    <div class="lg:order-2">
                         <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-zinc-300 mb-6">
                            <span class="w-2 h-2 rounded-full bg-zinc-500"></span> 1915: General Relativity
                        </div>
                        <h3 class="text-4xl font-cinzel text-white mb-6">Einstein's Revolution</h3>

                        <!-- Intro -->
                        <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                            In November 1915, Albert Einstein presented his field equations to the Prussian Academy of Sciences. He dismantled the Newtonian framework of fixed space and absolute time. Instead, he proposed a dynamic, four-dimensional fabric called spacetime, which is warped by the presence of mass and energy. Gravity is not a force, but a geometric feature.
                        </p>

                        <!-- Deep Dive Accordion -->
                        <details class="deep-dive mb-8">
                            <summary>DEEP DIVE: The Field Equations</summary>
                            <div class="deep-dive-content">
                                <p class="mb-4">
                                    The equation <strong>G<sub>μν</sub> = 8πT<sub>μν</sub></strong> is deceptive in its brevity. It represents a system of 10 non-linear partial differential equations.
                                </p>
                                <ul class="list-disc pl-5 space-y-2 mb-4 text-zinc-400">
                                    <li><strong>G<sub>μν</sub> (Einstein Tensor):</strong> Describes the curvature of space and time.</li>
                                    <li><strong>T<sub>μν</sub> (Stress-Energy Tensor):</strong> Describes the density and flux of energy and momentum.</li>
                                </ul>
                                <p>
                                    This framework predicted that light follows the curvature of space (geodesics). Near a massive object, these paths bend. If the mass is concentrated enough, the curvature becomes so steep that the geodesics loop back on themselves—trapping light not by pulling it back, but by bending the road it travels on.
                                </p>
                            </div>
                        </details>

                        <!-- Data Viz -->
                        <div class="mb-8">
                            <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                                <span>THEORY VERIFICATION</span>
                                <span>99.9%</span>
                            </div>
                            <div class="data-bar-container">
                                <div class="data-bar-fill" style="width: 99.9%"></div>
                            </div>
                        </div>

                         <!-- Key Figures Grid -->
                        <div class="key-figures-grid">
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Key Insight</div>
                                <div class="font-bold text-white text-sm">Equivalence</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Tool</div>
                                <div class="font-bold text-white text-sm">Tensors</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Rival</div>
                                <div class="font-bold text-white text-sm">Hilbert</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Legacy</div>
                                <div class="font-bold text-white text-sm">Spacetime</div>
                            </div>
                        </div>
                    </div>

                    <div class="relative lg:order-1">
                        <div class="glass-card p-2 rounded-2xl border-white/10">
                             <img src="https://image.pollinations.ai/prompt/albert%20einstein%20chalkboard%20general%20relativity%20formulas%20spacetime%20grid%20warped%20cinematic%20photorealistic?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover opacity-80" alt="Einstein">
                             <div class="absolute bottom-6 left-6 right-6 p-6 glass-card bg-black/80 rounded-xl border border-white/10">
                                <div class="font-serif italic text-zinc-300">"Matter tells space how to curve. Space tells matter how to move."</div>
                             </div>
                        </div>
                    </div>
                </div>

                <!-- 3. Schwarzschild -->
                <div class="grid lg:grid-cols-2 gap-16 items-start">
                    <div>
                         <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/5 border border-white/10 text-xs font-mono text-zinc-300 mb-6">
                            <span class="w-2 h-2 rounded-full bg-zinc-500"></span> 1916: The Exact Solution
                        </div>
                        <h3 class="text-4xl font-cinzel text-white mb-6">Schwarzschild's Limit</h3>

                        <!-- Intro -->
                        <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                            Serving on the Russian front during WWI, Karl Schwarzschild managed to solve Einstein's equations for a non-rotating spherical mass. He sent the letter to Einstein just months before dying of an autoimmune disease. His solution contained a singularity—a point where the math blew up—surrounded by a spherical boundary now known as the Event Horizon.
                        </p>

                        <!-- Deep Dive Accordion -->
                        <details class="deep-dive mb-8">
                            <summary>DEEP DIVE: The Mathematical Singularity</summary>
                            <div class="deep-dive-content">
                                <p class="mb-4">
                                    The metric contains two critical points where the coefficient goes to infinity or zero:
                                </p>
                                <ul class="list-disc pl-5 space-y-2 mb-4 text-zinc-400">
                                    <li><strong>r = 0:</strong> The physical singularity. Curvature is infinite. Physics breaks down.</li>
                                    <li><strong>r = 2GM/c²:</strong> The coordinate singularity. Originally thought to be physical, later proven (by Eddington and Finkelstein) to be an illusion of the coordinate system choice. It is a one-way membrane.</li>
                                </ul>
                                <p>
                                    This radius is shockingly small. To turn Earth into a black hole, you would need to compress its entire mass into a marble of radius 9mm. For the Sun, it is 3km.
                                </p>
                            </div>
                        </details>

                        <!-- Data Viz -->
                        <div class="mb-8">
                            <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                                <span>RADIUS COMPRESSION RATIO</span>
                                <span>1 : 100,000,000</span>
                            </div>
                            <div class="data-bar-container">
                                <div class="data-bar-fill" style="width: 15%"></div>
                            </div>
                        </div>

                         <!-- Key Figures Grid -->
                        <div class="key-figures-grid">
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Context</div>
                                <div class="font-bold text-white text-sm">WWI Front</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Discovery</div>
                                <div class="font-bold text-white text-sm">Exact Solution</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Radius</div>
                                <div class="font-bold text-white text-sm">2GM/c²</div>
                            </div>
                            <div class="glass-card p-4 rounded-lg text-center">
                                <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Fate</div>
                                <div class="font-bold text-white text-sm">Tragedy</div>
                            </div>
                        </div>
                    </div>

                    <div class="relative">
                        <div class="glass-card p-2 rounded-2xl border-white/10">
                             <img src="https://image.pollinations.ai/prompt/karl%20schwarzschild%20ww1%20trench%20physics%20letters%20sepia%20cinematic%20dramatic%20lighting?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover opacity-80" alt="Schwarzschild">
                             <div class="absolute bottom-6 left-6 right-6 p-6 glass-card bg-black/80 rounded-xl border border-white/10">
                                <div class="font-serif italic text-zinc-300">"The war treated me kindly enough to allow me this walk in the land of your ideas."</div>
                             </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

append_to_index(part2)
