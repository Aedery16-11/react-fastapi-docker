FROM node:20-alpine
WORKDIR /app
#d'abord copier les dépendances et ensuitez le reste du code  pour éviter des problèmes de cache
COPY package*.json ./ 
RUN npm install
COPY . .
CMD [ "npm", "run", "dev", "--", "--host", "0.0.0.0" ]