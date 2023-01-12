FROM node:lts-alpine
ENV NODE_ENV=development
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
# RUN npm install --production --silent && mv node_modules ../
RUN apk update
RUN npm install
COPY . .
EXPOSE 3000
EXPOSE 5000
# RUN chown -R node /usr/src/app
# USER node
CMD ["npm", "start"]
