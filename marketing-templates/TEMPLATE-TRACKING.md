# 📊 Template Tracking Clienti - 747 Disco

Usa questo template per tracciare tutti i tuoi preventivi e follow-up.

---

## 🗂️ Foglio Excel/Google Sheets

### Istruzioni:
1. Crea un nuovo Google Sheets o Excel
2. Copia la struttura qui sotto
3. Aggiungi una riga per ogni preventivo
4. Aggiorna man mano che procedi con il funnel

---

## 📋 STRUTTURA COLONNE

```
| A | B | C | D | E | F | G | H | I | J | K | L | M | N |
```

### Intestazioni:

```
A: ID Cliente
B: Data Preventivo
C: Nome Cliente
D: Tipo Evento
E: Data Evento
F: N. Invitati
G: Importo Totale
H: Email #1
I: Email #2
J: Email #3
K: Email #4
L: WhatsApp
M: Esito
N: Data Conferma
O: Note
```

---

## 📝 ESEMPIO COMPILATO

| ID | Data Prev. | Cliente | Tipo Evento | Data Evento | Invitati | Importo | E1 | E2 | E3 | E4 | WA | Esito | Conferma | Note |
|----|------------|---------|-------------|-------------|----------|---------|----|----|----|----|-------|-------|----------|------|
| 001 | 01/11/25 | Mario Rossi | Compleanno 30 | 15/06/25 | 80 | 4.500 | ✓ | ✓ | ✓ | - | ✓✓✓ | ✅ OK | 08/11/25 | Convertito in 7gg |
| 002 | 02/11/25 | Laura Bianchi | Matrimonio | 20/07/25 | 150 | 8.500 | ✓ | ✓ | ✓ | ✓ | ✓✓ | ❌ NO | - | Ha scelto altra location |
| 003 | 03/11/25 | Paolo Verdi | 18 Anni | 10/05/25 | 100 | 5.200 | ✓ | ✓ | - | - | ✓ | ⏳ IN CORSO | - | Chiesto sopralluogo |
| 004 | 05/11/25 | Sara Neri | Evento Aziendale | 15/12/25 | 60 | 3.800 | ✓ | - | - | - | ✓ | ⏳ IN CORSO | - | Appena iniziato |

---

## 🎨 LEGENDA SIMBOLI

### Colonne Email/WhatsApp:
- `✓` = Inviato
- `✓✓` = Inviato + Risposto
- `✓✓✓` = Inviato + Risposto + Conferma interesse
- `-` = Non ancora inviato/necessario
- `❌` = Non risponde

### Colonna Esito:
- `✅ OK` = Preventivo convertito, acconto ricevuto
- `❌ NO` = Cliente ha rifiutato/scelto altro
- `⏳ IN CORSO` = Funnel in corso
- `🕐 ATTESA` = In pausa, attendiamo risposta
- `❓ DA RICONTATTARE` = Da seguire più avanti

---

## 📊 DASHBOARD RIEPILOGO

Crea una sezione separata nel foglio con queste metriche:

```
═══════════════════════════════════════════════════════════
                    DASHBOARD 747 DISCO
═══════════════════════════════════════════════════════════

📅 PERIODO: [Mese/Anno]

┌─────────────────────────────────────────────────────────┐
│ METRICHE PRINCIPALI                                     │
├─────────────────────────────────────────────────────────┤
│ Preventivi Inviati:              [   25   ]            │
│ Preventivi Convertiti:           [   5    ]            │
│ Conversion Rate:                 [   20%  ]            │
│ Valore Totale Convertito:       [ € 22.500]            │
│ Valore Medio per Evento:        [ € 4.500 ]            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ STATO FUNNEL                                            │
├─────────────────────────────────────────────────────────┤
│ ⏳ In Corso:                      [   8    ]            │
│ 🕐 In Attesa Risposta:           [   6    ]            │
│ ✅ Convertiti:                    [   5    ]            │
│ ❌ Persi:                         [   6    ]            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ PERFORMANCE EMAIL                                       │
├─────────────────────────────────────────────────────────┤
│ Email #1 Tasso Apertura:         [   68%  ]            │
│ Email #2 Tasso Apertura:         [   45%  ]            │
│ Email #3 Tasso Apertura:         [   72%  ] ⭐         │
│ Email #4 Tasso Apertura:         [   55%  ]            │
│                                                         │
│ Email Più Performante: #3 (Scarsità)                   │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ WHATSAPP                                                │
├─────────────────────────────────────────────────────────┤
│ Messaggi Inviati:                [   48   ]            │
│ Tasso di Risposta:               [   45%  ]            │
│ Conversioni via WA:              [   3    ]            │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ TIMING CONVERSIONE                                      │
├─────────────────────────────────────────────────────────┤
│ Tempo Medio Conversione:         [ 6.2 gg ]            │
│ Più Veloce:                      [ 2 giorni]            │
│ Più Lento:                       [ 11 giorni]           │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ TIPO EVENTI PIÙ RICHIESTI                               │
├─────────────────────────────────────────────────────────┤
│ 1. Compleanni 18 anni:           [   35%  ] ████████   │
│ 2. Feste private:                [   25%  ] ██████      │
│ 3. Matrimoni:                    [   20%  ] █████       │
│ 4. Eventi Aziendali:             [   15%  ] ███         │
│ 5. Altro:                        [   5%   ] █           │
└─────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════
```

---

## 📈 FORMULE EXCEL UTILI

### Conversion Rate:
```excel
=COUNTIF(M:M,"✅ OK")/COUNTA(A:A)*100
```
*(Dove M è la colonna Esito)*

### Valore Totale Convertito:
```excel
=SUMIF(M:M,"✅ OK",G:G)
```
*(Dove G è la colonna Importo)*

### Tempo Medio Conversione:
```excel
=AVERAGE(N:N-B:B)
```
*(Dove N è Data Conferma e B è Data Preventivo)*

### Count In Corso:
```excel
=COUNTIF(M:M,"⏳ IN CORSO")
```

---

## 🎯 TRACKING SETTIMANALE

Ogni settimana, compila questa checklist:

```
SETTIMANA DEL: [__/__/2025]

┌─────────────────────────────────────────┐
│ ATTIVITÀ                                │
├─────────────────────────────────────────┤
│ [ ] Nuovi preventivi inviati: ____     │
│ [ ] Email #2 da inviare: ____          │
│ [ ] Email #3 da inviare: ____          │
│ [ ] Email #4 da inviare: ____          │
│ [ ] WhatsApp follow-up: ____           │
│ [ ] Chiamate da fare: ____             │
│ [ ] Sopralluoghi fissati: ____         │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ RISULTATI                               │
├─────────────────────────────────────────┤
│ Preventivi convertiti: ____            │
│ Acconto totale ricevuto: € ____        │
│ Nuovi lead da seguire: ____            │
│ Pratiche chiuse (NO): ____             │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ NOTE / OSSERVAZIONI                     │
├─────────────────────────────────────────┤
│                                         │
│ _____________________________________   │
│ _____________________________________   │
│ _____________________________________   │
│                                         │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ AZIONI PER SETTIMANA PROSSIMA           │
├─────────────────────────────────────────┤
│ 1. ________________________________     │
│ 2. ________________________________     │
│ 3. ________________________________     │
└─────────────────────────────────────────┘
```

---

## 📱 TRACKING OBIEZIONI

Tieni traccia delle obiezioni più comuni per migliorare il tuo approach:

| Cliente | Obiezione | Come L'hai Gestita | Esito |
|---------|-----------|-------------------|-------|
| Mario R. | "Troppo caro" | Aggiunto valore + bonus | ✅ Convertito |
| Laura B. | "Altra location meno cara" | Differenziazione qualità | ❌ Perso |
| Paolo V. | "Devo pensarci" | Offerto sopralluogo | ⏳ In corso |
| Sara N. | "Budget limitato" | Proposto Menu Standard | ⏳ In corso |

### Top 3 Obiezioni:
1. **Prezzo troppo alto** (45%)
2. **Confronto con altre location** (30%)
3. **Indecisione generale** (25%)

### Strategie Vincenti:
- ✅ Aggiungere valore invece di scontare
- ✅ Offrire sopralluogo gratuito
- ✅ Mostrare social proof (recensioni)
- ✅ Creare urgenza con scarsità date

---

## 🗓️ CALENDARIO REMINDER

Usa questo template per settare reminder:

```
CLIENTE: [Nome]
PREVENTIVO #: [ID]

┌─────────────────────────────────────────┐
│ TIMELINE AUTOMATICA                     │
├─────────────────────────────────────────┤
│ ✅ GG 0:  Email #1 + WhatsApp #1        │
│ ⏰ GG 3:  Email #2 + WhatsApp #2        │
│ ⏰ GG 7:  Email #3 + WhatsApp #3        │
│ ⏰ GG 10: Email #4 + WhatsApp #4        │
│ ⏰ GG 12: Chiusura pratica              │
└─────────────────────────────────────────┘

REMINDER IMPOSTATI:
[ ] Google Calendar
[ ] Reminder telefono
[ ] CRM/Software gestionale
[ ] Foglio Excel
```

---

## 💰 TRACKING PAGAMENTI

Quando un cliente conferma, traccia i pagamenti:

| Cliente | Importo Tot. | Acconto (30%) | Data Acc. | Saldo (70%) | Data Saldo | Status |
|---------|--------------|---------------|-----------|-------------|------------|--------|
| Mario R. | € 4.500 | € 1.350 | 08/11/25 | € 3.150 | 14/06/25 | ✅ Acconto OK |
| Luca T. | € 3.200 | € 960 | 15/11/25 | € 2.240 | 01/03/25 | ✅ Acconto OK |

---

## 📊 ANALISI MENSILE

Alla fine di ogni mese, compila questa analisi:

```
═══════════════════════════════════════════════════════════
              ANALISI MENSILE - [MESE ANNO]
═══════════════════════════════════════════════════════════

📈 NUMERI DEL MESE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Preventivi Inviati:                [    ]
Conversion Rate:                   [    %]
Revenue Totale:                    [ €     ]
Valore Medio Evento:              [ €     ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 OBIETTIVI vs RISULTATI:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Obiettivo Preventivi:             [    ] → Risultato: [    ]
Obiettivo Conversion:              [  % ] → Risultato: [  % ]
Obiettivo Revenue:                 [ €  ] → Risultato: [ €  ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ COSA HA FUNZIONATO:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

❌ COSA NON HA FUNZIONATO:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

💡 MIGLIORAMENTI PER IL PROSSIMO MESE:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

🎓 LEZIONI IMPARATE:
___________________________________________________
___________________________________________________
___________________________________________________

═══════════════════════════════════════════════════════════
```

---

## 🎯 OBIETTIVI SMART

Setta obiettivi specifici e misurabili:

```
OBIETTIVI TRIMESTRE: [Q1/Q2/Q3/Q4 2025]

┌─────────────────────────────────────────────────────────┐
│ OBIETTIVO 1: NUMERO PREVENTIVI                          │
├─────────────────────────────────────────────────────────┤
│ Target: [ 30 ] preventivi inviati                       │
│ Attuale: [    ]                                         │
│ Gap: [    ]                                             │
│ Azioni: _________________________________________       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ OBIETTIVO 2: CONVERSION RATE                            │
├─────────────────────────────────────────────────────────┤
│ Target: [ 25% ] conversion                              │
│ Attuale: [    %]                                        │
│ Gap: [    %]                                            │
│ Azioni: _________________________________________       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ OBIETTIVO 3: REVENUE                                    │
├─────────────────────────────────────────────────────────┤
│ Target: [ € 35.000 ] revenue totale                     │
│ Attuale: [ €        ]                                   │
│ Gap: [ €        ]                                       │
│ Azioni: _________________________________________       │
└─────────────────────────────────────────────────────────┘
```

---

## 📂 ORGANIZZAZIONE FILE

Organizza una cartella per ogni cliente:

```
/747Disco-Clienti/
│
├── /001-Mario-Rossi/
│   ├── preventivo.pdf
│   ├── contratto.pdf
│   ├── ricevuta-acconto.pdf
│   ├── email-inviate.txt
│   ├── whatsapp-chat.pdf
│   └── note.txt
│
├── /002-Laura-Bianchi/
│   ├── preventivo.pdf
│   ├── note-sopralluogo.txt
│   └── email-inviate.txt
│
└── ...
```

---

## 🔔 REMINDER AUTOMATICI

Imposta questi reminder nel calendario:

### Google Calendar:
1. **Ogni Lunedì 9:00**: "Review preventivi settimana"
2. **Ogni Mercoledì 15:00**: "Check email da inviare"
3. **Ogni Venerdì 17:00**: "Follow-up WhatsApp pendenti"
4. **Fine Mese**: "Analisi mensile + report"

---

## 💻 STRUMENTI CONSIGLIATI

### Gratis:
- ✅ Google Sheets (tracking)
- ✅ Google Calendar (reminder)
- ✅ WhatsApp Business (messaggi)
- ✅ Gmail (email)

### A Pagamento (Opzionali):
- Mailchimp (€13/mese) - Email automation
- Pipedrive (€14/mese) - CRM completo
- Calendly (€10/mese) - Booking sopralluoghi
- Notion (€8/mese) - Organizzazione avanzata

---

## ✅ CHECKLIST GIORNALIERA

Stampa e attacca questa checklist alla scrivania:

```
┌─────────────────────────────────────────┐
│   CHECKLIST GIORNALIERA 747 DISCO      │
├─────────────────────────────────────────┤
│ MATTINA:                                │
│ [ ] Check email clienti                │
│ [ ] Check WhatsApp                     │
│ [ ] Aggiorna foglio tracking           │
│ [ ] Identifica email da inviare oggi   │
│                                         │
│ POMERIGGIO:                             │
│ [ ] Invia email programmate            │
│ [ ] Follow-up WhatsApp                 │
│ [ ] Rispondi a tutti i messaggi        │
│ [ ] Prepara preventivi nuovi           │
│                                         │
│ SERA:                                   │
│ [ ] Review conversazioni del giorno    │
│ [ ] Imposta reminder per domani        │
│ [ ] Aggiorna metriche                  │
│ [ ] 5min: cosa migliorare domani       │
└─────────────────────────────────────────┘
```

---

## 🎉 CONCLUSIONE

Con questo sistema di tracking avrai:

✅ Controllo totale su tutti i preventivi
✅ Nessun follow-up dimenticato
✅ Metriche chiare per ottimizzare
✅ Professionalità verso i clienti
✅ Aumento del conversion rate

**Dedica 15 minuti al giorno al tracking e vedrai risultati incredibili! 📈**

---

*Template creato: 2025-11-04*
*Versione: 1.0*
*747 Disco - Sistema di Vendita Professionale* 🌟
