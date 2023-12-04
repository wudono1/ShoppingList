const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.static('public')); // Serve static files from the 'public' directory

app.post('/save-json', express.json(), (req, res) => {
  const jsonData = req.body;

  // Create a unique filename (you can customize this logic)
  const filename = `shopping_data_${Date.now()}.json`;

  const filePath = path.join(__dirname, 'public', filename);

  fs.writeFile(filePath, JSON.stringify(jsonData, null, 2), (err) => {
    if (err) {
      console.error('Error writing JSON file:', err);
      res.status(500).send('Error writing JSON file');
    } else {
      console.log('JSON file written successfully');
      res.json({ success: true, filename });
    }
  });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
