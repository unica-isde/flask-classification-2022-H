function processImage(inImg) {
    const width = inImg.width;
    const height = inImg.height;
    const src = new Uint32Array(inImg.data.buffer); // image data in Array
    
    // creating 4 arrays and initializing them to zero
    let histBrightness = new Array(256).fill(0);
    let histR = new Array(256).fill(0);
    let histG = new Array(256).fill(0);
    let histB = new Array(256).fill(0);
    
    for (let i = 0; i < src.length; i++) {
        let r = src[i] & 0xFF; // pixel's red component 
        let g = (src[i] >> 8) & 0xFF; // pixel's green component 
        let b = (src[i] >> 16) & 0xFF; // pixel's blue component
        histBrightness[r]++;
        histBrightness[g]++;
        histBrightness[b]++;
        histR[r]++; // frequency of red intensity level
        histG[g]++; // frequency of green intensity level
        histB[b]++; // frequency of blue intensity level
    }
  
    // checking the brightest intensity level in R, G and B
    let maxBrightness = 0;
    for (let i = 0; i < 256; i++) {
        if (maxBrightness < histR[i]) { // Red
            maxBrightness = histR[i];
        } else if (maxBrightness < histG[i]) { // Green 
            maxBrightness = histG[i]; 
        } else if (maxBrightness < histB[i]) { // Blue
            maxBrightness = histB[i];
        }
    }
  
    // drawing the canvas 
    const canvas = document.getElementById("histogramOutput");
    const ctx = canvas.getContext("2d");
    let guideHeight = 8;
    let startY = canvas.height - guideHeight; // starting y-coordinate for the graph
    let dx = canvas.width / 256; // pixel width for each histogram bar
    let dy = startY / maxBrightness;
    ctx.lineWidth = dx; // thickness of histogram bar
    ctx.fillStyle = "#fff"; // color of the canvas
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  
    for (let i = 0; i < 256; i++) {
        let x = i * dx; // x-coord of each vertical line 
        // Red levels in canvas
        ctx.strokeStyle = "rgba(220,0,0,0.5)";
        ctx.beginPath();
        ctx.moveTo(x, startY); 
        ctx.lineTo(x, startY - histR[i] * dy);
        ctx.closePath();
        ctx.stroke();
        // Green levels in canvas
        ctx.strokeStyle = "rgba(0,210,0,0.5)";
        ctx.beginPath();
        ctx.moveTo(x, startY);
        ctx.lineTo(x, startY - histG[i] * dy);
        ctx.closePath();
        ctx.stroke();
        // Blue levels in canvas
        ctx.strokeStyle = "rgba(0,0,255,0.5)";
        ctx.beginPath();
        ctx.moveTo(x, startY);
        ctx.lineTo(x, startY - histB[i] * dy);
        ctx.closePath();
        ctx.stroke();
        // Guide
        ctx.strokeStyle = "rgb(" + i + ", " + i + ", " + i + ")";
        ctx.beginPath();
        ctx.moveTo(x, startY);
        ctx.lineTo(x, canvas.height);
        ctx.closePath();
        ctx.stroke();
    }
}
 
// retrieves the image from the canvas 
function getImageData(image_id) {
    const canvas = document.createElement("canvas");
    const context = canvas.getContext("2d");
    const img = document.getElementById(image_id);
    canvas.width = img.width;
    canvas.height = img.height;
    context.drawImage(img, 0, 0);
    return context.getImageData(0, 0, img.width, img.height);
}
  
$("#image").load(function() {
    processImage(getImageData("image"));
})