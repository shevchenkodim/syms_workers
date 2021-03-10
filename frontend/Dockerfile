FROM node:latest

WORKDIR /usr/src/frontend

COPY package*.json ./

RUN npm install \
    && npm fund

COPY ./ .

EXPOSE 8080

CMD ["npm", "run", "serve"]
