# 🎯 747 DISCO - Sistema di Pre-Vendita Email & WhatsApp

Sistema completo di email marketing e messaggi WhatsApp per convertire i preventivi in prenotazioni confermate.

## 📋 Indice

1. [Panoramica del Funnel](#panoramica-del-funnel)
2. [Struttura dei File](#struttura-dei-file)
3. [Timeline di Invio](#timeline-di-invio)
4. [Come Personalizzare](#come-personalizzare)
5. [Placeholder Disponibili](#placeholder-disponibili)
6. [Best Practices](#best-practices)
7. [Metriche da Monitorare](#metriche-da-monitorare)

---

## 🎯 Panoramica del Funnel

Il funnel di pre-vendita è strutturato in **4 fasi progressive** che accompagnano il cliente dal preventivo alla conferma:

```
GIORNO 0: Conferma Preventivo
    ↓ (Entusiasmo + Informazioni)
    
GIORNO 3: Follow-up Emozionale  
    ↓ (Visualizzazione + Social Proof)
    
GIORNO 7: Scarsità e Urgenza
    ↓ (FOMO + Pressione Leggera)
    
GIORNO 10: Ultima Chiamata
    ↓ (Ultimatum + Bonus Last Minute)
    
RISULTATO: Conferma o Chiusura
```

### 🎨 Psicologia del Funnel

- **Email #1**: Crea FIDUCIA e conferma il valore
- **Email #2**: Attiva l'EMOZIONE e la visualizzazione
- **Email #3**: Introduce SCARSITÀ e urgenza controllata
- **Email #4**: Crea l'ULTIMATUM con exit strategy

---

## 📁 Struttura dei File

```
marketing-templates/
│
├── emails/
│   ├── 01-conferma-preventivo.html          [GIORNO 0]
│   ├── 02-followup-emozionale.html           [GIORNO 3]
│   ├── 03-scarsita-urgenza.html              [GIORNO 7]
│   └── 04-ultima-occasione.html              [GIORNO 10]
│
├── whatsapp/
│   ├── 01-conferma-preventivo.txt            [GIORNO 0]
│   ├── 02-followup-giorno3.txt               [GIORNO 3]
│   ├── 03-scarsita-giorno7.txt               [GIORNO 7]
│   ├── 04-ultima-chiamata.txt                [GIORNO 10]
│   └── 05-messaggi-extra.txt                 [SITUAZIONI SPECIFICHE]
│
└── README.md                                  [QUESTA GUIDA]
```

---

## ⏰ Timeline di Invio

### 📅 Calendario Completo

| Giorno | Azione | Canale | Obiettivo | Tono |
|--------|--------|--------|-----------|------|
| **0** | Preventivo inviato | Email + WhatsApp | Informare + Entusiasmare | Positivo, Accogliente |
| **1-2** | Pausa strategica | - | Far sedimentare | - |
| **3** | Follow-up emozionale | Email + WhatsApp | Visualizzazione evento | Empatico, Coinvolgente |
| **4-6** | Pausa | - | Dare tempo | - |
| **7** | Scarsità e urgenza | Email + WhatsApp | Creare FOMO | Urgente ma non aggressivo |
| **8-9** | Pausa | - | Far riflettere | - |
| **10** | Ultima chiamata | Email + WhatsApp | Chiusura finale | Decisivo, Onesto |
| **11+** | Chiusura pratica | - | Archiviare o ricontattare | - |

### 🔔 Timing Ottimale di Invio

**Email:**
- Migliore orario: 10:00 - 11:30 o 15:00 - 16:30
- Giorni migliori: Martedì, Mercoledì, Giovedì
- Evitare: Lunedì mattina, Venerdì sera, Weekend

**WhatsApp:**
- Migliore orario: 11:00 - 13:00 o 17:00 - 19:00
- OK anche weekend (più informale)
- Evitare: Prime mattina (<9:00), Tarda sera (>21:00)

---

## ✏️ Come Personalizzare

### 1. Sostituisci i Placeholder

Tutti i file contengono placeholder che DEVI sostituire con i dati reali del cliente:

```
{{nome_referente}}        → Mario
{{cognome_referente}}     → Rossi
{{nome_cliente}}          → Mario Rossi
{{tipo_evento}}           → Festa di Compleanno 30 anni
{{data_evento}}           → 15/06/2025
{{numero_invitati}}       → 80
{{tipo_menu}}             → Menu Premium con Open Bar
{{importo_totale}}        → 4.500,00
{{acconto}}               → 1.350,00
{{telefono_sede}}         → +39 06 XXXXXXX
{{email_sede}}            → info@747disco.it
```

### 2. Personalizza il Tuo Nome

Nei messaggi WhatsApp, sostituisci `[TUO NOME]` con il tuo nome reale:

```
Esempio:
"Sono [TUO NOME] di 747 Disco"
    ↓
"Sono Marco di 747 Disco"
```

### 3. Aggiorna Link e Contatti

Verifica che tutti i link siano corretti:

- Logo: `https://747disco.it/wp-content/uploads/2025/06/images.png`
- Sito: `https://747disco.it`
- Instagram: Aggiorna con il tuo handle reale
- Facebook: Aggiorna con la tua pagina reale
- WhatsApp: Usa formato `https://wa.me/39XXXXXXXXX` (senza spazi)

### 4. Testa Prima di Inviare

**Checklist Pre-Invio:**
- [ ] Tutti i placeholder sostituiti?
- [ ] Nome del cliente corretto?
- [ ] Data formattata correttamente?
- [ ] Importi con virgola corretta (es: 3.500,00)?
- [ ] Link cliccabili e funzionanti?
- [ ] Email inviata a te stesso per test?
- [ ] Visualizzazione OK su mobile?
- [ ] Nessun errore ortografico?

---

## 🏷️ Placeholder Disponibili

### Informazioni Cliente

| Placeholder | Descrizione | Esempio |
|-------------|-------------|---------|
| `{{nome_referente}}` | Nome di battesimo | Mario |
| `{{cognome_referente}}` | Cognome | Rossi |
| `{{nome_cliente}}` | Nome completo | Mario Rossi |

### Dettagli Evento

| Placeholder | Descrizione | Esempio |
|-------------|-------------|---------|
| `{{tipo_evento}}` | Tipo di evento | Matrimonio / Compleanno 18 anni / Evento Aziendale |
| `{{data_evento}}` | Data in formato IT | 25/12/2025 |
| `{{numero_invitati}}` | Numero ospiti | 150 |
| `{{tipo_menu}}` | Pacchetto menu | Menu Premium / Menu Standard / Menu Deluxe |

### Informazioni Commerciali

| Placeholder | Descrizione | Esempio |
|-------------|-------------|---------|
| `{{importo_totale}}` | Costo totale | 5.500,00 |
| `{{acconto}}` | Acconto richiesto (30%) | 1.650,00 |

### Contatti 747 Disco

| Placeholder | Descrizione | Esempio |
|-------------|-------------|---------|
| `{{telefono_sede}}` | Telefono location | +39 06 XXXXXXX |
| `{{email_sede}}` | Email contatti | info@747disco.it |

---

## 💡 Best Practices

### ✅ Email

1. **Subject Line Efficaci:**
   - Email #1: "✨ Il Tuo Preventivo 747 Disco - [Tipo Evento] [Data]"
   - Email #2: "💭 [Nome], Immagina il Tuo Evento Perfetto..."
   - Email #3: "⏰ [Nome], Aggiornamento sulla Tua Data [Data]"
   - Email #4: "🚨 [Nome], Ultima Chiamata per [Data]"

2. **Personalizzazione:**
   - Usa SEMPRE il nome del cliente
   - Riferimenti specifici al tipo di evento
   - Adatta il tono al target (più formale per eventi aziendali, casual per compleanni)

3. **Mobile First:**
   - Testa su smartphone (70% degli utenti legge da mobile)
   - Pulsanti CTA grandi e cliccabili
   - Font leggibili (min 14px)

4. **Call-to-Action Chiari:**
   - Un CTA principale per email
   - Massimo 3 opzioni di contatto
   - Bottoni visibili e colorati

### ✅ WhatsApp

1. **Tono Conversazionale:**
   - Scrivi come parleresti di persona
   - Usa emoji (ma con moderazione)
   - Vai a capo spesso (leggibilità)

2. **Tempismo:**
   - Rispondi entro 15 minuti se possibile
   - Non inviare più di 2 messaggi senza risposta
   - Rispetta orari ragionevoli (9:00 - 21:00)

3. **Multimediale:**
   - Invia foto della location
   - Video brevi di eventi passati
   - Note vocali per spiegazioni complesse

4. **Follow-up:**
   - Se non risponde: aspetta 2-3 giorni prima di ricontattare
   - Se visualizza ma non risponde: messaggio leggero "Tutto ok?"
   - Se rifiuta: chiudi con positività

### ❌ Errori da Evitare

- ❌ Inviare tutte le email lo stesso giorno
- ❌ Essere troppo aggressivi/insistenti
- ❌ Dimenticare di personalizzare i placeholder
- ❌ Inviare email generiche "Caro Cliente"
- ❌ Promettere cose che non puoi mantenere
- ❌ Ignorare le risposte dei clienti
- ❌ Usare solo un canale (usa email + WhatsApp)
- ❌ Mandare messaggi troppo lunghi su WhatsApp

---

## 📊 Metriche da Monitorare

### KPI Principali

| Metrica | Target | Come Misurare |
|---------|--------|---------------|
| **Tasso di Apertura Email** | >25% | Email marketing tool |
| **Tasso di Click (CTR)** | >3% | Link tracking |
| **Tasso di Risposta WhatsApp** | >40% | Manuale |
| **Conversion Rate** | >20% | Preventivi → Conferme |
| **Tempo Medio di Conversione** | 5-7 giorni | CRM |

### 📈 Come Tracciare

1. **Foglio Excel/Google Sheets:**
   ```
   | Cliente | Data Preventivo | Email 1 | Email 2 | Email 3 | Email 4 | WA | Esito | Data Conferma |
   |---------|-----------------|---------|---------|---------|---------|-----|-------|---------------|
   | Mario R.| 01/01/25        | ✓       | ✓       | ✓       | -       | ✓   | OK    | 08/01/25      |
   ```

2. **Analizza Cosa Funziona:**
   - Quale email converte di più?
   - WhatsApp o Email è più efficace?
   - Quali obiezioni tornano spesso?
   - Quale tipo di evento converte meglio?

3. **A/B Testing:**
   - Testa subject line diverse
   - Prova timing di invio diversi
   - Varia il tono dei messaggi
   - Sperimenta con offerte diverse

---

## 🎓 Strategia Avanzata

### 🔥 Quando il Cliente Risponde

**SCENARIO 1: Interessato ma indeciso**
→ Proponi sopralluogo gratuito
→ Offri chiamata per chiarimenti
→ Invia foto/video personalizzati
→ Condividi recensioni simili al suo evento

**SCENARIO 2: Chiede sconto**
→ Non scontare subito
→ Aggiungi valore invece (upgrade, extra)
→ Offri bonus se conferma subito
→ Spiega perché il prezzo è giusto

**SCENARIO 3: Confronta con altre location**
→ Evidenzia i tuoi punti di forza unici
→ Non parlare male della concorrenza
→ Offri confronto trasparente
→ Fai leva sull'esperienza/atmosfera

**SCENARIO 4: "Ci penso"**
→ OK, rispetta i tempi
→ Chiedi: "Cosa ti aiuterebbe a decidere?"
→ Risolvi obiezioni specifiche
→ Segui la timeline del funnel

### 💼 Segmentazione Clienti

**TIPO A - Deciso e veloce (20%)**
- Conferma entro 3 giorni
- Poche domande
- Focus: Velocità e conferma rapida

**TIPO B - Valutatore attento (50%)**
- Valuta 2-3 location
- Molte domande
- Focus: Valore e differenziazione

**TIPO C - Indeciso cronico (30%)**
- Chiede continuamente modifiche
- Non decide mai
- Focus: Urgenza e deadline

Adatta il tuo approccio al tipo di cliente!

---

## 🚀 Automazione (Opzionale)

Se vuoi automatizzare il processo, considera:

### Strumenti Consigliati:

**Email Marketing:**
- Mailchimp (€13/mese)
- Sendinblue (€25/mese)
- ActiveCampaign (€29/mese)

**WhatsApp Business API:**
- Twilio
- WhatsApp Business (gratuito base)
- Respond.io

**CRM:**
- HubSpot (free/paid)
- Pipedrive
- Google Sheets (manuale ma funzionale)

### Setup Automazione Semplice:

1. Cliente richiede preventivo
2. Aggiungi a lista email
3. Automazione invia Email #1
4. Dopo 3gg → Email #2
5. Dopo 7gg → Email #3
6. Dopo 10gg → Email #4
7. WhatsApp manuale (più personale!)

---

## 📞 Gestione Obiezioni Comuni

### "È troppo caro"
✅ "Capisco la tua preoccupazione! Considera però che il prezzo include [lista tutto]. Molti clienti pensavano lo stesso, poi hanno capito il valore quando hanno visto che [beneficio]. Posso mostrarti esattamente cosa include?"

### "Devo parlarne con [partner/famiglia]"
✅ "Assolutamente! È una decisione importante. Ti va se ti invio qualche foto/video da mostrare? Così hanno un'idea più chiara!"

### "Ho visto un'altra location più economica"
✅ "Ottimo che tu stia valutando! Posso chiederti cosa ti ha colpito di più di 747 Disco? Voglio essere sicuro che tu scelga il posto giusto per te, anche se non fossi noi!"

### "Non so se la data è quella giusta"
✅ "Ti capisco! Vuoi che controllo anche altre date disponibili? Così hai più opzioni!"

### "Devo ancora decidere sul numero esatto"
✅ "Nessun problema! Possiamo bloccare la data con una stima. Poi aggiustiamo il numero fino a [X giorni prima]. Che ne dici?"

---

## 📋 Checklist Operativa

### Prima di Iniziare il Funnel:
- [ ] Database clienti organizzato
- [ ] Template email personalizzati
- [ ] Template WhatsApp pronti
- [ ] Calendario invii pianificato
- [ ] Sistema di tracking attivo
- [ ] Numeri e email aggiornati

### Dopo Ogni Preventivo:
- [ ] Inserisci cliente in foglio tracking
- [ ] Personalizza tutti i placeholder
- [ ] Imposta reminder per follow-up
- [ ] Prepara materiale extra (foto/video)
- [ ] Rispondi entro 24h a ogni contatto

### Analisi Settimanale:
- [ ] Quanti preventivi inviati?
- [ ] Quanti convertiti?
- [ ] Quali email performano meglio?
- [ ] Quali obiezioni ricorrenti?
- [ ] Cosa migliorare la prossima settimana?

---

## 🎯 Obiettivi di Conversione

### Benchmark Realistici:

| Fase Funnel | % Successo Target |
|-------------|-------------------|
| Preventivo inviato → Email aperta | 60-70% |
| Email aperta → Risposta | 30-40% |
| Risposta → Meeting/Chiamata | 50-60% |
| Meeting → Conferma acconto | 40-50% |
| **TOTALE: Preventivo → Conferma** | **15-25%** |

Se converti 20 preventivi su 100 = OTTIMO RISULTATO! 💪

---

## 🆘 Supporto e Contatti

**Hai domande su come usare questi template?**

1. Rileggi questa guida
2. Testa su piccola scala prima
3. Adatta al tuo stile personale
4. Monitora risultati e ottimizza

**Remember:**
> "Il miglior funnel è quello che rispecchia la TUA personalità e il TUO brand. Usa questi template come base, ma rendili TUOI!" ✨

---

## 📜 Licenza e Note Legali

✅ Questi template sono creati specificamente per **747 Disco**
✅ Puoi modificarli liberamente per il tuo business
✅ Rispetta sempre le norme GDPR per privacy
✅ Ottieni consenso prima di inviare comunicazioni marketing
✅ Offri sempre possibilità di opt-out

⚠️ **Importante:** Assicurati di avere il consenso del cliente per comunicazioni marketing prima di usare questo funnel!

---

## 🌟 Buona Fortuna!

Ora hai tutto quello che serve per convertire i tuoi preventivi in prenotazioni confermate! 🚀

**Ricorda:** La chiave del successo non è solo nei template, ma nella tua capacità di costruire una relazione autentica con il cliente.

Sii genuino, ascolta le loro esigenze e mostra passione per il tuo lavoro. 

Il resto viene da sé! 💪✨

---

**747 Disco - Dove ogni evento diventa leggenda** 🌟

*README creato il: 2025-11-04*
*Versione: 1.0*
