
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

# PART 5: MODULE 4 (FORMATION) & MODULE 5 (THERMODYNAMICS)
part5 = """
    <!-- MODULE 4: FORMATION & EVOLUTION -->
    <section id="formation" class="py-32 relative border-t border-white/5 overflow-hidden">
        <div class="absolute inset-0 z-0 opacity-20 pointer-events-none">
            <img src="https://image.pollinations.ai/prompt/supernova%20explosion%20star%20collapse%20nebula%20cosmic%20dust%20cinematic%208k%20photorealistic?width=1920&height=1080&nologo=true" class="w-full h-full object-cover mix-blend-lighten" alt="Formation BG">
        </div>

        <div class="max-w-[1400px] mx-auto px-6 relative z-10">
             <div class="flex items-center gap-6 mb-20">
                <span class="text-8xl font-cinzel text-white/5 font-bold absolute -left-6 -top-10 select-none">04</span>
                <div class="relative">
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] mb-2 font-semibold">Module Four</div>
                    <h2 class="text-5xl md:text-6xl font-semibold tracking-tight">Formation &amp; Evolution</h2>
                </div>
            </div>

            <div class="space-y-32">
                <!-- 1. Stellar Mass -->
                <div class="grid lg:grid-cols-2 gap-16 items-start">
                    <div>
                        <h3 class="text-3xl font-cinzel text-white mb-6">Stellar Mass Black Holes</h3>
                        <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                            The most common type of black hole forms from the death of massive stars. When a star at least 20 times more massive than our Sun runs out of fuel, thermal pressure can no longer support its weight. The core collapses in a fraction of a second, causing a supernova explosion while the center crushes down into a singularity.
                        </p>
                        <details class="deep-dive mb-8">
                            <summary>DEEP DIVE: The TOV Limit</summary>
                            <div class="deep-dive-content">
                                <p class="mb-4">
                                    The Tolman-Oppenheimer-Volkoff limit defines the maximum mass of a neutron star (approx 2.17 solar masses). If the remnant core exceeds this mass, neutron degeneracy pressure fails, and total collapse is inevitable.
                                </p>
                            </div>
                        </details>
                        <div class="mb-8">
                            <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                                <span>POPULATION ESTIMATE (Milky Way)</span>
                                <span>~100,000,000</span>
                            </div>
                            <div class="data-bar-container">
                                <div class="data-bar-fill" style="width: 20%"></div>
                            </div>
                        </div>
                        <div class="key-figures-grid">
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Source</div><div class="font-bold text-white text-sm">Supernova</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Mass</div><div class="font-bold text-white text-sm">3-100 M☉</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Example</div><div class="font-bold text-white text-sm">Cygnus X-1</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Rate</div><div class="font-bold text-white text-sm">1/Sec</div></div>
                        </div>
                    </div>
                    <div class="glass-card p-2 rounded-2xl border-white/10"><img src="https://image.pollinations.ai/prompt/cygnus%20x-1%20accretion%20disk%20binary%20star%20system%20x-ray%20jets%20cinematic%20photorealistic?width=800&height=600&nologo=true" class="rounded-xl w-full object-cover" alt="Stellar Mass"></div>
                </div>

                <!-- 2. Supermassive -->
                <div class="grid lg:grid-cols-2 gap-16 items-start">
                    <div class="lg:order-2">
                        <h3 class="text-3xl font-cinzel text-white mb-6">Supermassive Black Holes</h3>
                        <p class="text-zinc-400 text-lg leading-relaxed mb-6 text-justify-academic">
                            Monsters residing at the centers of nearly all large galaxies. Ranging from millions to billions of solar masses, their origin remains a mystery. They may have formed from the direct collapse of pristine gas clouds in the early universe, or from the rapid merger of smaller seeds.
                        </p>
                        <details class="deep-dive mb-8">
                            <summary>DEEP DIVE: Quasars &amp; AGNs</summary>
                            <div class="deep-dive-content">
                                <p class="mb-4">
                                    When these giants feed, they become Active Galactic Nuclei (AGNs). A Quasar is an AGN so bright it outshines its entire host galaxy. The energy comes from the accretion disk converting mass to energy with up to 40% efficiency (nuclear fusion is only 0.7%).
                                </p>
                            </div>
                        </details>
                        <div class="mb-8">
                            <div class="flex justify-between text-xs font-mono text-zinc-500 mb-2">
                                <span>MAX OBSERVED MASS (TON 618)</span>
                                <span>66,000,000,000 M☉</span>
                            </div>
                            <div class="data-bar-container">
                                <div class="data-bar-fill bg-purple-500" style="width: 100%"></div>
                            </div>
                        </div>
                        <div class="key-figures-grid">
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Example</div><div class="font-bold text-white text-sm">Sgr A*</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Role</div><div class="font-bold text-white text-sm">Anchor</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Engine</div><div class="font-bold text-white text-sm">Quasar</div></div>
                            <div class="glass-card p-4 rounded-lg text-center"><div class="text-xs text-zinc-500 uppercase mb-1">Age</div><div class="font-bold text-white text-sm">Primordial</div></div>
                        </div>
                    </div>
                    <div class="lg:order-1 glass-card p-2 rounded-2xl border-white/10"><img src="https://image.pollinations.ai/prompt/supermassive%20black%20hole%20galactic%20center%20active%20nucleus%20jet%20cosmic%20scale%20cinematic?width=800&height=600&nologo=true" class="rounded-xl w-full object-cover" alt="Supermassive"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- MODULE 5: THERMODYNAMICS -->
    <section id="thermodynamics" class="py-32 relative border-t border-white/5 bg-zinc-950">
        <div class="max-w-[1400px] mx-auto px-6 relative z-10">
             <div class="flex items-center gap-6 mb-20">
                <span class="text-8xl font-cinzel text-white/5 font-bold absolute -left-6 -top-10 select-none">05</span>
                <div class="relative">
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] mb-2 font-semibold">Module Five</div>
                    <h2 class="text-5xl md:text-6xl font-semibold tracking-tight">Thermodynamics</h2>
                </div>
            </div>

            <div class="grid lg:grid-cols-2 gap-12">
                <!-- Hawking Radiation -->
                <div class="glass-card p-8 rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-blue-500/5 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <h3 class="text-2xl font-cinzel text-white mb-4 relative z-10">Hawking Radiation</h3>
                    <p class="text-zinc-400 mb-6 leading-relaxed relative z-10">
                        Classically, black holes are perfect absorbers. Quantum mechanically, they glow. Stephen Hawking showed that particle-antiparticle pairs popping into existence near the horizon can be separated—one falls in, one escapes. The escaping particle becomes radiation, stealing mass from the black hole.
                    </p>
                    <details class="deep-dive mb-6 relative z-10">
                        <summary>DEEP DIVE: Evaporation Time</summary>
                        <div class="deep-dive-content">
                            <p>Evaporation time is proportional to M³. A solar mass black hole would take 10⁶⁷ years to evaporate. A microscopic black hole would flash out of existence instantly.</p>
                            <div class="mt-4 font-mono text-xs text-center border p-2 rounded border-white/10">T ~ 1/M</div>
                        </div>
                    </details>
                    <div class="grid grid-cols-2 gap-4 relative z-10">
                         <div class="glass-card p-3 text-center"><div class="text-[10px] text-zinc-500">Year</div><div class="font-bold">1974</div></div>
                         <div class="glass-card p-3 text-center"><div class="text-[10px] text-zinc-500">Temp</div><div class="font-bold">Nano-Kelvin</div></div>
                    </div>
                </div>

                <!-- Entropy -->
                <div class="glass-card p-8 rounded-2xl relative overflow-hidden group">
                    <div class="absolute inset-0 bg-green-500/5 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <h3 class="text-2xl font-cinzel text-white mb-4 relative z-10">Bekenstein Entropy</h3>
                    <p class="text-zinc-400 mb-6 leading-relaxed relative z-10">
                        Entropy is a measure of hidden information. Bekenstein realized that if a black hole had no entropy, dropping a tea cup into it would violate the Second Law of Thermodynamics. He proposed the entropy is proportional to the surface area of the horizon.
                    </p>
                    <details class="deep-dive mb-6 relative z-10">
                        <summary>DEEP DIVE: The Holographic Principle</summary>
                        <div class="deep-dive-content">
                            <p>This realization led to the Holographic Principle: the maximum amount of information held in a volume of space is proportional to the surface area of its boundary, not its volume. The 3D universe might be a projection of 2D data.</p>
                        </div>
                    </details>
                     <div class="grid grid-cols-2 gap-4 relative z-10">
                         <div class="glass-card p-3 text-center"><div class="text-[10px] text-zinc-500">Symbol</div><div class="font-bold">S</div></div>
                         <div class="glass-card p-3 text-center"><div class="text-[10px] text-zinc-500">Relation</div><div class="font-bold">Area (A)</div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

append_to_index(part5)
