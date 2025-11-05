# streamlit-claude-chat

Streamlit LLM Chat App by anthropic claude with ISAKMP & Network Security Analysis

![screen_shot](./image/screen_shot_1.gif)

## Features

### 🔐 ISAKMP & Network Security
- **ISAKMP Protocol Analysis**: Analyze ISAKMP packets and configurations
- **IPsec Configuration**: Generate secure IPsec/VPN configurations
- **Security Association Negotiation**: Understand SA negotiation processes
- **VPN Troubleshooting**: Debug VPN connection issues
- **Key Exchange Protocols**: Implement and analyze key exchange mechanisms
- **Vulnerability Assessment**: Check for security vulnerabilities in configurations
- **Protocol Analysis**: Analyze network traffic for ISAKMP patterns

### 🚀 Web Development
- PHP debugging and optimization
- WordPress plugin and hook development
- MySQL query optimization
- CSS responsive design
- Code security analysis

## git clone

```
git clone https://github.com/festiva1300/streamlit-claude-chat.git
cd streamlit-claude-chat
```

## environment setting

Write the Anthripic access key, the model to be used in the `.env` file.

```
API_KEY=XX-XXXXX...
AI_MODEL=claude-3-sonnet-20240229
```

## execute

### build a container

```bash
docker build ./ -t streamlit-claude-chat
```

### deploy on local

```bash
docker compose up -d
```

## Usage

### ISAKMP/Network Security Features

The application now includes specialized templates for ISAKMP and network security analysis:

- **🔑 ISAKMP Analysis**: Analyze ISAKMP packets, configurations, and identify security issues
- **🛡️ IPsec Config**: Generate secure IPsec configurations for various scenarios
- **🔐 SA Negotiation**: Get detailed explanations of Security Association negotiations
- **🌐 VPN Setup**: Configure VPN tunnels using ISAKMP/IKE protocols
- **🔒 Key Exchange**: Implement secure key exchange protocols
- **⚠️ Vulnerability Check**: Assess ISAKMP/IKE configurations for vulnerabilities
- **📊 Protocol Analysis**: Analyze network traffic for ISAKMP patterns
- **🔧 Troubleshoot VPN**: Debug VPN connection and ISAKMP issues

### Supported File Types

The application supports analysis of:
- Configuration files (`.conf`, `.cfg`)
- Log files (`.log`)
- Network captures (`.pcap`)
- Code files (`.php`, `.js`, `.css`, `.html`, `.py`, `.sql`)
- Data files (`.json`, `.xml`, `.txt`)

### ISAKMP/IKE Key Concepts

The assistant is trained on these core ISAKMP/IKE concepts:

- **Phase 1**: Establishes a secure channel using Main Mode or Aggressive Mode
- **Phase 2**: Negotiates IPsec Security Associations using Quick Mode
- **Oakley Key Determination Protocol**: Provides perfect forward secrecy
- **SKEYID**: Shared secret key material derived from the authentication method
- **SA Payload**: Contains security association proposals
- **Authentication Methods**: Pre-shared keys, RSA signatures, RSA encrypted nonces

