##########################
###### BUILD STAGE #######
##########################

FROM node:latest as build-stage
WORKDIR /usr/src/frontend
COPY frontend/package*.json /usr/src/frontend/
RUN npm install \
    && npm fund
COPY frontend /usr/src/frontend
RUN npm run build


##########################
#### PRODUCTION STAGE ####
##########################

FROM nginx:1.19.7-alpine as production-stage
COPY proxy/nginx.prod.conf /etc/nginx/nginx.conf
COPY --from=build-stage /usr/src/frontend/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]