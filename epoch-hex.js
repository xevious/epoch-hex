(function() {
  const END_EPOCH = 2147483647;
  const overlay = document.getElementById("epochOverlay");
  const hexDisplay = document.getElementById("epochHex");
  const bar = document.getElementById("epochBar");
  const fill = document.getElementById("epochBarFill");

  // Insert decade ticks (1980–2030)
  const decadeEpochs = [
    315532800, 631152000, 946684800,
    1262304000, 1577836800, 1893456000
  ];
  decadeEpochs.forEach(ts => {
    const percent = ts / END_EPOCH;
    const tick = document.createElement("div");
    tick.className = "epochTick";
    tick.style.left = `${percent * 100}%`;
    bar.appendChild(tick);
  });

  function updateEpochDisplay() {
    const now = Math.floor(Date.now() / 1000);
    const wrapped = now % (2 ** 31);
    hexDisplay.textContent = "0x" + wrapped.toString(16).padStart(8, '0');
    const percent = Math.min(wrapped / END_EPOCH, 1.0);
    fill.style.width = `${percent * 100}%`;
  }

  updateEpochDisplay();
  setInterval(updateEpochDisplay, 1000);
})();