#  The Kripto King — MVP de Corretora Inteligente com IA no Telegram

**The Kripto King** é um MVP de uma corretora cripto automatizada, com sugestões baseadas em inteligência artificial, alertas por horário, carteira simulada e painel completo de investidor — tudo integrado via Telegram.

**Este é um projeto para mostrar, na prática, como queremos a versão funcional do Kripto King**

>  Projeto desenvolvido com foco em experiência fluida, personalização, simulação de investimento e usabilidade para portfólio.

---

##  Funcionalidades

* **Login simulado** com e-mail e senha
* **Escolha de corretora** (Binance, Coinbase, etc)
* **Sugestões diárias de criptomoedas via IA**
* **Alertas automáticos com hora personalizada**
* **Carteira fictícia com valores em cripto**
* **Simulação de compras e perfil de investidor**
* **Menu interativo com 8 opções**
* **IA SmartTrade (modo beta simulado)**
* **Painel dinâmico e conversas naturais com o usuário**

---

## 💻 Tecnologias utilizadas

* `Python`
* `Telebot (pyTelegramBotAPI)`
* `Threading` (para alertas em tempo real)
* `Markdown` (para mensagens mais visuais)

---

##  Como rodar o projeto localmente

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/the-kripto-king.git
cd the-kripto-king
```

2. Instale as dependências:

```bash
pip install pyTelegramBotAPI
```

3. Crie seu bot no Telegram usando o [@BotFather](https://t.me/BotFather) e copie a `API_TOKEN`.

4. Cole sua token no arquivo:

```python
API_TOKEN = 'SUA_CHAVE_AQUI'
```

5. Execute o bot:

```bash
python bot.py
```

---

##  Como funciona

1. O usuário inicia o bot com `/start`
2. O bot coleta e-mail, senha e nome (login simulado)
3. O usuário escolhe uma corretora
4. Um painel é apresentado com 8 opções
5. O bot interage com sugestões, carteira e alertas automatizados
6. O MVP simula uma experiência de corretora real com IA orientando decisões

---

##  Issues para desenvolvimento futuro

### 📌 Funcionalidade

* [ ] Integração com CoinGecko ou CoinMarketCap para preços reais
* [ ] Implementar simulação real de compras com histórico salvo
* [ ] Persistência de dados (ex: SQLite ou Firebase)
* [ ] Login real com autenticação de múltiplos usuários
* [ ] Criação de painéis via Telegram WebApp

###  Design e UX

* [ ] Adicionar emojis por categoria de moeda (stablecoin, memecoin, utilitária)
* [ ] Traduzir o bot para inglês e espanhol
* [ ] Opção de modo escuro/claro para WebApp futuro
* [ ] Melhorar fluxo com inline buttons

###  IA e Sugestões

* [ ] Treinar modelo real de recomendação com base em sentimento de mercado
* [ ] IA preditiva conectada a padrões históricos reais
* [ ] Simulação de carteira otimizada com IA SmartTrade

### 📈 Performance e Segurança

* [ ] Limitar acessos simultâneos com timeout inteligente
* [ ] Modo silencioso para grupos
* [ ] Adicionar logs de uso e mensagens

---

## 📚 Licença

Este projeto está sob licença **MIT** e foi desenvolvido apenas com fins educacionais e de portfólio. Nenhum investimento real é realizado, e o projeto não tem conexão com corretoras verdadeiras.
