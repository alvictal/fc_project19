# Projeto da imersão Full Cycle 19 

O projeto consiste em duas atividades
*  Atividade 1 - Django - Sistema simples para fazer gestão de blogs
*  Atividade 2 - NextJs - Fetch de uma página que possui uma lista de json objetos e mostrar o resultado dessa consulta com estilização usando Tailwind

## Construindo o ambiente com docker-compose
Foi usado cadeias de docker-compose para construir as imagens docker que foram usados nas atividades
Para buildar as imagens use o comando a baixo
```bash
docker-compose up -d 
```
### Django
Para acessar o django siga os passos abaixo
1. Acessar a imagem docker com o comando ```docker-compose exec django bash```
2. Entrar com o comando ```pipenv shell```
3. Instalar dependencias ```pipenv install```
4. Iniciar o servidor ```python manager.py runserver 0.0.0.0:8000```
5. Acessar no seu browser o endereço htpp://localhost:8000

### NextJs
🔴 Atenção!! Não foi utilizado node como requisitado na atividade, no lugar como toolkit foi o usado [bun](https://bun.sh/)
1. Acessar a imagem docker com o comando ```docker-compose exec nextjs bash```
2. Entrar com o comando ```bun install``` para instalar as depências do projeto
3. Iniciar o serviço http com ```bun --bun run dev```
4. Acessar no seu browser o endereço htpp://localhost:3000

