CRIA UMA PASTA
mkdir evo_api

cd evo_api
git clone o repositório

MOSTRAR ARQUIVOS OCULTOS
ls -lha
nano .env // altere o ip e porta do servidor

# Atualiza pacotes
sudo apt update
sudo apt upgrade -y

# Instala dependências
sudo apt install ca-certificates curl gnupg lsb-release -y

# Adiciona chave oficial do Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Adiciona repositório oficial
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Atualiza de novo
sudo apt update

# Instala Docker Engine + CLI + containerd
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Testa instalação
docker --version


INICIAR CONTAINER 
docker compose up -d

PARA O CONTEINER DOCKER
docker compose down

LISTA CONTAINER 
docker ps

LISTA IMAGENS
docker images


