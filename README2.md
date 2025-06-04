# 🏆 Netshoes Web Scraper – Evolução e Resolução de Problemas  

## 🚀 Objetivo  
Criar um coletor de preços automatizado para o site **Netshoes**, inicialmente utilizando **Selenium** para capturar os dados diretamente da interface web.  

---

## ⚠ Problemas Encontrados vs Soluções  
Durante o desenvolvimento, enfrentei desafios que me levaram a **refinar estratégias**, testar hipóteses e pivotar para uma solução mais viável. Aqui está um resumo dos problemas encontrados e como os resolvi:  

### **1️⃣ Configuração do ChromeDriver e Variáveis de Ambiente**  
🔹 **Problema:** Inicialmente, minha configuração do **Selenium não reconhecia o WebDriver corretamente**, impedindo a execução do script.  
✔ **Solução:** Configurei manualmente o **ChromeDriver como variável de ambiente**, garantindo que o Selenium pudesse localizar o executável automaticamente em futuras execuções.  

### **2️⃣ XPath e Captura de Preços**  
🔹 **Problema:** Os elementos de preços não estavam sendo encontrados corretamente, pois o site **carregava os valores via JavaScript**.  
✔ **Solução:** Testei diferentes **XPath dinâmicos**, refinei a estratégia de captura de elementos e implementei tempos de espera para garantir que os preços fossem carregados antes da extração.  

### **3️⃣ Barreiras Anti-Scraping**  
🔹 **Problema:** A Netshoes usa mecanismos de segurança que **bloqueiam requisições automatizadas**, impedindo que Selenium extraia os preços diretamente.  
✔ **Solução:** Após testes, decidi **migrar para a API oficial da Netshoes**, garantindo acesso seguro e estruturado aos dados sem violar políticas de uso do site.  

---

## 🔄 Nova Estratégia  
🎯 **Mudança para API oficial da Netshoes** → Estruturando a integração via requisições HTTP para obter os dados de forma segura e eficiente.  
🎯 **Implementação gradual da API (`api_netshoes.py`)** → Mesmo sem o acesso completo ainda, já preparei a lógica inicial para conexão e extração de informações.  
🎯 **Comparação entre Selenium e API** → Analisando vantagens e limitações de cada abordagem para futuras melhorias no projeto.  

---

## 📌 Próximos Passos  
✅ Validar acesso à API oficial da Netshoes  
✅ Implementar requisições para buscar preços e detalhes dos produtos  
✅ Comparar eficácia do scraping via Selenium vs API para entender qual abordagem funciona melhor em diferentes cenários  

---


🔥 **Esse projeto está em constante evolução – acompanhe os commits!** 😃  
Essa transição fortalece **boas práticas de dados** e permite uma solução mais sustentável a longo prazo.  

