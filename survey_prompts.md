# Participant Prompts

Full prompt texts submitted by each participant in response to the product brief. Prompts are reproduced verbatim; no editing was applied. Participant IDs correspond to `survey_responses.csv`.

---

## P1 — Minimal Extraction (95 words, Portuguese)

> Quero que você atue como uma pessoa especialista em UX e UI Design e desenvolva uma proposta de interface para o gerenciamento de frota logística. A interface precisa ser clara e objetiva, com foco na exibição de informações como:
>
> - Nome do motorista
> - Nome da empresa
> - Tempo até entrega
> - Possível atraso da entrega
> - Lista de todos os motoristas em atividade
>
> Requisitos para o sistema
>
> - Cores claras com elementos leves
> - Exibição de informações essenciais
> - Foco no gerenciamento da entrega
> - Sistema leve e otimizado com armazenamento de dados off-line

**Stated rationale:** Analyzed the briefing and used the most important information such as the area of operation, solution objective, and infrastructure limitation.

---

## P2 — Contextual Specification (297 words, Portuguese)

> Projete uma interface de plataforma B2B para gerenciamento de frotas logísticas, focada no uso por coordenadores operacionais que precisam monitorar e gerenciar até 50 motoristas simultaneamente em tempo real.
>
> O sistema deve priorizar velocidade de decisão, clareza visual e resposta rápida a problemas, já que o coordenador precisa garantir prazos de entrega, resolver conflitos de rota e lidar com imprevistos ao longo do dia.
>
> Contexto crítico de uso:
> - Operação em regiões rurais com infraestrutura precária
> - Conectividade limitada ou instável
> - Uso frequente em desktop, mas com necessidade de adaptação para tablet
>
> Principais funcionalidades da interface:
> - Dashboard em tempo real com status dos motoristas (em rota, atrasado, parado, concluído)
> - Mapa interativo com localização dos veículos
> - Alertas inteligentes (atrasos, desvios de rota, paradas longas)
> - Lista priorizada de ocorrências críticas
> - Comunicação rápida com motoristas (chat ou ações rápidas)
> - Filtros por região, status e prioridade
> - Linha do tempo das entregas
>
> Diretrizes de UX/UI:
> - Design altamente funcional e objetivo (evitar excesso visual)
> - Hierarquia clara de informações (o que é urgente deve se destacar)
> - Uso de cores para status (verde, amarelo, vermelho)
> - Interface resiliente: deve funcionar bem mesmo com baixa conexão (offline-first ou baixa carga de dados)
> - Componentes grandes e legíveis (pensando em uso em campo)
> - Feedback visual imediato para ações
>
> Estilo visual:
> - Profissional, robusto e confiável (estética próxima a sistemas industriais/logísticos)
> - Inspiração em dashboards de operações e controle
> - Paleta sóbria com acentos de cor para alertas
>
> Entregáveis esperados:
> - Tela principal (dashboard)
> - Visualização de mapa com veículos
> - Painel de alertas
> - Tela de detalhes do motorista/rota
> - Versão responsiva (tablet)
>
> O foco principal deve ser tomada de decisão rápida sob pressão, com uma experiência clara, eficiente e confiável mesmo em ambientes adversos.

**Stated rationale:** The product logic is to allow the coordinator to manage many drivers at once with speed and clarity, having a real-time view of the operation to identify and prioritize problems immediately. The interface needs to be simple, direct, and visual, highlighting what requires urgent action and facilitating quick decisions. Since usage occurs in regions with unstable internet, the system must be light, reliable, and work well even with low connectivity.

---

## P3 — Exhaustive Specification (~2100 words, English)

> Role: Act as a World-Class Senior Product Designer, UX Strategist, and Lead Systems Designer specialized in B2B operational dashboards for logistics and dispatch control.
>
> Objective: Design a high-fidelity, production-ready "1:1 Pixel Perfect" fleet management interface for a B2B logistics operation. The user is a logistics coordinator responsible for monitoring and managing 50 drivers simultaneously throughout the day, ensuring delivery deadlines are met and operational conflicts are resolved in real time.
>
> Product Context: This is not a generic SaaS dashboard. It is a mission-critical dispatch console used for live fleet orchestration. The interface must help the coordinator instantly understand who is delayed, who is off-route, which deliveries are at risk, and what action should be taken next. The design must prioritize visibility, scanning speed, operational triage, and fast intervention, which are core needs in real-time logistics dashboards.
>
> Operational Constraint: Coordinators operate in rural regions with precarious infrastructure. Design for unreliable internet, partial GPS signal loss, slow hardware, glare-prone environments, and long continuous usage. The interface should feel resilient, low-friction, legible, and stable under pressure. Include explicit UX patterns for offline sync states, degraded connectivity, stale location data, and low-bandwidth behavior, since logistics systems need to preserve visibility even when live inputs become incomplete.
>
> Aesthetic Identity: "Rugged Operational Clarity" / "Industrial Mission Control." The product should feel like a fusion of a rural field operations console, a modern dispatch center, and a robust enterprise control tower. Avoid startup marketing aesthetics. Make it functional, dense, calm, and highly actionable.
>
> **1. CORE DESIGN SYSTEM (STRICT)**
>
> Palette:
> - Deep Forest (Primary): #1F3A34
> - Safety Amber (Alert Accent): #F2A93B
> - Earth Clay (Secondary Accent): #C96B3B
> - Mist Gray (Background): #F4F5F3
> - Slate Graphite (Text / Panels): #232B2B
> - Success Green: #2E7D32
> - Critical Red: #C0392B
>
> Typography:
> - Headings: Inter Tight or Plus Jakarta Sans, bold, compact, high legibility
> - Body/UI: Inter, medium/regular, optimized for data density
> - Data/Telemetry: IBM Plex Mono or JetBrains Mono for timestamps, ETAs, route IDs, latency indicators, and sync states
>
> Visual Language:
> - Strong hierarchy, minimal ornament
> - Large-radius system should be restrained: rounded-xl for cards, rounded-2xl only for key panels
> - High-contrast panels, clear dividers, low-noise backgrounds
> - Use color sparingly and semantically: green for healthy flow, amber for risk, red for urgent failures
> - Prioritize table/map/status readability over visual spectacle
>
> **2. INFORMATION ARCHITECTURE & SCREEN LAYOUT**
>
> A. TOP COMMAND BAR — Fixed header with company name, shift status, live connectivity indicator, sync health, search, notification center, user profile.
>
> B. LEFT SIDEBAR NAVIGATION — Persistent vertical nav: Overview, Live Fleet, Deliveries, Routes, Incidents, Drivers, Maintenance, Reports, Settings. Compact, enterprise-grade, collapsible.
>
> C. PRIMARY OPERATIONS AREA — Split into 3 zones:
> - Zone 1: Fleet Status Overview (KPI strip with Active Drivers, Deliveries At Risk, Delayed Routes, Vehicles Offline, Conflict Alerts, On-Time Rate)
> - Zone 2: Live Dispatch Map (50 driver markers, cluster logic, route lines, delayed vehicles, stale GPS markers, delivery hotspots, incident zones, fallback degraded state)
> - Zone 3: Real-Time Action Queue (prioritized command rail with severity, time detected, suggested action, CTAs)
>
> **3. KEY COMPONENTS & MICRO-INTERFACES**
>
> A. DRIVER DETAIL DRAWER — Contextual slide-over with driver name, vehicle ID, current delivery batch, ETA vs promised time, route adherence, signal quality, last checkpoint, contact actions, event timeline.
>
> B. LIVE DRIVER TABLE — Dense operational table with 50-driver capacity. Columns: Driver, Vehicle, Current Route, Stops Remaining, ETA, SLA Risk, Signal, Status, Last Update, Action. Sticky header, sort by urgency, filter chips.
>
> C. INCIDENT RESOLUTION MODULE — Conflict management for delays, no signal, route deviation, vehicle issues, delivery conflicts, duplicate assignments. Each with recommended workflow: Identify → Assess → Choose action → Confirm → Log.
>
> D. CONNECTIVITY RESILIENCE STATES — Explicit UI states for Online, Weak network, Offline mode, GPS stale, Last sync failed, Retrying synchronization. Calm, operationally clear presentation.
>
> **4. EXPERIENCE PRINCIPLES**
>
> Optimize for: fast scanning over visual novelty; decision support over data decoration; high information density with strong hierarchy; reliable use in stressful, time-sensitive contexts; graceful degradation in poor infrastructure.
>
> **5. VISUAL AND INTERACTION DIRECTION**
>
> Avoid: oversized hero sections, decorative illustrations, generic analytics cards, soft crypto/AI gradient look, glassmorphism-heavy aesthetic, dribbblized concept UI.
>
> Instead: dense but clean layout, strong panels and structured grids, clear status semantics, lightweight motion only where it improves awareness.
>
> **6. RESPONSIVE BEHAVIOR**
>
> Desktop primary. For narrower screens: collapse sidebar, stack KPI modules, convert action queue to bottom sheet, preserve map + alert visibility.
>
> **7. CONTENT TONE**
>
> Use realistic B2B logistics language: "At risk", "Delayed", "Route deviation", "Signal lost", "ETA updated", "Reassigned", "Awaiting confirmation", "Checkpoint missed", "Conflict detected".
>
> Execution Directive: Do not design a pretty dashboard. Design a live operational command system for dispatchers managing fleet risk in rural, low-connectivity conditions. Every component must reduce cognitive load, accelerate intervention, and support real-time logistics control with confidence and clarity.

**Stated rationale:** Thought of the prompt as a way to transform the brief into a real operation interface, not just a pretty screen. Directed the prompt toward information hierarchy, alerts, maps, action queues, and connectivity states. Has pre-tested prompts from other exercises designed to avoid generic AI outputs, and adapted proven prompt structures to this specific problem.

---

## P4 — Meta-Description (38 words, Portuguese)

> Da maneira como tenho feito, escrever esse prompt demandaria mais detalhes de informações e levaria cerca de 1h. Eu daria o contexto do produto, objetivo do fluxo, descreveria os componentes, conteúdos da tela e direcionamentos para a ia.

**Stated rationale:** "It's like a reduced PRD."

**Note:** P4 described their approach rather than writing the actual prompt. They indicated the process would take approximately 1 hour and would include product context, flow objectives, component descriptions, screen contents, and AI direction.

---

## P5 — AI-Delegated (235 words, Portuguese)

**Note:** P5 reported using ChatGPT to help construct the prompt before submitting it to Figma Make. The text below is the resulting prompt.

> Projete uma interface de gerenciamento de frotas logísticas B2B para um coordenador responsável por monitorar e gerenciar até 50 motoristas simultaneamente ao longo do dia.
>
> O sistema deve permitir o monitoramento em tempo real das entregas, localização dos motoristas, progresso das rotas, atrasos e conflitos operacionais.
>
> Contexto: os coordenadores frequentemente operam em regiões rurais com infraestrutura de internet instável, portanto a interface deve priorizar clareza, baixa carga cognitiva e tomada de decisão rápida.
>
> Projete um dashboard para desktop otimizado para controle operacional.
>
> A interface deve incluir:
> - um mapa ao vivo mostrando a localização dos motoristas e suas rotas
> - um painel com lista de motoristas e indicadores de status (em rota, atrasado, parado, entrega concluída)
> - alertas de entrega e notificações de conflitos
> - botões de ação rápida para contatar motoristas ou redistribuir rotas
> - filtros para organizar motoristas por região, atraso ou prioridade
> - uma linha do tempo ou agenda de entregas
>
> Prioridades de UX:
> - forte hierarquia de informação
> - mínimo ruído visual
> - sistema de status com cores bem definidas
> - tipografia grande e legível
> - layout eficiente para monitorar muitos motoristas simultaneamente
>
> Estilo visual:
> - dashboard profissional B2B para logística
> - moderno, mas altamente funcional
> - paleta de cores neutra com cores de status (verde, amarelo, vermelho)
> - elementos de visualização de dados como cards, listas e painel de mapa

**Stated rationale:** To facilitate the interface development process, obtaining insights not initially apparent about the interface and the company.

---

## P6 — Structural Specification (427 words, Portuguese)

> Crie uma interface web responsiva (desktop-first) para um sistema de gerenciamento de frotas logísticas B2B. O usuário principal é um coordenador que precisa monitorar e gerenciar simultaneamente cerca de 50 motoristas ao longo do dia, com foco em cumprir prazos de entrega e resolver conflitos em tempo real. Considere que o sistema será usado em regiões rurais com infraestrutura precária (baixa conectividade, latência alta), então priorize carregamento leve, estados offline e legibilidade.
>
> Estruture a interface como um dashboard operacional em tempo real com as seguintes áreas principais:
>
> 1. Topo (Header fixo):
> - Nome do sistema + seleção de região/filial
> - Indicador de conectividade (online/offline/sincronizando)
> - Notificações críticas (alertas de atraso, conflitos, falhas)
> - Perfil do usuário
>
> 2. Painel principal dividido em 3 colunas:
>
> Coluna esquerda (Lista de motoristas):
> - Lista vertical com até 50 motoristas
> - Cada item deve conter: nome, status (em rota, parado, atraso, offline), progresso da rota (%), última atualização
> - Cores de status bem evidentes (verde, amarelo, vermelho, cinza offline)
> - Campo de busca e filtros (status, região, prioridade)
> - Seleção ativa destaca o motorista
>
> Coluna central (Mapa + rotas):
> - Mapa principal ocupando maior área da tela
> - Pins para cada motorista com cor de status
> - Rotas desenhadas com origem/destino
> - Destaque visual para rotas com problema
> - Interações: clicar no motorista na lista centraliza no mapa
> - Modo simplificado para baixa conexão (mapa reduzido ou fallback para lista geográfica)
>
> Coluna direita (Detalhes e ações):
> - Painel dinâmico do motorista selecionado
> - Informações: rota atual, entregas pendentes, horário estimado vs real, histórico recente
> - Alertas de conflito (atraso, rota interrompida, desvio)
> - Botões de ação rápida: reatribuir rota, contatar motorista, resolver conflito
> - Log de eventos em tempo real
>
> 3. Camada de alertas e priorização:
> - Sistema de alertas persistente (toast + fixo)
> - Ordenação automática por criticidade
> - Destaque para problemas que exigem ação imediata
>
> 4. Estados offline / baixa conectividade:
> - Interface continua funcional com dados em cache
> - Indicador claro de dados desatualizados
> - Botão de sincronização manual
> - Redução de elementos pesados (mapa simplificado)
>
> 5. Design e usabilidade:
> - UI limpa, densa em informação, focada em produtividade
> - Tipografia altamente legível
> - Alto contraste para uso em ambientes externos
> - Uso consistente de cores para status
> - Componentes modulares (cards, listas, badges)
>
> 6. Extras importantes:
> - Atualização em tempo real (simulada visualmente)
> - Feedback imediato nas ações
> - Minimizar cliques para ações críticas
> - Priorizar visão geral + capacidade de intervenção rápida
>
> Gere a interface completa com layout bem definido, hierarquia clara de informação e componentes reutilizáveis.

**Stated rationale:** Thought of the prompt as building a real operation dashboard, not just a pretty interface. Focused on organizing information by priority: first providing an overview (list + map), then enabling quick action (side panel). Also considered the critical infrastructure context, including offline states and sync feedback. Aimed to balance macro vision with quick intervention capability.

**Additional comment:** Did not prioritize avoiding conventional patterns per se. Preferred a conventional dashboard base because this type of tool demands speed and familiarity. Differentiation focused on prioritization logic (alerts, offline states, action speed) rather than layout innovation. Found it interesting how prompts must balance sufficient detail to guide the AI without over-constraining the result.
