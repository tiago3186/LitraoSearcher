## LitraoSearcher
Uma aplicação Flask para pesquisa e compartilhamento de informações sobre litrão e butecos bons e baratos. Usa a API OpenStreetMap para renderizar mapas.  

Para rodar localmente, baixe esse repositório e instale as dependências.  
Em seguida, configure suas variáveis de ambiente locais e crie um banco de dados MySQL e as tabelas conforme o models.py.  
Crie um usuário e senha de padrão (ou mais de um se quiser) dando um INSERT, rode a aplicação e be happy.

Atualmente estou subindo uma versão que seria mais de produção na Azure, disponível em breve.  

![image](https://github.com/tiago3186/LitraoSearcher/assets/132753395/dad46a5a-e3b3-4989-b44e-e61b300b2a06)

### Features atuais
- Após logar, você pode inserir um marcador no mapa  
![image](https://github.com/tiago3186/LitraoSearcher/assets/132753395/0050e25f-cd6c-41ee-bb17-b8946d4910c7)

- O marcador depois fica pra ser visualizado  
![image](https://github.com/tiago3186/LitraoSearcher/assets/132753395/cfe54718-b89c-4d84-b0db-eb8cfeb5ab0f)

- busca se existe esse usuario e senha no banco de dados MySQL e caso não exista retorna um erro  
![image](https://github.com/tiago3186/LitraoSearcher/assets/132753395/1f6fe6a2-74b5-414e-8bff-cb8450cdf6db)

- Os dados dos bares e posição dos marcadores são salvos no banco MySQL, de modo que qualquer usuário consegue ver o que qualquer outro usuário tenha marcado  
![image](https://github.com/tiago3186/LitraoSearcher/assets/132753395/4ac0576b-3931-437d-b593-203b5a23c0d4)
