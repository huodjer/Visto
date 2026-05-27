# 🐦 Canto Livre — PWA para Torneios de Aves

Aplicativo web progressivo (PWA) para contagem de cantos em torneios de aves.
Funciona no navegador e pode ser instalado no celular como um app nativo.

---

## Como hospedar no Vercel (grátis, recomendado)

1. Acesse https://vercel.com e crie uma conta grátis (pode usar Google ou GitHub)
2. Clique em **"Add New Project"**
3. Escolha **"Upload"** (ou arraste a pasta do projeto)
4. Suba todos os arquivos desta pasta
5. Clique em **Deploy**
6. Pronto! Você receberá um link tipo `cantalivre.vercel.app`

---

## Como hospedar no Netlify (alternativa grátis)

1. Acesse https://netlify.com e crie uma conta
2. Arraste a pasta inteira do projeto para a área de drop do site
3. Aguarde o deploy automático
4. Você receberá um link tipo `cantalivre.netlify.app`

---

## Como instalar no celular (Android)

1. Abra o link no **Chrome**
2. Um banner "Adicionar à tela inicial" vai aparecer — toque nele
3. Ou: toque nos 3 pontinhos do Chrome → "Adicionar à tela inicial"
4. O app aparece na tela inicial com ícone próprio

## Como instalar no celular (iPhone)

1. Abra o link no **Safari**
2. Toque no ícone de compartilhar (quadrado com seta pra cima)
3. Escolha "Adicionar à Tela de Início"

---

## Estrutura dos arquivos

```
cantos-app/
├── index.html       ← o app completo
├── manifest.json    ← configuração do PWA
├── sw.js            ← service worker (funciona offline)
└── icons/
    ├── icon-192.png ← ícone do app
    └── icon-512.png ← ícone do app (alta resolução)
```

---

## Funcionalidades

- ⏱ Cronômetro regressivo (Parcial ~1min, 10min ou 15min)
- 🐦 Contador de cantos com toque
- 💾 Salva registros no aparelho (localStorage)
- 📲 Compartilha resultado pelo WhatsApp
- 🔒 Funciona offline após primeira visita
- 📱 Instalável como app nativo no celular
