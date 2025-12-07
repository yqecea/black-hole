
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

# PART 4: MODULE 3 (DEEP DIVE: PHYSICS & MATH)
part4 = """
    <!-- MODULE 3: DEEP DIVE (PHYSICS & MATH) -->
    <section id="deep-dive" class="py-32 relative border-t border-white/5 overflow-hidden">
        <div class="absolute inset-0 z-0 opacity-10 pointer-events-none">
            <img src="https://image.pollinations.ai/prompt/blackboard%20physics%20equations%20general%20relativity%20calculus%20tensor%20math%20dark%20cinematic?width=1920&height=1080&nologo=true" class="w-full h-full object-cover" alt="Math BG">
        </div>

        <div class="max-w-[1400px] mx-auto px-6 relative z-10">
             <div class="flex items-center gap-6 mb-20">
                <span class="text-8xl font-cinzel text-white/5 font-bold absolute -left-6 -top-10 select-none">03</span>
                <div class="relative">
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] mb-2 font-semibold">Module Three</div>
                    <h2 class="text-5xl md:text-6xl font-semibold tracking-tight">Deep Dive: Physics &amp; Math</h2>
                </div>
            </div>

            <!-- Existing Intro Expanded -->
            <div class="max-w-4xl mb-24">
                <p class="text-xl text-zinc-300 leading-relaxed font-light mb-8 text-justify-academic">
                    To truly understand black holes, we must abandon Newtonian intuition. We enter the realm of Differential Geometry, where gravity is the curvature of the spacetime manifold itself. The Schwarzschild metric is the first solution to Einstein's field equations, describing the geometry of spacetime surrounding a spherical mass.
                </p>
                <div class="equation-box p-8 rounded-xl text-center shadow-2xl bg-black/50 backdrop-blur-xl border border-white/10">
                    <div class="text-2xl md:text-4xl text-white font-serif italic mb-4">
                         ds² = -(1 - <span class="text-zinc-400">R<sub>s</sub></span>/r)c²dt² + (1 - <span class="text-zinc-400">R<sub>s</sub></span>/r)<sup>-1</sup>dr² + r²dΩ²
                    </div>
                    <div class="text-xs text-zinc-500 font-mono uppercase tracking-widest">The Schwarzschild Line Element</div>
                </div>
            </div>

            <!-- NEW: GLOSSARY GRID (12 ITEMS) -->
            <div class="mb-32">
                <h3 class="text-2xl font-cinzel text-white mb-8 flex items-center gap-3">
                    <i data-lucide="book" class="w-5 h-5 text-zinc-500"></i> Glossary of Terms
                </h3>
                <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                    <!-- 1 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Concept</div>
                        <h4 class="text-white font-bold mb-2">Manifold</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">A topological space that locally resembles Euclidean space near each point.</p>
                    </div>
                    <!-- 2 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Math</div>
                        <h4 class="text-white font-bold mb-2">Geodesic</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">The shortest path between two points in a curved space. Light follows these.</p>
                    </div>
                    <!-- 3 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Object</div>
                        <h4 class="text-white font-bold mb-2">Metric Tensor</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">A function that defines distance and angles at every point in spacetime.</p>
                    </div>
                    <!-- 4 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Limit</div>
                        <h4 class="text-white font-bold mb-2">TOV Limit</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Tolman-Oppenheimer-Volkoff. Max mass of a neutron star (~2.2M☉) before collapse.</p>
                    </div>
                    <!-- 5 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Effect</div>
                        <h4 class="text-white font-bold mb-2">Frame Dragging</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Rotating mass drags spacetime with it. Also known as the Lense-Thirring effect.</p>
                    </div>
                    <!-- 6 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Region</div>
                        <h4 class="text-white font-bold mb-2">ISCO</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Innermost Stable Circular Orbit. The closest matter can orbit safely.</p>
                    </div>
                    <!-- 7 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Radiation</div>
                        <h4 class="text-white font-bold mb-2">Bremsstrahlung</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">"Braking radiation" emitted by decelerating charged particles in the disk.</p>
                    </div>
                    <!-- 8 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Structure</div>
                        <h4 class="text-white font-bold mb-2">Jet</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Relativistic beam of matter ejected along the rotation axis.</p>
                    </div>
                    <!-- 9 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Phenomenon</div>
                        <h4 class="text-white font-bold mb-2">Tidal Force</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Differential gravity force stretching an object. Source of Spaghettification.</p>
                    </div>
                    <!-- 10 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Light</div>
                        <h4 class="text-white font-bold mb-2">Gravitational Lens</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Bending of light from a distant source around a massive object.</p>
                    </div>
                    <!-- 11 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Effect</div>
                        <h4 class="text-white font-bold mb-2">Redshift</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Light losing energy as it climbs out of a gravity well, shifting red.</p>
                    </div>
                    <!-- 12 -->
                    <div class="glass-card p-4 rounded-lg hover:bg-white/5 transition-colors">
                        <div class="text-xs text-zinc-500 uppercase mb-1">Math</div>
                        <h4 class="text-white font-bold mb-2">Tensor</h4>
                        <p class="text-[10px] text-zinc-400 leading-relaxed">Geometric object describing linear relations between vectors/scalars.</p>
                    </div>
                </div>
            </div>

            <!-- SUBSECTION 1: TIME DILATION -->
            <div class="grid lg:grid-cols-2 gap-16 items-start mb-32 border-t border-white/5 pt-16">
                <div>
                     <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 border border-blue-500/20 text-xs font-mono text-blue-200 mb-6">
                        <i data-lucide="clock" class="w-3 h-3"></i> Temporal Mechanics
                    </div>
                    <h3 class="text-4xl font-cinzel text-white mb-6">Gravitational Time Dilation</h3>

                    <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                        Near a massive body, time itself flows slower relative to a distant observer. This is not an illusion or a mechanical failure of clocks; it is a fundamental property of the universe. The closer you are to the event horizon, the slower you move through time. At the horizon itself, time stands still from the perspective of the outside universe.
                    </p>

                    <details class="deep-dive mb-8">
                        <summary>DEEP DIVE: The Twin Paradox Extreme</summary>
                        <div class="deep-dive-content">
                            <p class="mb-4">
                                The formula for time dilation near a Schwarzschild black hole is:
                            </p>
                            <div class="bg-black/30 p-4 rounded border border-white/10 font-mono text-sm text-center mb-4 text-zinc-300">
                                t' = t * √(1 - Rs/r)
                            </div>
                            <p>
                                If you were to hover just outside the event horizon of a supermassive black hole for what felt like one hour, millions of years could pass in the outside universe. This effect allows for one-way time travel into the future. However, the energy required to maintain a stationary position there would be infinite.
                            </p>
                        </div>
                    </details>

                    <div class="mb-8">
                        <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                            <span>TIME RATE AT HORIZON (Relative to Earth)</span>
                            <span>0%</span>
                        </div>
                        <div class="data-bar-container">
                            <div class="data-bar-fill" style="width: 0%"></div>
                        </div>
                    </div>

                     <div class="key-figures-grid">
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Film</div>
                            <div class="font-bold text-white text-sm">Interstellar</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Concept</div>
                            <div class="font-bold text-white text-sm">Relativity</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Test</div>
                            <div class="font-bold text-white text-sm">GPS Satellites</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Limit</div>
                            <div class="font-bold text-white text-sm">Infinite</div>
                        </div>
                    </div>
                </div>

                <div class="relative">
                    <div class="glass-card p-2 rounded-2xl border-white/10 rotate-1 hover:rotate-0 transition-transform duration-500">
                         <img src="https://image.pollinations.ai/prompt/warped%20clocks%20melting%20time%20near%20black%20hole%20event%20horizon%20surreal%20dali%20style%20cinematic%20photorealistic?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover" alt="Time Dilation">
                    </div>
                </div>
            </div>

            <!-- SUBSECTION 2: SPAGHETTIFICATION -->
            <div class="grid lg:grid-cols-2 gap-16 items-start mb-32 border-t border-white/5 pt-16">
                 <div class="relative lg:order-2">
                     <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-500/10 border border-red-500/20 text-xs font-mono text-red-200 mb-6">
                        <i data-lucide="scissors" class="w-3 h-3"></i> Tidal Forces
                    </div>
                    <h3 class="text-4xl font-cinzel text-white mb-6">Spaghettification</h3>

                    <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                        Technically known as the tidal effect, this is the stretching of an object due to the difference in gravitational force between its head and its feet. In a small black hole, the gradient is so steep that you would be ripped apart into a stream of atoms long before crossing the horizon.
                    </p>

                    <details class="deep-dive mb-8">
                        <summary>DEEP DIVE: The Tidal Tensor</summary>
                        <div class="deep-dive-content">
                            <p class="mb-4">
                                The tidal force is proportional to M/r³. This means smaller black holes actually have <em>stronger</em> tidal forces at their horizons than supermassive ones.
                            </p>
                            <p>
                                For a stellar-mass black hole, the tidal force at the horizon is enough to shred steel. For a supermassive black hole like M87*, the horizon is so far away (billions of km) that the tidal forces are negligible at the crossing point. You could cross the event horizon of a supermassive black hole without feeling anything unusual—until you approached the singularity.
                            </p>
                        </div>
                    </details>

                    <div class="mb-8">
                        <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                            <span>STRUCTURAL INTEGRITY (Stellar Mass BH)</span>
                            <span>CRITICAL FAILURE</span>
                        </div>
                        <div class="data-bar-container">
                            <div class="data-bar-fill bg-red-500" style="width: 1%"></div>
                        </div>
                    </div>

                     <div class="key-figures-grid">
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Term</div>
                            <div class="font-bold text-white text-sm">Hawking</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Cause</div>
                            <div class="font-bold text-white text-sm">Gradient</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Outcome</div>
                            <div class="font-bold text-white text-sm">Atomization</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Geometry</div>
                            <div class="font-bold text-white text-sm">Vertical</div>
                        </div>
                    </div>
                </div>

                <div class="relative lg:order-1">
                    <div class="glass-card p-2 rounded-2xl border-white/10 -rotate-1 hover:rotate-0 transition-transform duration-500">
                         <img src="https://image.pollinations.ai/prompt/astronaut%20being%20stretched%20into%20spaghetti%20black%20hole%20tidal%20forces%20horror%20sci-fi%20cinematic%20dark?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover" alt="Spaghettification">
                    </div>
                </div>
            </div>

            <!-- SUBSECTION 3: REDSHIFT -->
            <div class="grid lg:grid-cols-2 gap-16 items-start border-t border-white/5 pt-16">
                <div>
                     <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-500/10 border border-orange-500/20 text-xs font-mono text-orange-200 mb-6">
                        <i data-lucide="arrow-down-right" class="w-3 h-3"></i> Spectral Shift
                    </div>
                    <h3 class="text-4xl font-cinzel text-white mb-6">Gravitational Redshift</h3>

                    <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                        As light attempts to climb out of the gravitational well of a black hole, it loses energy. Since the speed of light is constant, this loss of energy manifests as a decrease in frequency—a shift towards the red end of the spectrum.
                    </p>

                    <details class="deep-dive mb-8">
                        <summary>DEEP DIVE: Infinite Redshift</summary>
                        <div class="deep-dive-content">
                            <p class="mb-4">
                                At the event horizon, the redshift becomes infinite. A blue laser pointer shone outward from the horizon would be redshifted so far that its wavelength would exceed the size of the observable universe.
                            </p>
                            <p>
                                This is why black holes are black. It's not just that light can't escape; it's that any light emitted from just above the horizon is redshifted into invisibility (radio waves and beyond) by the time it reaches us.
                            </p>
                        </div>
                    </details>

                    <div class="mb-8">
                        <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                            <span>WAVELENGTH SHIFT</span>
                            <span>EXPONENTIAL</span>
                        </div>
                        <div class="data-bar-container">
                            <div class="data-bar-fill bg-orange-500" style="width: 85%"></div>
                        </div>
                    </div>

                     <div class="key-figures-grid">
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Exp</div>
                            <div class="font-bold text-white text-sm">Pound-Rebka</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Color</div>
                            <div class="font-bold text-white text-sm">Infrared</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Energy</div>
                            <div class="font-bold text-white text-sm">Loss</div>
                        </div>
                        <div class="glass-card p-4 rounded-lg text-center">
                            <div class="text-xs text-zinc-500 uppercase tracking-wider mb-1">Use</div>
                            <div class="font-bold text-white text-sm">Mapping</div>
                        </div>
                    </div>
                </div>

                <div class="relative">
                    <div class="glass-card p-2 rounded-2xl border-white/10 rotate-1 hover:rotate-0 transition-transform duration-500">
                         <img src="https://image.pollinations.ai/prompt/spectrum%20of%20light%20shifting%20to%20red%20gravity%20well%20physics%20visualization%20abstract%20cinematic?width=800&height=1000&nologo=true" class="rounded-xl w-full object-cover" alt="Redshift">
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

append_to_index(part4)
