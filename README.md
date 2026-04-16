<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>David Chaves — AI Engineer</title>

<style>
    :root {
        --bg: #050509;
        --card-bg: #0b0b12;
        --accent: #00ff88;
        --accent-soft: #00ff8855;
        --text-main: #e0e0e0;
        --text-muted: #9a9a9a;
    }

    * { box-sizing: border-box; }

    body {
        margin: 0;
        font-family: 'Segoe UI', sans-serif;
        background: radial-gradient(circle at top, #101020 0, #050509 45%, #000 100%);
        color: var(--text-main);
        overflow-x: hidden;
        min-height: 100vh;
        cursor: none;
    }

    #particles {
        position: fixed;
        inset: 0;
        z-index: -2;
    }

    .cursor-dot {
        position: fixed;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        pointer-events: none;
        background: var(--accent);
        box-shadow: 0 0 12px var(--accent);
        z-index: 9999;
        opacity: 0.9;
        transform: translate(-50%, -50%);
    }

    @keyframes neonGlow {
        0% { text-shadow: 0 0 5px var(--accent); }
        50% { text-shadow: 0 0 22px var(--accent); }
        100% { text-shadow: 0 0 5px var(--accent); }
    }

    header {
        text-align: center;
        padding: 80px 20px 40px;
        position: relative;
        z-index: 1;
    }

    h1 {
        font-size: 3.4rem;
        color: var(--accent);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        animation: neonGlow 3s infinite;
    }

    h2 {
        margin-top: 50px;
        border-left: 4px solid var(--accent);
        padding-left: 12px;
        font-size: 1.7rem;
    }

    .container {
        width: 90%;
        max-width: 1100px;
        margin: auto;
        padding-bottom: 80px;
        position: relative;
        z-index: 1;
    }

    .tag {
        display: inline-block;
        background: #00ff8822;
        color: var(--accent);
        padding: 5px 12px;
        border-radius: 999px;
        margin: 4px;
        font-size: 0.85rem;
    }

    .projects-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 24px;
        margin-top: 20px;
    }

    .project {
        background: linear-gradient(145deg, #07070c, #10101a);
        padding: 20px;
        border-radius: 14px;
        border: 1px solid var(--accent-soft);
        transition: transform 0.15s ease-out, box-shadow 0.15s ease-out, border-color 0.15s;
        cursor: pointer;
        box-shadow: 0 0 15px #00ff8822;
    }

    .project:hover {
        border-color: var(--accent);
        box-shadow: 0 0 25px #00ff8855;
    }

    .project-details {
        display: none;
        margin-top: 10px;
        color: var(--text-muted);
        font-size: 0.95rem;
    }

    footer {
        text-align: center;
        padding: 30px;
        color: var(--text-muted);
        font-size: 0.9rem;
        position: relative;
        z-index: 1;
    }

    a { color: var(--accent); }

    .sound-toggle {
        position: fixed;
        top: 16px;
        right: 16px;
        z-index: 1000;
        background: #0b0b12cc;
        border-radius: 999px;
        padding: 6px 14px;
        border: 1px solid var(--accent-soft);
        color: var(--text-main);
        font-size: 0.85rem;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 6px;
        box-shadow: 0 0 12px #00ff8833;
    }

    .sound-indicator {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--accent);
        box-shadow: 0 0 10px var(--accent);
    }

    .sound-toggle.muted .sound-indicator {
        background: #555;
        box-shadow: none;
    }

    /* Chatbot UI */
    #chatbot {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 280px;
        height: 380px;
        background: #0b0b12;
        border: 1px solid #00ff8855;
        border-radius: 12px;
        box-shadow: 0 0 15px #00ff8855;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        z-index: 9999;
    }

    #chat-header {
        background: #00ff88;
        color: #000;
        padding: 10px;
        font-weight: bold;
        text-align: center;
    }

    #chat-messages {
        flex: 1;
        padding: 10px;
        overflow-y: auto;
        color: #e0e0e0;
        font-size: 0.9rem;
    }

    #chat-input {
        border: none;
        padding: 10px;
        background: #1a1a22;
        color: #e0e0e0;
        outline: none;
    }

    @media (max-width: 600px) {
        body { cursor: auto; }
        .cursor-dot { display: none; }
        #chatbot { width: 90%; right: 5%; }
    }
</style>
</head>

<body>

<canvas id="particles"></canvas>
<div class="cursor-dot" id="cursorDot"></div>

<button class="sound-toggle" id="soundToggle">
    <span class="sound-indicator"></span>
    <span id="soundLabel">Sound: On</span>
</button>

<audio id="ambientAudio" loop>
    <source src="data:audio/mp3;base64,//uQxAAAAAAAAAAAAAAAAAAAAAAAWGluZwAAAA8AAAACAAACcQCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" type="audio/mp3">
</audio>

<audio id="hoverSound">
    <source src="data:audio/mp3;base64,//uQxAAAAAAAAAAAAAAAAAAAAAAAWGluZwAAAA8AAAACAAACcQCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" type="audio/mp3">
</audio>

<audio id="clickSound">
    <source src="data:audio/mp3;base64,//uQxAAAAAAAAAAAAAAAAAAAAAAAWGluZwAAAA8AAAACAAACcQCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" type="audio/mp3">
</audio>

<header>
    <h1>David Chaves</h1>
    <p>AI Engineer • Machine Learning Developer • LLM Specialist</p>
</header>

<div class="container">

    <h2>About Me</h2>
    <p>
        I’m an AI Engineer specializing in building practical, production‑ready machine learning systems. 
        My work focuses on large language models, deep learning pipelines, and automation tools that solve 
        real business problems. I develop end‑to‑end AI solutions — from data processing and model training 
        to deployment, optimization, and monitoring — with an emphasis on reliability, scalability, and 
        seamless integration into real‑world workflows.
    </p>

    <h2>Skills</h2>
    <p>
        <span class="tag">Python</span>
        <span class="tag">PyTorch</span>
        <span class="tag">TensorFlow</span>
        <span class="tag">Transformers</span>
        <span class="tag">RAG</span>
        <span class="tag">FastAPI</span>
        <span class="tag">Docker</span>
        <span class="tag">Azure</span>
        <span class="tag">Hugging Face</span>
    </p>

    <h2>AI Projects</h2>

    <div class="projects-grid">

        <div class="project" onclick="toggleDetails(1)">
            <h3>LLM‑Powered Chat Assistant</h3>
            <div id="details1" class="project-details">
                <p>
                    A domain‑specific conversational AI assistant built using a fine‑tuned transformer model 
                    with Retrieval‑Augmented Generation (RAG). Designed for high‑accuracy responses and 
                    scalable deployment.
                </p>
                <p><strong>Tech:</strong> Python, PyTorch, Transformers, FAISS, FastAPI, Docker</p>
                <p><strong>Impact:</strong> Improved response accuracy by 35% using custom embeddings and optimized retrieval.</p>
            </div>
        </div>

        <div class="project" onclick="toggleDetails(2)">
            <h3>Image Classification Pipeline</h3>
            <div id="details2" class="project-details">
                <p>
                    End‑to‑end deep learning pipeline for multi‑class image recognition using transfer learning 
                    and automated augmentation.
                </p>
                <p><strong>Tech:</strong> TensorFlow, Keras, OpenCV, NumPy</p>
                <p><strong>Impact:</strong> Achieved 92%+ validation accuracy with optimized training workflow.</p>
            </div>
        </div>

        <div class="project" onclick="toggleDetails(3)">
            <h3>AI‑Driven Automation Tool</h3>
            <div id="details3" class="project-details">
                <p>
                    NLP‑powered workflow automation system that interprets user instructions and triggers 
                    multi‑step actions through API integrations.
                </p>
                <p><strong>Tech:</strong> Python, spaCy, FastAPI, REST APIs</p>
                <p><strong>Impact:</strong> Reduced manual workload by 40% through automated task execution.</p>
            </div>
        </div>

    </div>

    <h2>Tools & Mini Projects</h2>
    <p>
        I also build small interactive tools and JavaScript utilities.  
        View them here: <a href="tools.html">JavaScript Mini Tools</a>
    </p>

    <h2>Contact</h2>
    <p>
        Email: <a href="mailto:david@example.com">david@example.com</a><br>
        GitHub: <a href="https://github.com/DavidChaves">github.com/DavidChaves</a><br>
        LinkedIn: <a href="https://linkedin.com/in/DavidChaves">linkedin.com/in/DavidChaves</a>
    </p>

</div>

<footer>
    © 2026 David Chaves — AI Portfolio
</footer>

<!-- Chatbot UI -->
<div id="chatbot">
    <div id="chat-header">AI Chatbot</div>
    <div id="chat-messages"></div>
    <input id="chat-input" placeholder="Type a message...">
</div>

<script>
    function toggleDetails(id) {
        const section = document.getElementById("details" + id);
        const clickSound = document.getElementById("clickSound");
        section.style.display = section.style.display === "block" ? "none" : "block";
        clickSound.currentTime = 0;
        clickSound.play().catch(() => {});
    }

    const tiltCards = document.querySelectorAll('.project');
    const hoverSound = document.getElementById("hoverSound");
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -8;
            const rotateY = ((x - centerX) / centerX) * 8;
            card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
        });
        card.addEventListener('mouseenter', () => {
            hoverSound.currentTime = 0;
            hoverSound.play().catch(() => {});
        });
    });

    const canvas = document.getElementById('particles');
    const ctx = canvas.getContext('2d');
    let particles = [];
    let hexes = [];
    const numParticles = 80;
    const numHexes = 12;

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    function initParticles() {
        particles = [];
        for (let i = 0; i < numParticles; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                r: Math.random() * 2 + 0.5,
                dx: (Math.random() - 0.5) * 0.4,
                dy: (Math.random() - 0.5) * 0.4,
                alpha: Math.random() * 0.6 + 0.2
            });
        }
    }

    function initHexes() {
        hexes = [];
        for (let i = 0; i < numHexes; i++) {
            hexes.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                size: Math.random() * 40 + 30,
                dx: (Math.random() - 0.5) * 0.15,
                dy: (Math.random() - 0.5) * 0.15,
                alpha: Math.random() * 0.25 + 0.05
            });
        }
    }

    function drawHex(x, y, size, alpha) {
        const sides = 6;
        ctx.beginPath();
        for (let i = 0; i < sides; i++) {
            const angle = (Math.PI * 2 / sides) * i;
            const px = x + size * Math.cos(angle);
            const py = y + size * Math.sin(angle);
            if (i === 0) ctx.moveTo(px, py);
            else ctx.lineTo(px, py);
        }
        ctx.closePath();
        ctx.strokeStyle = `rgba(0, 255, 136, ${alpha})`;
        ctx.lineWidth = 1;
        ctx.stroke();
    }

    function drawScene() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        hexes.forEach(h => {
            drawHex(h.x, h.y, h.size, h.alpha);
            h.x += h.dx;
            h.y += h.dy;
            if (h.x < -100) h.x = canvas.width + 100;
            if (h.x > canvas.width + 100) h.x = -100;
            if (h.y < -100) h.y = canvas.height + 100;
            if (h.y > canvas.height + 100) h.y = -100;
        });

        particles.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 255, 136, ${p.alpha})`;
            ctx.fill();
            p.x += p.dx;
            p.y += p.dy;
            if (p.x < 0 || p.x > canvas.width) p.dx *= -1;
            if (p.y < 0 || p.y > canvas.height) p.dy *= -1;
        });

        requestAnimationFrame(drawScene);
    }

    initParticles();
    initHexes();
    drawScene();

    const cursorDot = document.getElementById('cursorDot');
    const trail = [];
    const maxTrail = 18;

    window.addEventListener('mousemove', (e) => {
        cursorDot.style.left = e.clientX + 'px';
        cursorDot.style.top = e.clientY + 'px';

        trail.push({ x: e.clientX, y: e.clientY, alpha: 1 });
        if (trail.length > maxTrail) trail.shift();
    });

    function drawTrail() {
        const existing = document.querySelectorAll('.trail-dot');
        existing.forEach(el => el.remove());

        trail.forEach(p => {
            const dot = document.createElement('div');
            dot.className = 'trail-dot';
            dot.style.position = 'fixed';
            dot.style.width = '6px';
            dot.style.height = '6px';
            dot.style.borderRadius = '50%';
            dot.style.pointerEvents = 'none';
            dot.style.left = p.x + 'px';
            dot.style.top = p.y + 'px';
            dot.style.transform = 'translate(-50%, -50%)';
            dot.style.background = `rgba(0,255,136,${p.alpha})`;
            dot.style.boxShadow = `0 0 10px rgba(0,255,136,${p.alpha})`;
            dot.style.zIndex = 9998;
            document.body.appendChild(dot);
            p.alpha -= 0.06;
        });

        for (let i = trail.length - 1; i >= 0; i--) {
            if (trail[i].alpha <= 0) trail.splice(i, 1);
        }

        requestAnimationFrame(drawTrail);
    }
    drawTrail();

    const ambientAudio = document.getElementById('ambientAudio');
    const soundToggle = document.getElementById('soundToggle');
    const soundLabel = document.getElementById('soundLabel');

    ambientAudio.volume = 0.25;

    function setMuted(muted) {
        if (muted) {
            ambientAudio.pause();
            soundToggle.classList.add('muted');
            soundLabel.textContent = 'Sound: Off';
        } else {
            ambientAudio.play().catch(() => {});
            soundToggle.classList.remove('muted');
            soundLabel.textContent = 'Sound: On';
        }
    }

    soundToggle.addEventListener('click', () => {
        const isMuted = soundToggle.classList.contains('muted');
        setMuted(!isMuted);
    });

    ambientAudio.play().catch(() => {
        window.addEventListener('click', function once() {
            ambientAudio.play().catch(() => {});
            window.removeEventListener('click', once);
        });
    });

    /* Chatbot JS */
    const API_URL = "https://54c5743a-d4b2-4798-b9f5-05267a7cde00-00-3lix5lgl5snhr.worf.replit.dev";

    const chatInput = document.getElementById("chat-input");
    const chatMessages = document.getElementById("chat-messages");

    chatInput.addEventListener("keydown", async (e) => {
        if (e.key === "Enter") {
            const msg = chatInput.value.trim();
            if (!msg) return;
            chatInput.value = "";
            addMessage("You", msg);

            try {
                const response = await fetch(API_URL, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message: msg })
                });
                const data = await response.json();
                addMessage("Bot", data.response || "(no response)");
            } catch (err) {
                addMessage("Bot", "⚠️ Chatbot server offline or unreachable.");
            }
        }
    });

    function addMessage(sender, text) {
        const div = document.createElement("div");
        div.innerHTML = `<strong>${sender}:</strong> ${text}`;
        chatMessages.appendChild(div);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
</script>

</body>
</html>
