FROM node:alpine

ENV HOST=0.0.0.0

WORKDIR /app

COPY package*.json ./

RUN npm i @vue/cli-service
RUN npm install

COPY . ./

EXPOSE 8080

CMD ["npm", "run", "serve"]