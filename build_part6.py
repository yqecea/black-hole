
def append_to_index(content):
    with open('index.html', 'a') as f:
        f.write(content)

# PART 6: MODULE 6 (EVIDENCE), MODULE 7 (FRONTIER), FOOTER & SCRIPTS
part6 = """
    <!-- MODULE 6: OBSERVATIONAL EVIDENCE -->
    <section id="evidence" class="py-32 relative border-t border-white/5 bg-black">
         <div class="max-w-[1400px] mx-auto px-6 relative z-10">
             <div class="flex items-center gap-6 mb-20">
                <span class="text-8xl font-cinzel text-white/5 font-bold absolute -left-6 -top-10 select-none">06</span>
                <div class="relative">
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] mb-2 font-semibold">Module Six</div>
                    <h2 class="text-5xl md:text-6xl font-semibold tracking-tight">Hard Evidence</h2>
                </div>
            </div>

            <!-- EHT & LIGO Parallax -->
            <div class="space-y-6">
                <!-- EHT -->
                <div class="relative min-h-[60vh] rounded-3xl overflow-hidden flex items-center group">
                    <div class="absolute inset-0 z-0">
                         <img src="https://image.pollinations.ai/prompt/event%20horizon%20telescope%20black%20hole%20image%20m87%20radio%20telescope%20array%20data%20processing%20cinematic?width=1920&height=1080&nologo=true" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" alt="EHT">
                         <div class="absolute inset-0 bg-gradient-to-r from-black via-black/80 to-transparent"></div>
                    </div>
                    <div class="relative z-10 p-12 max-w-2xl">
                        <div class="inline-block bg-orange-500 text-black font-bold px-3 py-1 text-xs mb-4">2019 / 2022</div>
                        <h3 class="text-4xl font-cinzel text-white mb-4">The Event Horizon Telescope</h3>
                        <p class="text-zinc-300 text-lg mb-6 leading-relaxed">
                            Using Very Long Baseline Interferometry (VLBI), the EHT turned the Earth into a giant eye. It resolved the shadow of M87* (6.5 billion M☉) and Sgr A* (4 million M☉), proving the existence of the photon ring predicted by relativity.
                        </p>
                        <div class="grid grid-cols-2 gap-4 max-w-md">
                            <div class="border border-white/20 p-4 rounded bg-black/50 backdrop-blur">
                                <div class="text-xs text-zinc-500 uppercase">Resolution</div>
                                <div class="text-white font-mono">20 micro-arcsec</div>
                            </div>
                            <div class="border border-white/20 p-4 rounded bg-black/50 backdrop-blur">
                                <div class="text-xs text-zinc-500 uppercase">Data</div>
                                <div class="text-white font-mono">5 Petabytes</div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- LIGO -->
                <div class="relative min-h-[60vh] rounded-3xl overflow-hidden flex items-center justify-end text-right group">
                     <div class="absolute inset-0 z-0">
                         <img src="https://image.pollinations.ai/prompt/LIGO%20detector%20gravitational%20waves%20ripples%20in%20spacetime%20laser%20interferometer%20blue%20sci-fi?width=1920&height=1080&nologo=true" class="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105" alt="LIGO">
                         <div class="absolute inset-0 bg-gradient-to-l from-black via-black/80 to-transparent"></div>
                    </div>
                    <div class="relative z-10 p-12 max-w-2xl">
                         <div class="inline-block bg-blue-500 text-black font-bold px-3 py-1 text-xs mb-4">GW150914</div>
                        <h3 class="text-4xl font-cinzel text-white mb-4">LIGO &amp; Gravitational Waves</h3>
                        <p class="text-zinc-300 text-lg mb-6 leading-relaxed">
                            Ripples in the fabric of spacetime caused by the violent merger of black holes. Detected by measuring length changes smaller than a proton using 4km laser arms. It opened a new sense for humanity: we can now "hear" the universe.
                        </p>
                        <div class="flex justify-end gap-4">
                             <div class="border border-white/20 p-4 rounded bg-black/50 backdrop-blur text-left">
                                <div class="text-xs text-zinc-500 uppercase">Strain Sensitivity</div>
                                <div class="text-white font-mono">10⁻²¹</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Gallery of Simulations -->
            <div class="mt-20">
                <h3 class="text-2xl font-cinzel text-white mb-8">Simulation Gallery</h3>
                <div class="grid grid-cols-2 md:grid-cols-4 gap-4 h-64">
                    <div class="group relative overflow-hidden rounded-xl bg-zinc-900 cursor-pointer">
                        <img src="https://image.pollinations.ai/prompt/black%20hole%20accretion%20disk%20simulation%20doppler%20beaming%20scientific%20visualization?width=400&height=400&nologo=true" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity">
                    </div>
                    <div class="group relative overflow-hidden rounded-xl bg-zinc-900 cursor-pointer">
                        <img src="https://image.pollinations.ai/prompt/binary%20black%20hole%20merger%20simulation%20gravitational%20waves%20grid%20warp?width=400&height=400&nologo=true" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity">
                    </div>
                    <div class="group relative overflow-hidden rounded-xl bg-zinc-900 cursor-pointer">
                        <img src="https://image.pollinations.ai/prompt/supermassive%20black%20hole%20jet%20launch%20magnetic%20field%20lines%20simulation?width=400&height=400&nologo=true" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity">
                    </div>
                    <div class="group relative overflow-hidden rounded-xl bg-zinc-900 cursor-pointer">
                        <img src="https://image.pollinations.ai/prompt/black%20hole%20photon%20ring%20ray%20tracing%20simulation%20high%20resolution?width=400&height=400&nologo=true" class="w-full h-full object-cover opacity-60 group-hover:opacity-100 transition-opacity">
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- MODULE 7: FRONTIER -->
    <section id="frontier" class="py-32 relative border-t border-white/5 overflow-hidden">
        <div class="section-bg-container absolute inset-0">
             <img src="https://image.pollinations.ai/prompt/quantum%20gravity%20string%20theory%20holographic%20universe%20matrix%20code%20abstract%20dark?width=1920&height=1080&nologo=true" class="w-full h-full object-cover opacity-20" alt="Frontier BG">
        </div>

        <div class="max-w-[1400px] mx-auto px-6 relative z-10">
             <div class="flex items-center gap-6 mb-20">
                <span class="text-8xl font-cinzel text-white/5 font-bold absolute -left-6 -top-10 select-none">07</span>
                <div class="relative">
                    <div class="text-xs text-zinc-500 uppercase tracking-[0.2em] mb-2 font-semibold">Module Seven</div>
                    <h2 class="text-5xl md:text-6xl font-semibold tracking-tight">The Frontier</h2>
                </div>
            </div>

            <div class="grid lg:grid-cols-2 gap-16">
                <!-- Info Paradox -->
                <div class="glass-card p-10 rounded-3xl border border-red-500/20 shadow-[0_0_50px_-20px_rgba(255,0,0,0.1)]">
                    <h3 class="text-3xl font-cinzel text-white mb-6">The Information Paradox</h3>
                    <p class="text-zinc-400 mb-6 leading-relaxed text-justify-academic">
                        Quantum Mechanics states information is eternal (Unitary). Relativity states black holes evaporate into random thermal radiation, destroying the information of what fell in. These two pillars of physics contradict each other here.
                    </p>
                    <div class="space-y-4">
                        <div class="bg-black/40 p-4 rounded border-l-2 border-red-500">
                            <h4 class="text-white font-bold text-sm">Solution A: Information Loss</h4>
                            <p class="text-xs text-zinc-500">Quantum mechanics is wrong. Information is destroyed. (Hawking's original bet)</p>
                        </div>
                        <div class="bg-black/40 p-4 rounded border-l-2 border-green-500">
                            <h4 class="text-white font-bold text-sm">Solution B: Remnants</h4>
                            <p class="text-xs text-zinc-500">Evaporation stops at the Planck scale, leaving a dense nugget of info.</p>
                        </div>
                         <div class="bg-black/40 p-4 rounded border-l-2 border-blue-500">
                            <h4 class="text-white font-bold text-sm">Solution C: Holography/Islands</h4>
                            <p class="text-xs text-zinc-500">Information is encoded in the radiation via subtle quantum entanglements.</p>
                        </div>
                    </div>
                </div>

                <!-- Firewalls -->
                <div>
                     <h3 class="text-3xl font-cinzel text-white mb-6">Firewalls &amp; Wormholes</h3>
                     <p class="text-zinc-400 mb-8 leading-relaxed text-justify-academic">
                        To save quantum mechanics, some physicists propose a "Firewall" of high-energy particles at the horizon that incinerates anything attempting to enter. Others suggest "ER=EPR", implying that quantum entanglement (EPR) is connected by microscopic wormholes (ER).
                     </p>
                     <div class="grid grid-cols-2 gap-4">
                         <div class="glass-card p-6 rounded-xl text-center flex flex-col items-center justify-center aspect-square">
                             <i data-lucide="flame" class="w-8 h-8 text-orange-500 mb-4"></i>
                             <span class="font-cinzel text-lg">Firewall</span>
                         </div>
                         <div class="glass-card p-6 rounded-xl text-center flex flex-col items-center justify-center aspect-square">
                             <i data-lucide="link" class="w-8 h-8 text-blue-500 mb-4"></i>
                             <span class="font-cinzel text-lg">ER = EPR</span>
                         </div>
                     </div>
                </div>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="py-24 border-t border-white/5 bg-black relative z-10">
        <div class="max-w-[1400px] mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="text-left">
                <h4 class="text-2xl font-cinzel text-white mb-2">ZERO TO INFINITY</h4>
                <p class="text-zinc-600 text-sm">The Complete Guide to Black Holes</p>
            </div>
            <div class="flex gap-6 text-zinc-500">
                <a href="#" class="hover:text-white transition-colors">GitHub</a>
                <a href="#" class="hover:text-white transition-colors">Twitter</a>
                <a href="#" class="hover:text-white transition-colors">Research</a>
            </div>
        </div>
    </footer>

    <!-- SCRIPTS -->
    <script>
        lucide.createIcons();
        gsap.registerPlugin(ScrollTrigger);

        // ==========================================
        // 0. UTILS: SCRAMBLE TEXT & MAGNETIC
        // ==========================================

        class ScrambleText {
            constructor(element, chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&') {
                this.element = element;
                this.originalText = element.innerText;
                this.chars = chars;
                this.frameId = null;
                this.update = this.update.bind(this);
            }

            start(duration = 1000) {
                const startTime = Date.now();
                const length = this.originalText.length;

                const animate = () => {
                    const elapsed = Date.now() - startTime;
                    const progress = Math.min(elapsed / duration, 1);

                    let result = '';
                    const revealIndex = Math.floor(progress * length);

                    for (let i = 0; i < length; i++) {
                        if (i < revealIndex) {
                            result += this.originalText[i];
                        } else if (this.originalText[i] === ' ') {
                            result += ' ';
                        } else {
                            result += this.chars[Math.floor(Math.random() * this.chars.length)];
                        }
                    }

                    this.element.innerText = result;

                    if (progress < 1) {
                        this.frameId = requestAnimationFrame(animate);
                    } else {
                        this.element.innerText = this.originalText; // Ensure final state
                    }
                };

                if (this.frameId) cancelAnimationFrame(this.frameId);
                animate();
            }
        }

        // Magnetic Button Implementation
        class MagneticObject {
            constructor(el, strength = 20) {
                this.el = el;
                this.strength = strength;
                this.rect = this.el.getBoundingClientRect();
                this.isHovering = false;

                // Update rect on resize
                window.addEventListener('resize', () => this.rect = this.el.getBoundingClientRect());

                document.addEventListener('mousemove', (e) => {
                    const x = e.clientX;
                    const y = e.clientY;

                    // Check distance
                    const centerX = this.rect.left + this.rect.width / 2;
                    const centerY = this.rect.top + this.rect.height / 2;
                    const dist = Math.hypot(x - centerX, y - centerY);
                    const range = 100; // Activation range

                    if (dist < range) {
                        const magnetX = (x - centerX) / range * this.strength;
                        const magnetY = (y - centerY) / range * this.strength;

                        gsap.to(this.el, { x: magnetX, y: magnetY, duration: 0.5, ease: 'power2.out' });
                    } else {
                        gsap.to(this.el, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' });
                    }
                });
            }
        }

        // 3D Tilt for Glass Cards
        document.querySelectorAll('.glass-card').forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                // Spotlight
                card.style.setProperty('--mouse-x', `${x}px`);
                card.style.setProperty('--mouse-y', `${y}px`);

                // Tilt
                const centerX = rect.width / 2;
                const centerY = rect.height / 2;
                const tiltX = (y - centerY) / 20; // Rotate X based on Y
                const tiltY = (centerX - x) / 20; // Rotate Y based on X

                gsap.to(card, {
                    transform: `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`,
                    duration: 0.4,
                    ease: 'power2.out'
                });
            });

            card.addEventListener('mouseleave', () => {
                gsap.to(card, {
                    transform: `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`,
                    duration: 0.7,
                    ease: 'elastic.out(1, 0.8)'
                });
            });
        });

        // ==========================================
        // 1. HERO BOOT SEQUENCE (FIX)
        // ==========================================
        window.addEventListener('load', () => {
            // HUD Decoding Sound Effect (Visual only for now)

            // 1. Reveal "System Online" badge
            const systemOnline = document.querySelector('.reveal-container .text-mono'); // approx selector
            // Actually, let's use the .reveal-text classes

            const revealElements = document.querySelectorAll('.reveal-text');

            // Staggered Glitch Reveal
            revealElements.forEach((el, index) => {
                setTimeout(() => {
                    el.classList.add('revealed');
                    el.classList.add('glitch-text');

                    // Set data-text for glitch CSS
                    el.setAttribute('data-text', el.innerText);

                    // Scramble text content if it's the title
                    if (el.innerText.includes('ZERO') || el.innerText.includes('INFINITY') || el.innerText.includes('TO')) {
                         new ScrambleText(el).start(1500);
                    }

                    // Remove glitch effect after settling
                    setTimeout(() => {
                        el.classList.remove('glitch-text');
                    }, 2000);

                }, 500 + (index * 400));
            });

            // Reveal Buttons
            setTimeout(() => {
                const btn = document.getElementById('hero-buttons');
                if(btn) {
                    btn.style.transition = 'opacity 2s ease';
                    btn.style.opacity = '1';
                }
            }, 3000);
        });

        // ==========================================
        // 2. STARFIELD "WARP" INTERACTIVITY
        // ==========================================
        const starContainer = document.getElementById('starField');
        if (starContainer) {
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            starContainer.appendChild(renderer.domElement);

            // Stars
            const starsGeometry = new THREE.BufferGeometry();
            const starsCount = 3000;
            const posArray = new Float32Array(starsCount * 3);
            const originalZ = new Float32Array(starsCount); // Store original Z to reset

            for(let i = 0; i < starsCount * 3; i+=3) {
                posArray[i] = (Math.random() - 0.5) * 100; // x
                posArray[i+1] = (Math.random() - 0.5) * 100; // y
                posArray[i+2] = (Math.random() - 0.5) * 100; // z
                originalZ[i/3] = posArray[i+2];
            }

            starsGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

            const starMaterial = new THREE.PointsMaterial({
                size: 0.15,
                color: 0xffffff,
                transparent: true,
                opacity: 0.8
            });

            const starMesh = new THREE.Points(starsGeometry, starMaterial);
            scene.add(starMesh);
            camera.position.z = 20;

            // Mouse Velocity Tracking
            let mouseX = 0, mouseY = 0;
            let targetVelocity = 0;
            let currentVelocity = 0;

            document.addEventListener('mousemove', (e) => {
                // Calculate rough velocity
                const newX = e.clientX;
                const newY = e.clientY;
                const dx = newX - mouseX;
                const dy = newY - mouseY;
                const speed = Math.sqrt(dx*dx + dy*dy);

                targetVelocity = Math.min(speed * 0.05, 5); // Cap warp speed

                mouseX = newX;
                mouseY = newY;

                // Parallax
                gsap.to(scene.rotation, {
                    x: -(mouseY / window.innerHeight - 0.5) * 0.5,
                    y: -(mouseX / window.innerWidth - 0.5) * 0.5,
                    duration: 2
                });
            });

            const animate = () => {
                requestAnimationFrame(animate);

                // Decay velocity
                targetVelocity *= 0.95;
                currentVelocity += (targetVelocity - currentVelocity) * 0.1;

                // Base rotation
                scene.rotation.z += 0.0005;

                // Warp Effect: Stretch stars based on velocity
                const positions = starsGeometry.attributes.position.array;

                for(let i = 0; i < starsCount; i++) {
                    const i3 = i * 3;
                    // Move stars towards camera (warp)
                    positions[i3 + 2] += (0.05 + currentVelocity * 0.5);

                    // Reset if too close
                    if (positions[i3 + 2] > 30) {
                        positions[i3 + 2] = -50;
                        positions[i3] = (Math.random() - 0.5) * 100; // Reshuffle XY
                        positions[i3+1] = (Math.random() - 0.5) * 100;
                    }
                }
                starsGeometry.attributes.position.needsUpdate = true;

                // Stretch lines if fast
                if (currentVelocity > 0.5) {
                    starMaterial.size = 0.15 + currentVelocity * 0.2;
                } else {
                    starMaterial.size = 0.15;
                }

                renderer.render(scene, camera);
            };

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });

            animate();
        }


        // ==========================================
        // 3. GSAP SCROLL & DATA INTERACTIVITY
        // ==========================================

        // Horizontal Scroll
        const scrollContainer = document.querySelector('.horizontal-timeline-container');
        if(scrollContainer) {
            scrollContainer.addEventListener('wheel', (evt) => {
                evt.preventDefault();
                scrollContainer.scrollLeft += evt.deltaY;
            });
        }

        // Heavy "Cinematic" Parallax on Headers
        gsap.utils.toArray('h2').forEach(header => {
            gsap.from(header, {
                scrollTrigger: {
                    trigger: header,
                    start: 'top 100%',
                    scrub: 1.5 // Heavy scrubbing
                },
                y: 100,
                opacity: 0,
                ease: 'power2.out'
            });
        });

        // Matrix Scramble for Dashboard Data
        ScrollTrigger.batch('.font-mono, .glass-card h4', {
            onEnter: (elements) => {
                elements.forEach(el => {
                    new ScrambleText(el).start(2000);
                });
            }
        });

        // Initialize Magnetic Buttons
        document.querySelectorAll('a.group, button, nav a').forEach(el => {
            new MagneticObject(el, 30); // Strength 30
        });


        // ==========================================
        // 4. BLACK HOLE VISUALIZER (Existing)
        // ==========================================
        const canvas = document.getElementById('blackhole-canvas');
        const container = document.getElementById('blackhole-wrapper');

        if (canvas && container) {
            const scene = new THREE.Scene();
            // Match container aspect ratio
            const camera = new THREE.PerspectiveCamera(60, container.clientWidth / container.clientHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });

            const updateSize = () => {
                const w = container.clientWidth;
                const h = container.clientHeight;
                renderer.setSize(w, h);
                camera.aspect = w / h;
                camera.updateProjectionMatrix();
            };
            updateSize();
            window.addEventListener('resize', updateSize);

            // Black Hole Mesh Construction
            const eventHorizon = new THREE.Mesh(
                new THREE.SphereGeometry(1, 64, 64),
                new THREE.MeshBasicMaterial({ color: 0x000000 })
            );
            scene.add(eventHorizon);

            // Photon Ring (Gold)
            const photonRing = new THREE.Mesh(
                new THREE.TorusGeometry(1.5, 0.02, 16, 100),
                new THREE.MeshBasicMaterial({ color: 0xffcc00, transparent: true, opacity: 0.8 })
            );
            photonRing.rotation.x = Math.PI / 2;
            scene.add(photonRing);

            // Accretion Disk (Orange/Red Gradient via particles for performance/look)
            const diskParticles = new THREE.BufferGeometry();
            const diskCount = 2000;
            const posArray = new Float32Array(diskCount * 3);
            const colorArray = new Float32Array(diskCount * 3);

            const colorInside = new THREE.Color(0xffaa00);
            const colorOutside = new THREE.Color(0xff0000);

            for(let i=0; i<diskCount; i++) {
                const angle = Math.random() * Math.PI * 2;
                const radius = 2.0 + Math.random() * 3.5; // 2.0 to 5.5

                posArray[i*3] = Math.cos(angle) * radius; // x
                posArray[i*3+1] = (Math.random() - 0.5) * 0.1; // y (flat)
                posArray[i*3+2] = Math.sin(angle) * radius; // z

                // Color gradient based on radius
                const t = (radius - 2.0) / 3.5;
                const finalColor = colorInside.clone().lerp(colorOutside, t);
                colorArray[i*3] = finalColor.r;
                colorArray[i*3+1] = finalColor.g;
                colorArray[i*3+2] = finalColor.b;
            }

            diskParticles.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            diskParticles.setAttribute('color', new THREE.BufferAttribute(colorArray, 3));

            const diskMaterial = new THREE.PointsMaterial({
                size: 0.05,
                vertexColors: true,
                transparent: true,
                opacity: 0.8,
                blending: THREE.AdditiveBlending
            });

            const accretionDisk = new THREE.Points(diskParticles, diskMaterial);
            // Tilt the disk
            accretionDisk.rotation.x = 0.2;
            accretionDisk.rotation.z = 0.1;
            scene.add(accretionDisk);

            camera.position.z = 6;
            camera.position.y = 1;
            camera.lookAt(0,0,0);

            // Animation
            const animate = () => {
                requestAnimationFrame(animate);
                accretionDisk.rotation.y -= 0.005; // Spin disk
                photonRing.lookAt(camera.position); // Billboard effect for ring
                renderer.render(scene, camera);
            };
            animate();
        }
    </script>
</body>
</html>
"""

append_to_index(part6)
