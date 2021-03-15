FROM node:latest

# make the '/usr/src/frontend' folder the current working directory
WORKDIR /usr/src/frontend

COPY package*.json ./

# install project dependencies
RUN npm install \
    && npm fund

# copy project files and folders to the current working directory
COPY ./ .

EXPOSE 8080

CMD ["npm", "run", "serve"]
