const fs = require('fs');
const http = require('http');

const port = 3000;
const logfile = 'logfile.txt';

const server = http.createServer((req, res) => {
  fs.readFile(logfile, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.writeHead(500, {'Content-Type': 'text/plain'});
      res.end('Internal Server Error');
    } else {
      res.writeHead(200, {'Content-Type': 'text/plain'});
      res.end(data);
    }
  });
});

server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
