FROM node:alpine

WORKDIR /app

COPY package*.json ./

RUN npm i @vue/cli-service
RUN npm install

COPY . ./

EXPOSE 8080

CMD ["npm", "run", "serve"]