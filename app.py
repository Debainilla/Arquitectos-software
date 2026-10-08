# -*- coding: utf-8 -*-
"""
🏗️ ARQUITECTOS DE SOFTWARE — Construye el sistema correcto
Experiencia interactiva para exponer 5 estilos de arquitectura de software.

Ejecutar:  streamlit run app.py
Todo funciona sin conexión a Internet (sin imágenes ni APIs externas).
"""

import time

import streamlit as st

st.set_page_config(
    page_title="Arquitectos de Software",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================================
# 1) DATOS: páginas, modelos y contenido
# =====================================================================

P_HOME = "🏠 Inicio"
P_INTRO = "🧠 Introducción"
P_COMP = "⚔️ Comparación"
P_QUIZ = "🎯 Reto"
P_RES = "🏆 Resultado"

MODELS = [
    {"id": "capas", "page": "🏢 Capas", "emoji": "🏢", "short": "Capas",
     "name": "Arquitectura por Capas", "color": "#3b82f6", "tag": "Cada piso, una función"},
    {"id": "cs", "page": "🖥️ Cliente-Servidor", "emoji": "🖥️", "short": "Cliente-Servidor",
     "name": "Cliente-Servidor", "color": "#14b8a6", "tag": "Uno pide, otro sirve"},
    {"id": "mvc", "page": "🎬 MVC", "emoji": "🎬", "short": "MVC",
     "name": "Modelo-Vista-Controlador", "color": "#f59e0b", "tag": "Guion, pantalla y director"},
    {"id": "micro", "page": "🏙️ Microservicios", "emoji": "🏙️", "short": "Microservicios",
     "name": "Microservicios", "color": "#ec4899", "tag": "Una ciudad de servicios"},
    {"id": "pf", "page": "🏭 Pipe & Filter", "emoji": "🏭", "short": "Pipe & Filter",
     "name": "Pipe & Filter", "color": "#8b5cf6", "tag": "Una fábrica por etapas"},
]
MODEL_BY_ID = {m["id"]: m for m in MODELS}
MODEL_BY_PAGE = {m["page"]: m for m in MODELS}
PAGES = [P_HOME, P_INTRO] + [m["page"] for m in MODELS] + [P_COMP, P_QUIZ, P_RES]

TABS = ["🎯 Idea", "🎮 Simulación", "📚 Ejemplos y balance", "🎤 Guía para exponer", "🧪 Reto"]

CONTENT = {
    "capas": {
        "meta_title": "🏢 Metáfora: un edificio",
        "metaphor": "Imaginen un edificio. Cada piso tiene una función diferente. "
                    "En una arquitectura por capas ocurre algo parecido.",
        "how": ["El sistema se divide en niveles apilados, cada uno con una tarea.",
                "Cada capa se comunica solo con la capa de arriba o la de abajo.",
                "Si cambias una capa, las demás casi no se enteran."],
        "examples": ["🏦 Sistemas empresariales", "🌐 Aplicaciones web", "📋 Sistemas administrativos"],
        "pros": ["Fácil de entender", "Buena separación de responsabilidades", "Fácil mantenimiento"],
        "cons": ["Puede volverse rígida", "Demasiadas capas pueden aumentar la complejidad"],
        "guide": ["En esta arquitectura cada capa tiene una responsabilidad específica y normalmente "
                  "se comunica con la capa que está debajo o encima de ella.",
                  "Toquen cada piso del edificio para ver qué hace cada capa.",
                  "Si el usuario quiere ver sus pedidos, la petición baja piso por piso hasta la base "
                  "de datos y la respuesta vuelve a subir."],
        "tip": "⏱️ Tiempo sugerido: 2 minutos. Usa el edificio y la simulación de la petición.",
        "reto": {"q": "Una aplicación tiene interfaz, lógica, acceso a datos y base de datos. "
                      "¿Qué arquitectura podría utilizar?",
                 "options": ["A) Microservicios", "B) Capas", "C) Pipe & Filter"], "correct": 1,
                 "exp": "Tener interfaz, lógica, acceso a datos y base de datos como niveles "
                        "separados es la idea central de la arquitectura por capas."},
    },
    "cs": {
        "meta_title": "🍽️ Metáfora: un restaurante",
        "metaphor": "El cliente pide un servicio y el servidor se encarga de proporcionarlo. "
                    "Como en un restaurante: tú pides, la cocina prepara y te entregan el plato.",
        "how": ["El cliente (navegador o app) hace una solicitud.",
                "El servidor la recibe, consulta los datos y prepara la respuesta.",
                "El servidor responde y el cliente muestra la información."],
        "examples": ["🌐 Sitios web", "🏦 Bancos", "📧 Correo electrónico", "🎮 Juegos online"],
        "pros": ["Centralización", "Fácil administración del servidor", "Permite atender muchos clientes"],
        "cons": ["El servidor puede convertirse en un punto crítico", "Depende de la comunicación de red"],
        "guide": ["Aquí hay dos roles claros: el cliente pide y el servidor responde.",
                  "Cuando abren una página web, su navegador es el cliente y la página vive en un servidor.",
                  "Si el servidor se cae, todos los clientes se quedan sin servicio: ese es su punto débil."],
        "tip": "⏱️ Tiempo sugerido: 2 minutos. Pulsa 'Ver solicitud en acción' mientras narras.",
        "reto": {"q": "¿Quién realiza la solicitud?",
                 "options": ["A) Cliente", "B) Servidor", "C) Base de datos"], "correct": 0,
                 "exp": "El cliente siempre inicia la conversación pidiendo algo; el servidor solo responde."},
    },
    "mvc": {
        "meta_title": "🎬 Metáfora: una película",
        "metaphor": "En una película, el guion es el Modelo, la pantalla del cine es la Vista "
                    "y el director es el Controlador que coordina todo.",
        "how": ["El usuario hace una acción (por ejemplo, pulsa un botón).",
                "El Controlador la recibe y le pide al Modelo que actúe.",
                "El Modelo actualiza los datos y la Vista muestra el resultado."],
        "examples": ["🛍️ Tiendas en línea", "🌐 Frameworks web (Django, Spring, ASP.NET MVC)",
                     "📱 Aplicaciones con pantallas y formularios"],
        "pros": ["Separación de responsabilidades", "Código más organizado", "Facilita el mantenimiento"],
        "cons": ["Puede aumentar la cantidad de componentes",
                 "Puede resultar complejo para proyectos pequeños"],
        "guide": ["MVC separa tres cosas: los datos (Modelo), lo que se ve (Vista) y quien coordina (Controlador).",
                  "Cuando alguien pulsa 'Comprar', no llega directo a los datos: primero pasa por el Controlador.",
                  "Gracias a esta separación, se puede cambiar el diseño sin tocar la lógica de los datos."],
        "tip": "⏱️ Tiempo sugerido: 2 minutos. Simula la compra y señala cada paso.",
        "reto": {"q": "Un usuario pulsa el botón 'Comprar' en una tienda en línea. "
                      "¿Qué componente recibe la acción del usuario?",
                 "options": ["A) Vista", "B) Modelo", "C) Controlador"], "correct": 2,
                 "exp": "El Controlador recibe las acciones del usuario y coordina qué debe pasar. "
                        "La Vista solo muestra y el Modelo maneja los datos."},
    },
    "micro": {
        "meta_title": "🏙️ Metáfora: una ciudad",
        "metaphor": "En lugar de construir una aplicación gigante, dividimos el sistema en pequeños "
                    "servicios independientes, como los edificios de una ciudad.",
        "how": ["Cada servicio hace una sola cosa y tiene su propio código y sus propios datos.",
                "Los servicios se comunican entre sí con mensajes o API.",
                "Si uno falla o necesita crecer, se trabaja solo con ese servicio."],
        "examples": ["🍔 Apps de comida (Usuarios, Restaurantes, Pedidos, Pagos, Entregas)",
                     "🎬 Plataformas de streaming", "🛒 Grandes tiendas en línea"],
        "pros": ["Escalabilidad", "Independencia de servicios", "Permite desplegar servicios por separado"],
        "cons": ["Mayor complejidad", "Comunicación entre servicios", "Monitoreo más complicado"],
        "guide": ["Un microservicio es un pedacito del sistema que hace una sola tarea y puede vivir solo.",
                  "Ahora voy a simular que falla el servicio de pagos: fíjense que los demás siguen funcionando.",
                  "La contrapartida es que coordinar muchos servicios es más complicado."],
        "tip": "⏱️ Tiempo sugerido: 3 minutos. El botón de falla es tu momento 'wow'.",
        "reto": {"q": "Una aplicación divide usuarios, pagos y envíos en servicios independientes. "
                      "¿Qué arquitectura representa mejor esta idea?",
                 "options": ["A) MVC", "B) Microservicios", "C) Capas"], "correct": 1,
                 "exp": "Dividir el sistema en servicios pequeños e independientes es la esencia de los microservicios."},
    },
    "pf": {
        "meta_title": "🏭 Metáfora: una fábrica",
        "metaphor": "Cada filtro realiza una tarea específica. La salida de un filtro se convierte "
                    "en la entrada del siguiente, como una línea de producción.",
        "how": ["Cada filtro hace una sola transformación.",
                "Los filtros se conectan con tuberías (pipes): la salida de uno es la entrada del siguiente.",
                "Se pueden agregar, quitar o reutilizar filtros con facilidad."],
        "examples": ["💻 Compiladores", "🐧 Comandos encadenados en la terminal",
                     "🖼️ Procesamiento de imágenes y audio", "📊 Limpieza y transformación de datos"],
        "pros": ["Cada etapa tiene una responsabilidad", "Fácil reutilización de filtros",
                 "Procesamiento por etapas"],
        "cons": ["Puede haber sobrecarga entre etapas", "No todos los problemas se adaptan bien a este modelo"],
        "guide": ["Piensen en una fábrica: la materia prima entra, pasa por estaciones y sale el producto final.",
                  "Un compilador es el ejemplo clásico: lee código y lo transforma etapa por etapa.",
                  "Si una etapa cambia, las demás no se enteran, porque solo importa lo que entra y lo que sale."],
        "tip": "⏱️ Tiempo sugerido: 2 minutos. Pulsa 'Procesar' y narra cada etapa.",
        "reto": {"q": "Una aplicación procesa información en varias etapas consecutivas. "
                      "¿Cuál modelo representa mejor esta situación?",
                 "options": ["A) Cliente-Servidor", "B) Pipe & Filter", "C) MVC"], "correct": 1,
                 "exp": "Etapas consecutivas donde la salida de una es la entrada de la siguiente: Pipe & Filter."},
    },
}

LAYERS = [
    ("pres", "👤", "PRESENTACIÓN", "Lo que ve el usuario", "#3b82f6",
     "Es la cara del sistema: pantallas, botones y formularios. Muestra la información y recibe lo que hace el usuario.",
     "Ejemplo: la página web o la app del banco."),
    ("neg", "🧠", "LÓGICA DE NEGOCIO", "Reglas del sistema", "#8b5cf6",
     "Aquí se toman las decisiones: validar datos, calcular totales y aplicar las reglas del sistema.",
     "Ejemplo: comprobar que hay saldo antes de transferir."),
    ("dat", "🔌", "ACCESO A DATOS", "Comunicación con datos", "#f59e0b",
     "Es el traductor entre la lógica y la base de datos: guarda, busca y actualiza información.",
     "Ejemplo: la consulta que busca tus pedidos."),
    ("bd", "🗄️", "BASE DE DATOS", "Información", "#10b981",
     "Es el almacén donde vive la información de forma permanente.",
     "Ejemplo: tablas de clientes, productos y pedidos."),
]

SERVICES = [("👤", "USUARIOS"), ("📦", "PRODUCTOS"), ("🛒", "CARRITO"),
            ("💳", "PAGOS"), ("🚚", "ENVÍOS"), ("🔐", "AUTENTICACIÓN")]

COMPARE = {
    "capas": ("Separar niveles", "Sistema empresarial", "Organización", "Puede volverse rígida"),
    "cs": ("Cliente solicita / servidor responde", "Web", "Centralización", "El servidor es punto crítico"),
    "mvc": ("Separar responsabilidades", "Aplicaciones web", "Mantenimiento", "Más componentes"),
    "micro": ("Servicios independientes", "Plataformas grandes", "Escalabilidad", "Mayor complejidad"),
    "pf": ("Procesamiento por etapas", "Compiladores", "Modularidad", "Sobrecarga entre etapas"),
}

CASES = [
    ("Una aplicación tiene presentación, lógica y acceso a datos.",
     "Hay niveles separados: presentación, lógica y acceso a datos. Eso es Arquitectura por Capas."),
    ("Un navegador solicita información a un servidor.",
     "Un cliente (el navegador) pide y un servidor responde: Cliente-Servidor."),
    ("Una aplicación separa Modelo, Vista y Controlador.",
     "Separar Modelo, Vista y Controlador es justamente el patrón MVC."),
    ("Una plataforma divide usuarios, pagos y envíos en servicios independientes.",
     "Servicios pequeños e independientes (usuarios, pagos, envíos): Microservicios."),
    ("Un sistema procesa información mediante varias etapas consecutivas.",
     "Etapas consecutivas donde la salida de una alimenta a la siguiente: Pipe & Filter."),
]

UBER_COMPONENTS = [("👤", "Usuarios"), ("🍔", "Restaurantes"), ("🛒", "Pedidos"),
                   ("💳", "Pagos"), ("🚚", "Entregas")]

UBER_REASONS = [
    "Necesito que cada parte pueda crecer y fallar por separado",
    "Quiero organizar el código en niveles con responsabilidades claras",
    "La app del usuario debe pedir información a un servidor central",
    "Quiero separar lo que se ve, lo que se decide y los datos",
    "El pedido pasa por varias etapas de procesamiento",
    "Otra razón (la escribo abajo)",
]

UBER_ANALYSIS = {
    "capas": ("Ordena bien el sistema: pantallas, reglas de pedidos y pagos, y acceso a datos. "
              "Es sencilla de construir y entender.",
              "Si la plataforma crece mucho, todo vive en el mismo bloque y cuesta escalar solo una parte."),
    "cs": ("Es la base natural: la app del cliente y la del restaurante piden información a servidores.",
           "Por sí sola no dice cómo organizar el interior del servidor; conviene combinarla con otros estilos."),
    "mvc": ("Muy útil para organizar las pantallas de la app: lo que se ve, las acciones y los datos.",
            "MVC organiza una aplicación, pero no resuelve cómo escalar pagos o entregas por separado."),
    "micro": ("Cada componente (Usuarios, Restaurantes, Pedidos, Pagos, Entregas) puede crecer, "
              "desplegarse y fallar de forma independiente.",
              "Exige más trabajo de comunicación, monitoreo y coordinación entre servicios."),
    "pf": ("Sirve para partes concretas, como procesar un pedido por etapas: validar, cobrar, notificar.",
           "No es natural para toda la app, que es interactiva y tiene muchas peticiones de usuarios."),
}

UBER_COMBO = [
    "🖥️ Cliente-Servidor: las apps (cliente, restaurante, repartidor) hablan con servidores.",
    "🏙️ Microservicios: Usuarios, Restaurantes, Pedidos, Pagos y Entregas como servicios independientes.",
    "🏢 Capas: dentro de cada servicio, presentación/API, lógica y acceso a datos.",
    "🎬 MVC: para organizar las pantallas de las apps.",
    "🏭 Pipe & Filter: para procesar un pedido por etapas (validar → cobrar → notificar).",
]

# =====================================================================
# 2) ESTILOS (CSS limpio, sin recursos externos)
# =====================================================================

CSS = """
.block-container{padding-top:1.2rem;max-width:1300px;}
section[data-testid="stSidebar"] label{font-size:1.05rem;}
.stButton>button{width:100%;border-radius:14px;font-size:1.05rem;font-weight:700;padding:.6rem 1rem;transition:all .2s;}
.stButton>button:hover{transform:translateY(-2px);}
.stButton>button[kind="primary"],button[data-testid="stBaseButton-primary"]{background:linear-gradient(90deg,#7c3aed,#db2777);border:none;color:#fff;}
@keyframes fadein{from{opacity:0;transform:translateY(8px);}to{opacity:1;transform:none;}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(255,255,255,.55);}70%{box-shadow:0 0 0 16px rgba(255,255,255,0);}100%{box-shadow:0 0 0 0 rgba(255,255,255,0);}}
@keyframes shake{0%,100%{transform:translateX(0);}20%{transform:translateX(-8px);}40%{transform:translateX(8px);}60%{transform:translateX(-6px);}80%{transform:translateX(6px);}}
.hero{background:linear-gradient(135deg,#1e3a8a,#7c3aed 55%,#db2777);border-radius:26px;padding:2.4rem 2rem;text-align:center;color:#fff;box-shadow:0 12px 34px rgba(124,58,237,.35);margin-bottom:1.4rem;}
.hero-t{font-size:3.4rem;font-weight:900;letter-spacing:1px;line-height:1.1;}
.hero-s{font-size:1.7rem;font-style:italic;margin-top:.5rem;opacity:.95;}
.hero-d{font-size:1.2rem;margin-top:1rem;opacity:.92;}
.mcard{background:#111827;border:3px solid var(--c);border-radius:20px;padding:1.1rem .6rem;text-align:center;color:#f8fafc;box-shadow:0 6px 18px rgba(0,0,0,.35);transition:all .25s;margin-bottom:.6rem;}
.mcard:hover{transform:translateY(-5px);box-shadow:0 10px 26px var(--c);}
.mcard .e{font-size:3rem;}
.mcard .n{font-weight:800;font-size:1.15rem;margin-top:.2rem;}
.mcard .t{font-size:.9rem;opacity:.75;margin-top:.2rem;}
.mcard.done{background:linear-gradient(180deg,#052e16,#111827);}
.mhead{display:flex;align-items:center;gap:1rem;padding:1rem 1.4rem;border-radius:20px;color:#fff;background:linear-gradient(135deg,var(--c),#0f172a);margin-bottom:1rem;}
.mh-e{font-size:3.4rem;}
.mh-t{font-size:2.3rem;font-weight:900;line-height:1.1;}
.mh-s{font-size:1.15rem;opacity:.9;}
.sec{font-size:1.5rem;font-weight:800;margin:1.1rem 0 .5rem 0;}
.meta{background:#1e293b;color:#f1f5f9;border-left:8px solid var(--c);border-radius:14px;padding:1rem 1.3rem;font-size:1.25rem;line-height:1.5;margin-bottom:1rem;}
.meta b{display:block;font-size:1.3rem;margin-bottom:.3rem;color:var(--c);}
.how{display:grid;grid-template-columns:repeat(3,1fr);gap:.8rem;}
.how div{background:#111827;color:#f8fafc;border-top:5px solid var(--c);border-radius:14px;padding:.9rem 1rem;font-size:1.1rem;animation:fadein .5s both;}
.how span{display:block;font-size:2rem;margin-bottom:.2rem;}
.guide{background:linear-gradient(135deg,#78350f,#b45309);color:#fff;border-radius:16px;padding:1rem 1.4rem;font-size:1.3rem;line-height:1.5;margin-bottom:.8rem;}
.guide b{display:block;font-size:1.1rem;opacity:.85;margin-bottom:.2rem;}
.tip{background:#082f49;color:#e0f2fe;border-radius:12px;padding:.7rem 1rem;font-size:1.05rem;}
.pc{border-radius:14px;padding:.7rem 1rem;margin-bottom:.5rem;font-size:1.15rem;color:#f8fafc;background:#111827;}
.pc.pro{border-left:7px solid #22c55e;}
.pc.con{border-left:7px solid #f97316;}
.pc.ex{border-left:7px solid #38bdf8;}
.stage{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:.5rem;margin:.6rem 0;}
.stage.v{flex-direction:column;}
.node{min-width:125px;text-align:center;background:#1f2937;color:#e5e7eb;border:3px solid #374151;border-radius:16px;padding:.7rem .6rem;opacity:.55;transition:all .3s;}
.node .ne{font-size:2.2rem;}
.node .nl{font-size:.95rem;font-weight:700;}
.node.done{opacity:1;border-color:#22c55e;background:#14532d;}
.node.active{opacity:1;border-color:var(--c);background:var(--c);color:#fff;transform:scale(1.1);animation:pulse 1.2s infinite;}
.arrow{font-size:1.5rem;opacity:.7;}
.banner{margin-top:.8rem;padding:1rem 1.4rem;border-radius:14px;background:#0f172a;border-left:8px solid var(--c);color:#f8fafc;}
.banner .bt{font-size:1.4rem;font-weight:700;}
.pbar{height:8px;border-radius:8px;background:#334155;margin-top:.7rem;overflow:hidden;}
.pbar div{height:100%;transition:width .4s;}
.layers{max-width:560px;margin:0 auto;}
.roof{text-align:center;font-size:1.3rem;font-weight:800;padding:.5rem;background:#334155;color:#f8fafc;border-radius:16px 16px 0 0;}
.layer{background:#1e293b;color:#f1f5f9;border:3px solid #475569;border-top:none;padding:.9rem 1.3rem;font-size:1.25rem;display:flex;flex-direction:column;opacity:.6;transition:all .25s;}
.layer span{font-size:.95rem;opacity:.85;}
.layer.sel{opacity:1;background:var(--c);border-color:#fff;transform:scale(1.03);box-shadow:0 0 22px var(--c);}
.layer:last-child{border-radius:0 0 16px 16px;}
.expl{background:#111827;color:#f8fafc;border:3px solid var(--c);border-radius:18px;padding:1.2rem 1.4rem;font-size:1.3rem;line-height:1.5;animation:fadein .4s both;}
.expl b{font-size:1.5rem;display:block;margin-bottom:.4rem;}
.expl i{display:block;margin-top:.7rem;opacity:.8;font-size:1.1rem;}
.svcgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:.8rem;margin:.6rem 0;}
.svc{text-align:center;background:#111827;color:#f8fafc;border:3px solid #22c55e;border-radius:18px;padding:1rem .5rem;}
.svc .se{font-size:2.6rem;}
.svc .sn{font-weight:800;font-size:1.1rem;}
.svc .ss{font-size:.95rem;margin-top:.2rem;color:#86efac;}
.svc.down{border-color:#ef4444;background:#450a0a;animation:shake .6s;}
.svc.down .ss{color:#fca5a5;font-weight:800;}
.alert{border-radius:14px;padding:1rem 1.3rem;font-size:1.3rem;margin-top:.5rem;color:#fff;}
.alert.ok{background:#14532d;}
.alert.bad{background:#7c2d12;}
.mvcrow{display:grid;grid-template-columns:repeat(3,1fr);gap:.8rem;margin-top:.5rem;}
.mvcrow div{background:#111827;color:#f8fafc;border-radius:16px;padding:1rem;text-align:center;font-size:1.05rem;border-top:6px solid var(--c);}
.mvcrow span{display:block;font-size:2.4rem;}
.mvcrow b{display:block;font-size:1.2rem;}
.mvctop{text-align:center;font-size:1.8rem;font-weight:900;color:#fff;background:#78350f;border-radius:14px;padding:.5rem;max-width:260px;margin:0 auto;}
.mvcline{text-align:center;font-size:1.6rem;opacity:.7;}
.q{background:#1e1b4b;color:#f8fafc;border-radius:18px;padding:1.1rem 1.4rem;font-size:1.4rem;margin-bottom:.8rem;border-left:8px solid var(--c);}
.res{border-radius:16px;padding:1rem 1.3rem;margin-top:.8rem;font-size:1.2rem;color:#fff;animation:fadein .4s both;}
.res.ok{background:#14532d;}
.res.bad{background:#7f1d1d;}
.res b{font-size:1.5rem;display:block;}
.score{display:inline-block;background:linear-gradient(90deg,#f59e0b,#ef4444);color:#fff;font-size:1.8rem;font-weight:900;padding:.4rem 1.4rem;border-radius:40px;}
.cmp{width:100%;border-collapse:collapse;font-size:1.1rem;color:#f8fafc;}
.cmp th{background:#312e81;padding:.7rem;text-align:left;}
.cmp td{padding:.7rem;border-bottom:1px solid #334155;background:#111827;}
.cmp tr.hl td{background:var(--c);color:#fff;font-weight:700;}
.chip{display:inline-block;background:#1e293b;color:#f8fafc;border:2px solid #475569;border-radius:30px;padding:.4rem 1rem;margin:.2rem;font-size:1.15rem;}
.introd{text-align:center;color:#f8fafc;}
.ibox{display:inline-block;background:#1e293b;border:3px solid #475569;border-radius:16px;padding:.7rem 1.4rem;font-size:1.3rem;font-weight:800;margin:.2rem;transition:all .25s;}
.ibox.sel{background:#7c3aed;border-color:#fff;box-shadow:0 0 22px #7c3aed;transform:scale(1.07);}
.ibox.final{background:linear-gradient(90deg,#2563eb,#db2777);border-color:#fff;}
.iline{font-size:1.5rem;opacity:.7;line-height:1.1;}
.final-card{text-align:center;background:linear-gradient(135deg,#065f46,#1e3a8a);color:#fff;border-radius:26px;padding:2rem;margin-bottom:1rem;}
.final-card .big{font-size:3rem;font-weight:900;}
@media (max-width:900px){.how,.svcgrid,.mvcrow{grid-template-columns:1fr;}.hero-t{font-size:2.2rem;}}
"""

# =====================================================================
# 3) UTILIDADES
# =====================================================================


def H(s: str) -> str:
    """Compacta HTML en una sola línea (evita que Markdown lo trate como código)."""
    return "".join(line.strip() for line in s.splitlines())


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;")


def html(s: str):
    st.markdown(H(s), unsafe_allow_html=True)


def sec(title: str):
    html(f'<div class="sec">{title}</div>')


def init_state():
    """Todo el progreso vive en st.session_state (no se pierde al cambiar de sección)."""
    defaults = {
        "nav": P_HOME,
        "visited": set(),       # modelos explorados
        "mini": {},             # respuestas de los retos por modelo
        "quiz": {},             # respuestas del reto final
        "quiz_idx": 0,          # caso actual del reto final
        "extra": {"model": None, "reason": None, "text": "", "done": False},
        "sim": {},              # estado de cada simulación
        "layer": "pres",        # capa seleccionada
        "ms_mode": "normal",    # microservicios: normal / fail
        "intro_sel": None,      # introducción: componentes / comunicación
        "balloons": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def quiz_score() -> int:
    return sum(1 for i, a in st.session_state.quiz.items() if a == int(i[1:]))


def n_visited() -> int:
    return len(st.session_state.visited)


# ---- callbacks (se ejecutan ANTES de volver a dibujar la página) ----

def go(page: str):
    st.session_state.nav = page


def reset_challenge():
    st.session_state.quiz = {}
    st.session_state.quiz_idx = 0
    st.session_state.extra = {"model": None, "reason": None, "text": "", "done": False}
    st.session_state.balloons = False
    st.session_state.nav = P_QUIZ


def reset_all():
    reset_challenge()
    st.session_state.visited = set()
    st.session_state.mini = {}
    st.session_state.sim = {}
    st.session_state.layer = "pres"
    st.session_state.ms_mode = "normal"
    st.session_state.intro_sel = None
    st.session_state.nav = P_HOME


def set_state(key, value):
    st.session_state[key] = value


def answer(store: str, qid: str, idx: int):
    st.session_state[store][qid] = idx


def clear_answer(store: str, qid: str):
    st.session_state[store].pop(qid, None)


def next_case():
    st.session_state.quiz_idx += 1


def set_extra(key, value):
    st.session_state.extra[key] = value


def finish_extra():
    st.session_state.extra["text"] = st.session_state.get("extra_text_widget", "").strip()
    st.session_state.extra["done"] = True


# =====================================================================
# 4) COMPONENTES VISUALES REUTILIZABLES
# =====================================================================


def stage_html(nodes, active, color, vertical=False):
    """Cadena de nodos. Los anteriores al activo se marcan como completados."""
    arrow = "⬇️" if vertical else "➡️"
    parts = []
    for i, (emo, label) in enumerate(nodes):
        cls = "node"
        if active >= 0:
            cls += " active" if i == active else (" done" if i < active else "")
        parts.append(f'<div class="{cls}" style="--c:{color}"><div class="ne">{emo}</div>'
                     f'<div class="nl">{esc(label)}</div></div>')
        if i < len(nodes) - 1:
            parts.append(f'<div class="arrow">{arrow}</div>')
    return f'<div class="stage{" v" if vertical else ""}">{"".join(parts)}</div>'


def banner_html(text, color, pct):
    return (f'<div class="banner" style="--c:{color}"><div class="bt">{esc(text)}</div>'
            f'<div class="pbar"><div style="width:{pct}%;background:{color}"></div></div></div>')


def sim_block(key, label, nodes, steps, actives, color, vertical=False, delay=1.1):
    """Simulación paso a paso. El último paso queda guardado en session_state."""
    st.session_state.sim.setdefault(key, -1)
    clicked = st.button(label, key=f"btn_{key}", type="primary")
    holder = st.empty()

    def draw(i):
        if i < 0:
            txt, pct, act = "👆 Pulsa el botón para iniciar la simulación", 0, -1
        else:
            txt, pct, act = steps[i], int((i + 1) / len(steps) * 100), actives[i]
        holder.markdown(H(stage_html(nodes, act, color, vertical) + banner_html(txt, color, pct)),
                        unsafe_allow_html=True)

    if clicked:
        for i in range(len(steps)):
            st.session_state.sim[key] = i
            draw(i)
            time.sleep(delay)
    else:
        draw(st.session_state.sim[key])


def quiz_card(store, qid, question, options, correct, explanation, color, retry=True):
    """Pregunta con botones. Respuesta guardada en session_state[store]."""
    ans = st.session_state[store].get(qid)
    html(f'<div class="q" style="--c:{color}">{esc(question)}</div>')
    cols = st.columns(len(options))
    for i, opt in enumerate(options):
        with cols[i]:
            st.button(opt, key=f"{store}_{qid}_{i}", on_click=answer, args=(store, qid, i),
                      disabled=ans is not None, type="primary" if ans == i else "secondary")
    if ans is not None:
        if ans == correct:
            html(f'<div class="res ok"><b>✅ CORRECTO</b>{esc(explanation)}</div>')
        else:
            html(f'<div class="res bad"><b>❌ INCORRECTO</b>La respuesta correcta era: '
                 f'{esc(options[correct])}. {esc(explanation)}</div>')
        if retry:
            st.button("🔁 Intentar de nuevo", key=f"retry_{store}_{qid}",
                      on_click=clear_answer, args=(store, qid))
    return ans


def model_header(m):
    html(f'<div class="mhead" style="--c:{m["color"]}"><span class="mh-e">{m["emoji"]}</span>'
         f'<div><div class="mh-t">{esc(m["name"])}</div><div class="mh-s">{m["tag"]}</div></div></div>')


def how_cards(c, color):
    items = "".join(f'<div><span>{n}</span>{esc(t)}</div>'
                    for n, t in zip(["1️⃣", "2️⃣", "3️⃣"], c["how"]))
    html(f'<div class="how" style="--c:{color}">{items}</div>')


def metaphor_box(c, color):
    html(f'<div class="meta" style="--c:{color}"><b>{c["meta_title"]}</b>{esc(c["metaphor"])}</div>')


# ---- diagramas estáticos ----

def layers_building_html(selected):
    rows = ['<div class="roof">🏢 SISTEMA</div>']
    for lid, emo, name, desc, color, _, _ in LAYERS:
        cls = "layer sel" if lid == selected else "layer"
        rows.append(f'<div class="{cls}" style="--c:{color}"><b>{emo} {name}</b><span>{desc}</span></div>')
    return f'<div class="layers">{"".join(rows)}</div>'


CS_NODES = [("👤", "CLIENTE"), ("📨", "Solicitud"), ("🖥️", "SERVIDOR"), ("🗄️", "BASE DE DATOS"),
            ("🖥️", "SERVIDOR"), ("📨", "Respuesta"), ("👤", "CLIENTE")]
MVC_NODES = [("👤", 'Usuario pulsa "Comprar"'), ("🎛️", "Controlador"), ("🧠", "Modelo"),
             ("💾", "Actualiza información"), ("👁️", "Vista"), ("✅", '"Compra realizada"')]
PF_NODES = [("💻", "Código fuente"), ("🔍", "Análisis léxico"), ("🧩", "Análisis sintáctico"),
            ("🧠", "Análisis semántico"), ("⚙️", "Generación de código"), ("✅", "Código generado")]
FACTORY_NODES = [("📦", "ENTRADA"), ("🔍", "FILTRO 1"), ("⚙️", "FILTRO 2"), ("🔧", "FILTRO 3"),
                 ("📦", "RESULTADO")]
LAYER_FLOW_NODES = [("👤", "Usuario"), ("🖼️", "Presentación"), ("🧠", "Lógica de negocio"),
                    ("🔌", "Acceso a datos"), ("🗄️", "Base de datos"), ("✅", "Respuesta en pantalla")]


def mvc_diagram_html(color):
    return (f'<div class="mvctop">🎬 MVC</div><div class="mvcline">│<br>┌──────┼──────┐<br>↓ ↓ ↓</div>'
            f'<div class="mvcrow" style="--c:{color}">'
            '<div><span>🧠</span><b>MODELO</b>Administra los datos y la lógica relacionada con ellos.</div>'
            '<div><span>👁️</span><b>VISTA</b>Es lo que el usuario observa.</div>'
            '<div><span>🎛️</span><b>CONTROLADOR</b>Recibe las acciones del usuario y coordina lo que debe suceder.</div>'
            '</div>')


def services_html(fail):
    cards = []
    for emo, name in SERVICES:
        down = fail and name == "PAGOS"
        cls = "svc down" if down else "svc"
        status = "❌ FUERA DE SERVICIO" if down else "✅ Funcionando"
        cards.append(f'<div class="{cls}"><div class="se">{emo}</div><div class="sn">{name}</div>'
                     f'<div class="ss">{status}</div></div>')
    return f'<div class="svcgrid">{"".join(cards)}</div>'


# =====================================================================
# 5) PÁGINAS GENERALES
# =====================================================================


def sidebar():
    with st.sidebar:
        st.markdown("## 🏗️ Arquitectos de Software")
        st.caption("Construye el sistema correcto")
        st.radio("Navegación", PAGES, key="nav", label_visibility="collapsed")
        st.divider()
        st.progress(n_visited() / 5, text=f"📘 Modelos explorados: {n_visited()} / 5")
        st.progress(quiz_score() / 5, text=f"🏆 Puntuación: {quiz_score()} / 5")
        st.divider()
        st.select_slider("🔎 Zoom para proyector (%)", options=[100, 115, 130, 150], value=100, key="zoom")
        st.button("🧹 Reiniciar toda la exposición", on_click=reset_all)
    z = st.session_state.get("zoom", 100) / 100
    st.markdown(f"<style>.block-container{{zoom:{z};}}</style>", unsafe_allow_html=True)


def page_home():
    html('<div class="hero"><div class="hero-t">🏗️ ARQUITECTOS DE SOFTWARE</div>'
         '<div class="hero-s">"Construye el sistema correcto"</div>'
         '<div class="hero-d">Una experiencia interactiva para comprender 5 modelos de arquitectura de software</div></div>')
    cols = st.columns(5)
    for col, m in zip(cols, MODELS):
        done = "done" if m["id"] in st.session_state.visited else ""
        with col:
            html(f'<div class="mcard {done}" style="--c:{m["color"]}"><div class="e">{m["emoji"]}</div>'
                 f'<div class="n">{esc(m["short"])}</div><div class="t">{m["tag"]}</div></div>')
            st.button("Abrir", key=f"open_{m["id"]}", on_click=go, args=(m["page"],))
    st.write("")
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.button("▶️ COMENZAR EXPOSICIÓN", key="start", on_click=go, args=(P_INTRO,), type="primary")
        st.progress(n_visited() / 5, text=f"{n_visited()} / 5 modelos")


def page_intro():
    html('<div class="mhead" style="--c:#7c3aed"><span class="mh-e">🧠</span><div>'
         '<div class="mh-t">¿Qué es una arquitectura de software?</div>'
         '<div class="mh-s">Antes de conocer los modelos, entendamos la idea</div></div></div>')
    sel = st.session_state.intro_sel

    def box(k, txt):
        return f'<div class="ibox{" sel" if sel == k else ""}">{txt}</div>'

    c1, c2 = st.columns([1.1, 1])
    with c1:
        html('<div class="introd"><div class="ibox">🏠 SISTEMA</div><div class="iline">│<br>┌────────┴────────┐</div>'
             f'{box("comp", "🧩 Componentes")}{box("com", "🔗 Comunicación")}'
             '<div class="iline">└────────┬────────┘<br>↓</div><div class="ibox final">🏗️ ARQUITECTURA</div></div>')
    with c2:
        html('<div class="meta" style="--c:#7c3aed"><b>💡 En una frase</b>La arquitectura de software define cómo se '
             'organizan las diferentes partes de un sistema y cómo se comunican entre ellas.</div>')
        b1, b2 = st.columns(2)
        b1.button("🧩 Componentes", key="b_comp", on_click=set_state, args=("intro_sel", "comp"),
                  type="primary" if sel == "comp" else "secondary")
        b2.button("🔗 Comunicación", key="b_com", on_click=set_state, args=("intro_sel", "com"),
                  type="primary" if sel == "com" else "secondary")
        if sel == "comp":
            html('<div class="expl" style="--c:#7c3aed"><b>🧩 Componentes</b>Son las piezas del sistema: pantallas, '
                 'módulos, servicios y bases de datos. Como las habitaciones de una casa.</div>')
        elif sel == "com":
            html('<div class="expl" style="--c:#7c3aed"><b>🔗 Comunicación</b>Es la forma en que las piezas se hablan: '
                 'peticiones, mensajes y llamadas. Como los pasillos y las puertas de una casa.</div>')
        else:
            html('<div class="expl" style="--c:#7c3aed">👆 Pulsa un botón para ver su explicación.</div>')
    if sel:
        st.write("")
        html('<div class="meta" style="--c:#ec4899"><b>🏗️ Sin arquitectura…</b>Sería como construir una casa sin planos. '
             'Existen diferentes formas de organizar un sistema.</div>')
    with st.expander("🎤 GUÍA PARA EXPONER"):
        st.write("Puedes decir: «Antes de ver los modelos, pensemos en una casa. Tiene habitaciones (componentes) y "
                 "pasillos (comunicación). La arquitectura es el plano que decide cómo se organiza todo.»")
    st.write("")
    st.button("➡️ CONOCER LOS 5 MODELOS", key="to_models", on_click=go, args=(MODELS[0]["page"],), type="primary")


# =====================================================================
# 6) PÁGINAS DE MODELOS
# =====================================================================


def tab_idea(m, c):
    color = m["color"]
    metaphor_box(c, color)
    mid = m["id"]
    if mid == "capas":
        sec("🏢 Toca cada piso del edificio")
        cols = st.columns(4)
        for col, (lid, emo, name, _, _, _, _) in zip(cols, LAYERS):
            col.button(f"{emo} {name.title()}", key=f"layer_{lid}", on_click=set_state,
                       args=("layer", lid), type="primary" if st.session_state.layer == lid else "secondary")
        sel = st.session_state.layer
        left, right = st.columns([1.1, 1])
        with left:
            html(layers_building_html(sel))
        with right:
            _, emo, name, _, lcolor, text, ex = next(l for l in LAYERS if l[0] == sel)
            html(f'<div class="expl" style="--c:{lcolor}"><b>{emo} {name}</b>{esc(text)}<i>{esc(ex)}</i></div>')
    elif mid == "cs":
        sec("🔄 El viaje de una solicitud")
        html(stage_html(CS_NODES, -1, color))
    elif mid == "mvc":
        html(mvc_diagram_html(color))
    elif mid == "micro":
        sec("🏙️ Un sistema hecho de servicios independientes")
        html(services_html(False))
    elif mid == "pf":
        sec("🏭 La línea de producción")
        html(stage_html(FACTORY_NODES, -1, color))
    sec("⚙️ ¿Cómo funciona?")
    how_cards(c, color)


def tab_sim(m, c):
    mid, color = m["id"], m["color"]
    if mid == "capas":
        sec("Mira cómo una petición baja y sube por las capas")
        sim_block("capas", "▶️ VER UNA PETICIÓN RECORRER LAS CAPAS", LAYER_FLOW_NODES,
                  ['El usuario pulsa "Ver mis pedidos".',
                   "La capa de Presentación envía la acción a la lógica.",
                   "La Lógica de negocio valida y decide qué datos necesita.",
                   "El Acceso a datos arma la consulta.",
                   "La Base de datos devuelve la información.",
                   "La respuesta sube capa por capa y aparece en pantalla."],
                  [0, 1, 2, 3, 4, 5], color, vertical=False)
    elif mid == "cs":
        sec("Simulación de una solicitud")
        sim_block("cs", "▶️ VER SOLICITUD EN ACCIÓN", CS_NODES,
                  ["El cliente solicita información...", "El servidor recibe la solicitud...",
                   "El servidor consulta los datos...", "La base de datos responde...",
                   "El servidor envía la respuesta...", "El cliente recibe la información."],
                  [0, 2, 3, 3, 5, 6], color)
    elif mid == "mvc":
        sec("Simulación: comprar en una tienda")
        sim_block("mvc", "▶️ SIMULAR COMPRA", MVC_NODES,
                  ['El usuario pulsa el botón "Comprar".',
                   "El Controlador recibe la acción y coordina.",
                   "El Controlador le pide al Modelo que actúe.",
                   "El Modelo actualiza la información (stock, pedido).",
                   "La Vista toma los datos nuevos del Modelo.",
                   'La Vista muestra: "Compra realizada" ✅'],
                  [0, 1, 2, 3, 4, 5], color)
    elif mid == "micro":
        sec("¿Qué pasa si un servicio falla?")
        b1, b2 = st.columns(2)
        mode = st.session_state.ms_mode
        b1.button("▶️ FUNCIONAMIENTO NORMAL", key="ms_normal", on_click=set_state, args=("ms_mode", "normal"),
                  type="primary" if mode == "normal" else "secondary")
        b2.button("💥 SIMULAR FALLA DE PAGOS", key="ms_fail", on_click=set_state, args=("ms_mode", "fail"),
                  type="primary" if mode == "fail" else "secondary")
        html(services_html(mode == "fail"))
        if mode == "fail":
            html('<div class="alert bad">💥 El sistema de pagos falló, pero los demás servicios pueden '
                 'continuar funcionando.</div>')
            st.caption("Esto demuestra la independencia de los servicios. En una aplicación única, "
                       "un error en pagos podría detener todo el sistema.")
        else:
            html('<div class="alert ok">✅ Todos los servicios funcionan y cada uno puede crecer por separado.</div>')
    elif mid == "pf":
        sec("Ejemplo: así trabaja un compilador")
        sim_block("pf", "▶️ PROCESAR", PF_NODES,
                  ["Entra el código fuente: x = 2 + 3",
                   "Análisis léxico: separa en piezas → x  =  2  +  3",
                   "Análisis sintáctico: arma la estructura → x = (2 + 3)",
                   "Análisis semántico: revisa que sea válido → números sumados con números ✔",
                   "Generación de código: LOAD 2, ADD 3, STORE x",
                   "Resultado: código generado listo para ejecutarse ✅"],
                  [0, 1, 2, 3, 4, 5], color, delay=1.3)


def tab_examples(m, c):
    with st.expander("🌍 Ejemplos", expanded=False):
        for e in c["examples"]:
            html(f'<div class="pc ex">{esc(e)}</div>')
        if m["id"] == "micro":
            st.write("**App de comida:**")
            html("".join(f'<span class="chip">{e} {n}</span>' for e, n in UBER_COMPONENTS))
    with st.expander("✅ Ventajas", expanded=False):
        for p in c["pros"]:
            html(f'<div class="pc pro">✅ {esc(p)}</div>')
    with st.expander("⚠️ Desventajas", expanded=False):
        for p in c["cons"]:
            html(f'<div class="pc con">⚠️ {esc(p)}</div>')


def tab_guide(m, c):
    html(f'<div class="guide"><b>🎤 PUEDES EXPLICAR:</b>«{esc(c["guide"][0])}»</div>')
    sec("💬 Frases de apoyo")
    for g in c["guide"][1:]:
        html(f'<div class="guide" style="background:#1e293b"><b>➕</b>«{esc(g)}»</div>')
    html(f'<div class="tip">{esc(c["tip"])}</div>')
    sec("✅ No olvides mencionar")
    st.write("**Idea clave** → **Metáfora** → **Demostración** → **Una ventaja y una desventaja** → **Reto para el público**")


def tab_reto(m, c):
    r = c["reto"]
    sec("🧪 RETO PARA EL PÚBLICO")
    quiz_card("mini", m["id"], r["q"], r["options"], r["correct"], r["exp"], m["color"])


def model_page(m):
    st.session_state.visited.add(m["id"])
    c = CONTENT[m["id"]]
    model_header(m)
    tab = st.radio("Sección", TABS, horizontal=True, key=f"tab_{m['id']}", label_visibility="collapsed")
    st.write("")
    if tab == TABS[0]:
        tab_idea(m, c)
    elif tab == TABS[1]:
        tab_sim(m, c)
    elif tab == TABS[2]:
        tab_examples(m, c)
    elif tab == TABS[3]:
        tab_guide(m, c)
    else:
        tab_reto(m, c)
    st.divider()
    i = MODELS.index(m)
    left, right = st.columns(2)
    prev_page = MODELS[i - 1]["page"] if i > 0 else P_INTRO
    left.button("⬅️ ANTERIOR", key=f"prev_{m['id']}", on_click=go, args=(prev_page,))
    if i < len(MODELS) - 1:
        right.button("➡️ SIGUIENTE MODELO", key=f"next_{m['id']}", on_click=go,
                     args=(MODELS[i + 1]["page"],), type="primary")
    else:
        right.button("⚔️ COMPARAR LOS 5 MODELOS", key=f"next_{m['id']}", on_click=go,
                     args=(P_COMP,), type="primary")


# =====================================================================
# 7) COMPARACIÓN, RETO, RESULTADO
# =====================================================================


def page_compare():
    html('<div class="mhead" style="--c:#6366f1"><span class="mh-e">⚔️</span><div>'
         '<div class="mh-t">Compara los 5 modelos</div><div class="mh-s">Elige uno para resaltarlo</div></div></div>')
    options = ["Ver todos"] + [f'{m["emoji"]} {m["short"]}' for m in MODELS]
    choice = st.radio("Resaltar", options, horizontal=True, key="cmp_choice", label_visibility="collapsed")
    rows = []
    for idx, m in enumerate(MODELS):
        idea, ex, pro, con = COMPARE[m["id"]]
        hl = choice == options[idx + 1]
        rows.append(f'<tr class="{"hl" if hl else ""}" style="--c:{m["color"]}">'
                    f'<td>{m["emoji"]} {esc(m["short"])}</td><td>{esc(idea)}</td><td>{esc(ex)}</td>'
                    f'<td>{esc(pro)}</td><td>{esc(con)}</td></tr>')
    html('<table class="cmp"><tr><th>Modelo</th><th>Idea principal</th><th>Ejemplo</th><th>Ventaja</th>'
         f'<th>Punto débil</th></tr>{"".join(rows)}</table>')
    if choice != "Ver todos":
        m = MODELS[options.index(choice) - 1]
        c = CONTENT[m["id"]]
        st.write("")
        html(f'<div class="expl" style="--c:{m["color"]}"><b>{m["emoji"]} {esc(m["name"])}</b>'
             f'{esc(c["metaphor"])}<i>Ejemplos: {esc(" · ".join(c["examples"]))}</i></div>')
    st.write("")
    html('<div class="meta" style="--c:#6366f1"><b>💡 Recuerda</b>No hay un modelo "mejor" para todo. '
         'Cada uno resuelve un problema distinto y, en sistemas reales, se combinan.</div>')
    st.button("🎯 IR AL RETO", key="cmp_to_quiz", on_click=go, args=(P_QUIZ,), type="primary")


def extra_challenge():
    ex = st.session_state.extra
    st.divider()
    html('<div class="mhead" style="--c:#f97316"><span class="mh-e">🍔</span><div>'
         '<div class="mh-t">Diseñemos un sistema</div>'
         '<div class="mh-s">Tenemos que construir una aplicación parecida a Uber Eats</div></div></div>')
    html("".join(f'<span class="chip">{e} {n}</span>' for e, n in UBER_COMPONENTS))
    sec("1️⃣ ¿Qué arquitectura elegirías?")
    cols = st.columns(5)
    for col, m in zip(cols, MODELS):
        col.button(f'{m["emoji"]} {m["short"]}', key=f"ex_model_{m['id']}", on_click=set_extra,
                   args=("model", m["id"]), type="primary" if ex["model"] == m["id"] else "secondary")
    if ex["model"] and not ex["done"]:
        sec("2️⃣ ¿Por qué elegiste este modelo?")
        for i, r in enumerate(UBER_REASONS):
            st.button(r, key=f"ex_reason_{i}", on_click=set_extra, args=("reason", i),
                      type="primary" if ex["reason"] == i else "secondary")
        st.text_area("✍️ Escribe tu razón (opcional)", key="extra_text_widget", height=80)
        if ex["reason"] is not None:
            st.button("💡 VER EXPLICACIÓN SUGERIDA", key="ex_done", on_click=finish_extra, type="primary")
    if ex["done"] and ex["model"]:
        m = MODEL_BY_ID[ex["model"]]
        fit, care = UBER_ANALYSIS[m["id"]]
        sec(f'💡 Sobre tu elección: {m["emoji"]} {m["short"]}')
        html(f'<div class="pc pro">✅ <b>Por qué puede funcionar:</b> {esc(fit)}</div>')
        html(f'<div class="pc con">⚠️ <b>Qué cuidar:</b> {esc(care)}</div>')
        if ex["reason"] is not None:
            html(f'<div class="pc ex">🗣️ <b>Tu razón:</b> {esc(UBER_REASONS[ex["reason"]])}</div>')
        if ex["text"]:
            html(f'<div class="pc ex">✍️ <b>Tus palabras:</b> {esc(ex["text"])}</div>')
        html('<div class="meta" style="--c:#f97316"><b>🧭 No existe una única respuesta correcta</b>'
             'La mejor arquitectura depende de los requisitos del sistema (tamaño, equipo, crecimiento, tiempo) '
             'y diferentes arquitecturas pueden combinarse. Una posible combinación para esta app:</div>')
        for line in UBER_COMBO:
            html(f'<div class="pc ex">{esc(line)}</div>')
        st.write("")
        st.button("🏆 VER RESULTADO FINAL", key="to_result", on_click=go, args=(P_RES,), type="primary")


def page_quiz():
    score = quiz_score()
    idx = st.session_state.quiz_idx
    html('<div class="mhead" style="--c:#ef4444"><span class="mh-e">🚨</span><div>'
         '<div class="mh-t">¿Qué arquitectura utilizarías?</div>'
         '<div class="mh-s">Reto final: 5 situaciones</div></div></div>')
    html(f'<div style="text-align:center"><span class="score">🏆 PUNTUACIÓN: {score} / 5</span></div>')
    st.write("")
    if idx < len(CASES):
        st.progress(idx / len(CASES), text=f"Caso {idx + 1} de {len(CASES)}")
        sec(f"Caso {idx + 1}")
        text, exp = CASES[idx]
        options = [f'{m["emoji"]} {m["short"]}' for m in MODELS]
        ans = quiz_card("quiz", f"c{idx}", text, options, idx, exp, "#ef4444", retry=False)
        if ans is not None:
            st.write("")
            label = "➡️ SIGUIENTE CASO" if idx < len(CASES) - 1 else "🏁 TERMINAR Y VER RETO EXTRA"
            st.button(label, key=f"nextcase_{idx}", on_click=next_case, type="primary")
    else:
        st.progress(1.0, text="Reto completado")
        st.success(f"🎉 ¡Terminaste los 5 casos! Obtuviste {score} de 5.")
        extra_challenge()


def page_result():
    score = quiz_score()
    finished = st.session_state.quiz_idx >= len(CASES)
    if finished and not st.session_state.balloons:
        st.balloons()
        st.session_state.balloons = True
    html('<div class="final-card"><div class="big">🎉 ¡MISIÓN COMPLETADA!</div>'
         '<div style="font-size:1.5rem;margin-top:.5rem">Ahora conoces 5 modelos de arquitectura de software.</div></div>')
    cols = st.columns(5)
    for col, m in zip(cols, MODELS):
        done = m["id"] in st.session_state.visited
        with col:
            html(f'<div class="mcard {"done" if done else ""}" style="--c:{m["color"]}"><div class="e">{m["emoji"]}</div>'
                 f'<div class="n">{esc(m["short"])} {"✅" if done else "⬜"}</div></div>')
    if n_visited() < 5:
        st.info(f"Aún faltan {5 - n_visited()} modelo(s) por explorar (marcados con ⬜).")
    st.write("")
    html(f'<div style="text-align:center"><span class="score">🏆 PUNTUACIÓN FINAL: {score} / 5</span></div>')
    if not finished:
        st.warning("Todavía no terminaste el reto final. Ve a 🎯 Reto para completarlo.")
    elif score == 5:
        st.success("🌟 ¡Puntuación perfecta! Eres un verdadero arquitecto de software.")
    elif score >= 3:
        st.success("👏 ¡Muy bien! Ya dominas casi todos los modelos.")
    else:
        st.info("💪 ¡Buen intento! Repite el reto para reforzar los conceptos.")
    st.write("")
    c1, c2 = st.columns(2)
    c1.button("🔄 REPETIR RETO", key="repeat", on_click=reset_challenge, type="primary")
    c2.button("🏠 VOLVER AL INICIO", key="home", on_click=go, args=(P_HOME,))


# =====================================================================
# 8) PROGRAMA PRINCIPAL
# =====================================================================


def main():
    init_state()
    st.markdown("<style>" + H(CSS) + "</style>", unsafe_allow_html=True)
    sidebar()
    page = st.session_state.nav
    if page == P_HOME:
        page_home()
    elif page == P_INTRO:
        page_intro()
    elif page in MODEL_BY_PAGE:
        model_page(MODEL_BY_PAGE[page])
    elif page == P_COMP:
        page_compare()
    elif page == P_QUIZ:
        page_quiz()
    else:
        page_result()


main()