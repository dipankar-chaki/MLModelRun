FROM node:20-slim

WORKDIR /web
COPY . /web
RUN npm install


CMD ["npm", "run", "dev", "--", "--host"]
